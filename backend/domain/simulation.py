from dataclasses import dataclass


@dataclass
class Simulation:
    id: str
    name: str
    current_year: int
    total_years: int
    status: str
