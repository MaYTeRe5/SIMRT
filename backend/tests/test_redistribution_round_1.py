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
        demand_units=230000,
        available_supply=180000,
        sales_units=180000,
        unmet_demand=50000,
        remaining_supply=0
    ),

    UnmetDemandResult(
        company_id="B",
        demand_units=160000,
        available_supply=300000,
        sales_units=160000,
        unmet_demand=0,
        remaining_supply=140000
    ),

    UnmetDemandResult(
        company_id="C",
        demand_units=90000,
        available_supply=120000,
        sales_units=90000,
        unmet_demand=0,
        remaining_supply=30000
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

allocations = (
    engine.calculate_redistribution_round(
        round_no=1,
        unmet_results=unmet_results,
        redistribution_scores=redistribution_scores
    )
)

print()

print("Round 1 Allocations")

print()

print(allocations)
