from domain.company_segment_demand import (
    CompanySegmentDemand
)

from engines.segment_demand_aggregation_engine import (
    SegmentDemandAggregationEngine
)


segment_demands = [

    CompanySegmentDemand(
        company_id="A",
        segment_name="VALUE",
        demand_units=100000
    ),

    CompanySegmentDemand(
        company_id="A",
        segment_name="BALANCED",
        demand_units=80000
    ),

    CompanySegmentDemand(
        company_id="A",
        segment_name="PREMIUM",
        demand_units=50000
    ),

    CompanySegmentDemand(
        company_id="B",
        segment_name="VALUE",
        demand_units=70000
    ),

    CompanySegmentDemand(
        company_id="B",
        segment_name="BALANCED",
        demand_units=60000
    ),

    CompanySegmentDemand(
        company_id="B",
        segment_name="PREMIUM",
        demand_units=30000
    )
]

engine = (
    SegmentDemandAggregationEngine()
)

results = engine.aggregate(
    segment_demands
)

for result in results:
    print(result)
