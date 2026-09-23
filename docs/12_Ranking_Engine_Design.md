# SIMRT Ranking Engine Design

## Purpose

Ranking Engine şirketlerin yıllık performans sıralamasını oluşturur.

Sıralama TOPSIS yöntemi ile hesaplanır.

---

# Engine Position

```text
Financial Engine
        ↓

KPI Engine
        ↓

Ranking Engine
        ↓

Leaderboard
```

---

# Ranking Inputs

Ranking Engine aşağıdaki KPI'ları kullanır:

- Market Share
- EBITDA
- ROE
- Debt / Asset Ratio
- Inventory Turn

---

# KPI Classification

## Benefit Criteria

Yüksek olması tercih edilir.

- Market Share
- EBITDA
- ROE
- Inventory Turn

---

## Cost Criteria

Düşük olması tercih edilir.

- Debt / Asset Ratio

---

# KPI Weights

Tüm KPI'lar eşit ağırlıklıdır.

```text
20%
20%
20%
20%
20%
```

---

# Decision Matrix

Örnek:

```text
               Market   EBITDA   ROE   Debt/Asset   Inv.Turn

Company A
Company B
Company C
Company D
```

---

# TOPSIS Process

## Step 1

Normalize Matrix

---

## Step 2

Apply Equal Weights

---

## Step 3

Determine Positive Ideal Solution

---

## Step 4

Determine Negative Ideal Solution

---

## Step 5

Calculate Relative Closeness

---

## Step 6

Generate Ranking Score

---

# Ranking Score

Her şirket için:

```text
Ranking Score

0.0000
-
1.0000
```

arasında bir puan üretilir.

---

# Annual Ranking

Şirketler Ranking Score değerine göre sıralanır.

Örnek:

```text
1st Company A

2nd Company C

3rd Company B

4th Company D
```

---

# Outputs

## RankingResult

- company_id
- year_no
- ranking_score
- rank
