from engines.topsis_engine import TopsisEngine


engine = TopsisEngine()

normalized_value = 0.45

positive_ideal = 0.40

negative_ideal = 0.60

positive_difference = (
    engine.calculate_positive_difference(
        normalized_value,
        positive_ideal
    )
)

negative_difference = (
    engine.calculate_negative_difference(
        normalized_value,
        negative_ideal
    )
)

print("Positive Difference:")
print(positive_difference)

print()

print("Negative Difference:")
print(negative_difference)
