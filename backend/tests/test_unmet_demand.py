from domain.company_total_demand import (
    CompanyTotalDemand
)

from domain.company_available_supply import (
    CompanyAvailableSupply
)

from engines.demand_redistribution_engine import (
    DemandRedistributionEngine
)


demands = [

    CompanyTotalDemand(
        company_id="A",

        value_demand=100000,
        balanced_demand=80000,
        premium_demand=50000,

        total_demand=230000
    ),

    CompanyTotalDemand(
        company_id="B",

        value_demand=70000,
        balanced_demand=60000,
        premium_demand=30000,

        total_demand=160000
    )
]

supplies = [

    CompanyAvailableSupply(
        company_id="A",
        available_units=180000
    ),

    CompanyAvailableSupply(
        company_id="B",
        available_units=300000
    )
]

engine = DemandRedistributionEngine()

results = engine.calculate_unmet_demand(
    demands,
    supplies
)

for result in results:
    print(result)
