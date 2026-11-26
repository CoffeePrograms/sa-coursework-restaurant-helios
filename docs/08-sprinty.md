---
icon: material/calendar-month
---

# 8. Спринты

Работа разбита на спринты длительностью 1 месяц ([таблица 8.1](#tablitsa-8-1)). Истории бэклога в спринты не вошли. Нагрузочное тестирование планировалось в спринте 4 и перенесено в бэклог ([US-17](06-kriterii/6.7-istorii-bekloga.md#us-17)).

Таблица 8.1 — Спринты и состав работ
{: #tablitsa-8-1 .caption }

| Спринт | Длительность | Что вошло | Истории | Статус |
| --- | --- | --- | --- | --- |
| Спринт 1. Базовый функционал | 1 месяц | Меню на день, управление меню на сервере, выбор блюд, список обедов, BFF и gRPC между сервисами | [US-01](06-kriterii/6.1-menyu.md#us-01), [US-03](06-kriterii/6.2-bronirovanie-obeda.md#us-03) | Реализовано |
| Спринт 2. Меню, доступ, логи | 1 месяц | Меню с датой активности, создание обеда, отчет в PDF и Excel, регистрация по логину и паролю с проверкой данных, скрытие недоступных функций, структурные логи через RabbitMQ | [US-01](06-kriterii/6.1-menyu.md#us-01), [US-05](06-kriterii/6.2-bronirovanie-obeda.md#us-05), [US-06](06-kriterii/6.3-otchety-dlya-restorana.md#us-06), [US-07](06-kriterii/6.3-otchety-dlya-restorana.md#us-07), [US-12](06-kriterii/6.4-polzovateli-i-roli.md#us-12), [US-14](06-kriterii/6.4-polzovateli-i-roli.md#us-14), [US-15](06-kriterii/6.5-monitoring.md#us-15) | Частично: правила брони проверяет только интерфейс, роли на сервере проверяются не везде, см. [раздел 7.2](07-rezultat/7.2-naydeno-pri-revizii.md) |
| Спринт 3. Схема зала, метрики, роли | 1 месяц | Схема зала, выбор места с обновлением через SignalR, роли администратора и менеджера, Prometheus и Grafana | [US-18](06-kriterii/6.6-shema-zala.md#us-18), [US-04](06-kriterii/6.2-bronirovanie-obeda.md#us-04), [US-13](06-kriterii/6.4-polzovateli-i-roli.md#us-13), [US-16](06-kriterii/6.5-monitoring.md#us-16) | Частично: занятость места не проверяется на сервере, метрики сервисов не собираются, см. [раздел 7.2](07-rezultat/7.2-naydeno-pri-revizii.md) |
| Спринт 4. Качество | 1 месяц | CI с шагом тестов, модульные тесты, внешний кеш (Redis) в BFF | — | Частично: есть CI в GitHub Actions с тестами и деплоем, тесты сервисов меню и брони и контроллеров; нет Redis в BFF |
| Спринт 5. Доработки интерфейса | 1 месяц | Скрытие пустых разделов времени в отчете и пустых типов блюд в меню | [US-03](06-kriterii/6.2-bronirovanie-obeda.md#us-03), [US-06](06-kriterii/6.3-otchety-dlya-restorana.md#us-06) | Частично: в отчете пустые разделы времени скрываются, в редакторе меню скрываются пустые типы блюд; на экране сотрудника пустой тип показывается ([US-03](06-kriterii/6.2-bronirovanie-obeda.md#us-03) [AC-4](06-kriterii/6.2-bronirovanie-obeda.md#us-03-ac-4)) |
| Бэклог | — | Вход через Яндекс, загрузка меню из iiko, передача обедов через API, отправка отчета по email и по расписанию, удаление данных старше 30 дней, нагрузочное тестирование | [US-02](06-kriterii/6.7-istorii-bekloga.md#us-02), [US-08](06-kriterii/6.7-istorii-bekloga.md#us-08)–[US-10](06-kriterii/6.7-istorii-bekloga.md#us-10), [US-11](06-kriterii/6.7-istorii-bekloga.md#us-11), [US-17](06-kriterii/6.7-istorii-bekloga.md#us-17), [US-19](06-kriterii/6.7-istorii-bekloga.md#us-19) | Не реализовано |
