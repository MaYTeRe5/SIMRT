from engines.topsis_engine import TopsisEngine


engine = TopsisEngine()

score = engine.calculate_relative_closeness(
    positive_distance=0.10,
    negative_distance=0.30
)

print(score)
