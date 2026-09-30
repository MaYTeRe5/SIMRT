# ADR-0001: GitHub as the Single Source of Truth

## Status

Accepted

## Context

SIMRT uzun süreli ve sürekli geliştirilecek bir yazılım projesidir.

Proje geliştirme sürecinde aşağıdaki araçlar kullanılmaktadır:

- GitHub
- Replit
- Microsoft 365 Copilot

Kodun GitHub ve Replit üzerinde ayrı ayrı değiştirilmesi sürüm farklılıklarına, çakışmalara ve hangi dosyanın güncel olduğuna ilişkin belirsizliğe neden olabilir.

Uzun konuşma geçmişleri de proje bağlamını tek başına güvenli ve kalıcı biçimde taşımak için yeterli değildir.

Bu nedenle kod, dokümantasyon, testler ve proje kararları için tek ve açık bir ana kaynak belirlenmelidir.

## Decision

GitHub repository, SIMRT projesinin tek gerçek ve kalıcı bilgi kaynağıdır.

```text
GitHub = Source of Truth
``
