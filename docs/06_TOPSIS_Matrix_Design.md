# SIMRT TOPSIS Matrix Design

## Purpose

Bu doküman SIMRT içerisinde kullanılan TOPSIS karar matrisinin yapısını tanımlar.

TOPSIS Engine'in görevi:

- Şirketleri karşılaştırmak
- Segment bazlı puan üretmek
- Talep dağıtımına temel oluşturmak

TOPSIS yalnızca serbest talep havuzu için çalışır.

Brand Loyalty Demand TOPSIS dışında hesaplanır.

---

# TOPSIS Position

```text
Market Volume Update
        ↓

Brand Loyalty Allocation
        ↓

TOPSIS Pool Calculation
        ↓

TOPSIS Matrix Generation
        ↓

TOPSIS Calculation
        ↓

Demand Allocation
```

---

# TOPSIS Unit of Analysis

Her segment için ayrı TOPSIS çalıştırılır.

Örnek:

```text
Value Segment

Company A
Company B
Company C
Company D
```

---

```text
Balanced Segment

Company A
Company B
Company C
Company D
```

---

```text
Premium Segment

Company A
Company B
Company C
Company D
```

---

# TOPSIS Criteria

TOPSIS aşağıdaki kriterleri kullanır.

## Price

Kaynak:

```text
Decision.Price
```

Tip:

```text
Cost Criterion
```

Yorum:

```text
Düşük fiyat daha iyidir.
```

---

## Brand Score

Kaynak:

```text
CompanyState.BrandScore
```

Tip:

```text
Benefit Criterion
```

Yorum:

```text
Yüksek marka gücü daha iyidir.
```

---

## Innovation Score

Kaynak:

```text
CompanyState.InnovationScore
```

Tip:

```text
Benefit Criterion
```

Yorum:

```text
Yüksek inovasyon puanı daha iyidir.
```

---

## Credit Terms

Kaynak:

```text
Decision.AR_Days
```

Tip:

```text
Benefit Criterion
```

Yorum:

```text
Uzun müşteri vadeleri daha iyidir.
```

---

# Decision Matrix

Örnek:

```text
               Price   Brand   Innovation   Credit
Company A       100      75        55         90

Company B       110      70        70         60

Company C        95      60        50         75

Company D       120      80        65         45
```

---

# Matrix Generation Rules

## Price

Karar ekranından doğrudan alınır.

```text
Decision.Price
```

---

## Brand Score

Bir önceki yılın Company State değerinden alınır.

```text
CompanyState.BrandScore
```

---

## Innovation Score

Bir önceki yılın Company State değerinden alınır.

```text
CompanyState.InnovationScore
```

---

## Credit Terms

Müşteri vadesi kullanılır.

```text
Decision.AR_Days
```

---

# Segment Weight Application

Her segment aynı matrisi kullanır.

Fakat farklı ağırlık setleri uygular.

---

## Value Segment Example

```text
Price            60%

Brand            15%

Innovation       10%

Credit Terms     15%
```

---

## Balanced Segment Example

```text
Price            25%

Brand            25%

Innovation       25%

Credit Terms     25%
```

---

## Premium Segment Example

```text
Price            10%

Brand            40%

Innovation       40%

Credit Terms     10%
```

---

Gerçek ağırlıklar Variable List üzerinden yönetilir.

Bu değerler her yıl değişebilir.

---

# TOPSIS Process

## Step 1

Matrix Generation

---

## Step 2

Normalization

---

## Step 3

Weight Application

---

## Step 4

Positive Ideal Solution

---

## Step 5

Negative Ideal Solution

---

## Step 6

Distance Calculation

---

## Step 7

Relative Closeness Calculation

---

# TOPSIS Output

Her segment için:

```text
Company Score
```

üretilir.

Örnek:

```text
Company A = 0.81

Company B = 0.72

Company C = 0.55

Company D = 0.49
```

---

# Segment Demand Allocation

Her segment için:

```text
Company Demand Share

=

Company Score
/
Total Segment Scores
```

---

```text
Company Segment Demand

=

Segment Demand
×
Company Demand Share
```

---

# Output Objects

## Segment Score

Şirketin belirli segmentte aldığı TOPSIS puanı.

Örnek:

```text
Company A

Value Score = 0.81

Balanced Score = 0.76

Premium Score = 0.65
```

---

## Demand Allocation

Segment bazlı talep dağıtımı.

Örnek:

```text
Company A

Value Demand = 120.000

Balanced Demand = 85.000

Premium Demand = 40.000
```

---

# Redistribution Usage

Demand Redistribution aşamasında kullanılacak puan:

```text
Value Score
+
Balanced Score
+
Premium Score
```

# SIMRT TOPSIS Implementation Note

SIMRT içerisinde kullanılan TOPSIS yaklaşımı klasik akademik TOPSIS akışından farklı bir hesaplama sırası kullanır.

SIMRT sırası:

```text
Decision Matrix
↓
Normalization
↓
Positive / Negative Ideal Values
↓
Distance Calculation
↓
Weight Application
↓
Relative Closeness
```

---

## Mathematical Equivalence

SIMRT yaklaşımında ağırlıklar ideal ve negatif ideal değerlere olan farklar üzerinde uygulanır.

```text
Weighted Difference

=

Criterion Weight
×
(Normalized Value - Ideal Value)
```

Daha sonra uzaklık hesaplamasında kullanılır.

```text
Distance

=

√Σ(Weighted Difference²)
```

Bu yöntem, pozitif ağırlıklar kullanıldığında klasik TOPSIS'te ağırlıklandırılmış normalize matris üzerinden yapılan hesaplamalarla matematiksel olarak eşdeğer sonuç üretir.

---

## Design Principle

SIMRT'nin amacı akademik TOPSIS'in birebir uygulanması değil, Excel tabanlı referans motor ile birebir tutarlı sonuç üretmektir.

Bu nedenle Python uygulaması öncelikli olarak Excel hesaplama mantığını takip edecektir.

```text
Excel Result
=
Python Result
```

hedefi temel tasarım prensibidir.
`

toplamıdır.

Bu toplam puan ikinci ve sonraki dağıtım turlarında kullanılır.
