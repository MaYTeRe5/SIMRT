from dataclasses import dataclass


@dataclass
class Segment:
    id: str
    scenario_id: str
    name: str
    market_share: float
