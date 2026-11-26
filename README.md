# Таверна Helios

Документация сервиса бронирования обедов: сотрудники компании выбирают блюда из меню на день, время и место за столом, менеджер передает ресторану отчет.

Учебный командный проект, программа OTUS «C# ASP.NET Core разработчик». Проект выполнен с января по июнь 2025 года, документ я переработала в 2026 году.

Сайт: https://coffeeprograms.github.io/sa-coursework-restaurant-helios/

Репозиторий кода: https://github.com/CoffeePrograms/coursework-restaurant-helios

## Что внутри

- Бизнес-требования, бизнес-процессы, ограничения, нефункциональные требования и пользовательские истории
- Доменная и логическая модели, связи, кратность и статусные модели
- Обоснование архитектурного стиля, диаграммы C4 и интеграции
- Перечень API и контракт метода POST /api/Reservation
- Критерии приемки, результат ревизии кода и спринты
- Исходники схем PlantUML: [docs/diagrams](docs/diagrams)

## Автор

Липова Эльвира Евгеньевна, системный аналитик и разработчик. 6 лет — разработчик C#, 1 год — системный аналитик.

Telegram-канал: [Эльвира Липова · От требований к коду](https://t.me/lipova_ee)

Telegram: [@CoffeePrograms](https://t.me/CoffeePrograms)

## Стек документации

MkDocs Material, PlantUML, GitHub Actions → Pages.

## Локальная сборка

Нужен Python 3.12.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Сайт откроется по адресу http://127.0.0.1:8000/

```bash
mkdocs build --strict
```

## Публикация

Workflow [.github/workflows/pages.yml](.github/workflows/pages.yml) собирает сайт командой `mkdocs build --strict` и публикует каталог `site` на GitHub Pages при push в ветку `main` и при ручном запуске.

В настройках репозитория нужно один раз выбрать источник: Settings → Pages → Build and deployment → Source: **GitHub Actions**.

После этого адрес сайта: https://coffeeprograms.github.io/sa-coursework-restaurant-helios/
