from engines.topsis_engine import TopsisEngine


engine = TopsisEngine()


price_values = [
    0.45,
    0.50,
    0.40,
    0.60
]

print("Price Values:")
print(price_values)

positive_ideal = engine.get_positive_ideal(
    price_values,
    is_cost_criterion=True
)

negative_ideal = engine.get_negative_ideal(
    price_values,
    is_cost_criterion=True
)

print()

print("Positive Ideal:")
print(positive_ideal)

print()

print("Negative Ideal:")
print(negative_ideal)
