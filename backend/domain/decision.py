from dataclasses import dataclass


@dataclass
class Decision:
    id: str
    company_id: str
    year_no: int

    price: float

    marketing_investment: float

    product_rd: float

    process_rd: float

    production_quantity: int

    capacity_investment: float

    ar_days: int

    ap_days: int
