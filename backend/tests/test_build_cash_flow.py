from engines.algorithm_engine import (
    AlgorithmEngine
)


engine = AlgorithmEngine()

result = engine.build_cash_flow_result(
    company_id="A",

    operating_cash_flow=5110000,

    investing_cash_flow=-2000000,

    financing_cash_flow=1000000
)

print(result)
