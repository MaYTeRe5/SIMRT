# SIMRT TOPSIS Matrix Design

## Purpose

Bu doküman SIMRT içerisinde kullanılan TOPSIS karar matrisinin yapısını ve hesaplama yöntemini tanımlar.

TOPSIS Engine'in görevleri:

- Şirketleri segment bazında karşılaştırmak
- Her şirket için segment bazlı tercih puanı üretmek
- TOPSIS talep havuzunun şirketler arasında dağıtılmasına temel oluşturmak
- Talep yeniden dağıtımında kullanılacak şirket puanlarını üretmek

TOPSIS yalnızca serbest talep havuzu için çalışır.

Brand Loyalty Demand, TOPSIS dışında hesaplanır.

---

## TOPSIS Position

```text
Market Volume Update
        ↓
Brand Loyalty Allocation
        ↓
TOPSIS Pool Calculation
        ↓
TOPSIS Matrix Generation
        ↓
Segment-Based TOPSIS Calculation
        ↓
Segment Demand Allocation
```

---

## TOPSIS Unit of Analysis

Her müşteri segmenti için ayrı bir TOPSIS hesaplaması yapılır.

Mevcut segmentler:

```text
Value

Balanced

Premium
```

Her segment:

- Aynı şirketleri
- Aynı karar matrisini
- Farklı kriter ağırlıklarını

kullanır.

Örnek:

```text
Value Segment

Company A
Company B
Company C
Company D
```

```text
Balanced Segment

Company A
Company B
Company C
Company D
```

```text
Premium Segment

Company A
Company B
Company C
Company D
```

---

## TOPSIS Criteria

TOPSIS aşağıdaki dört kriteri kullanır:

- Price
- Brand Score
- Innovation Score
- Credit Terms

---

### Price

Kaynak:

```text
Decision.Price
```

Kriter türü:

```text
Cost Criterion
```

Düşük fiyat daha avantajlıdır.

---

### Brand Score

Kaynak:

```text
State Update Result.Brand Score
```

Kriter türü:

```text
Benefit Criterion
```

Yüksek Brand Score daha avantajlıdır.

Brand Score, mevcut yıl ve geçmiş yıllardaki Marketing yatırımlarının zaman ağırlıklı etkisinden oluşur.

Mevcut yılın Marketing yatırımı aynı yılın TOPSIS hesaplamasına dahil edilir.

---

### Innovation Score

Kaynak:

```text
State Update Result.Innovation
