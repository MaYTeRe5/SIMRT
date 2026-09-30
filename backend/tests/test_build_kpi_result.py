from engines.kpi_engine import KPIEngine


engine = KPIEngine()

result = engine.build_kpi_result(
    company_id="A",

    market_share=0.25,

    ebitda=5260000,

    net_profit=4810000,

    equity=20100000,

    debt=3000000,

    total_assets=24300000,

    average_inventory=5900000,

    cogs=10800000
)

print(result)
