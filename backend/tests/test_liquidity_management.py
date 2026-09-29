from engines.algorithm_engine import (
    AlgorithmEngine
)


engine = AlgorithmEngine()

loan_needed = (
    engine.calculate_required_borrowing(
        ending_cash=-50000,
        minimum_cash=250000
    )
)

print("Required Borrowing")

print(loan_needed)
