from engines.algorithm_engine import (
    AlgorithmEngine
)


engine = AlgorithmEngine()

receivables = (
    engine.calculate_receivables(
        revenue=18000000,
        ar_days=90
    )
)

payables = (
    engine.calculate_payables(
        purchases=12000000,
        ap_days=60
    )
)

print("Receivables")
print(receivables)

print()

print("Payables")
print(payables)
