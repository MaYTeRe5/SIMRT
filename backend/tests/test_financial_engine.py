from engines.algorithm_engine import (
    AlgorithmEngine
)

from domain.financial_result import (
    FinancialResult
)


engine = AlgorithmEngine()

result = engine.build_financial_result(
    company_id="A",

    revenue=18000000,

    cogs=10800000,

    gross_profit=7200000,

    operating_expense=1940000,

    ebitda=5260000,

    depreciation=300000,

    interest_income=100000,

    interest_expense=250000,

    tax_rate=0
)

print(result)
