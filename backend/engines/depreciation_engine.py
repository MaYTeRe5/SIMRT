class DepreciationEngine:

    def calculate_annual_depreciation(
        self,
        asset_value: float,
        useful_life_years: int
    ) -> float:

        if useful_life_years <= 0:
            return 0.0

        return (
            asset_value
            / useful_life_years
        )
