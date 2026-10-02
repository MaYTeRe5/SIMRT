from services.simulation_year_runner import (
    SimulationYearRunner
)

runner = SimulationYearRunner()

result = runner._run_market_phase()

print(result)
