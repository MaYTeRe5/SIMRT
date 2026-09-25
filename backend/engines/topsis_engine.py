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
