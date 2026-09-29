from domain.financial_result import (
    FinancialResult
)


result = FinancialResult(
    company_id="A",

    revenue=18000000,

    cogs=10800000,

    gross_profit=7200000,

    operating_expense=1940000,

    ebitda=5260000,

    depreciation=300000,

    ebit=4960000,

    interest_income=100000,

    interest_expense=250000,

    profit_before_tax=4810000,

    tax_expense=0,

    net_profit=4810000
)

print(result)
