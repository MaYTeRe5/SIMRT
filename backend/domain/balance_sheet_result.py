from dataclasses import dataclass


@dataclass
class BalanceSheetResult:

    company_id: str

    cash: float

    receivables: float

    inventory_value: float

    fixed_assets: float

    total_assets: float

    payables: float

    debt: float

    total_liabilities: float

    equity: float
