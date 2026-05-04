---
title: Интерактивные аннотации с использованием Python
linktitle: Интерактивные аннотации
type: docs
weight: 60
url: /python-net/interactive-annotations/
description: Узнайте, как добавлять, считывать и удалять аннотации‑ссылки, а также как создавать навигационные и кнопки печати в PDF‑документах с использованием Aspose.PDF for Python via .NET.
lastmod: "2026-04-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Работайте с интерактивными PDF‑аннотациями и кнопками в Python.
Abstract: В этой статье объясняется, как работать с интерактивными аннотациями в PDF‑файлах с использованием Aspose.PDF for Python via .NET. Рассматривается добавление ссылочных аннотаций, чтение существующих областей ссылок, удаление ссылочных аннотаций, создание кнопок навигации по страницам и добавление кнопки печати в PDF‑документ.
---

В этой статье показано, как работать с интерактивными аннотациями в PDF‑документах с использованием Aspose.PDF for Python via .NET.

Пример скрипта демонстрирует несколько общих рабочих процессов:

- добавить аннотацию ссылки к существующему тексту
- получить прямоугольники ссылочных аннотаций со страницы
- удалить аннотации ссылок
- создать кнопки навигации
- создать кнопку печати

## Аннотация ссылки

### Добавить аннотацию ссылки

Этот пример ищет фрагмент текста на первой странице `"file"` и размещает кликабельную аннотацию ссылки над соответствующей областью текста. Когда пользователь нажимает на аннотацию, PDF открывает указанный веб‑адрес.

#### Загрузите документ и найдите целевой текст

Создать `Document` объект и использовать `TextFragmentAbsorber` для поиска текста, который станет интерактивным.

```python
document = ap.Document(infile)
text_fragment_absorber = ap.text.TextFragmentAbsorber("file")

document.pages[1].accept(text_fragment_absorber)
phone_number_fragment = text_fragment_absorber.text_fragments[1]
```

#### Создать аннотацию ссылки

Создать `LinkAnnotation` используя прямоугольник найденного фрагмента текста и назначая для него действие URI.

```python
link_annotation = ap.annotations.LinkAnnotation(
    document.pages[1], phone_number_fragment.rectangle
)
link_annotation.action = ap.annotations.GoToURIAction("https://www.aspose.com")
```

#### Добавьте аннотацию и сохраните PDF

Добавьте аннотацию на страницу и сохраните обновлённый файл.

```python
document.pages[1].annotations.append(link_annotation)
document.save(outfile)
```

#### Полный пример

```python
def link_add(infile, outfile):
    document = ap.Document(infile)
    text_fragment_absorber = ap.text.TextFragmentAbsorber("file")

    document.pages[1].accept(text_fragment_absorber)
    phone_number_fragment = text_fragment_absorber.text_fragments[1]

    link_annotation = ap.annotations.LinkAnnotation(
        document.pages[1], phone_number_fragment.rectangle
    )
    link_annotation.action = ap.annotations.GoToURIAction("https://www.aspose.com")

    document.pages[1].annotations.append(link_annotation)
    document.save(outfile)
```

### Получить аннотацию ссылки

Чтобы просмотреть существующие интерактивные ссылки, отфильтруйте коллекцию аннотаций на первой странице и оставьте только элементы, тип которых `LINK`. Затем пример выводит прямоугольник для каждой соответствующей аннотации.

#### Загрузите PDF и соберите аннотации ссылок

```python
document = ap.Document(infile)
link_annotations = [
    a
    for a in document.pages[1].annotations
    if (a.annotation_type == ap.annotations.AnnotationType.LINK)
]
```

#### Прочитать прямоугольники аннотаций

Переберите отфильтрованные аннотации и выведите координаты каждой области ссылки.

```python
for link_annotation in link_annotations:
    print(link_annotation.rect)
```

#### Полный пример

```python
def link_get(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for link_annotation in link_annotations:
        print(link_annotation.rect)
```

### Удалить аннотацию ссылки

Этот рабочий процесс удаляет все аннотации ссылок с первой страницы и сохраняет очищенный PDF в новый файл.

#### Найдите аннотации ссылок для удаления

```python
document = ap.Document(infile)
link_annotations = [
    a
    for a in document.pages[1].annotations
    if (a.annotation_type == ap.annotations.AnnotationType.LINK)
]
```

#### Удалить каждую аннотацию ссылки

```python
for link_annotation in link_annotations:
    document.pages[1].annotations.delete(link_annotation)
```

#### Сохранить обновлённый документ

```python
document.save(outfile)
```

#### Полный пример

```python
def link_delete(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for link_annotation in link_annotations:
        document.pages[1].annotations.delete(link_annotation)

    document.save(outfile)
```

## Виджет-аннотация

### Добавить кнопку навигации

Кнопки навигации полезны в многостраничных PDF, когда вы хотите, чтобы читатели перемещались между страницами без использования интерфейса просмотрщика. Этот пример добавляет `Previous Page` и `Next Page` кнопки к каждой странице.

#### Определить настройки кнопки

Сохраните подписи кнопок, их позиции и предопределённые действия в простой список конфигурации.

```python
button_config = [
    ("Previous Page", 120.0, ap.annotations.PredefinedAction.PREV_PAGE),
    ("Next Page", 230.0, ap.annotations.PredefinedAction.NEXT_PAGE),
]
```

#### Загрузите PDF и убедитесь, что существует несколько страниц

Пример открывает исходный документ и добавляет ещё одну страницу, чтобы навигационные действия имели как минимум две страницы для работы.

```python
document = ap.Document(infile)
document.pages.add()
```

#### Создайте кнопки на каждой странице

Для каждой страницы создайте `ButtonField`, установить его текст и цвета, назначить предопределённое действие навигации и добавить его в форму.

```python
for page in document.pages:
    for name, x_pos, action in button_config:
        rect = ap.Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
        button = ap.forms.ButtonField(page, rect)
        button.partial_name = name
        button.value = name
        button.characteristics.border = ap.Color.red.to_rgb()
        button.characteristics.background = ap.Color.orange.to_rgb()
        button.actions.on_release_mouse_btn = ap.annotations.NamedAction(action)
        document.form.add(button)
```

#### Сохранить результат

```python
document.save(outfile)
```

#### Полный пример

```python
def navigation_buttons_add(infile, outfile):
    button_config = [
        ("Previous Page", 120.0, ap.annotations.PredefinedAction.PREV_PAGE),
        ("Next Page", 230.0, ap.annotations.PredefinedAction.NEXT_PAGE),
    ]

    document = ap.Document(infile)
    document.pages.add()

    for page in document.pages:
        for name, x_pos, action in button_config:
            rect = ap.Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
            button = ap.forms.ButtonField(page, rect)
            button.partial_name = name
            button.value = name
            button.characteristics.border = ap.Color.red.to_rgb()
            button.characteristics.background = ap.Color.orange.to_rgb()
            button.actions.on_release_mouse_btn = ap.annotations.NamedAction(action)
            document.form.add(button)

    document.save(outfile)
```

### Добавить кнопку печати

Этот пример создает новый одностраничный PDF и размещает кнопку печати возле верхней части страницы. Нажатие кнопки вызывает предопределённое действие печати в совместимом просмотрщике PDF.

#### Создайте новый PDF и добавьте страницу

```python
document = ap.Document()
page = document.pages.add()
```

#### Создать и настроить кнопку

Определите прямоугольник кнопки, создайте `ButtonField`, установите его подпись и прикрепите действие печати.

```python
rect = ap.Rectangle(72, 748, 164, 768, True)

print_button = ap.forms.ButtonField(page, rect)
print_button.alternate_name = "Print current document"
print_button.color = ap.Color.black
print_button.partial_name = "printBtn1"
print_button.value = "Print Document"
print_button.actions.on_release_mouse_btn = ap.annotations.NamedAction(
    ap.annotations.PredefinedAction.FILE_PRINT
)
```

#### Установить стили границы и фона

Пример определяет сплошную рамку и применяет пользовательские цвета, чтобы сделать кнопку видимой в документе.

```python
border = ap.annotations.Border(print_button)
border.style = ap.annotations.BorderStyle.SOLID
border.width = 2
print_button.border = border

print_button.characteristics.border = ap.Color.blue.to_rgb()
print_button.characteristics.background = ap.Color.light_blue.to_rgb()
```

#### Добавьте кнопку и сохраните PDF

```python
document.form.add(print_button)
document.save(outfile)
```

#### Полный пример

```python
def print_button_add(infile, outfile):
    document = ap.Document()
    page = document.pages.add()

    rect = ap.Rectangle(72, 748, 164, 768, True)

    print_button = ap.forms.ButtonField(page, rect)
    print_button.alternate_name = "Print current document"
    print_button.color = ap.Color.black
    print_button.partial_name = "printBtn1"
    print_button.value = "Print Document"
    print_button.actions.on_release_mouse_btn = ap.annotations.NamedAction(
        ap.annotations.PredefinedAction.FILE_PRINT
    )

    border = ap.annotations.Border(print_button)
    border.style = ap.annotations.BorderStyle.SOLID
    border.width = 2
    print_button.border = border

    print_button.characteristics.border = ap.Color.blue.to_rgb()
    print_button.characteristics.background = ap.Color.light_blue.to_rgb()

    document.form.add(print_button)
    document.save(outfile)
```

## Связанные темы

- [Импорт и экспорт аннотаций](/python-net/import-export-annotations/)
- [Разметка аннотаций](/python-net/markup-annotations/)
- [Медиа аннотации](/python-net/media-annotations/)
- [Аннотации безопасности](/python-net/security-annotations/)
- [Фигурные аннотации](/python-net/shape-annotations/)
- [Текстовые аннотации](/python-net/text-based-Annotations/)
- [Аннотации водяного знака](/python-net/watermark-annotations/)
