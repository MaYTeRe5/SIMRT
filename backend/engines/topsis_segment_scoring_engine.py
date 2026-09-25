from domain.topsis_matrix import TopsisMatrix
from domain.segment_preference import SegmentPreference
from domain.segment_topsis_result import SegmentTopsisResult

from engines.topsis_engine import TopsisEngine


class TopsisSegmentScoringEngine:

    def __init__(self):
        self.topsis_engine = TopsisEngine()

    def score(
        self,
        matrix: TopsisMatrix,
        segment_preference: SegmentPreference
    ) -> list[SegmentTopsisResult]:

        if not matrix.rows:
            return []

        weights = self._prepare_weights(
            segment_preference
        )

        price_values = [
            row.price
            for row in matrix.rows
        ]

        brand_values = [
            row.brand_score
            for row in matrix.rows
        ]

        innovation_values = [
            row.innovation_score
            for row in matrix.rows
        ]

        credit_values = [
            row.credit_terms
            for row in matrix.rows
        ]

        normalized_price = (
            self.topsis_engine.normalize_column(
                price_values
            )
        )

        normalized_brand = (
            self.topsis_engine.normalize_column(
                brand_values
            )
        )

        normalized_innovation = (
            self.topsis_engine.normalize_column(
                innovation_values
            )
        )

        normalized_credit = (
            self.topsis_engine.normalize_column(
                credit_values
            )
        )

        positive_ideals = {
            "price": self.topsis_engine.get_positive_ideal(
                normalized_price,
                is_cost_criterion=True
            ),
            "brand": self.topsis_engine.get_positive_ideal(
                normalized_brand,
                is_cost_criterion=False
            ),
            "innovation": self.topsis_engine.get_positive_ideal(
                normalized_innovation,
                is_cost_criterion=False
            ),
            "credit": self.topsis_engine.get_positive_ideal(
                normalized_credit,
                is_cost_criterion=False
            )
        }

        negative_ideals = {
            "price": self.topsis_engine.get_negative_ideal(
                normalized_price,
                is_cost_criterion=True
            ),
            "brand": self.topsis_engine.get_negative_ideal(
                normalized_brand,
                is_cost_criterion=False
            ),
            "innovation": self.topsis_engine.get_negative_ideal(
                normalized_innovation,
                is_cost_criterion=False
            ),
            "credit": self.topsis_engine.get_negative_ideal(
                normalized_credit,
                is_cost_criterion=False
            )
        }

        results = []

        for index, row in enumerate(matrix.rows):

            normalized_values = {
                "price": normalized_price[index],
                "brand": normalized_brand[index],
                "innovation": normalized_innovation[index],
                "credit": normalized_credit[index]
            }

            weighted_positive_differences = []
            weighted_negative_differences = []

            for criterion_name in normalized_values:

                normalized_value = normalized_values[
                    criterion_name
                ]

                positive_difference = (
                    self.topsis_engine
                    .calculate_positive_difference(
                        normalized_value,
                        positive_ideals[criterion_name]
                    )
                )

                negative_difference = (
                    self.topsis_engine
                    .calculate_negative_difference(
                        normalized_value,
                        negative_ideals[criterion_name]
                    )
                )

                weighted_positive_difference = (
                    self.topsis_engine.apply_weight(
                        positive_difference,
                        weights[criterion_name]
                    )
                )

                weighted_negative_difference = (
                    self.topsis_engine.apply_weight(
                        negative_difference,
                        weights[criterion_name]
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

            topsis_score = (
                self.topsis_engine
                .calculate_relative_closeness(
                    positive_distance,
                    negative_distance
                )
            )

            results.append(
                SegmentTopsisResult(
                    company_id=row.company_id,
                    segment_name=segment_preference.segment_id,
                    topsis_score=topsis_score
                )
            )

        return results

    def _prepare_weights(
        self,
        segment_preference: SegmentPreference
    ) -> dict[str, float]:

        weights = {
            "price": segment_preference.weight_price,
            "brand": segment_preference.weight_brand,
            "innovation": (
                segment_preference.weight_innovation
            ),
            "credit": (
                segment_preference.weight_credit_terms
            )
        }

        total_weight = sum(weights.values())

        if total_weight == 0:
            raise ValueError(
                "Segment preference weights cannot total zero."
            )

        if abs(total_weight - 100.0) < 0.000001:
            return {
                name: value / 100.0
                for name, value in weights.items()
            }

        if abs(total_weight - 1.0) < 0.000001:
            return weights

        raise ValueError(
            "Segment preference weights must total "
            "1.0 or 100.0."
        )
