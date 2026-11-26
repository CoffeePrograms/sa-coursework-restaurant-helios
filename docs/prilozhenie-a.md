---
icon: material/file-code-outline
---

# Приложение А. Исходники схем

В [таблице А.1](#tablitsa-a-1) приведены исходники схем PlantUML, по которым сделаны рисунки документа. Рисунки на страницах — готовые PNG. Схемы C4 подключают стандартную библиотеку C4-PlantUML: `!include <C4/C4_Context>` и `!include <C4/C4_Container>`.

Таблица А.1 — Исходники схем PlantUML
{: #tablitsa-a-1 .caption }

| Рисунок | Название | Исходник |
| --- | --- | --- |
| [Рисунок 3.1](03-informacionnaya-model/3.1-domennaya-model.md#risunok-3-1) | Доменная модель | [domain_model.puml](diagrams/domain_model.puml) |
| [Рисунок 3.2](03-informacionnaya-model/3.2-logicheskaya-model-dannyh.md#risunok-3-2) | Логическая модель данных по сервисам | [data_model.puml](diagrams/data_model.puml) |
| [Рисунок 3.3](03-informacionnaya-model/3.5-perechisleniya-i-statusnye-modeli.md#risunok-3-3) | Статусная модель брони | [st_reservation.puml](diagrams/st_reservation.puml) |
| [Рисунок 3.4](03-informacionnaya-model/3.5-perechisleniya-i-statusnye-modeli.md#risunok-3-4) | Статусная модель меню на дату | [st_menu_schedule.puml](diagrams/st_menu_schedule.puml) |
| [Рисунок 4.1](04-arhitektura/4.2-diagrammy-c4.md#risunok-4-1) | Системный контекст, уровень 1 | [c4_L1.puml](diagrams/c4_L1.puml) |
| [Рисунок 4.2](04-arhitektura/4.2-diagrammy-c4.md#risunok-4-2) | Контейнеры системы, уровень 2 | [c4_L2.puml](diagrams/c4_L2.puml) |
| [Рисунок 4.3](04-arhitektura/4.2-diagrammy-c4.md#risunok-4-3) | Логи и мониторинг, уровень 2 | [c4_L2_service.puml](diagrams/c4_L2_service.puml) |
| [Рисунок 4.4](04-arhitektura/4.4-shema-i-opisanie-integracii.md#risunok-4-4) | Физическая схема взаимодействия | [physical.puml](diagrams/physical.puml) |
| [Рисунок 4.5](04-arhitektura/4.4-shema-i-opisanie-integracii.md#risunok-4-5) | Бронирование обеда | [seq_booking.puml](diagrams/seq_booking.puml) |
| [Рисунок 4.6](04-arhitektura/4.4-shema-i-opisanie-integracii.md#risunok-4-6) | Вход и проверка прав | [seq_login.puml](diagrams/seq_login.puml) |
| [Рисунок 7.1](07-rezultat/7.1-chto-realizovano.md#risunok-7-1) | Экран выбора блюд из меню на день | [screen_menu.html](assets/screen-menu/screen_menu.html) |

Макет экрана меню открывается в браузере: [screen_menu.html](assets/screen-menu/screen_menu.html). Фото блюд сгенерированы, источники записаны в [sources.json](assets/screen-menu/sources.json).

- [assets/screen-menu/img/borsch_card.jpg](assets/screen-menu/img/borsch_card.jpg)
- [assets/screen-menu/img/borsch_gen.jpg](assets/screen-menu/img/borsch_gen.jpg)
- [assets/screen-menu/img/cutlet_card.jpg](assets/screen-menu/img/cutlet_card.jpg)
- [assets/screen-menu/img/cutlet_gen.jpg](assets/screen-menu/img/cutlet_gen.jpg)
- [assets/screen-menu/img/mors_card.jpg](assets/screen-menu/img/mors_card.jpg)
- [assets/screen-menu/img/mors_gen.jpg](assets/screen-menu/img/mors_gen.jpg)
- [assets/screen-menu/img/noodle_card.jpg](assets/screen-menu/img/noodle_card.jpg)
- [assets/screen-menu/img/noodle_gen.jpg](assets/screen-menu/img/noodle_gen.jpg)
- [assets/screen-menu/img/olivier_card.jpg](assets/screen-menu/img/olivier_card.jpg)
- [assets/screen-menu/img/olivier_gen.jpg](assets/screen-menu/img/olivier_gen.jpg)
- [assets/screen-menu/img/pasta_card.jpg](assets/screen-menu/img/pasta_card.jpg)
- [assets/screen-menu/img/pasta_gen.jpg](assets/screen-menu/img/pasta_gen.jpg)
- [assets/screen-menu/img/tea_card.jpg](assets/screen-menu/img/tea_card.jpg)
- [assets/screen-menu/img/tea_gen.jpg](assets/screen-menu/img/tea_gen.jpg)
- [assets/screen-menu/img/vegsalad_card.jpg](assets/screen-menu/img/vegsalad_card.jpg)
- [assets/screen-menu/img/vegsalad_gen.jpg](assets/screen-menu/img/vegsalad_gen.jpg)
- [assets/screen-menu/screen_menu.html](assets/screen-menu/screen_menu.html)
- [assets/screen-menu/sources.json](assets/screen-menu/sources.json)
