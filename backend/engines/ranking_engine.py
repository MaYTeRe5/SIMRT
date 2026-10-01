from domain.kpi_result import KPIResult
from domain.ranking_result import RankingResult

from engines.ranking_topsis_matrix_builder import (
    RankingTopsisMatrixBuilder
)
from engines.topsis_engine import TopsisEngine


class RankingEngine:

    def __init__(self):
        self.matrix_builder = RankingTopsisMatrixBuilder()
        self.topsis_engine = TopsisEngine()

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

                weighted_negative_difference = (
                    self.topsis_engine.apply_weight(
                        negative_difference,
                        prepared_weights[
                            criterion_name
                        ]
                    )
                )

                weighted_positive_differences.append(
                    weighted_positive_difference
                )

                weighted_negative_differences.append(
                    weighted_negative_difference
                )

            positive_distance = (
                self.topsis_engine.calculate_distance(
                    weighted_positive_differences
                )
            )

            negative_distance = (
                self.topsis_engine.calculate_distance(
                    weighted_negative_differences
                )
            )

            ranking_score = (
                self.topsis_engine
                .calculate_relative_closeness(
                    positive_distance,
                    negative_distance
                )
            )

            company_scores.append(
                {
                    "company_id": row.company_id,
                    "ranking_score": ranking_score
                }
            )

        sorted_scores = sorted(
            company_scores,
            key=lambda item: (
                -item["ranking_score"],
                item["company_id"]
            )
        )

        return self._assign_ranks(
            sorted_scores
        )

    def _prepare_weights(
        self,
        weights: dict[str, float]
    ) -> dict[str, float]:

        required_criteria = {
            "market_share",
            "ebitda",
            "roe",
            "debt_asset_ratio",
            "inventory_turn"
        }

        provided_criteria = set(
            weights.keys()
        )

        if provided_criteria != required_criteria:
            missing = (
                required_criteria
                - provided_criteria
            )

            unexpected = (
                provided_criteria
                - required_criteria
            )

            raise ValueError(
                f"Invalid ranking weights. "
                f"Missing: {sorted(missing)}. "
                f"Unexpected: {sorted(unexpected)}."
            )

        if any(
            weight < 0
            for weight in weights.values()
        ):
            raise ValueError(
                "Ranking weights cannot be negative."
            )

        total_weight = sum(
            weights.values()
        )

        if abs(total_weight - 100.0) < 0.000001:
            return {
                name: value / 100.0
                for name, value in weights.items()
            }

        if abs(total_weight - 1.0) < 0.000001:
            return weights.copy()

        raise ValueError(
            "Ranking weights must total "
            "1.0 or 100.0."
        )

    def _assign_ranks(
        self,
        sorted_scores: list[dict]
    ) -> list[RankingResult]:

        ranking_results = []

        previous_score = None
        previous_rank = 0

        for position, item sorted_scores,
            start=1
        ):

            current_score = item[
                "ranking_score"
            ]

            if (
                previous_score is not None
                and abs(
                    current_score
                    - previous_score
                ) <= 0.000000000001
            ):
                rank = previous_rank

            else:
                rank = position

            ranking_results.append(
                RankingResult(
                    company_id=item["company_id"],
                    ranking_score=current_score,
                    rank=rank
                )
            )

            previous_score = current_score
            previous_rank = rank


        return ranking_results
