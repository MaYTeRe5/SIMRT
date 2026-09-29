from engines.algorithm_engine import (
    AlgorithmEngine
)


engine = AlgorithmEngine()

gross_profit = 7200000

operating_expense = 1940000

ebitda = (
    engine.calculate_ebitda(
        gross_profit,
        operating_expense
    )
)

print("EBITDA")

print(ebitda)
