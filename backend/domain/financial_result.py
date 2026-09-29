from dataclasses import dataclass


@dataclass
class FinancialResult:

    company_id: str

    revenue: float

    cogs: float

    gross_profit: float

    operating_expense: float

    ebitda: float

    depreciation: float

    ebit: float

    interest_income: float

    interest_expense: float

    profit_before_tax: float

    tax_expense: float

    net_profit: float
