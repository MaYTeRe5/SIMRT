from domain.year_close_result import (
    YearCloseResult
)

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
            f"Running Simulation "
            f"{simulation_id}"
        )

        print(
            f"Year {year_no}"
        )

        print()

        market_results = (
            self._run_market_phase()
        )

        financial_results = (
            self._run_financial_phase()
        )

        kpi_results = (
            self._run_kpi_phase()
        )

        ranking_results = (
            self._run_ranking_phase()
        )

        result = YearCloseResult(
            financial_results=
                financial_results,

            balance_sheet_results=[],

            cash_flow_results=[],

            kpi_results=
                kpi_results,

            ranking_results=
                ranking_results
        )

        print()

        print(
            "Year execution completed."
        )

        return result

    def _run_market_phase(
        self
    ):

        print(
            "1. State Update Engine"
        )

        print(
            "2. Market Engine"
        )

        print(
            "3. Demand Redistribution Engine"
        )

        return []

    def _run_financial_phase(
        self
    ):

        print(
            "4. Algorithm Engine"
        )

        print(
            "5. Financial Engine"
        )

        return []

    def _run_kpi_phase(
        self
    ):

        print(
            "6. KPI Engine"
        )

        return []

    def _run_ranking_phase(
        self
    ):

        print(
            "7. Ranking Engine"
        )

        return []
