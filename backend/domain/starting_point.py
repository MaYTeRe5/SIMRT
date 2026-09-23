from dataclasses import dataclass


@dataclass
class StartingPoint:
    cash: float

    debt: float

    equity: float

    capacity: int

    inventory_units: int

    brand_score: float

    innovation_score: float

    efficiency_score: float
