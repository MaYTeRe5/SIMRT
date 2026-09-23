# SIMRT ERD Design

## Purpose

Bu doküman SIMRT veritabanı tasarımının mantıksal modelini tanımlar.

Amaç:

- Domain nesnelerini veritabanına dönüştürmek
- İlişkileri tanımlamak
- Yazılım geliştirme aşamasında referans oluşturmak

---

# High Level ERD

```text
Simulation
│
├── Teams
│   ├── Players
│   └── Advisors
│
├── Companies
│
├── Scenarios
│   ├── Segments
│   └── Segment Preferences
│
├── Decisions
│
├── Company States
│
├── Market Results
│
├── Financial Results
│
├── KPI Results
│
└── Ranking Results
```

---

# Simulation

Bir simülasyonu temsil eder.

## Fields

- id (PK)
- name
- current_year
- total_years
- status

---

# Team

Bir oyuncu takımını temsil eder.

## Fields

- id (PK)
- simulation_id (FK)
- assigned_company_id (FK)
- advisor_id (FK)
- name

---

# Player

Oyuncu bilgileri.

## Fields

- id (PK)
- first_name
- last_name
- email

---

# TeamPlayer

Takım üyelik tablosu.

## Fields

- team_id (FK)
- player_id (FK)

---

# Advisor

Danışman bilgileri.

## Fields

- id (PK)
- first_name
- last_name
- email

---

# Company

Simülasyondaki şirket.

## Fields

- id (PK)
- simulation_id (FK)
- name

---

# StartingPoint

Başlangıç finansal durumu.

## Fields

- id (PK)

- cash
- debt
- equity

- capacity
- inventory_units

- brand_score
- innovation_score
- efficiency_score

---

# Scenario

Yıl bazlı makro koşullar.

## Fields

- id (PK)
- simulation_id (FK)

- year_no

- market_growth_rate

- interest_rate
- deposit_rate

- inflation_rate

- brand_loyalty_rate

- brand_loyalty_price_limit

- tax_rate

---

# Segment

Müşteri segmentleri.

## Fields

- id (PK)
- scenario_id (FK)

- name

- share_percent

---

# SegmentPreference

TOPSIS ağırlıkları.

## Fields

- id (PK)

- scenario_id (FK)

- segment_id (FK)

- weight_price

- weight_brand

- weight_innovation

- weight_credit_terms

---

# Decision

Takım kararları.

## Fields

- id (PK)

- company_id (FK)

- year_no

- price

- marketing_investment

- product_rd

- process_rd

- production_quantity

- capacity_investment

- ar_days

- ap_days

---

# CompanyState

Bir şirketin yıl sonu durumu.

## Fields

- id (PK)

- company_id (FK)

- year_no

- demand_units
- sales_units

- market_share

- capacity

- inventory_units

- utilization_rate

- revenue

- gross_profit

- ebit

- net_profit

- cash

- debt

- equity

- receivables

- payables

- brand_score

- innovation_score

- efficiency_score

---

# MarketResult

Market Engine çıktısı.

## Fields

- id (PK)

- company_id (FK)

- year_no

- topsis_score

- brand_loyalty_demand

- topsis_demand

- initial_demand

- redistributed_demand

- final_demand

- market_share

---

# AlgorithmResult

Algorithm Engine çıktısı.

## Fields

- id (PK)

- company_id (FK)

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

---

# FinancialResult

Financial Engine çıktısı.

## Fields

- id (PK)

- company_id (FK)

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

---

# KPIResult

KPI Engine çıktısı.

## Fields

- id (PK)

- company_id (FK)

- year_no

- market_share

- ebitda

- roe

- debt_asset_ratio

- inventory_turn

---

# RankingResult

Ranking Engine çıktısı.

## Fields

- id (PK)

- company_id (FK)

- year_no

- ranking_score

- rank

---

# Key Relationships

```text
Simulation
    1
    ↓
    N
Team
```

```text
Simulation
    1
    ↓
    N
Company
```

```text
Team
    N
    ↓
    N
Player
```

```text
Scenario
    1
    ↓
    N
Segment
```

```text
Segment
    1
    ↓
    1
SegmentPreference
```

```text
Company
    1
    ↓
    N
Decision
```

```text
Company
    1
    ↓
    N
CompanyState
```

```text
Company
    1
    ↓
    N
MarketResult
```

```text
Company
    1
    ↓
    N
FinancialResult
```

```text
Company
    1
    ↓
    N
KPIResult
```

```text
Company
    1
    ↓
    N
RankingResult
```
