from engines.topsis_engine import TopsisEngine


engine = TopsisEngine()

distance = engine.calculate_distance(
    [
        0.03,
        -0.09
    ]
)

print(distance)
