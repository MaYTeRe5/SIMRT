from domain.kpi_result import (
    KPIResult
)

from engines.ranking_topsis_row_builder import (
    RankingTopsisRowBuilder
)


kpi_result = KPIResult(
    company_id="A",

    market_share=0.25,

    ebitda=5260000,

    roe=0.24,

    debt_asset_ratio=0.12,

    inventory_turn=1.83
)

builder = RankingTopsisRowBuilder()

row = builder.build(
    kpi_result
)

print(row)
