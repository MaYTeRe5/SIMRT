from domain.topsis_row import TopsisRow

from engines.topsis_matrix_builder import (
    TopsisMatrixBuilder
)


rows = [
    TopsisRow(
        company_id="A",
        price=100,
        brand_score=3000000,
        innovation_score=2000000,
        credit_terms=90
    ),
    TopsisRow(
        company_id="B",
        price=110,
        brand_score=2500000,
        innovation_score=1800000,
        credit_terms=60
    ),
    TopsisRow(
        company_id="C",
        price=95,
        brand_score=3500000,
        innovation_score=2200000,
        credit_terms=120
    )
]

builder = TopsisMatrixBuilder()

matrix = builder.build(rows)

print(matrix)
