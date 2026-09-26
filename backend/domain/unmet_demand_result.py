from dataclasses import dataclass


@dataclass
class UnmetDemandResult:
    company_id: str

    demand_units: int

    available_supply: int

    sales_units: int

    unmet_demand: int

    remaining_supply: int
