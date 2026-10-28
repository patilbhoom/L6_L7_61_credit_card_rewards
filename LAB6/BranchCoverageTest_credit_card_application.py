import pytest
from credit_card_rewards import reward_points, late_payment_fee, card_status


# ---------- REWARD POINTS: BRANCHES ----------

@pytest.mark.parametrize("tier,amount,category,weekend,expected", [
    ("classic", 1000, "grocery", False, 10),
    ("gold", 500, "grocery", False, 10),
    ("platinum", 500, "grocery", False, 20),
    ("gold", 500, "fuel", False, 0),
    ("gold", 500, "dining", False, 20),
    ("classic", 500, "travel", False, 10),
    ("classic", 500, "shopping", False, 5),
    ("classic", 500, "grocery", True, 5),
    ("gold", 500, "grocery", True, 60),
    ("platinum", 500, "dining", True, 90),
])
def test_reward_points_valid_paths(tier, amount, category, weekend, expected):
    assert reward_points(tier, amount, category, weekend) == expected


def test_reward_points_unknown_tier():
    with pytest.raises(ValueError, match="unknown card tier"):
        reward_points("diamond", 100, "grocery", False)


@pytest.mark.parametrize("amount", [0, -1])
def test_reward_points_invalid_amount(amount):
    with pytest.raises(ValueError, match="invalid amount"):
        reward_points("classic", amount, "grocery", False)


# ---------- LATE PAYMENT FEE: BRANCHES ----------

@pytest.mark.parametrize("outstanding,days_late,expected", [
    (5000, 0, 0),
    (0, 10, 0),
    (-1, 10, 0),
    (100, -1, 0),
    (1000, 1, 100),
    (1001, 1, 500),
    (10000, 30, 500),
    (10001, 1, 1000),
    (1000, 30, 100),
    (1000, 31, 850),
    (5000, 31, 1250),
    (15000, 31, 1750),
])
def test_late_payment_fee_paths(outstanding, days_late, expected):
    assert late_payment_fee(outstanding, days_late) == expected


# ---------- CARD STATUS: BRANCHES ----------

@pytest.mark.parametrize("utilisation,missed,frozen,expected", [
    (10, 0, True, "frozen"),
    (10, 3, False, "blocked"),
    (10, 4, False, "blocked"),
    (95, 0, False, "over limit risk"),
    (90, 0, False, "watch"),
    (31, 0, False, "watch"),
    (30, 1, False, "watch"),
    (30, 0, False, "good"),
    (95, 3, True, "frozen"),
    (95, 3, False, "blocked"),
])
def test_card_status_paths(utilisation, missed, frozen, expected):
    assert card_status(utilisation, missed, frozen) == expected