from domain.balance_sheet_result import (
    BalanceSheetResult
)


result = BalanceSheetResult(

    company_id="A",

    cash=5000000,

    receivables=2500000,

    inventory_value=6800000,

    fixed_assets=10000000,

    total_assets=24300000,

    payables=1200000,

    debt=3000000,

    total_liabilities=4200000,

    equity=20100000
)

print(result)

print()

print("Balance Sheet Check")

print(
    result.total_assets
    ==
    (
        result.total_liabilities
        + result.equity
    )
)
``
