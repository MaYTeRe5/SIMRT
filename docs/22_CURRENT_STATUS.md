# SIMRT Current Status

## Last Confirmed Test

Cash Flow Result

## Last Passing Command

PYTHONPATH=backend python backend/tests/test_build_cash_flow.py

## Current Work

Treasury and liquidity loop design

## Next Step

Implement TreasuryEngine or solve_liquidity()

## Completed Engines

- StateUpdateEngine
- MarketEngine
- TopsisEngine
- SegmentDemandAllocationEngine
- DemandRedistributionEngine
- AlgorithmEngine, partial

## Important Confirmed Rules

- GitHub is the source of truth.
- Replit is reset from origin/main before tests.
- Redistribution runs for a maximum of two additional rounds.
- Only companies with remaining supply participate.
- Round 2 remaining demand is lost.
- Inventory valuation uses weighted average cost.
- Minimum cash requirement is an admin variable.
