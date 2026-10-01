from domain.year_close_result import YearCloseResult

from engines.state_update_engine import (
    StateUpdateEngine
)
from engines.market_engine import (
    MarketEngine
)
from engines.demand_redistribution_engine import (
    DemandRedistributionEngine
)
from engines.algorithm_engine import (
    AlgorithmEngine
)
from engines.kpi_engine import (
    KPIEngine
)
from engines.ranking_engine import (
    RankingEngine
)


class SimulationYearRunner:

    def __init__(self):
        self.state_update_engine = (
            StateUpdateEngine()
        )

        self.market_engine = (
            MarketEngine()
        )

        self.demand_redistribution_engine = (
            DemandRedistributionEngine()
        )

        self.algorithm_engine = (
            AlgorithmEngine()
        )

        self.kpi_engine = (
            KPIEngine()
        )

        self.ranking_engine = (
            RankingEngine()
        )

    def run_year(
        self,
        simulation_id: str,
        year_no: int
    ) -> YearCloseResult:

        print()

        print(
            f"Running Simulation {simulation_id}"
        )

        print(
            f"Year {year_no}"
        )

        print()

        print(
            "1. State Update Engine"
        )

        print(
            "2. Market Engine"
        )

        print(
            "3. Demand Redistribution Engine"
        )

        print(
            "4. Algorithm Engine"
        )

        print(
            "5. KPI Engine"
        )

        print(
            "6. Ranking Engine"
        )

        result = YearCloseResult(
            financial_results=[],
            balance_sheet_results=[],
            cash_flow_results=[],
            kpi_results=[],
            ranking_results=[]
        )

        print()

        print(
            "Year execution completed."
        )

        return result
