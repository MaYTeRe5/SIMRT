# SIMRT Results Panel Design

## Purpose

Results Panel, yıl sonunda şirket performansının analiz edildiği ekrandır.

Takımlar:

- Finansal sonuçlarını inceler
- KPI performanslarını değerlendirir
- Rakiplerle karşılaştırma yapar
- Güçlü ve zayıf yönlerini analiz eder

Bu ekran simülasyonun öğrenme değerini oluşturan en önemli ekrandır.

---

# Access Rules

Results Panel yalnızca:

```text
Year Closed
```

durumunda erişilebilir.

Yıl açıkken sonuçlar görüntülenemez.

---

# Screen Structure

```text
Results Dashboard
│
├── Executive Summary
├── Market Results
├── Financial Results
├── KPI Results
├── Ranking Results
├── Historical Trends
└── Benchmark Analysis
```

---

# Executive Summary

Takımın genel performans özeti.

---

## Displayed Information

- Company Name
- Team Name
- Current Year
- Current Ranking
- Ranking Score

---

## Key Highlights

- Market Share
- EBITDA
- Net Profit
- Cash Position
- Equity

---

# Market Results

Pazar performansı sonuçları gösterilir.

---

## Demand Information

Gösterilen bilgiler:

- Brand Loyalty Demand
- TOPSIS Demand
- Initial Demand
- Redistributed Demand
- Final Demand

---

## Market Share

```text
Market Share

=

Final Demand
/
Total Market Volume
```

---

## TOPSIS Information

Gösterilen bilgiler:

- TOPSIS Score
- Segment Performance

---

# Segment Results

Her segment için sonuçlar gösterilir.

---

## Value Segment

- Score
- Demand
- Share

---

## Balanced Segment

- Score
- Demand
- Share

---

## Premium Segment

- Score
- Demand
- Share

---

# Financial Results

---

## Income Statement

Gösterilen bilgiler:

- Revenue
- COGS
- Gross Profit
- EBITDA
- EBIT
- Interest Expense
- Net Profit

---

## Balance Sheet

Gösterilen bilgiler:

### Assets

- Cash
- Receivables
- Inventory
- Fixed Assets

---

### Liabilities

- Payables
- Debt

---

### Equity

- Equity

---

## Cash Flow Statement

Gösterilen bilgiler:

### Operating Cash Flow

### Investing Cash Flow

### Financing Cash Flow

### Ending Cash

---

# Operations Results

Şirketin operasyonel performansı.

---

## Production

- Production Quantity
- Sales Units
- Capacity

---

## Inventory

- Beginning Inventory
- Ending Inventory
- Inventory Value

---

## Utilization

```text
Capacity Utilization

=

Sales Units
/
Capacity
```

---

## Unit Cost

Dönem sonu birim maliyet.

---

# KPI Results

Official Ranking KPI'ları görüntülenir.

---

## Market Share

---

## EBITDA

---

## ROE

---

## Debt / Asset Ratio

---

## Inventory Turn

---

# Ranking Results

Yıl sonu sıralaması.

---

## Displayed Information

- Rank
- Ranking Score

---

## Ranking Method

TOPSIS

---

## Comparison Table

Tüm şirketlerin sıralaması gösterilir.

Örnek:

```text
Rank    Company      Score

1       Company A    0.821

2       Company C    0.774

3       Company B    0.711

4       Company D    0.653
```

---

# Historical Trends

Geçmiş yılların performans gelişimi.

---

## Revenue Trend

Year by Year

---

## Market Share Trend

Year by Year

---

## EBITDA Trend

Year by Year

---

## Equity Trend

Year by Year

---

## Ranking Trend

Year by Year

---

# Benchmark Analysis

Şirketin diğer şirketlerle karşılaştırılması.

---

## KPI Comparison

Gösterilen bilgiler:

- Team Value
- Simulation Average
- Leader Value

---

## Financial Comparison

Gösterilen bilgiler:

- Revenue
- EBITDA
- ROE
- Debt Ratio
- Inventory Turn

---

# Advisor View

Danışmanlar tüm sonuçları görüntüleyebilir.

---

## Permissions

Can:

- View Results
- View Trends
- View Benchmarks

Cannot:

- Modify Results
- Change Rankings

---

# Export Options

Takımlar sonuçlarını dışarı aktarabilir.

---

## Excel Export

---

## PDF Export

---

# Future Enhancements

İleride aşağıdaki raporlar eklenebilir:

- ESG Performance
- Carbon Impact
- AI Investment Performance
- Export Performance
- M&A Impact Analysis
``
