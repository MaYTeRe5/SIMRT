from dataclasses import dataclass


@dataclass
class CompanyTotalDemand:
    company_id: str

    value_demand: int

    balanced_demand: int

    premium_demand: int

    total_demand: int
