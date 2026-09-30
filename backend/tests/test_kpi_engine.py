from engines.kpi_engine import KPIEngine


engine = KPIEngine()

roe = engine.calculate_roe(
    net_profit=4810000,
    equity=24810000
)

debt_asset = engine.calculate_debt_asset_ratio(
    debt=3000000,
    total_assets=24300000
)

inventory_turn = engine.calculate_inventory_turn(
    cogs=10200000,
    average_inventory=5900000
)

print("ROE")
print(roe)

print()

print("Debt / Asset")
print(debt_asset)

print()

print("Inventory Turn")
print(inventory_turn)
