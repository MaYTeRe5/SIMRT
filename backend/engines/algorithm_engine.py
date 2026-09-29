from domain.algorithm_result import (
    AlgorithmResult
)


class AlgorithmEngine:

    def calculate_weighted_average_cost(
        self,
        beginning_inventory_units: int,
        beginning_inventory_value: float,
        production_units: int,
        production_cost: float
    ) -> float:

        total_units = (
            beginning_inventory_units
            + production_units
        )

        if total_units == 0:
            return 0.0

        total_cost = (
            beginning_inventory_value
            + production_cost
        )

        return (
            total_cost
            / total_units
        )

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

    def calculate_cogs(
           self,
           sales_units: int,
            weighted_average_cost: float
       ) -> float:

           return (
               sales_units
               * weighted_average_cost
           )

    def calculate_inventory_value(
           self,
           ending_inventory_units: int,
           weighted_average_cost: float
       ) -> float:
            return (
               ending_inventory_units
               * weighted_average_cost
           )
    def calculate_depreciation(
        self,
        asset_value: float,
        useful_life: int
    ) -> float:

        if useful_life == 0:
            return 0.0

        return (
            asset_value
            / useful_life
        )
