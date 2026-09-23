# SIMRT Financial Engine Design

## Purpose

Financial Engine şirketlerin finansal tablolarını üretir.

Kaynakları:

- Company State
- Market Result
- Algorithm Result
- Scenario
- Decisions

kullanarak:

- Income Statement
- Balance Sheet
- Cash Flow Statement

oluşturur.

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

# Financial Statements

Financial Engine aşağıdaki finansal tabloları üretir:

## Income Statement

Gelir Tablosu

---

## Balance Sheet

Bilanço

---

## Cash Flow Statement

Nakit Akış Tablosu

---

# Income Statement

## Revenue

Kaynak:

```text
Sales Units
×
Price
```

---

## Cost Of Goods Sold (COGS)

Kaynak:

```text
Sales Units
×
Unit Cost
```

---

## Gross Profit

```text
Revenue
-
COGS
```

---

## Operating Expenses

Operating Expenses aşağıdaki kalemlerden oluşur:

### Marketing

```text
Marketing Investment
```

Tamamı dönem gideridir.

---

### Product R&D

```text
Product R&D Investment
```

Tamamı dönem gideridir.

OPEX olarak değerlendirilir.

---

### Depreciation Expense

Aşağıdaki yatırımlar için hesaplanır:

- Starting Point Fixed Assets
- Capacity Investments
- Process R&D Investments

---

## EBIT

```text
Gross Profit
-
Operating Expenses
```

---

## Interest Expense

Borçlar üzerinden hesaplanır.

Faiz oranı Scenario tarafından belirlenir.

---

## Profit Before Tax

```text
EBIT
-
Interest Expense
```

---

## Net Profit

```text
Profit Before Tax
-
Tax Expense
```

---

# Balance Sheet

## Assets

### Cash

Dönem sonu nakit.

---

### Receivables

```text
Revenue
×
AR Days
/
365
```

---

### Inventory

```text
Ending Inventory
×
Unit Cost
```

---

### Fixed Assets

```text
Previous Fixed Assets
+
New CAPEX
-
Accumulated Depreciation
```

---

## Liabilities

### Payables

```text
Purchases
×
AP Days
/
365
```

---

### Financial Debt

Şirket borçları.

---

## Equity

```text
Previous Equity
+
Net Profit
```

---

# Cash Flow Statement

## Operating Cash Flow

Kaynak:

```text
Net Profit
```

düzeltmeleri ile hesaplanır.

---

### Add Back Depreciation

Amortisman nakit çıkışı yaratmaz.

Bu nedenle geri eklenir.

---

### Working Capital Changes

Dikkate alınır:

- Receivables
- Inventory
- Payables

---

## Investing Cash Flow

Aşağıdaki yatırımlar içerilir:

### Capacity Investment

CAPEX

---

### Process R&D Investment

CAPEX

---

## Financing Cash Flow

Aşağıdaki hareketleri içerir:

- New Loans
- Debt Repayments

---

# Depreciation Rules

## Method

```text
Straight Line
```

---

## Useful Life

```text
10 Years
```

---

## Applies To

- Starting Point Assets
- Capacity Investments
- Process R&D Investments

---

# OPEX vs CAPEX

## Marketing

```text
OPEX
```

Dönem gideri.

---

## Product R&D

```text
OPEX
```

Dönem gideri.

---

## Capacity Investment

```text
CAPEX
```

Aktifleştirilir.

---

## Process R&D

```text
CAPEX
```

Aktifleştirilir.

---

# Outputs

Financial Engine aşağıdaki sonuçları üretir:

## Income Statement

- Revenue
- COGS
- Gross Profit
- Operating Expenses
- EBIT
- Interest Expense
- Net Profit

---

## Balance Sheet

- Cash
- Receivables
- Inventory
- Fixed Assets
- Debt
- Payables
- Equity

---

## Cash Flow Statement

- Operating Cash Flow
- Investing Cash Flow
- Financing Cash Flow

---

# Output Object

FinancialResult

İçerik:

- company_id
- year_no

- revenue
- cogs
- gross_profit

- depreciation_expense

- ebit
- interest_expense
- net_profit

- cash

- receivables
- inventory
- fixed_assets

- payables
- debt

- equity
``

# Liquidity Management

SIMRT'de şirketlerin minimum bir acil durum nakdi taşımaları zorunludur.

---

## Minimum Cash Rule

Her şirket dönem sonunda minimum:

```text
250.000 TL
```
# Taxation

SIMRT içerisinde vergi oranı sistem parametresi olarak tanımlanır.

Bu oran admin tarafından değiştirilebilir.

---

## Current Version

İlk sürümde:

```text
Tax Rate = 0%
``
