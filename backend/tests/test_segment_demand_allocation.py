from domain.segment_topsis_result import (
    SegmentTopsisResult
)

from engines.segment_demand_allocation_engine import (
    SegmentDemandAllocationEngine
)


results = [
    SegmentTopsisResult(
        company_id="A",
        segment_name="VALUE",
        topsis_score=0.73
    ),

    SegmentTopsisResult(
        company_id="B",
        segment_name="VALUE",
        topsis_score=0.40
    ),

    SegmentTopsisResult(
        company_id="C",
        segment_name="VALUE",
        topsis_score=1.00
    ),

    SegmentTopsisResult(
        company_id="D",
        segment_name="VALUE",
        topsis_score=0.00
    )
]

engine = SegmentDemandAllocationEngine()

allocations = engine.allocate(
    segment_name="VALUE",
    segment_demand=374000,
    topsis_results=results
)

for allocation in allocations:
    print(allocation)
