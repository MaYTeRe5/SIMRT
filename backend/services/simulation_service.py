from domain.simulation import Simulation


class SimulationService:

    def create_simulation(
        self,
        simulation_id: str,
        name: str,
        total_years: int = 10
    ) -> Simulation:

        return Simulation(
            id=simulation_id,
            name=name,
            current_year=1,
            total_years=total_years,
            status="CREATED"
        )
