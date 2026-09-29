from engines.algorithm_engine import (
    AlgorithmEngine
)


engine = AlgorithmEngine()

ebit = engine.calculate_ebit(
    ebitda=5260000,
    depreciation=300000
)

print("EBIT")

print(ebit)
