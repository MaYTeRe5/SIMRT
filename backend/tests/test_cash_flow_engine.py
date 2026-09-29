from engines.algorithm_engine import (
    AlgorithmEngine
)


engine = AlgorithmEngine()

operating_cash_flow = (
    engine.calculate_operating_cash_flow(
        net_profit=4810000,
        depreciation=300000
    )
)

print("Operating Cash Flow")

print(operating_cash_flow)
