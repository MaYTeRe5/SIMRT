from dataclasses import dataclass


@dataclass
class MarketResult:
    company_id: str

    year_no: int

    topsis_score: float

    demand_units: int

    sales_forecast: int

    market_share: float
