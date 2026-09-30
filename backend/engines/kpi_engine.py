class KPIEngine:

    def calculate_roe(
        self,
        net_profit: float,
        equity: float
    ) -> float:

        if equity == 0:
            return 0.0

        return (
            net_profit
            / equity
        )

    def calculate_debt_asset_ratio(
        self,
        debt: float,
        total_assets: float
    ) -> float:

        if total_assets == 0:
            return 0.0

        return (
            debt
            / total_assets
        )

    def calculate_inventory_turn(
        self,
        cogs: float,
        average_inventory: float
    ) -> float:

        if average_inventory == 0:
            return 0.0

        return (
            cogs
            / average_inventory
        )
