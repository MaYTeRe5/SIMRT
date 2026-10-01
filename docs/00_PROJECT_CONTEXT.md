# SIMRT Project Context

## Project Name

SIMRT

Strategic Integrated Management & Results Tournament

---

# Project Purpose

SIMRT, Capsim ve Cesim benzeri bir işletme yönetim simülasyonudur.

Katılımcılar ekipler halinde şirket yönetim kurulu rolünü üstlenir.

Her ekip bir şirketi yönetir.

Amaç:

- Pazar payı yaratmak
- Karlılık sağlamak
- Nakit yönetmek
- Şirket değerini artırmak

Nihai başarı ölçümü TOPSIS tabanlı Ranking Engine ile yapılır.

---

# Source of Truth

GitHub repository proje için tek gerçek kaynaktır.

```text
GitHub
=
Source of Truth
```

Replit yalnızca:

```text
Development
Testing
Execution
```

ortamıdır.

---

# Working Method

Kod geliştirme süreci:

```text
1. GitHub'da değişiklik yapılır

2. Commit edilir

3. Replit güncellenir

git fetch origin
git reset --hard origin/main

4. Test çalıştırılır

5. Sonuç doğrulanır
```

---

# Confirmed Business Rules

## Company Structure

Tüm şirketler eşit başlar.

Başlangıç verileri:

```text
Starting Point
```

sheetinden gelir.

---

## Market Structure

Segmentler:

- Value
- Balanced
- Premium

---

## TOPSIS Inputs

Kriterler:

- Price
- Brand Score
- Innovation Score
- Credit Terms

---

## Criterion Types

### Cost Criterion

```text
Price
```

---

### Benefit Criteria

```text
Brand Score

Innovation Score

Credit Terms
```

---

## Brand Loyalty

Brand Loyalty Rate senaryo tarafından belirlenir.

Brand Loyalty Demand:

```text
Current Market Volume
×
Brand Loyalty Rate
```

---

## Brand Loyalty Distribution

Tüm aktif şirketlere eşit dağıtılır.

---

## Brand Loyalty Price Rule

Şirket fiyatı:

```text
Average Market Price
×
Brand Loyalty Price Limit
```

eşik değerini aşarsa:

```text
Brand Loyalty Demand = 0
```

olur.

---

## Lost Loyalty Rule

Kaybedilen sadakat talebi diğer şirketlere verilmez.

TOPSIS havuzuna geri döner.

---

## Redistribution Rule

Karşılanamayan talebin tamamı yeniden dağıtıma çıkar.

---

## Eligible Company Rule

Sadece:

```text
remaining_supply > 0
```

olan şirketler yeniden dağıtıma katılır.

---

## Redistribution Score

```text
Value Score
+
Balanced Score
+
Premium Score
```

toplamıdır.

---

## Redistribution Score Total

Sadece uygun şirketlerin skorları kullanılır.

---

## Redistribution Round Count

Maksimum:

```text
2 redistribution round
```

uygulanır.

---

## Lost Demand

Round 2 sonrasında hala karşılanamayan talep varsa:

```text
Lost Demand
```

olarak kaybolur.

Satışa dönüşmez.

---

# Finance Rules

## Inventory Valuation

```text
Weighted Average Cost
```

kullanılır.

---

## Product R&D

Muhasebe sınıfı:

```text
OPEX
```

TOPSIS etkisi:

```text
Innovation Score
```

---

## Process R&D

Muhasebe sınıfı:

```text
CAPEX
```

etkisi:

```text
Efficiency Score
↓
Unit Cost Reduction
```

---

## Capacity Investment

Muhasebe sınıfı:

```text
CAPEX
```

---

## Depreciation

Tüm CAPEX kalemleri:

- Capacity Investment
- Process R&D
- Starting Point Fixed Assets

için:

```text
10 Year Straight Line
```

uygulanır.

---

## Minimum Cash Requirement

Şu anki varsayılan değer:

```text
250.000 TL
```

Ancak bu:

```text
Variable List
```

tarafından yönetilecek.

Admin tarafından değiştirilebilir.

---

## Tax

Current Version:

```text
Tax Rate = 0%
```

---

## Loss Carry Forward

Desteklenir.

---

## Target Annual Execution Flow

```text
Starting Point / Previous Company State
↓
Decision + Scenario + Variable List
↓
State Update Engine
↓
Algorithm Pre-Market Phase
↓
Market Engine
↓
Demand Redistribution Engine
↓
Algorithm Post-Market Phase
↓
Financial Processing
↓
Treasury Processing
↓
KPI Engine
↓
Ranking Engine
↓
Persist New Company State
↓
Publish Results
```

The Algorithm layer is divided into pre-market and post-market phases.
The pre-market phase prepares:
Available capacity
Actual production
Available product
Cost preparation
The post-market phase calculates:
Final sales
Ending inventory
Revenue
COGS
Gross profit


---

## Architecture Rules

### Dependency Direction

Allowed:

Engine → Domain
Service → Engine
Service → Domain

Forbidden:

Domain → Engine
Domain → Service

### Validation Rule

A feature is NOT considered completed unless:

- implemented
- committed
- tested
- verified

### Documentation Rule

Architectural decisions must be documented through ADRs.

### Source of Truth Rule

GitHub is the single source of truth.

If there is a conflict between:

- conversation
- AI memory
- Replit
- documentation

GitHub repository takes priority.

### Excel Validation Rule

Excel Rule Wins.

Whenever a difference exists between:

- academic theory
- software convention
- Excel calculation

validated Excel behavior wins.

### Balance Sheet Rule

Every completed company-year calculation must satisfy:

Assets = Liabilities + Equity

### Configuration Rule

Scenario-dependent values should eventually be controlled by Variable List rather than hard-coded values.


# Future Features

Planned:

- Industry PR
- Market Insight Purchase
- ESG Module
- Carbon Tax
- AI Investments
- Export Markets
- M&A

---

# Guiding Principle

Whenever there is a conflict between:

```text
Academic Theory
vs
Excel Engine
```

use:

```text
Excel Rule Wins
```

Goal:

```text
Excel Result
=
Python Result
```
## AI Onboarding Protocol 
Before contributing to SIMRT, an AI assistant or developer must review the project in the following order: 
1. `docs/00_PROJECT_CONTEXT.md`
2. `docs/22_CURRENT_STATUS.md`
3. Relevant files under `docs/adr/`
4. Recent entries in `docs/23_AI_WORKLOG.md`
5. Relevant domain models
6.  Relevant engine implementations
7.  Relevant tests
8.  Available Excel reconciliation evidence

The assistant must never assume that: 
- Proposed code was implemented
- A suggested file was created
- A change was committed to GitHub
- A test was executed
- A test passed
- A feature was completed
unless this has been explicitly verified.

If sources conflict, use the following priority: 
1. GitHub repository
2. Passing test results
3. Validated Excel results
4. Current status documentation
5. Worklog and ADR documents
6. Conversations and AI-generated summaries

Before recommending a new implementation step, identify: 
- Goal
- Relevant business rule
- Affected files
- Expected inputs
- Expected outputs
- Acceptance criteria
- Required tests

A feature is complete only when it is: 
- Implemented
- Committed
- Tested
- Verified
