from domain.topsis_row import TopsisRow
from domain.topsis_matrix import TopsisMatrix


class TopsisMatrixBuilder:

    def build(
        self,
        rows: list[TopsisRow]
    ) -> TopsisMatrix:

        return TopsisMatrix(
            rows=rows
        )
