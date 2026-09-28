from domain.algorithm_result import (
    AlgorithmResult
)


class AlgorithmEngine:

    def calculate_operating_result(
        self,
        company_id: str,
        final_demand: int,
        available_product: int,
        price: float,
        unit_cost: float,
        ending_capacity: int
    ) -> AlgorithmResult:

        sales_units = min(
            final_demand,
            available_product
        )

        ending_inventory = (
            available_product
            - sales_units
        )

        revenue = (
            sales_units
            * price
        )

        cogs = (
            sales_units
            * unit_cost
        )

        gross_profit = (
            revenue
            - cogs
        )

        return AlgorithmResult(
            company_id=company_id,

            sales_units=sales_units,

            ending_inventory=ending_inventory,

            ending_capacity=ending_capacity,

            unit_cost=unit_cost,

            revenue=revenue,

            cogs=cogs,

            gross_profit=gross_profit
        )
