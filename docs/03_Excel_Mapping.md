# SIMRT Excel Mapping

## Amaç

Bu doküman Excel tabanlı SIMRT simülasyonundaki sayfaların yazılım mimarisindeki karşılıklarını tanımlar.

---

# Mapping Table

## Team

### Excel Amacı

Takımların, oyuncuların ve danışmanların tanımlanması.

### Yazılım Karşılığı

Domain Layer

### Modüller

- Team
- Player
- Advisor

### Kullanıcı

- Admin

---

## Limit&CoEff&Facts

### Excel Amacı

Oyun boyunca kullanılan katsayılar, limitler ve sabitlerin tutulması.

### İçerik Örnekleri

- Maliyet katsayıları
- Yatırım etkileri
- Kapasite limitleri
- Vade seçenekleri
- KPI ağırlıkları
- TOPSIS ağırlıkları

### Yazılım Karşılığı

Configuration Layer

### Modüller

- GameParameters
- InvestmentParameters
- CapacityParameters
- CreditParameters

---

## TOPSIS

### Excel Amacı

Müşteri satın alma davranışlarını hesaplamak.

### Girdiler

- Fiyat
- Marketing
- R&D
- Vade kararları

### Çıktılar

- Talep
- Satış adedi
- Pazar payı

### Yazılım Karşılığı

Market Engine

---

## Algorithm

### Excel Amacı

TOPSIS sonuçlarını ve oyuncu kararlarını kullanarak operasyonel ve finansal sonuçları hesaplamak.

### Girdiler

- TOPSIS sonuçları
- Karar girişleri
- Katsayılar

### Çıktılar

- Gelir
- Maliyet
- Stok
- Alacaklar
- Borçlar
- Kapasite

### Yazılım Karşılığı

Simulation Engine

---

## Financial Statements

### Excel Amacı

Finansal raporları oluşturmak.

### Çıktılar

- Gelir Tablosu
- Bilanço
- Nakit Akış Tablosu

### Yazılım Karşılığı

Financial Engine

---

## KPI

### Excel Amacı

Performans göstergelerini hesaplamak.

### Yazılım Karşılığı

KPI Engine

---

## Ranking

### Excel Amacı

Takımların sıralamasını oluşturmak.

### Yazılım Karşılığı

Ranking Engine

---

# Katmanlar

## Domain Layer

- Team
- Player
- Advisor
- Company
- Simulation

---

## Configuration Layer

- Limits
- Coefficients
- Facts

---

## Engine Layer

- Scenario Engine
- Market Engine
- Simulation Engine
- Financial Engine
- KPI Engine
- Ranking Engine

---

## Reporting Layer

- Dashboards
- Financial Reports
- Ranking Reports
