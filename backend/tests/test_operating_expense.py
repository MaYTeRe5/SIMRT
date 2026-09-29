from engines.algorithm_engine import (
    AlgorithmEngine
)


engine = AlgorithmEngine()

result = engine.calculate_operating_expense(
    marketing_fixed_cost=150000,
    marketing_variable_cost=1000000,

    product_rd_fixed_cost=90000,
    product_rd_variable_cost=500000,

    general_management_fixed_cost=200000,
    general_management_variable_cost=0
)

print(result)
