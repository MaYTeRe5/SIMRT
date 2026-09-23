# SIMRT KPI Engine Design

## Purpose

KPI Engine şirket performans göstergelerini üretir.

Bu göstergeler şirket performansının değerlendirilmesinde kullanılır ve Ranking Engine'e girdi sağlar.

SIMRT'nin mevcut versiyonunda resmi takım sıralaması 5 KPI üzerinden hesaplanmaktadır.

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

# Official Ranking KPIs

SIMRT içerisinde resmi takım sıralaması aşağıdaki KPI'lar kullanılarak hesaplanır.

---

## Market Share

```text
Market Share

=

Final Demand
/
Total Market Volume
```

Amaç:

Pazardaki rekabet başarısını ölçmek.

KPI Türü:

```text
Benefit KPI
```

Yüksek olması tercih edilir.

---

## EBITDA

```text
EBITDA

=

EBIT
+
Depreciation
```

Amaç:

Şirketin operasyonel karlılığını ölçmek.

KPI Türü:

```text
Benefit KPI
```

Yüksek olması tercih edilir.

---

## ROE

```text
ROE

=

Net Profit
/
Equity
```

Amaç:

Özkaynağın ne kadar verimli kullanıldığını ölçmek.

KPI Türü:

```text
Benefit KPI
```

Yüksek olması tercih edilir.

---

## Debt / Asset Ratio

```text
Debt
/
Total Assets
```

Amaç:

Finansal risk seviyesini ölçmek.

KPI Türü:

```text
Cost KPI
```

Düşük olması tercih edilir.

---

## Inventory Turn

```text
Inventory Turn

=

COGS
/
Average Inventory
```

Amaç:

Stok yönetim performansını ölçmek.

KPI Türü:

```text
Benefit KPI
```

Yüksek olması tercih edilir.

---

# Ranking KPI Weights

Tüm KPI'lar eşit ağırlıklıdır.

```text
Market Share      20%

EBITDA            20%

ROE               20%

Debt / Asset      20%

Inventory Turn    20%
```

---

# KPI Classification Summary

## Benefit KPIs

- Market Share
- EBITDA
- ROE
- Inventory Turn

---

## Cost KPIs

- Debt / Asset Ratio

---

# Annual KPI Snapshot

Her yıl sonunda her şirket için KPI seti oluşturulur.

Örnek:

```text
Company A

Market Share      24.8%

EBITDA            18.200.000

ROE               16.4%

Debt / Asset      0.38

Inventory Turn    8.7
```

---

# Output Object

KPIResult

İçerik:

- company_id
- year_no

- market_share
- ebitda
- roe
- debt_asset_ratio
- inventory_turn
