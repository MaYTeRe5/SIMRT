from domain.kpi_result import (
    KPIResult
)

from domain.ranking_topsis_row import (
    RankingTopsisRow
)


class RankingTopsisRowBuilder:

    def build(
        self,
        kpi_result: KPIResult
    ) -> RankingTopsisRow:

        return RankingTopsisRow(
            company_id=kpi_result.company_id,

            market_share=kpi_result.market_share,

            ebitda=kpi_result.ebitda,

            roe=kpi_result.roe,

            debt_asset_ratio=(
                kpi_result.debt_asset_ratio
            ),

            inventory_turn=(
                kpi_result.inventory_turn
            )
        )
