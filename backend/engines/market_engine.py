from domain.market_context import MarketContext
from domain.market_pool_result import MarketPoolResult
from domain.company_offer import CompanyOffer
from domain.brand_loyalty_result import BrandLoyaltyResult
from domain.brand_loyalty_distribution_result import (
    BrandLoyaltyDistributionResult
)


class MarketEngine:

    def calculate_current_market_volume(
        self,
        previous_market_volume: int,
        market_growth_rate: float
    ) -> int:

        return int(
            previous_market_volume
            * (1 + market_growth_rate)
        )

    def calculate_brand_loyalty_demand(
        self,
        current_market_volume: int,
        brand_loyalty_rate: float
    ) -> int:

        return int(
            current_market_volume
            * brand_loyalty_rate
        )

    def calculate_topsis_pool(
        self,
        current_market_volume: int,
        brand_loyalty_demand: int
    ) -> int:

        return (
            current_market_volume
            - brand_loyalty_demand
        )

    def run(
        self,
        market_context: MarketContext
    ) -> MarketPoolResult:

        current_market_volume = (
            self.calculate_current_market_volume(
                market_context.previous_market_volume,
                market_context.market_growth_rate
            )
        )

        brand_loyalty_demand = (
            self.calculate_brand_loyalty_demand(
                current_market_volume,
                market_context.brand_loyalty_rate
            )
        )

        topsis_pool = (
            self.calculate_topsis_pool(
                current_market_volume,
                brand_loyalty_demand
            )
        )

        return MarketPoolResult(
            current_market_volume=current_market_volume,

            brand_loyalty_demand=brand_loyalty_demand,

            distributed_brand_loyalty_demand=brand_loyalty_demand,

            lost_brand_loyalty_demand=0,

            topsis_pool=topsis_pool
        )

    def distribute_brand_loyalty(
        self,
        companies: list[CompanyOffer],
        brand_loyalty_demand: int,
        average_market_price: float,
        price_limit: float
    ) -> list[BrandLoyaltyResult]:
    
        company_count = len(companies)

        if company_count == 0:
            return []

        equal_share = int(
            brand_loyalty_demand / company_count
        )

        lost_demand = 0

        distributed_demand = 0
        
        results = []

        for company in companies:

            maximum_price = (
                average_market_price
                * price_limit
            )

            eligible = (
                company.price <= maximum_price
            )

            demand = (
                equal_share
                if eligible
                else 0
            )

            if eligible:
                distributed_demand += demand
            else:
                lost_demand += equal_share
                
            results.append(
                BrandLoyaltyResult(
                    company_id=company.company_id,
                    brand_loyalty_demand=demand,
                    eligible=eligible
                )
            )

        return BrandLoyaltyDistributionResult(
            results=results,
            distributed_demand=distributed_demand,
            lost_demand=lost_demand
        )
