"""Иконки разделов левого меню, у которых нет собственной страницы."""

SECTION_ICONS = {
    "1. Бизнес-требования": "material/silverware-fork-knife",
    "2. Требования к приложению": "material/file-document-outline",
    "3. Информационная модель": "material/graph-outline",
    "4. Архитектура": "material/sitemap",
    "5. API": "material/api",
    "7. Результат": "material/clipboard-check-outline",
}
def on_nav(nav, config, files):
    for item in nav.items:
        icon = SECTION_ICONS.get(getattr(item, "title", None))
        if icon and not getattr(item, "meta", None):
            item.meta = {"icon": icon}
    return nav
