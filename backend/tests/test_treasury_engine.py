from engines.treasury_engine import TreasuryEngine


engine = TreasuryEngine()


borrowing_result = engine.solve_liquidity(
    company_id="A",

    cash_before_treasury=-50000,

    minimum_cash_requirement=250000,

    loan_interest_rate=0.20,

    deposit_interest_rate=0.10
)


print("Borrowing Scenario")

print(borrowing_result)

print()


deposit_result = engine.solve_liquidity(
    company_id="B",

    cash_before_treasury=1250000,

    minimum_cash_requirement=250000,

    loan_interest_rate=0.20,

    deposit_interest_rate=0.10
)


print("Deposit Scenario")

print(deposit_result)

print()


assert borrowing_result.converged is True

assert abs(
    borrowing_result.ending_cash - 250000
) <= 0.01

assert abs(
    borrowing_result.borrowing - 375000
) <= 0.01

assert abs(
    borrowing_result.interest_expense - 75000
) <= 0.01

assert borrowing_result.deposit == 0


assert deposit_result.converged is True

assert abs(
    deposit_result.ending_cash - 250000
) <= 0.01

assert abs(
    deposit_result.deposit
    - 1111111.111111
) <= 0.01

assert abs(
    deposit_result.interest_income
    - 111111.111111
) <= 0.01

assert deposit_result.borrowing == 0


print("Treasury Engine test passed.")
