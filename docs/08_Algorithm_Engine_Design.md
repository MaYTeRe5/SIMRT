# SIMRT Algorithm Engine Design

## Purpose

Algorithm Engine, Market Engine tarafından üretilen talep sonuçlarını kullanarak operasyonel ve finansal sonuçları hesaplar.

Bu motor:

- Satış adetlerini belirler
- Stokları günceller
- Kapasiteleri günceller
- Gelirleri hesaplar
- Maliyetleri hesaplar
- İşletme sermayesini hesaplar

Algorithm Engine finansal sonuçların temel üreticisidir.

---

# Engine Position

```text
Decision
        ↓

State Update Engine
        ↓

Market Engine
        ↓

Algorithm Engine
        ↓

Financial Engine
        ↓

Company State
```

---

# Inputs

## Scenario

Kaynak:

```text
Scenario
```

Örnek:

- Interest Rate
- Inflation
- Raw Material Index
- Capacity Limits

---

## Company State

Bir önceki yıl sonu şirket durumu.

Örnek:

- Cash
- Debt
- Inventory
- Capacity
- Equity

---

## Decision

Takımlar tarafından verilen kararlar.

Örnek:

- Price
- Production Quantity
- Capacity Investment
- Product R&D
- Process R&D
- Marketing
- AR Days
- AP Days

---

## Market Result

Market Engine çıktısı.

Örnek:

- Initial Demand
- Redistributed Demand
- Final Demand
- Market Share

---

## Configuration

Limit&CoEff&Facts sayfasından gelen parametreler.

Örnek:

- Base Cost
- Capacity Cost
- Depreciation Rules
- Working Capital Factors

---

# Algorithm Workflow

```text
Market Result
        ↓

Available Product Calculation
        ↓

Sales Calculation
        ↓

Inventory Calculation
        ↓

Capacity Update
        ↓

Cost Calculation
        ↓

Revenue Calculation
        ↓

Working Capital Calculation
        ↓

Operational Result
```

---

# Available Product Calculation

Satılabilir ürün miktarı:

```text
Available Product

=

Beginning Inventory
+
Production Quantity
```

---

# Sales Calculation

Gerçek satış:

```text
Sales Units

=

MIN
(
Final Demand,
Available Product
)
```

---

# Inventory Calculation

Dönem sonu stok:

```text
Ending Inventory

=

Available Product
-
Sales Units
```

---

# Capacity Update

Yeni kapasite:

```text
Ending Capacity

=

Beginning Capacity
+
Capacity Increase
```

Capacity Increase değeri yatırım kararından üretilir.

---

# Unit Cost Calculation

Birim maliyet aşağıdaki unsurların birleşimidir:

```text
Base Cost

×

Scenario Cost Factors

×

Efficiency Modifier
```

---

# Efficiency Modifier

Efficiency Score kullanılır.

Process R&D yatırımlarının zaman ağırlıklı etkisi maliyeti azaltır.

---

# Revenue Calculation

Gelir:

```text
Revenue

=

Sales Units
×
Price
```

---

# Cost of Goods Sold

Satılan mal maliyeti:

```text
COGS

=

Sales Units
×
Unit Cost
```

---

# Gross Profit

```text
Gross Profit

=

Revenue
-
COGS
```

---

# Working Capital Calculation

## Receivables

```text
Receivables

=

Revenue
×
AR Days
/
365
```

---

## Payables

```text
Payables

=

Purchases
×
AP Days
/
365
```

---

## Inventory Value

```text
Inventory Value

=

Ending Inventory
×
Unit Cost
```

---

# Operational Outputs

Algorithm Engine aşağıdaki çıktıları üretir:

## Sales Units

Gerçek satış miktarı

---

## Ending Inventory

Dönem sonu stok

---

## Ending Capacity

Dönem sonu kapasite

---

## Revenue

Toplam gelir

---

## COGS

Satılan mal maliyeti

---

## Gross Profit

Brüt kar

---

## Receivables

Dönem sonu alacaklar

---

## Payables

Dönem sonu borçlar

---

## Inventory Value

Dönem sonu stok değeri

---

# Output Object

AlgorithmResult

İçerik:

- company_id
- year_no

- sales_units

- ending_inventory

- ending_capacity

- unit_cost

- revenue

- cogs

- gross_profit

- receivables

- payables

- inventory_value
