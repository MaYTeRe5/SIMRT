from engines.state_update_engine import (
    StateUpdateEngine
)

from engines.market_engine import (
    MarketEngine
)

from engines.algorithm_engine import (
    AlgorithmEngine
)


class SimulationYearRunner:

    def __init__(self):

        self.state_update_engine = (
            StateUpdateEngine()
        )

        self.market_engine = (
            MarketEngine()
        )

        self.algorithm_engine = (
            AlgorithmEngine()
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
            "3. Algorithm Engine"
        )

        print()

        print(
            "Year execution completed."
        )
