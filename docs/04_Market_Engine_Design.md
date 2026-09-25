# SIMRT Market Engine Design

## Purpose

Market Engine müşteri satın alma davranışını simüle eder.

Takımların verdiği kararlar ile senaryo koşullarını değerlendirir ve pazar talebini şirketlere dağıtır.

Market Engine'in temel hesaplama yöntemi TOPSIS'tir.

Ancak toplam talebin tamamı TOPSIS ile dağıtılmaz.

Önce Brand Loyalty mekanizması çalışır.

Brand Loyalty sonrasında kalan talep TOPSIS aracılığıyla segmentlere dağıtılır.

Kapasite yetersizlikleri oluştuğunda karşılanamayan talep yeniden dağıtıma tabi tutulur.

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

- Market Volume Growth
- Brand Loyalty Rate
- Brand Loyalty Price Limit
- Segment Distribution
- Economic Conditions
# SIMRT Market Engine Design

## Purpose

Market Engine müşteri satın alma davranışını simüle eder.

Takımların verdiği kararlar ile senaryo koşullarını değerlendirir ve pazar talebini şirketlere dağıtır.

Market Engine'in temel hesaplama yöntemi TOPSIS'tir.

Ancak toplam talebin tamamı TOPSIS ile dağıtılmaz.

Önce Brand Loyalty mekanizması çalışır.

Brand Loyalty sonrasında kalan talep TOPSIS aracılığıyla segmentlere dağıtılır.

Kapasite yetersizlikleri oluştuğunda karşılanamayan talep yeniden dağıtıma tabi tutulur.

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

- Market Volume Growth
- Brand Loyalty Rate
- Brand Loyalty Price Limit
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

Bu ağırlıklar senaryo yılına göre değişebilir.

---

## Company State

Bir önceki yıldan gelen şirket durumu.

Örnek:

- Brand Score
- Innovation Score
- Efficiency Score

---

## Decision

Takımlar tarafından girilen yıllık kararlar.

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

Market Volume Update
    ↓

Brand Loyalty Allocation
    ↓

Brand Loyalty Price Check
    ↓

TOPSIS Pool Calculation
    ↓

Segment Allocation
    ↓

TOPSIS Calculation
    ↓

Initial Demand
    ↓

Capacity Check
    ↓

Demand Redistribution
    ↓

Final Demand
    ↓

Market Share
```

---

# Market Volume Update

Yılın toplam pazar hacmi güncellenir.

```text
Current Market Volume

=

Previous Market Volume
×
(1 + Growth Rate)
```

Growth Rate değeri Variable List'ten alınır.

---

# Brand Loyalty Allocation

Her senaryo yılı için bir Brand Loyalty Rate tanımlanır.

Örnek:

```text
10%
20%
35%
```

Brand Loyalty Demand aşağıdaki şekilde hesaplanır:

```text
Brand Loyalty Demand

=

Current Market Volume
×
Brand Loyalty Rate
```

---

# Brand Loyalty Distribution

Brand Loyalty Demand tüm aktif şirketlere eşit dağıtılır.

Örnek:

```text
Brand Loyalty Demand

200.000
```

4 şirket varsa:

```text
Company A = 50.000

Company B = 50.000

Company C = 50.000

Company D = 50.000
```

---

# Brand Loyalty Price Rule

Marka bağlılığından yararlanabilmek için şirket fiyatı belirlenen eşik değeri aşmamalıdır.

Senaryo tarafından belirlenir:

```text
Brand Loyalty Price Limit
```

Örnek:

```text
175%
```

Pazar ortalama fiyatı:

```text
100
```

ise:

```text
Maximum Allowed Price

=

100 × 1.75

=

175
```

olur.

---

# Price Violation

Bir şirket:

```text
Price > Maximum Allowed Price
```

ise:

```text
Brand Loyalty Demand = 0
```

olur.

Şirket ilgili yıl için marka bağlılığı avantajını kaybeder.

---

# Lost Loyalty Demand Rule

Kaybedilen Brand Loyalty Demand diğer şirketlere dağıtılmaz.

Kaybedilen miktar doğrudan TOPSIS havuzuna aktarılır.

Örnek:

```text
Brand Loyalty Pool

200.000
```

Company A hakkını kaybeder:

```text
50.000
```

adet.

Yeni durum:

```text
Distributed Brand Loyalty

150.000
```

TOPSIS Pool:

```text
+50.000
```

ek talep alır.

---

# TOPSIS Pool Calculation

TOPSIS ile dağıtılacak talep:

```text
TOPSIS Pool

=

Current Market Volume
-
Distributed Brand Loyalty Demand
```

şeklinde hesaplanır.

---

# Segment Allocation

TOPSIS Pool segmentlere ayrılır.

Segment oranları Variable List'ten alınır.

Örnek:

```text
Value      40%

Balanced   35%

Premium    25%
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

# Initial Demand

Her segment için oluşan TOPSIS talebi hesaplanır.

İlk talep:

```text
Initial Demand

=

Brand Loyalty Demand
+
TOPSIS Demand
```

---

# Capacity Check

Şirketin satışa sunabileceği ürün miktarı hesaplanır.

```text
Available Product

=

Beginning Inventory
+
Production
```

---

# Unmet Demand

Eğer:

```text
Initial Demand
>
Available Product
```

ise:

```text
Unmet Demand
```

oluşur.

---

# Demand Redistribution

Karşılanamayan talep yeniden dağıtılır.

Yalnızca satılabilir ürünü kalan şirketler yeniden dağıtıma katılır.

---

# Redistribution Score

Yeniden dağıtım puanı:

```text
Value TOPSIS Score
+
Balanced TOPSIS Score
+
Premium TOPSIS Score
```

toplamı olarak hesaplanır.

Bu puan kullanılarak yeniden dağıtım yapılır.

---

# Iterative Redistribution Rule

Yeniden dağıtım tek seferle sınırlı değildir.

Her yeniden dağıtım turundan sonra:

```text
Remaining Unmet Demand
```

hesaplanır.

Eğer:

```text
Remaining Unmet Demand > 0
```

ve

```text
Satılabilir ürünü olan şirket bulunuyorsa
```

yeniden dağıtım işlemi tekrar çalıştırılır.

---

# Redistribution Stop Conditions

Aşağıdaki koşullardan biri gerçekleşirse yeniden dağıtım sona erer.

## Condition 1

```text
Remaining Unmet Demand = 0
```

Tüm talep karşılanmıştır.

---

## Condition 2

```text
Available Product = 0
```

Pazardaki tüm satılabilir ürün tükenmiştir.

---

# Final Demand

```text
Final Demand

=

Initial Demand
+
Redistributed Demand
```

---

# Market Share

Market Share aşağıdaki şekilde hesaplanır:

```text
Market Share

=

Final Demand
/
Current Market Volume
```

---

# Outputs

## MarketResult

Her şirket için aşağıdaki bilgiler üretilir:

- company_id
- year_no
- topsis_score
- brand_loyalty_demand
- topsis_demand
- initial_demand
- redistributed_demand
- final_demand
- market_share

TOPSIS Pool

=

Current Market Volume
-
Distributed Brand Loyalty Demand
