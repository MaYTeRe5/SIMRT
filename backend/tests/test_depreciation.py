from engines.depreciation_engine import (
    DepreciationEngine
)


engine = DepreciationEngine()

annual_depreciation = (
    engine.calculate_annual_depreciation(
        asset_value=1000000,
        useful_life_years=10
    )
)

print("Annual Depreciation")

print(annual_depreciation)
