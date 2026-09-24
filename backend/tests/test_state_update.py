from engines.state_update_engine import StateUpdateEngine

engine = StateUpdateEngine()

result = engine.run(
    company_id="COMP001",
    year_no=3,
    marketing_history=[
        1_000_000,
        4_000_000,
        1_000_000
    ],
    product_rd_history=[
        500_000,
        1_000_000,
        2_000_000
    ],
    process_rd_history=[
        300_000,
        300_000,
        300_000
    ]
)

print(result)
