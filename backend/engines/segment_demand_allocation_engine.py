from domain.segment_topsis_result import SegmentTopsisResult
from domain.company_segment_demand import (
    CompanySegmentDemand
)


class SegmentDemandAllocationEngine:

    def allocate(
        self,
        segment_name: str,
        segment_demand: int,
        topsis_results: list[SegmentTopsisResult]
    ) -> list[CompanySegmentDemand]:

        pass
