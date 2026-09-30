# ADR-0008: Use Iterative Treasury Calculation

## Status

Accepted

## Context

Loan interest changes cash requirement, while cash requirement changes borrowing.

## Decision

Treasury calculations will use an iterative solution with convergence tolerance and maximum iteration protection.

## Consequences

- Interest and liquidity remain internally consistent.
- Calculation is more complex than a single-pass estimate.
- Minimum cash remains an admin-configurable variable.
