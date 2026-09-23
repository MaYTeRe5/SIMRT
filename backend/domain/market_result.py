from dataclasses import dataclass


@dataclass
class MarketResult:
    company_id: str

    year_no: int

    topsis_score: float

    brand_loyalty_demand: int

    topsis_demand: int

    initial_demand: int

    redistributed_demand: int

    final_demand: int

    market_share: float
