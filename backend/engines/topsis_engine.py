    from domain.topsis_matrix import TopsisMatrix


class TopsisEngine:

    def normalize_column(
        self,
        values: list[float]
    ) -> list[float]:

        denominator = (
            sum(v ** 2 for v in values)
        ) ** 0.5

        if denominator == 0:
            return [0.0 for _ in values]

        return [
            v / denominator
            for v in values
        ]

    def get_positive_ideal(
        self,
        values: list[float],
        is_cost_criterion: bool
    ) -> float:

        if is_cost_criterion:
            return min(values)

        return max(values)

    def get_negative_ideal(
        self,
        values: list[float],
        is_cost_criterion: bool
    ) -> float:

        if is_cost_criterion:
            return max(values)

        return min(values)

    def calculate_positive_difference(
        self,
        normalized_value: float,
        positive_ideal: float
    ) -> float:

        return (
            normalized_value
            - positive_ideal
        )

    def calculate_negative_difference(
        self,
        normalized_value: float,
        negative_ideal: float
    ) -> float:

        return (
            normalized_value
            - negative_ideal
        )

    def apply_weight(
        self,
        difference: float,
        weight: float
    ) -> float:

        return difference * weight

    def calculate_distance(
        self,
        weighted_differences: list[float]
    ) -> float:

        return (
            sum(
                difference ** 2
                for difference in weighted_differences
            )
        ) ** 0.5

    def calculate_relative_closeness(
        self,
        positive_distance: float,
        negative_distance: float
    ) -> float:

        denominator = (
            positive_distance
            + negative_distance
        )

        if denominator == 0:
            return 0.0

        return (
            negative_distance
            / denominator
        )
