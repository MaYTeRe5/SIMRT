from domain.market_context import MarketContext
from engines.market_engine import MarketEngine


market_context = MarketContext(
    year_no=1,

    previous_market_volume=1_000_000,

    market_growth_rate=0.10,

    brand_loyalty_rate=0.20,

    brand_loyalty_price_limit=1.75
)

engine = MarketEngine()

result = engine.run(market_context)

print(result)
