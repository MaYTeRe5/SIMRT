from dataclasses import dataclass


@dataclass
class TreasuryResult:
    company_id: str

    cash_before_treasury: float
    minimum_cash_requirement: float

    borrowing: float
    deposit: float

    interest_expense: float
    interest_income: float

    ending_cash: float

    iteration_count: int
    converged: bool
