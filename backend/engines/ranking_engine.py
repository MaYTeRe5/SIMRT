from domain.kpi_result import KPIResult
from domain.ranking_result import RankingResult

from engines.ranking_topsis_matrix_builder import (
    RankingTopsisMatrixBuilder
)
from engines.topsis_engine import TopsisEngine


class RankingEngine:

    def __init__(self):
        self.matrix_builder = (
            RankingTopsisMatrixBuilder()
        )

        self.topsis_engine = (
            TopsisEngine()
        )

    def rank(
        self,
        kpi_results: list[KPIResult],
        weights: dict[str, float]
    ) -> list[RankingResult]:

        if not kpi_results:
            return []

        prepared_weights = self._prepare_weights(
            weights
        )

        matrix = self.matrix_builder.build(
            kpi_results
        )

        normalized_values = {
            "market_share":
                self.topsis_engine.normalize_column(
                    [
                        row.market_share
                        for row in matrix.rows
                    ]
                ),

            "ebitda":
                self.topsis_engine.normalize_column(
                    [
                        row.ebitda
                        for row in matrix.rows
                    ]
                ),

            "roe":
                self.topsis_engine.normalize_column(
                    [
                        row.roe
                        for row in matrix.rows
                    ]
                ),

            "debt_asset_ratio":
                self.topsis_engine.normalize_column(
                    [
                        row.debt_asset_ratio
                        for row in matrix.rows
                    ]
                ),

            "inventory_turn":
                self.topsis_engine.normalize_column(
                    [
                        row.inventory_turn
                        for row in matrix.rows
                    ]
                )
        }

        criterion_types = {
            "market_share": "benefit",
            "ebitda": "benefit",
            "roe": "benefit",
            "debt_asset_ratio": "cost",
            "inventory_turn": "benefit"
        }

        positive_ideals = {}
        negative_ideals = {}

        for criterion_name, values in (
            normalized_values.items()
        ):
            is_cost_criterion = (
                criterion_types[criterion_name]
                == "cost"
            )

            positive_ideals[criterion_name] = (
                self.topsis_engine.get_positive_ideal(
                    values,
                    is_cost_criterion
                )
            )

            negative_ideals[criterion_name] = (
                self.topsis_engine.get_negative_ideal(
                    values,
                    is_cost_criterion
                )
            )

        company_scores = []

        for index, row in enumerate(matrix.rows):
            weighted_positive_differences = []
            weighted_negative_differences = []

            for criterion_name in normalized_values:
                normalized_value = (
                    normalized_values[
                        criterion_name
                    ][index]
                )

                positive_difference = (
                    self.topsis_engine
                    .calculate_positive_difference(
                        normalized_value,
                        positive_ideals[
                            criterion_name
                        ]
                    )
                )

                negative_difference = (
                    self.topsis_engine
                    .calculate_negative_difference(
                        normalized_value,
                        negative_ideals[
                            criterion_name
                        ]
                    )
                )

                weighted_positive_difference = (
                    self.topsis_engine.apply_weight(
                        positive_difference,
                        prepared_weights[
                            criterion_name
                        ]
                    )
                )

                weighted_negative_difference =
