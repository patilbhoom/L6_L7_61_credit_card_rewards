import pytest
from credit_card_rewards import reward_points, late_payment_fee, card_status


# ---------- REWARD POINTS ----------

def test_classic_grocery():
    assert reward_points("classic", 1000, "grocery", False) == 10


def test_gold_grocery():
    assert reward_points("gold", 500, "grocery", False) == 10


def test_platinum_grocery():
    assert reward_points("platinum", 500, "grocery", False) == 20


def test_fuel_returns_zero():
    assert reward_points("gold", 5000, "fuel", True) == 0


def test_dining_double_points():
    assert reward_points("classic", 500, "dining", False) == 10


def test_travel_double_points():
    assert reward_points("gold", 500, "travel", False) == 20


def test_other_category():
    assert reward_points("gold", 500, "shopping", False) == 10


def test_weekend_bonus_for_gold():
    assert reward_points("gold", 500, "grocery", True) == 60


def test_weekend_bonus_for_platinum():
    assert reward_points("platinum", 500, "grocery", True) == 70


def test_classic_has_no_weekend_bonus():
    assert reward_points("classic", 500, "grocery", True) == 5


def test_unknown_card_tier():
    with pytest.raises(ValueError, match="unknown card tier"):
        reward_points("diamond", 500, "grocery", False)


@pytest.mark.parametrize("amount", [0, -100])
def test_invalid_amount(amount):
    with pytest.raises(ValueError, match="invalid amount"):
        reward_points("classic", amount, "grocery", False)


# ---------- LATE PAYMENT FEE ----------

@pytest.mark.parametrize("outstanding,days_late", [
    (5000, 0),
    (0, 10),
    (-100, 10),
    (5000, -1),
])
def test_no_late_payment_fee(outstanding, days_late):
    assert late_payment_fee(outstanding, days_late) == 0


def test_fee_for_small_outstanding():
    assert late_payment_fee(500, 10) == 100


def test_fee_at_1000_boundary():
    assert late_payment_fee(1000, 10) == 100


def test_fee_for_medium_outstanding():
    assert late_payment_fee(1001, 10) == 500


def test_fee_at_10000_boundary():
    assert late_payment_fee(10000, 10) == 500


def test_fee_for_large_outstanding():
    assert late_payment_fee(10001, 10) == 1000


def test_extra_fee_after_30_days_small_outstanding():
    assert late_payment_fee(500, 31) == 850


def test_extra_fee_after_30_days_medium_outstanding():
    assert late_payment_fee(5000, 31) == 1250


def test_extra_fee_after_30_days_large_outstanding():
    assert late_payment_fee(15000, 31) == 1750


def test_exactly_30_days_has_no_extra_fee():
    assert late_payment_fee(500, 30) == 100


# ---------- CARD STATUS ----------

def test_frozen_card():
    assert card_status(10, 0, True) == "frozen"


def test_three_missed_payments_blocks_card():
    assert card_status(10, 3, False) == "blocked"


def test_more_than_three_missed_payments_blocks_card():
    assert card_status(10, 4, False) == "blocked"


def test_utilisation_above_90():
    assert card_status(91, 0, False) == "over limit risk"


def test_utilisation_exactly_90():
    assert card_status(90, 0, False) == "watch"


def test_utilisation_above_30():
    assert card_status(31, 0, False) == "watch"


def test_missed_payment_causes_watch():
    assert card_status(20, 1, False) == "watch"


def test_good_card_status():
    assert card_status(30, 0, False) == "good"


def test_frozen_takes_priority():
    assert card_status(95, 3, True) == "frozen"


def test_blocked_takes_priority_over_utilisation():
    assert card_status(95, 3, False) == "blocked"