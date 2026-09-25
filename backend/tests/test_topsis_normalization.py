from engines.topsis_engine import TopsisEngine


engine = TopsisEngine()

result = engine.normalize_column(
    [100, 200, 300]
)

print(result)
