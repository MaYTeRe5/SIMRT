# SIMRT Decision Entry Design

## Purpose

Decision Entry ekranı takımların her simülasyon yılı için şirket kararlarını girdiği ana ekrandır.

Tüm ticari, operasyonel ve finansal kararlar bu ekran üzerinden toplanır.

Her takım bir yıl için yalnızca bir karar seti gönderir.

---

# Screen Position

```text
Login
    ↓

Team Dashboard
    ↓

Decision Entry
    ↓

Submit Decision
```

---

# Decision Categories

Kararlar üç ana gruba ayrılır:

- Commercial Decisions
- Operations Decisions
- Finance Decisions

---

# Commercial Decisions

## Price

Ürün satış fiyatı.

---

### Data Type

```text
Decimal
```

---

### Validation

```text
Price > 0
```

---

### Engine Impact

- Market Engine
- TOPSIS
- Revenue Calculation

---

## Marketing Investment

Marka yatırımı.

---

### Data Type

```text
Currency
```

---

### Validation

```text
Marketing >= 0
```

---

### Engine Impact

- State Update Engine
- Brand Score
- TOPSIS

---

## Product R&D Investment

Ürün geliştirme yatırımı.

---

### Data Type

```text
Currency
```

---

### Validation

```text
Product R&D >= 0
```

---

### Financial Classification

```text
OPEX
```

---

### Engine Impact

- State Update Engine
- Innovation Score
- TOPSIS

---

## Customer Credit Terms (AR Days)

Müşteriye verilen vade.

---

### Data Type

```text
Single Select
```

---

### Allowed Values

```text
0
30
60
90
120
150
180
210
240
270
300
330
360
```

---

### Validation

Sadece tanımlı seçeneklerden biri seçilebilir.

---

### Engine Impact

- TOPSIS
- Receivables Calculation

---

# Operations Decisions

## Production Quantity

Üretilecek ürün miktarı.

---

### Data Type

```text
Integer
```

---

### Validation

```text
Production Quantity >= 0
```

---

### Engine Impact

- Algorithm Engine
- Inventory
- Sales

---

## Capacity Investment

Kapasite artırımı yatırımı.

---

### Data Type

```text
Currency
```

---

### Validation

```text
Capacity Investment >= 0
```

---

### Financial Classification

```text
CAPEX
```

---

### Engine Impact

- Capacity Increase
- Fixed Assets
- Depreciation

---

## Process R&
