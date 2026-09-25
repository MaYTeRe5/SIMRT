from domain.company_state import CompanyState
from domain.decision import Decision

from engines.topsis_row_builder import TopsisRowBuilder


company_state = CompanyState(
    company_id="COMP001",
    year_no=1,

    demand_units=0,
    sales_units=0,
    market_share=0,

    capacity=100000,
    inventory_units=0,
    utilization_rate=0,

    revenue=0,
    gross_profit=0,
    ebit=0,
    net_profit=0,

    cash=5000000,
    debt=0,
    equity=5000000,

    receivables=0,
    payables=0,

    brand_score=3333333,
    innovation_score=2666666,
    efficiency_score=550000
)

decision = Decision(
    id="DEC001",
    company_id="COMP001",
    year_no=1,

    price=100,

    marketing_investment=1000000,

    product_rd=500000,

    process_rd=300000,

    production_quantity=100000,

    capacity_investment=0,

    ar_days=90,

    ap_days=60
)

builder = TopsisRowBuilder()

row = builder.build(
    company_state,
    decision
)

print(row)
