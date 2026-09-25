from domain.topsis_matrix import TopsisMatrix
from domain.topsis_row import TopsisRow
from domain.segment_preference import SegmentPreference

from engines.topsis_segment_scoring_engine import (
    TopsisSegmentScoringEngine
)


matrix = TopsisMatrix(
    rows=[
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
        ),

        TopsisRow(
            company_id="D",
            price=125,
            brand_score=2200000,
            innovation_score=1700000,
            credit_terms=30
        )
    ]
)


segment_preference = SegmentPreference(
    segment_id="VALUE",

    weight_price=60,
    weight_brand=15,
    weight_innovation=10,
    weight_credit_terms=15
)

engine = TopsisSegmentScoringEngine()

results = engine.score(
    matrix,
    segment_preference
)

for result in results:
    print(result)
