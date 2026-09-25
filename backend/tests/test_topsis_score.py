from engines.topsis_engine import TopsisEngine


engine = TopsisEngine()

positive_distance = 0.10

negative_distance = 0.30

score = engine.calculate_relative_closeness(
    positive_distance,
    negative_distance
)

print("TOPSIS Score:")

print(score)
