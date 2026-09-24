from dataclasses import dataclass
from domain.brand_loyalty_result import BrandLoyaltyResult


@dataclass
class BrandLoyaltyDistributionResult:
    results: list[BrandLoyaltyResult]

    distributed_demand: int

    lost_demand: int
