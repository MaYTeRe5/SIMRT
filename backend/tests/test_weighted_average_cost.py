from engines.algorithm_engine import (
    AlgorithmEngine
)


engine = AlgorithmEngine()

weighted_average_cost = (
    engine.calculate_weighted_average_cost(
        beginning_inventory_units=100000,
        beginning_inventory_value=5000000,

        production_units=200000,
        production_cost=12000000
    )
)

print("Weighted Average Cost")

print(weighted_average_cost)
