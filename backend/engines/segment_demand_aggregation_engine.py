from domain.company_total_demand import (
    CompanyTotalDemand
)

from domain.company_segment_demand import (
    CompanySegmentDemand
)


class SegmentDemandAggregationEngine:

    def aggregate(
        self,
        segment_demands: list[CompanySegmentDemand]
    ) -> listcompany_totals = {}

        for demand in segment_demands:

            company_id = demand.company_id

            if company_id not in company_totals:

                company_totals[company_id] = (
                    CompanyTotalDemand(
                        company_id=company_id,

                        value_demand=0,
                        balanced_demand=0,
                        premium_demand=0,

                        total_demand=0
                    )
                )

            company_total = company_totals[
                company_id
            ]

            if demand.segment_name == "VALUE":
                company_total.value_demand += (
                    demand.demand_units
                )

            elif demand.segment_name == "BALANCED":
                company_total.balanced_demand += (
                    demand.demand_units
                )

            elif demand.segment_name == "PREMIUM":
                company_total.premium_demand += (
                    demand.demand_units
                )

            company_total.total_demand = (
                company_total.value_demand
                + company_total.balanced_demand
                + company_total.premium_demand
            )

        return list(
            company_totals.values()
        )
