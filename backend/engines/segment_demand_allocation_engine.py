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

                if not topsis_results:
            return []

        total_score = sum(
            result.topsis_score
            for result in topsis_results
        )

        if total_score == 0:

            equal_share = int(
                segment_demand
                / len(topsis_results)
            )

            return [
                CompanySegmentDemand(
                    company_id=result.company_id,
                    segment_name=segment_name,
                    demand_units=equal_share
                )
                for result in topsis_results
            ]

        allocations = []

        for result in topsis_results:

            demand_units = int(
                segment_demand
                *
                (
                    result.topsis_score
                    / total_score
                )
            )

            allocations.append(
                CompanySegmentDemand(
                    company_id=result.company_id,
                    segment_name=segment_name,
                    demand_units=demand_units
                )
            )

        return allocations
