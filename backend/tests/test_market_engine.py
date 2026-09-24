from domain.market_context import MarketContext
from domain.company_offer import CompanyOffer

from engines.market_engine import MarketEngine


market_context = MarketContext(
    year_no=1,

    previous_market_volume=1_000_000,

    market_growth_rate=0.10,

    brand_loyalty_rate=0.20,

    brand_loyalty_price_limit=1.75
)

companies = [
    CompanyOffer(
        company_id="A",
        price=100
    ),
    CompanyOffer(
        company_id="B",
        price=120
    ),
    CompanyOffer(
        company_id="C",
        price=150
    ),
    CompanyOffer(
        company_id="D",
        price=180
    )
]

engine = MarketEngine()

print(market_context)

print(companies)

