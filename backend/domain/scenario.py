from dataclasses import dataclass


@dataclass
class Scenario:
    id: str
    year_no: int
    market_volume: int
    interest_rate: float
    inflation_rate: float
