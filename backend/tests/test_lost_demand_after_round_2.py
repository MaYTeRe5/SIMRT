from domain.company_total_demand import CompanyTotalDemand
from domain.company_available_supply import (
    CompanyAvailableSupply
)
from domain.company_redistribution_score import (
    CompanyRedistributionScore
)

from engines.demand_redistribution_engine import (
    DemandRedistributionEngine
)


demands = [
    CompanyTotalDemand(
        company_id="A",
        value_demand=120000,
        balanced_demand=100000,
        premium_demand=180000,
        total_demand=400000
    ),

    CompanyTotalDemand(
        company_id="B",
        value_demand=70000,
        balanced_demand=60000,
        premium_demand=30000,
        total_demand=160000
    ),

    CompanyTotalDemand(
        company_id="C",
        value_demand=40000,
        balanced_demand=30000,
        premium_demand=20000,
        total_demand=90000
    )
]


supplies = [
    CompanyAvailableSupply(
        company_id="A",
        available_units=180000
    ),

    CompanyAvailableSupply(
        company_id="B",
        available_units=170000
    ),

    CompanyAvailableSupply(
        company_id="C",
        available_units=100000
    )
]


redistribution_scores = [
    CompanyRedistributionScore(
        company_id="A",
        redistribution_score=2.2
    ),

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

result = engine.run_redistribution(
    demands=demands,
    supplies=supplies,
    redistribution_scores=redistribution_scores,
    maximum_rounds=2
)


print("Round Results")

for round_result in result["round_results"]:
    print(round_result)

print()

print("Final Company Results")

for company_result in result["final_company_results"]:
    print(company_result)

print()

print("Final Demands")

for final_demand in result["final_demands"]:
    print(final_demand)

print()

assert result["lost_demand"] == 200000
assert result["round_results"][0].distributed_demand == 20000
assert result["round_results"][1].distributed_demand == 0

final_results = {
    item.company_id: item
    for item in result["final_company_results"]
}

assert final_results["A"].sales_units == 180000
assert final_results["B"].sales_units == 170000
assert final_results["C"].sales_units == 100000

print("Lost demand after Round 2 test passed.")

print("Lost Demand")
print(result["lost_demand"])
