from domain.kpi_result import (
    KPIResult
)

from domain.ranking_topsis_matrix import (
    RankingTopsisMatrix
)

from engines.ranking_topsis_row_builder import (
    RankingTopsisRowBuilder
)


class RankingTopsisMatrixBuilder:

    def build(
        self,
        kpi_results: list[KPIResult]
    ) -> RankingTopsisMatrix:

        row_builder = (
            RankingTopsisRowBuilder()
        )

        rows = []

        for kpi_result in kpi_results:

            rows.append(
                row_builder.build(
                    kpi_result
                )
            )

        return RankingTopsisMatrix(
            rows=rows
        )
