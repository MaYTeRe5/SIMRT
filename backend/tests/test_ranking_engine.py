from domain.kpi_result import KPIResult

from engines.ranking_engine import (
    RankingEngine
)


kpi_results = [

    KPIResult(
        company_id="A",
        market_share=0.25,
        ebitda=5260000,
        roe=0.24,
        debt_asset_ratio=0.12,
        inventory_turn=1.83
    ),

    KPIResult(
        company_id="B",
        market_share=0.18,
        ebitda=4200000,
        roe=0.17,
        debt_asset_ratio=0.18,
        inventory_turn=1.50
    ),

    KPIResult(
        company_id="C",
        market_share=0.31,
        ebitda=6200000,
        roe=0.28,
        debt_asset_ratio=0.09,
        inventory_turn=2.10
    )
]


weights = {
    "market_share": 20,
    "ebitda": 20,
    "roe": 20,
    "debt_asset_ratio": 20,
    "inventory_turn": 20
}


engine = RankingEngine()

results = engine.rank(
    kpi_results=kpi_results,
    weights=weights
)


for result in results:
    print(result)


assert results[0].company_id == "C"
assert results[0].rank == 1

assert results[1].company_id == "A"
assert results[1].rank == 2

assert results[2].company_id == "B"
assert results[2].rank == 3

print()

print("Ranking Engine test passed.")
