from dataclasses import dataclass


@dataclass
class OperatingExpenseResult:
    marketing_expense: float

    product_rd_expense: float

    general_management_expense: float

    total_operating_expense: float
