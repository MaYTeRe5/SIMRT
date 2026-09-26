from dataclasses import dataclass


@dataclass
class RedistributionRoundResult:
    round_no: int

    unmet_demand_before: int

    distributed_demand: int

    remaining_unmet_demand: int

    eligible_company_count: int
