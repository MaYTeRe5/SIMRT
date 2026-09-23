from dataclasses import dataclass


@dataclass
class CompanyState:
    company_id: str
    year_no: int

    # Market

    demand_units: int
    sales_units: int

    market_share: float

    # Operations

    capacity: int

    inventory_units: int

    utilization_rate: float

    # Finance

    cash: float

    debt: float

    equity: float

    receivables: float

    payables: float
