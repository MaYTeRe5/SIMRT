# SIMRT Variable List Design

## Purpose

Variable List, oyun boyunca kullanılan tüm parametrelerin merkezi kaynağıdır.

Bu parametreler:

- Senaryoları yönetmek
- Oyun dengesini değiştirmek
- Yeni oyunlar oluşturmak

amacıyla kullanılır.

Variable List yalnızca Admin tarafından değiştirilebilir.

---

# Structure

Variable List aşağıdaki gruplardan oluşur:

- Market Parameters
- Segment Parameters
- Brand Loyalty Parameters
- TOPSIS Parameters
- Capacity Parameters
- Efficiency Parameters
- Financial Parameters
- Tax Parameters

---

# Market Parameters

## Market Growth Rate

Yıllık pazar büyüme oranı.

Örnek:

```text
-5%
+10%
+25%
```

---

## Market Volume

Bir önceki yıl üzerine uygulanır.

```text
Current Market

=

Previous Market
×
(1 + Growth Rate)
```

---

# Segment Parameters

Her yıl için segment dağılımları tanımlanır.

Örnek:

```text
Value Segment Share

Balanced Segment Share

Premium Segment Share
```

---

# Validation Rule

Segment toplamı:

```text
100%
```

olmalıdır.

---

# Brand Loyalty Parameters

## Brand Loyalty Rate

Toplam pazarın ne kadarının marka bağlılığı ile dağıtılacağını belirler.

Örnek:

```text
10%
20%
40%
```

---

## Brand Loyalty Price Limit

Şirketlerin marka bağlılığı hakkını kaybettiği eşik değeri tanımlar.

Örnek:

```text
175%
```

---

# TOPSIS Parameters

Her segment için ağırlıklar.

---

## Value Segment

```text
Price Weight

Brand Weight

Innovation Weight

Credit Terms Weight
```

---

## Balanced Segment

```text
Price Weight

Brand Weight

Innovation Weight

Credit Terms Weight
```

---

## Premium Segment

```text
Price Weight

Brand Weight

Innovation Weight

Credit Terms Weight
```

---

# Validation Rule

Her segment için:

```text
Toplam Ağırlık = 100%
```

olmalıdır.

---

# Capacity Parameters

## Capacity Investment Unit

Varsayılan:

```text
1.000.000 TL
```

---

## Capacity Increase Rate

Varsayılan:

```text
5%
```

---

## Capacity Activation

Varsayılan:

```text
Immediate
```

Yatırım yapıldığı yıl aktif olur.

---

# Efficiency Parameters

## Efficiency Investment Unit

Varsayılan:

```text
1.000.000 TL
```

---

## Cost Reduction Rate

Varsayılan:

```text
2%
```

---

## Maximum Annual Cost Reduction

Varsayılan:

```text
10%
```

---

# Financial Parameters

## Emergency Cash Requirement

Varsayılan:

```text
250.000 TL
```

---

## Loan Interest Rate

Senaryo tarafından belirlenebilir.

---

## Deposit Interest Rate

Senaryo tarafından belirlenebilir.

---

## Depreciation Method

Varsayılan:

```text
Straight Line
```

---

## Depreciation Life

Varsayılan:

```text
10 Years
```

---

# Tax Parameters

## Tax Rate

Varsayılan:

```text
0%
```

---

## Loss Carry Forward

Varsayılan:

```text
Enabled
```

---

## Minimum Tax

Varsayılan:

```text
Disabled
```

---

# Year Based Configuration

Tüm parametreler yıl bazında tanımlanabilir.

Örnek:

```text
Year 1

Brand Loyalty Rate = 10%

Market Growth = 5%

Interest Rate = 20%
```

---

```text
Year 2

Brand Loyalty Rate = 25%

Market Growth = -10%

Interest Rate = 35%
```

---

# Admin Control

Admin aşağıdaki işlemleri yapabilir:

- Yeni yıl parametreleri girmek
- Mevcut parametreleri değiştirmek
- Oyun zorluk seviyesini değiştirmek
- Yeni senaryolar oluşturmak

---

# Future Extensions

İleride aşağıdaki parametre grupları eklenebilir:

- ESG
- Carbon Tax
- FX Rates
- Export Markets
- M&A Rules
- AI Investments
