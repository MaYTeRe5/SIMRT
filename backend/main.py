from services.simulation_service import SimulationService
from services.team_service import TeamService


simulation_service = SimulationService()
team_service = TeamService()


simulation = simulation_service.create_simulation(
    "SIM001",
    "SIMRT Leadership Challenge"
)

team_a = team_service.create_team(
    "TEAM001",
    "Blue Tigers",
    "COMP001"
)

print(simulation)
print(team_a)
