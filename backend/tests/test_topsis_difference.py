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

weighted_positive_difference = (
    engine.apply_weight(
        positive_difference,
        0.60
    )
)

weighted_negative_difference = (
    engine.apply_weight(
        negative_difference,
        0.60
    )
)

print()

print("Weighted Positive Difference:")
print(weighted_positive_difference)

print()

print("Weighted Negative Difference:")
print(weighted_negative_difference)
