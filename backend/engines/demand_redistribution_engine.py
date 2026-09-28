from domain.company_total_demand import CompanyTotalDemand
from domain.company_available_supply import CompanyAvailableSupply
from domain.unmet_demand_result import UnmetDemandResult


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
