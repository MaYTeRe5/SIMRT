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

sales_units = 180000

ending_inventory_units = 120000

cogs = (
    engine.calculate_cogs(
        sales_units,
        weighted_average_cost
    )
)

inventory_value = (
    engine.calculate_inventory_value(
        ending_inventory_units,
        weighted_average_cost
    )
)

print("Weighted Average Cost")
print(weighted_average_cost)

print()

print("COGS")
print(cogs)

print()

print("Ending Inventory Value")
print(inventory_value)
