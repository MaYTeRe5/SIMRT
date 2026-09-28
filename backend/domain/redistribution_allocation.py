from dataclasses import dataclass


@dataclass
class RedistributionAllocation:
    company_id: str

    redistribution_score: float

    allocated_demand: int
`
