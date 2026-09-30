from domain.kpi_result import KPIResult


results = [

    KPIResult(
        company_id="A",

        market_share=0.25,

        ebitda=5260000,

        roe=0.24,

        debt_asset_ratio=0.12,

        inventory_turn=1.83
    ),

    KPIResult(
        company_id="B",

        market_share=0.18,

        ebitda=4200000,

        roe=0.17,

        debt_asset_ratio=0.18,

        inventory_turn=1.50
    ),

    KPIResult(
        company_id="C",

        market_share=0.31,

        ebitda=6200000,

        roe=0.28,

        debt_asset_ratio=0.09,

        inventory_turn=2.10
    )
]

print(results)
