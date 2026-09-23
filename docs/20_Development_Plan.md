# SIMRT Development Plan

## Purpose

Bu doküman SIMRT'nin tasarımdan çalışan ürüne dönüşüm planını tanımlar.

Amaç:

- Geliştirme sırasını belirlemek
- Öncelikleri netleştirmek
- MVP hedeflerini yönetmek
- Teknik riski azaltmak

---

# Development Philosophy

Öncelik kullanıcı arayüzü değil, oyun motorudur.

SIMRT'nin en kritik bileşeni:

```text
Game Engine
```

olduğu için geliştirme sırası:

```text
Engine First
UI Later
```

olacaktır.

---

# Overall Roadmap

```text
Phase 1
Foundation

Phase 2
Core Engines

Phase 3
Database

Phase 4
Web Application

Phase 5
User Acceptance Testing

Phase 6
Production Ready MVP
```

---

# Phase 1

## Foundation

Amaç:

Temel yazılım mimarisini oluşturmak.

---

### Deliverables

```text
Domain Layer

Services Layer

Engine Skeletons
```

---

### Status

```text
Completed
```

---

# Phase 2

## Core Engines

Amaç:

Tüm hesaplama motorlarını çalışır hale getirmek.

---

### 2.1 State Update Engine

Görev:

- Brand Score
- Innovation Score
- Efficiency Score

hesaplamak.

---

### Input

```text
CompanyState
Decision History
