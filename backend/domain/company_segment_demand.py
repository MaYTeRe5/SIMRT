from dataclasses import dataclass


@dataclass
class CompanySegmentDemand:
    company_id: str

    segment_name: str

    demand_units: int
