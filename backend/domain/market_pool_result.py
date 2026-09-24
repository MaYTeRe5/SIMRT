from dataclasses import dataclass


@dataclass
class MarketPoolResult:
    current_market_volume: int

    brand_loyalty_demand: int

    distributed_brand_loyalty_demand: int

    lost_brand_loyalty_demand: int

    topsis_pool: int
