from dataclasses import dataclass


@dataclass
class BrandLoyaltyResult:
    company_id: str

    brand_loyalty_demand: int

    eligible: bool
