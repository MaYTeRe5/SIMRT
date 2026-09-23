from dataclasses import dataclass


@dataclass
class StateUpdateResult:
    company_id: str
    year_no: int

    brand_score: float

    innovation_score: float

    efficiency_score: float

