from domain.unmet_demand_result import (
    UnmetDemandResult
)

from domain.company_redistribution_score import (
    CompanyRedistributionScore
)

from engines.demand_redistribution_engine import (
    DemandRedistributionEngine
)


unmet_results = [

    UnmetDemandResult(
        company_id="A",
        demand_units=300000,
        available_supply=180000,
        sales_units=180000,
        unmet_demand=120000,
        remaining_supply=0
    ),

    UnmetDemandResult(
        company_id="B",
        demand_units=160000,
        available_supply=180000,
        sales_units=160000,
        unmet_demand=0,
        remaining_supply=20000
    ),

    UnmetDemandResult(
        company_id="C",
        demand_units=90000,
        available_supply=110000,
        sales_units=90000,
        unmet_demand=0,
        remaining_supply=20000
    )
]

redistribution_scores = [

    CompanyRedistributionScore(
        company_id="B",
        redistribution_score=1.9
    ),

    CompanyRedistributionScore(
        company_id="C",
        redistribution_score=1.6
    )
]

engine = DemandRedistributionEngine()

allocations, round_result = (
    engine.calculate_redistribution_round(
        round_no=1,
        unmet_results=unmet_results,
        redistribution_scores=redistribution_scores
    )
)

print()

print("Round Result")

print(round_result)

print()

print("Allocations")

for allocation in allocations:
    print(allocation)
