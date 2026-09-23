print("SIMRT Backend Started")
from services.simulation_service import SimulationService


service = SimulationService()

simulation = service.create_simulation(
    "SIM001",
    "SIMRT Leadership Challenge"
)

print(simulation)
``
