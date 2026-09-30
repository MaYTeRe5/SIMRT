# ADR-0002: Excel-Compatible TOPSIS Method

## Status

Accepted

---

## Context

SIMRT'nin referans hesaplama motoru Excel'dir.

Amaç:

```text
Excel Result
=
Python Result
```

uyumunu sağlamaktır.

Klasik TOPSIS akademik yaklaşımı ile Excel motoru arasında uygulama sırası açısından farklılık bulunmaktadır.

TOPSIS motorunun Python tarafında geliştirilmesi sırasında aşağıdaki karar alınmıştır.

---

## Decision

Python uygulaması TOPSIS'in akademik sıralamasını değil, Excel motorunun sıralamasını takip edecektir.

SIMRT TOPSIS sırası:

```text
Decision Matrix
↓
Normalization
↓
Positive Ideal Solution
↓
Negative Ideal Solution
↓
Difference Calculation
↓
Weight Application
↓
Distance Calculation
↓
Relative Closeness
```

---

## Criterion Types

### Cost Criteria

- Price

Kural:

```text
Positive Ideal = Minimum Normalized Value

Negative Ideal = Maximum Normalized Value
```

---

### Benefit Criteria

- Brand Score
- Innovation Score
- Credit Terms

Kural:

```text
Positive Ideal = Maximum Normalized Value

Negative Ideal = Minimum Normalized Value
```

---

## Weight Application Rule

Ağırlıklar normalize edilmiş ideal farklarına uygulanır.

```text
Weighted Difference

=

Criterion Weight
×
(
Normalized Value
-
Ideal Value
)
```

---

## Distance Formula
