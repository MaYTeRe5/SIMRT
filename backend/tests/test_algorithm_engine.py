from engines.algorithm_engine import (
    AlgorithmEngine
)


engine = AlgorithmEngine()

result = engine.calculate_operating_result(
    company_id="A",

    final_demand=230000,

    available_product=180000,

    price=100,

    unit_cost=60,

    ending_capacity=100000
)

print(result)

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
