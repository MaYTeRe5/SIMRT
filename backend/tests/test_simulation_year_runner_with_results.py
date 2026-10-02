from services.simulation_year_runner import (
    SimulationYearRunner
)

runner = SimulationYearRunner()

result = runner.run_year(
    simulation_id="SIM001",
    year_no=1
)

print("Financial Results")
print(result.financial_results)

print()

print("Ranking Results")
print(result.ranking_results)
