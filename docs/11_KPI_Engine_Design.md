# SIMRT KPI Engine Design

## Purpose

KPI Engine şirket performansını ölçmek için kullanılan göstergeleri üretir.

Bu göstergeler:

- Şirket analizi
- Takım performansı
- Ranking Engine

tarafından kullanılır.

---

# Engine Position

```text
Market Engine
        ↓

Algorithm Engine
        ↓

Financial Engine
        ↓

KPI Engine
        ↓

Ranking Engine
```

---

# KPI Categories

SIMRT içerisinde KPI'lar beş ana gruba ayrılır.

```text
Growth

Profitability

Market

Financial Health

Operations
```

---

# Growth KPIs

## Revenue Growth

```text
Revenue Growth

=

(Current Revenue
-
Previous Revenue)

/
Previous Revenue
```

Amaç:

Şirketin büyüme performansını ölçmek.

---

# Profitability KPIs

## Gross Margin

```text
Gross Margin

=

Gross Profit
/
Revenue
```

---

## EBIT Margin

```text
EBIT Margin

=

EBIT
/
Revenue
```

---

## Net Profit Margin

```text
Net Profit
/
Revenue
```

---

# Market KPIs

## Market Share

```text
Market Share

=

Final Demand
/
Total Market Volume
```

---

## Demand Growth

```text
Current Demand
-
Previous Demand
```

Amaç:

Pazardaki konum değişimini ölçmek.

---

# Financial Health KPIs

## Cash Position

```text
Ending Cash
```

---

## Debt Ratio

```text
Debt
/
Equity
```

---

## Equity

```text
Ending Equity
```

---

# Operations KPIs

## Capacity Utilization

```text
Sales Units
/
Capacity
```

---

## Inventory Turnover

```text
COGS
/
Average Inventory
```

---

## Unit Cost

```text
Unit Cost
```

Düşük olması tercih edilir.

---

# Strategic KPIs

## Brand Strength

Kaynak:

```text
Brand Score
```

---

## Innovation Strength

Kaynak:

```text
Innovation Score
```

---

## Efficiency Strength

Kaynak:

```text
Efficiency Score
```

---

# KPI Classification

## Benefit KPIs

Yüksek olması tercih edilir.

Örnek:

- Revenue Growth
- EBIT Margin
- Net Profit Margin
- Market Share
- Cash Position
- Equity
- Brand Strength
- Innovation Strength

---

## Cost KPIs

Düşük olması tercih edilir.

Örnek:

- Debt Ratio
- Unit Cost

---

# Annual KPI Snapshot

Her yıl sonunda her şirket için KPI seti oluşturulur.

Örnek:

```text
Company A

Revenue Growth      12%

EBIT Margin         18%

Market Share        27%

Debt Ratio          0.45

Capacity Utilization 91%
```

---

# Output Object

KPIResult

İçerik:

- company_id
- year_no

- revenue_growth

- gross_margin
- ebit_margin
- net_profit_margin

- market_share

- cash_position
- debt_ratio
- equity

- capacity_utilization
- inventory_turnover
- unit_cost

- brand_strength
- innovation_strength
- efficiency_strength
