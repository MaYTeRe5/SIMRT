# SIMRT Engine Specification

## Purpose

Bu doküman SIMRT oyun motorunun çalışma mantığını tanımlar.

---

# Engine Overview

SIMRT motoru aşağıdaki sırayla çalışır.

```text
Scenario
    ↓
Decision
    ↓
TOPSIS
    ↓
Algorithm
    ↓
Financial Results
    ↓
KPI Calculation
    ↓
Ranking
```

---

# Engine Modules

## Scenario Engine

Pazar koşullarını belirler.

Örnek:

- Pazar büyüklüğü
- Faiz oranları
- Maliyet katsayıları
- Segment davranışları

---

## Decision Engine

Takımların kararlarını toplar.

Örnek:

- Fiyat
- Marketing
- Product R&D
- Process R&D
- Üretim
- Vade kararları

---

## TOPSIS Engine

Müşteri satın alma tercihlerini hesaplar.

Çıktı:

- Takım bazında talep
- Satış adetleri
- Pazar payı

---

## Algorithm Engine

TOPSIS sonuçlarını ve kararları kullanarak operasyonel sonuçları hesaplar.

Kaynaklar:

- TOPSIS çıktıları
- Oyuncu kararları
- Limit&CoEff&Facts parametreleri

Çıktılar:

- Gelir
- Maliyet
- Stok
- Alacaklar
- Borçlar
- Kapasite

---

## Financial Engine

Finansal tabloları oluşturur.

Çıktılar:

- Gelir Tablosu
- Bilanço
- Nakit Akış Tablosu

---

## KPI Engine

Performans göstergelerini hesaplar.

Örnek:

- Market Share
- Revenue Growth
- EBITDA
- Cash Position

---

## Ranking Engine

TOPSIS yöntemi ile takım sıralamasını oluşturur.

Çıktılar:

- Yıllık sıralama
- Genel sıralama
