# Lab 6: Code and Branch Coverage Analysis

**Name:** Bhoomika Patil  
**SRN:** PES1UG25AM801  
**Repository:** L6_L7_61_credit_card_rewards

## 1. Objective

To write and execute test cases for the credit card rewards application and evaluate code coverage and branch coverage using pytest and coverage.py.

## 2. Application Functions Tested

- **reward_points():** Tested card tiers, invalid amounts, fuel transactions, reward multipliers, and weekend bonuses.
- **late_payment_fee():** Tested invalid payment conditions, fee ranges, boundary values, and additional fees for payments delayed by more than 30 days.
- **card_status():** Tested frozen, blocked, over-limit-risk, watch, and good statuses, including decision priority.

## 3. Code Coverage Analysis

The code coverage test suite tests normal execution paths, invalid inputs, and boundary conditions.

**Coverage achieved:** 100%

**Screenshot:** `code_coverage.png`

## 4. Branch Coverage Analysis

The branch coverage test suite tests conditional outcomes and threshold comparisons in the application.

**Coverage achieved:** 100%

**Screenshot:** `branch_coverage.png`

## 5. Tools Used

- Python
- pytest
- coverage.py
- Git and GitHub

## 6. Conclusion

Test cases were developed for the credit card rewards application to measure line and branch coverage. The coverage reports and screenshots provide evidence of the results achieved by the test suites.