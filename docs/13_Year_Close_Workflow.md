# SIMRT Year Close Workflow

## Purpose

Bu doküman bir simülasyon yılının kapatılması sırasında hangi işlemlerin hangi sırada çalışacağını tanımlar.

Year Close işlemi SIMRT'nin ana orkestrasyon sürecidir.

Tüm motorlar bu süreç içerisinde belirli bir sırada çalıştırılır.

---

# Trigger

Year Close işlemi yalnızca Admin tarafından başlatılabilir.

Tüm takım kararları kilitlenmiş olmalıdır.

```text
All Decisions Submitted
        ↓
Admin Close Year
        ↓
Year Close Workflow
```

---

# Workflow Overview

```text
Decision Validation
        ↓

State Update Engine
        ↓

Market Engine
        ↓

Algorithm Engine
        ↓

Financial Engine
        ↓

KPI Engine
        ↓

Ranking Engine
        ↓

Company State Creation
        ↓

Year Lock
        ↓

Next Year Creation
```

---

# Step 1

## Decision Validation

Amaç:

Tüm şirketlerin kararlarının eksiksiz olduğunu doğrulamak.

Kontrol edilen alanlar:

- Price
- Marketing
- Product R&D
- Process R&D
- Production Quantity
- Capacity Investment
- AR Days
- AP Days

Eksik karar varsa süreç durdurulur.

---

# Step 2

## State Update Engine

Amaç:

Kararların etkilerini TOPSIS öncesi güncellemek.

Üretilen değerler:

- Brand Score
- Innovation Score
- Efficiency Score

---

## Formula

```text
Current Investment

+

Previous Investment / 2

+

Older Investment / 3

+
...
```

---

# Step 3

## Market Engine

Amaç:

Pazar talebini hesaplamak.

---

### Market Volume Update

```text
Previous Market Volume
×
(1 + Growth Rate)
```

---

### Brand Loyalty Allocation

Brand Loyalty Demand hesaplanır.

---

### Price Check

Brand Loyalty Price Limit kontrol edilir.

---

### Segment Allocation

Kalan talep segmentlere dağıtılır.

---

### TOPSIS Calculation

Her segment için TOPSIS çalıştırılır.

---

### Initial Demand

```text
Brand Loyalty Demand

+

TOPSIS Demand
```

---

### Redistribution

Karşılanamayan talep yeniden dağıtılır.

---

### Output

```text
MarketResult
```

---

# Step 4

## Algorithm Engine

Amaç:

Operasyonel sonuçları oluşturmak.

---

### Available Product

```text
Beginning Inventory
+
Production
```

---

### Sales Units

```text
MIN
(
Final Demand,
Available Product
)
```

---

### Ending Inventory

```text
Available Product
-
Sales Units
```

---

### Capacity Update

Kapasite yatırımları uygulanır.

---

### Cost Calculation

Efficiency etkileri uygulanır.

---

### Output

```text
AlgorithmResult
```

---

# Step 5

## Financial Engine

Amaç:

Finansal tabloları üretmek.

---

### Income Statement

- Revenue
- COGS
- EBITDA
- EBIT
- Net Profit

---

### Balance Sheet

- Cash
- Receivables
- Inventory
- Fixed Assets
- Debt
- Payables
- Equity

---

### Cash Flow

- Operating Cash Flow
- Investing Cash Flow
- Financing Cash Flow

---

### Loan Calculation

Minimum nakit kuralı uygulanır.

```text
Minimum Cash

=
250.000 TL
```

---

### Deposit Calculation

Nakit fazlası mevduata aktarılır.

---

### Tax Calculation

İlk sürümde:

```text
Tax Rate = 0%
```

---

### Output

```text
FinancialResult
```

---

# Step 6

## KPI Engine

Amaç:

Şirket performans göstergelerini hesaplamak.

---

### KPIs

- Market Share
- EBITDA
- ROE
- Debt / Asset Ratio
- Inventory Turn

---

### Output

```text
KPIResult
```

---

# Step 7

## Ranking Engine

Amaç:

Takım sıralamasını oluşturmak.

---

### Method

TOPSIS

---

### Inputs

- Market Share
- EBITDA
- ROE
- Debt / Asset Ratio
- Inventory Turn

---

### Weights

```text
20%
20%
20%
20%
20%
```

---

### Output

```text
RankingResult
```

---

# Step 8

## Company State Creation

Amaç:

Yeni yılın başlangıç durumunu oluşturmak.

---

### Created Data

- Cash
- Debt
- Equity
- Capacity
- Inventory
- Brand Score
- Innovation Score
- Efficiency Score

Bu bilgiler yeni yılın başlangıç verisi olur.

---

# Step 9

## Year Lock

Amaç:

Tamamlanan yılın değiştirilmesini engellemek.

---

### Effects

- Decisions Locked
- Results Locked
- Rankings Locked

---

# Step 10

## Next Year Creation

Amaç:

Bir sonraki yılı açmak.

---

### New Objects

- Scenario
- Company State
- Decision Templates

oluşturulur.

---

# Workflow Outputs

Yıl kapatma işlemi sonunda oluşan nesneler:

```text
MarketResult

AlgorithmResult

FinancialResult

KPIResult

RankingResult

CompanyState
```

---

# End State

```text
Year N Closed
        ↓
Year N+1 Open
```

SIMRT yeni karar dönemine geçer.
