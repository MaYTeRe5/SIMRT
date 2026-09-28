from dataclasses import dataclass


@dataclass
class AlgorithmResult:
    company_id: str

    sales_units: int

    ending_inventory: int

    ending_capacity: int

    unit_cost: float

    revenue: float

    cogs: float

    gross_profit: float
