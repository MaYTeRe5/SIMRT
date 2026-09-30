from domain.kpi_result import (
    KPIResult
)

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

    def build_kpi_result(
        self,
        company_id: str,

        market_share: float,

        ebitda: float,

        net_profit: float,

        equity: float,

        debt: float,

        total_assets: float,

        average_inventory: float,

        cogs: float
    ):

        roe = self.calculate_roe(
            net_profit,
            equity
        )

        debt_asset_ratio = (
            self.calculate_debt_asset_ratio(
                debt,
                total_assets
            )
        )

        inventory_turn = (
            self.calculate_inventory_turn(
                cogs,
                average_inventory
            )
        )

        return KPIResult(
            company_id=company_id,

            market_share=market_share,

            ebitda=ebitda,

            roe=roe,

            debt_asset_ratio=debt_asset_ratio,

            inventory_turn=inventory_turn
        )
