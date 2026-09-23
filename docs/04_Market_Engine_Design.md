# SIMRT Market Engine Design

## Purpose

Market Engine, müşteri satın alma davranışını simüle eder.

Takımların verdiği kararlar ile senaryo koşullarını değerlendirir ve pazar talebini şirketlere dağıtır.

Market Engine'in temel hesaplama yöntemi TOPSIS'tir.

---

# Engine Position

```text
Starting Point
        ↓

Decision
        ↓

Market Engine
        ↓

Algorithm Engine
        ↓

Financial Results
```

---

# Inputs

## Scenario

Market Engine aşağıdaki senaryo bilgilerini kullanır:

- Market Volume
- Segment Distribution
- Economic Conditions

---

## Segment

Her segment farklı müşteri davranışına sahiptir.

Örnek:

- Value
- Balanced
- Premium

---

## Segment Preference

Her segment için kriter ağırlıkları tanımlanır.

Örnek:

- Price Weight
- Brand Weight
- Innovation Weight
- Credit Terms Weight

---

## Company State

Bir önceki yıldan gelen şirket durumu.

Örnek:

- Brand Score
- Innovation Score
- Efficiency Score

---

## Decision

Takım tarafından girilen yıllık kararlar.

Örnek:

- Price
- Marketing
- Product R&D
- AR Days

---

# Market Engine Workflow

```text
Scenario
    ↓

Company State
    ↓

Decision
    ↓

TOPSIS Matrix
    ↓

TOPSIS Score
    ↓

Demand Allocation
    ↓

Market Share
```

---

# Evaluation Criteria

## Price

Maliyet kriteridir.

Düşük fiyat daha avantajlıdır.

---

## Brand

Fayda kriteridir.

Yüksek marka gücü daha avantajlıdır.

---

## Innovation

Fayda kriteridir.

Yüksek inovasyon değeri daha avantajlıdır.

---

## Credit Terms

Fayda kriteridir.

Uzun müşteri vadesi daha avantajlıdır.

Credit Terms = Accounts Receivable Days

---

# TOPSIS Calculation

## Step 1

Decision Matrix oluşturulur.

Örnek:

```text
               Price  Brand  Innovation  Credit
Company A
Company B
Company C
Company D
```

---

## Step 2

Normalize Matrix

---

## Step 3

Apply Segment Weights

---

## Step 4

Determine Ideal Solution

---

## Step 5

Determine Negative Ideal Solution

---

## Step 6

Calculate Relative Closeness

---

## Step 7

Generate Segment Score

---

# Demand Allocation

Her segment için TOPSIS skorları hesaplanır.

---

## Segment Demand

```text
Segment Demand

=
Market Volume
×
Segment Share
```

---

## Company Demand Share

```text
Company Demand Share

=
Company Score
/
Total Segment Score
```

---

## Company Demand

```text
Company Demand

=
Segment Demand
×
Company Demand Share
```

---

# Total Demand

Her segmentten gelen talepler toplanır.

```text
Total Demand

=
Value Demand
+
Balanced Demand
+
Premium Demand
```

---

# Outputs

## Demand Units

Şirket bazında oluşan talep.

---

## Market Share

Şirket bazında oluşan pazar payı.

---

## Segment Results

Her segment için:

- Demand
- Share
- TOPSIS Score

---

# Output Object

Market Engine çıktısı:

```text
MarketResult
```

İçerik:

- company_id
- year_no
- demand_units
- market_share
- segment_scores
