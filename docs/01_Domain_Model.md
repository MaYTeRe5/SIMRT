# SIMRT Domain Model

## Amaç

Bu doküman SIMRT simülasyonundaki temel iş varlıklarını (business entities) tanımlar.

Domain modeli oyun kurallarından bağımsızdır.

TOPSIS, finansal hesaplar ve ranking mekanizmaları bu dokümanın kapsamı dışındadır.

---

# Simulation

Bir simülasyon oyununu temsil eder.

Örnek:

- SIMRT Leadership Challenge 2027

Özellikler:

- Başlangıç tarihi
- Aktif yıl
- Toplam yıl sayısı
- Durum

---

# Team

Oyunculardan oluşan ekip.

Özellikler:

- Takım adı
- Üyeler
- Danışman
- Atanmış şirket

---

# Player

Takım üyesi.

Özellikler:

- Ad
- Soyad
- E-posta

---

# Advisor

Takımlara destek veren danışman.

Özellikler:

- Ad
- Soyad
- E-posta

---

# Company

Simülasyondaki şirket.

Özellikler:

- Şirket kodu
- Şirket adı

---

# Simulation Year

Simülasyonun her yılı.

Özellikler:

- Yıl numarası
- Senaryo
- Durum

---

# Scenario

İlgili yılın pazar koşulları.

Özellikler:

- Pazar hacmi
- Faiz oranı
- Enflasyon
- Ham madde maliyeti

---

# Decision

Takım tarafından verilen kararlar.

Karar tipleri:

- Ticari
- Operasyonel
- Finansal

---

# Company State

Bir yıl sonundaki şirket durumu.

Özellikler:

- Nakit
- Borç
- Özkaynak
- Kapasite
- Stok
- Pazar payı
