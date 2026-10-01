from domain.year_close_result import (
    YearCloseResult
)

from domain.financial_result import (
    FinancialResult
)

from domain.balance_sheet_result import (
    BalanceSheetResult
)

from domain.cash_flow_result import (
    CashFlowResult
)

from domain.kpi_result import (
    KPIResult
)

from domain.ranking_result import (
    RankingResult
)


result = YearCloseResult(

    financial_results=[
        FinancialResult(
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
    ],

    balance_sheet_results=[
        BalanceSheetResult(
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
    ],

    cash_flow_results=[
        CashFlowResult(
            company_id="A",

            operating_cash_flow=5110000,

            investing_cash_flow=-2000000,

            financing_cash_flow=1000000,

            ending_cash=4110000
        )
    ],

    kpi_results=[
        KPIResult(
            company_id="A",

            market_share=0.25,

            ebitda=5260000,

            roe=0.2393,

            debt_asset_ratio=0.1235,

            inventory_turn=1.8305
        )
    ],

    ranking_results=[
        RankingResult(
            company_id="A",

            ranking_score=0.6033,

            rank=2
        )
    ]
)

print(result)
