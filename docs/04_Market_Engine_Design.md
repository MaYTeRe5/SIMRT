# SIMRT Market Engine Design

## Purpose

Market Engine, müşteri satın alma davranışını simüle eder.

Takımların verdiği kararlar ile senaryo koşullarını değerlendirir ve pazar talebini şirketlere dağıtır.

Market Engine'in temel hesaplama yöntemi TOPSIS'tir.

Ancak toplam talebin tamamı TOPSIS ile dağıtılmaz.

Önce Brand Loyalty mekanizması çalışır. Brand Loyalty sonrasında kalan talep TOPSIS aracılığıyla segmentlere dağıtılır.

Kapasite yetersizliği oluştuğunda karşılanamayan talep, satılabilir ürünü bulunan şirketlere yeniden dağıtılır.

---

## Engine Position

```text
Starting Point
        ↓
Decision
        ↓
State Update Engine
        ↓
Market Engine
        ↓
Algorithm Engine
        ↓
Financial Engine
```

---

## Inputs

### Scenario

Market Engine aşağıdaki senaryo bilgilerini kullanır:

- Market Volume Growth
- Brand Loyalty Rate
- Brand Loyalty Price Limit
- Segment Distribution
- Segment Preferences

### Segment

Her segment farklı müşteri davranışına sahiptir.

Mevcut segmentler:

- Value
- Balanced
- Premium

### Segment Preference

Her segment için aşağıdaki kriter ağırlıkları tanımlanır:

- Price Weight
- Brand Weight
- Innovation Weight
- Credit Terms Weight

Bu ağırlıklar simülasyon yılına ve senaryoya göre değişebilir.

Her segmentin kriter ağırlıkları toplamı yüzde 100 olmalıdır.

### Company State

Bir önceki yıldan ve State Update Engine'den gelen şirket bilgileri kullanılır.

Örnek:

- Beginning Inventory
- Brand Score
- Innovation Score
- Available Capacity

### Decision

Takımlar tarafından girilen yıllık kararlar kullanılır.

Market Engine açısından ilgili kararlar:

- Price
- Production Quantity
- Marketing Investment
- Product R&D Investment
- AR Days

---

## Market Engine Workflow

```text
Scenario
    ↓
Company State
    ↓
Decision
    ↓
Market Volume Update
    ↓
Brand Loyalty Pool Calculation
    ↓
Brand Loyalty Equal Allocation
    ↓
Brand Loyalty Price Check
    ↓
Distributed Brand Loyalty Calculation
    ↓
Lost Brand Loyalty Calculation
    ↓
TOPSIS Pool Calculation
    ↓
Segment Allocation
    ↓
Segment-Based TOPSIS Calculation
    ↓
Initial Demand
    ↓
Available Product Check
    ↓
Demand Redistribution
    ↓
Final Sales Demand
    ↓
Market Share
```

---

## Market Volume Update

Yılın toplam pazar hacmi, bir önceki yılın pazar hacmi üzerinden güncellenir.

```text
Current Market Volume

=

Previous Market Volume
×
(1 + Market Growth Rate)
```

Market Growth Rate değeri Variable List üzerinden alınır.

### Example

```text
Previous Market Volume = 1,000,000

Market Growth Rate = 10%

Current Market Volume = 1,100,000
```

---

## Brand Loyalty Pool Calculation

Her simülasyon yılı için bir Brand Loyalty Rate tanımlanır.

Brand Loyalty Rate, toplam pazarın ne kadarının marka bağlılığı mekanizmasıyla dağıtılacağını belirler.

```text
Brand Loyalty Demand

=

Current Market Volume
×
Brand Loyalty Rate
```

### Example

```text
Current Market Volume = 1,100,000

Brand Loyalty Rate = 20%

Brand Loyalty Demand = 220,000
```

---

## Brand Loyalty Equal Allocation

Brand Loyalty Demand, aktif şirket sayısına eşit olarak bölünür.
