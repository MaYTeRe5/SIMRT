from dataclasses import dataclass


@dataclass
class CompanyFinalDemand:
    company_id: str

    initial_demand: int

    redistributed_demand: int

    final_demand: int
