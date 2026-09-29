from domain.cash_flow_result import (
    CashFlowResult
)


result = CashFlowResult(

    company_id="A",

    operating_cash_flow=5000000,

    investing_cash_flow=-2000000,

    financing_cash_flow=1000000,

    ending_cash=4000000
)

print(result)

print()

print(
    result.operating_cash_flow
    +
    result.investing_cash_flow
    +
    result.financing_cash_flow
)
