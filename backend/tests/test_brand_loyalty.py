from domain.company_offer import CompanyOffer
from engines.market_engine import MarketEngine


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

result = engine.distribute_brand_loyalty(
    companies=companies,
    brand_loyalty_demand=220000,
    average_market_price=100,
    price_limit=1.75
)

for item in result:
    print(item)
