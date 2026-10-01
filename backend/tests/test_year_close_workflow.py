from services.simulation_year_runner import (
    SimulationYearRunner
)


runner = SimulationYearRunner()

runner.run_year(
    simulation_id="SIM001",
    year_no=1
)

print()

print("Year Close Workflow Test Passed.")
