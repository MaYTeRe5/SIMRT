from engines.algorithm_engine import (
    AlgorithmEngine
)


engine = AlgorithmEngine()

result = engine.build_balance_sheet_result(
    company_id="A",

    cash=5000000,

    receivables=2500000,

    inventory_value=6800000,

    fixed_assets=10000000,

    payables=1200000,

    debt=3000000,

    equity=20100000
)

print(result)

print()

print(
    result.total_assets
    ==
    result.total_liabilities
    + result.equity
)
