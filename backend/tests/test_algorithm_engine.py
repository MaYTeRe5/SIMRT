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
