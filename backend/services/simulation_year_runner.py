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

    def run_year(
        self,
        simulation_id: str,
        year_no: int
    ):

        print()

        print(
            f"Running Simulation "
            f"{simulation_id}"
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

        print()

        print(
            "Year execution completed."
        )
