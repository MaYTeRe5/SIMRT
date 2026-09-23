# State Update Design

## Purpose

Bu doküman Market Engine çalışmadan önce Company State değişkenlerinin nasıl güncellendiğini tanımlar.

Amaç:

- Brand Score
- Innovation Score
- Efficiency Score

değerlerini güncellemek ve Market Engine'e güncel değerlerle veri sağlamak.

---

# Engine Position

```text
Previous Company State
        ↓

Decision
        ↓

State Update Engine
        ↓

Updated Company State
        ↓

Market Engine
        ↓

Algorithm Engine
```

---

# Update Timing Rule

Marketing ve R&D yatırımları yapıldıkları yıl etkilerini gösterir.

Bu nedenle State Update işlemi Market Engine'den önce çalıştırılır.

---

# Updated Variables

## Brand Score

Kaynak:

```text
Marketing Investments
```

---

## Innovation Score

Kaynak:

```text
Product R&D Investments
```

---

## Efficiency Score

Kaynak:

```text
Process R&D Investments
```

---

# Historical Impact Principle

Geçmiş yatırımlar tamamen kaybolmaz.

Ancak etkileri zamanla azalır.

---

# Formula

```text
Current Year Investment

+

Previous Year Investment / 2

+

Two Years Ago Investment / 3

+

Three Years Ago Investment / 4

+
...
```

---

# Brand Score

```text
Brand Score

=

Current Marketing

+

Previous Marketing / 2

+

Older Marketing / 3

+
...
```

---

# Innovation Score

```text
Innovation Score

=

Current Product R&D

+

Previous Product R&D / 2

+

Older Product R&D / 3

+
...
```

---

# Efficiency Score

```text
Efficiency Score

=

Current Process R&D

+

Previous Process R&D / 2

+

Older Process R&D / 3

+
...
```

---

# Output

State Update Engine aşağıdaki güncellenmiş değerleri üretir:

- Brand Score
- Innovation Score
- Efficiency Score

Bu değerler doğrudan Market Engine tarafından kullanılır.
