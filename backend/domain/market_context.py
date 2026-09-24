from dataclasses import dataclass


@dataclass
class MarketContext:
    year_no: int

    previous_market_volume: int

    market_growth_rate: float

    brand_loyalty_rate: float

    brand_loyalty_price_limit: float
