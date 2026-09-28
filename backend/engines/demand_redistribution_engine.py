from domain.company_total_demand import CompanyTotalDemand
from domain.company_available_supply import CompanyAvailableSupply
from domain.company_redistribution_score import (
    CompanyRedistributionScore
)
from domain.unmet_demand_result import UnmetDemandResult
from domain.redistribution_allocation import (
    RedistributionAllocation
)
from domain.redistribution_round_result import (
    RedistributionRoundResult
)


class DemandRedistributionEngine:

    def calculate_unmet_demand(
        self,
        demands: list[CompanyTotalDemand],
        supplies: list[CompanyAvailableSupply]
    ):
        supply_lookup = {
            supply.company_id: supply.available_units
            for supply in supplies
        }

        results = []

        for demand in demands:
            available_supply = supply_lookup.get(
                demand.company_id,
                0
            )

            sales_units = min(
                demand.total_demand,
                available_supply
            )

            unmet_demand = max(
                demand.total_demand - sales_units,
                0
            )

            remaining_supply = max(
                available_supply - sales_units,
                0
            )

            results.append(
                UnmetDemandResult(
                    company_id=demand.company_id,
                    demand_units=demand.total_demand,
                    available_supply=available_supply,
                    sales_units=sales_units,
                    unmet_demand=unmet_demand,
                    remaining_supply=remaining_supply
                )
            )

        return results

    def calculate_redistribution_round(
        self,
        round_no: int,
        unmet_results: list[UnmetDemandResult],
        redistribution_scores: list[
            CompanyRedistributionScore
        ],
        unmet_demand_pool: int | None = None
    ):
        if unmet_demand_pool is None:
            unmet_demand_pool = sum(
                result.unmet_demand
                for result in unmet_results
            )

        score_lookup = {
            score.company_id: score.redistribution_score
            for score in redistribution_scores
        }

        eligible_results = [
            result
            for result in unmet_results
            if (
                result.remaining_supply > 0
                and score_lookup.get(
                    result.company_id,
                    0
                ) > 0
            )
        ]

        eligible_score_total = sum(
            score_lookup[result.company_id]
            for result in eligible_results
        )

        allocations = []

        if (
            unmet_demand_pool == 0
            or not eligible_results
            or eligible_score_total == 0
        ):
            round_result = RedistributionRoundResult(
                round_no=round_no,
                unmet_demand_before=unmet_demand_pool,
                distributed_demand=0,
                remaining_unmet_demand=unmet_demand_pool,
                eligible_company_count=len(
                    eligible_results
                )
            )

            return allocations, round_result

        remaining_pool = unmet_demand_pool

        for result in eligible_results:
            company_score = score_lookup[
                result.company_id
            ]

            calculated_allocation = round(
                unmet_demand_pool
                * company_score
                / eligible_score_total
            )

            allocated_demand = min(
                calculated_allocation,
                result.remaining_supply,
                remaining_pool
            )

            allocations.append(
                RedistributionAllocation(
                    company_id=result.company_id,
                    redistribution_score=company_score,
                    allocated_demand=allocated_demand
                )
            )

            remaining_pool -= allocated_demand

        distributed_demand = (
            unmet_demand_pool - remaining_pool
        )

        round_result = RedistributionRoundResult(
            round_no=round_no,
            unmet_demand_before=unmet_demand_pool,
            distributed_demand=distributed_demand,
            remaining_unmet_demand=remaining_pool,
            eligible_company_count=len(
                eligible_results
            )
        )

        return allocations, round_result

    def apply_redistribution_round(
        self,
        unmet_results: list[UnmetDemandResult],
        allocations: list[RedistributionAllocation]
    ):
        allocation_lookup = {
            allocation.company_id:
                allocation.allocated_demand
            for allocation in allocations
        }

        updated_results = []

        for result in unmet_results:
            allocated_demand = allocation_lookup.get(
                result.company_id,
                0
            )

            updated_sales_units = (
                result.sales_units
                + allocated_demand
            )

            updated_remaining_supply = max(
                result.remaining_supply
                - allocated_demand,
                0
            )

            updated_results.append(
                UnmetDemandResult(
                    company_id=result.company_id,
                    demand_units=result.demand_units,
                    available_supply=result.available_supply,
                    sales_units=updated_sales_units,
                    unmet_demand=0,
                    remaining_supply=updated_remaining_supply
                )
            )

        return updated_results

    def apply_redistribution_round(
        self,
        unmet_results: list[UnmetDemandResult],
        allocations: list[RedistributionAllocation]
    ):
        allocation_lookup = {
            allocation.company_id:
                allocation.allocated_demand
            for allocation in allocations
        }

        updated_results = []

        for result in unmet_results:

            allocated_demand = allocation_lookup.get(
                result.company_id,
                0
            )

            updated_sales_units = (
                result.sales_units
                + allocated_demand
            )

            updated_remaining_supply = max(
                result.remaining_supply
                - allocated_demand,
                0
            )

            updated_results.append(
                UnmetDemandResult(
                    company_id=result.company_id,
                    demand_units=result.demand_units,

                    available_supply=result.available_supply,

                    sales_units=updated_sales_units,

                    unmet_demand=0,

                    remaining_supply=updated_remaining_supply
                )
            )

        return updated_results


