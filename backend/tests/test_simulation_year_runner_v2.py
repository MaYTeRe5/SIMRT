from services.simulation_year_runner import (
    SimulationYearRunner
)

from domain.year_close_result import (
    YearCloseResult
)


runner = SimulationYearRunner()

result = runner.run_year(
    simulation_id="SIM001",
    year_no=1
)

print(type(result))

print()

print(result)
`
