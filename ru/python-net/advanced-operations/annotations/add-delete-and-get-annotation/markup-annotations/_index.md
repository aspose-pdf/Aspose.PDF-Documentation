---
title: Разметка аннотаций с помощью Python
linktitle: Разметка аннотаций
type: docs
weight: 30
url: /python-net/markup-annotations/
description: Узнайте, как добавлять, считывать и удалять текст, каретку и заменять аннотации в PDF‑документах с помощью Aspose.PDF for Python via .NET.
lastmod: "2026-04-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Работайте с разметочными аннотациями в PDF‑файлах с использованием Python.
Abstract: Эта статья объясняет, как создавать, проверять и удалять разметки аннотаций в PDF‑документах с использованием Aspose.PDF for Python via .NET. В ней рассматриваются текстовые аннотации, аннотации‑каретки и аннотации‑замены, при этом каждый рабочий процесс разбит на небольшие шаги и примеры кода.
---

Эта статья показывает, как работать с разметкой аннотаций в PDF‑документах с использованием Aspose.PDF for Python via .NET.

Пример скрипта демонстрирует три распространённых рабочего процесса аннотаций:

- текстовые аннотации для комментариев в виде заметок
- аннотации каретки для маркеров вставки
- заменить аннотации для разметки замены текста

## Текстовые аннотации

### Добавить текстовые аннотации

В этом примере создаётся текстовая аннотация на первой странице и связывается с всплывающим окном. Текстовые аннотации полезны для комментариев в стиле стикеров в процессах рецензирования.

#### Откройте исходный PDF

```python
document = ap.Document(infile)
```

#### Создать и настроить текстовую аннотацию

Определите прямоугольник аннотации и задайте его заголовок, тему, содержимое, флаги отображения, цвет и значок.

```python
text_annotation = ap.annotations.TextAnnotation(
    document.pages[1],
    ap.Rectangle(299.988, 613.664, 428.708, 680.769, True),
)
text_annotation.title = "Aspose User"
text_annotation.subject = "Sticky Note"
text_annotation.contents = (
    "This is a text annotation added by Aspose.PDF for Python via .NET"
)
text_annotation.flags = ap.annotations.AnnotationFlags.PRINT
text_annotation.color = ap.Color.blue
text_annotation.icon = ap.annotations.TextIcon.HELP
```

#### Создать всплывающую аннотацию

Создайте всплывающее окно и подключите его к текстовой аннотации.

```python
popup = ap.annotations.PopupAnnotation(
    document.pages[1],
    ap.Rectangle(428.708, 613.664, 528.708, 713.664, True),
)
popup.open = True

text_annotation.popup = popup
```

#### Добавьте аннотацию и сохраните PDF

```python
document.pages[1].annotations.add(text_annotation, consider_rotation=False)
document.save(outfile)
```

#### Полный пример

```python
def text_annotation_add(infile, outfile):
    document = ap.Document(infile)

    text_annotation = ap.annotations.TextAnnotation(
        document.pages[1],
        ap.Rectangle(299.988, 613.664, 428.708, 680.769, True),
    )
    text_annotation.title = "Aspose User"
    text_annotation.subject = "Sticky Note"
    text_annotation.contents = (
        "This is a text annotation added by Aspose.PDF for Python via .NET"
    )
    text_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    text_annotation.color = ap.Color.blue
    text_annotation.icon = ap.annotations.TextIcon.HELP

    popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(428.708, 613.664, 528.708, 713.664, True),
    )
    popup.open = True

    text_annotation.popup = popup

    document.pages[1].annotations.add(text_annotation, consider_rotation=False)
    document.save(outfile)
```

### Получить текстовые аннотации

Чтобы проверить существующие текстовые аннотации, отфильтруйте коллекцию аннотаций на первой странице и оставьте только элементы, тип которых является `TEXT`.

#### Загрузите документ и соберите текстовые аннотации

```python
document = ap.Document(infile)
text_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.TEXT
]
```

#### Выведите прямоугольники аннотаций

```python
for annotation in text_annotations:
    print(annotation.rect)
```

#### Полный пример

```python
def text_annotation_get(infile, outfile):
    document = ap.Document(infile)
    text_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.TEXT
    ]

    for annotation in text_annotations:
        print(annotation.rect)
```

### Удалить текстовые аннотации

Этот рабочий процесс удаляет все текстовые аннотации с первой страницы и сохраняет изменённый PDF.

#### Найдите текстовые аннотации, которые нужно удалить

```python
document = ap.Document(infile)
text_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.TEXT
]
```

#### Удалить аннотации и сохранить файл

```python
for annotation in text_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### Полный пример

```python
def text_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    text_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.TEXT
    ]

    for annotation in text_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

## Каретные аннотации

### Добавить аннотации каретки

Caret annotations используются для обозначения точек вставки в сценариях обзора. В этом примере добавляется caret annotation с прикреплённым всплывающим примечанием.

#### Откройте документ и получите целевую страницу

```python
document = ap.Document(infile)
page = document.pages[1]
```

#### Создать и настроить аннотацию caret

```python
caret_annotation = ap.annotations.CaretAnnotation(
    page, ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
)
caret_annotation.title = "Aspose User"
caret_annotation.subject = "Inserted text 1"
caret_annotation.flags = ap.annotations.AnnotationFlags.PRINT
caret_annotation.color = ap.Color.blue
```

#### Прикрепите всплывающее окно и сохраните документ

```python
caret_annotation.popup = ap.annotations.PopupAnnotation(
    page, ap.Rectangle(310, 713, 410, 730, True)
)
page.annotations.append(caret_annotation)

document.save(outfile)
```

#### Полный пример

```python
def caret_annotations_add(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    caret_annotation = ap.annotations.CaretAnnotation(
        page, ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
    )
    caret_annotation.title = "Aspose User"
    caret_annotation.subject = "Inserted text 1"
    caret_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    caret_annotation.color = ap.Color.blue
    caret_annotation.popup = ap.annotations.PopupAnnotation(
        page, ap.Rectangle(310, 713, 410, 730, True)
    )
    page.annotations.append(caret_annotation)

    document.save(outfile)
```

### Получить аннотации каретки

Чтобы просмотреть аннотации caret, пройдитесь по аннотациям страницы и отфильтруйте по `CARET` тип аннотации.

#### Загрузите документ и страницу

```python
document = ap.Document(infile)
page = document.pages[1]
```

#### Выводить прямоугольники аннотации caret

```python
for annot in page.annotations:
    if annot.annotation_type == ap.annotations.AnnotationType.CARET:
        print(annot.rect)
```

#### Полный пример

```python
def caret_annotations_get(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    for annot in page.annotations:
        if annot.annotation_type == ap.annotations.AnnotationType.CARET:
            print(annot.rect)
```

### Удалить аннотации каретки

Этот рабочий процесс сначала собирает аннотации caret, удаляет их по одной, а затем сохраняет обновлённый файл.

#### Загрузите документ и соберите аннотации карет

```python
document = ap.Document(infile)
page = document.pages[1]

caret_annotations = [
    annot
    for annot in page.annotations
    if annot.annotation_type == ap.annotations.AnnotationType.CARET
]
```

#### Удалите аннотации и сохраните документ

```python
for annot in caret_annotations:
    page.annotations.delete(annot)

document.save(outfile)
```

#### Полный пример

```python
def caret_annotations_delete(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    caret_annotations = [
        annot
        for annot in page.annotations
        if annot.annotation_type == ap.annotations.AnnotationType.CARET
    ]

    for annot in caret_annotations:
        page.annotations.delete(annot)

    document.save(outfile)
```

## Заменить аннотации

### Добавить замену аннотаций

Replace annotations комбинируют аннотацию caret и сгруппированную аннотацию strikeout. Этот шаблон отмечает текст, который следует заменить, и связывает заметку о замене с зачеркиваемым содержимым.

#### Откройте документ и получите страницу

```python
document = ap.Document(infile)
page = document.pages[1]
```

#### Создать аннотацию caret для заменяемого текста

```python
caret_annotation = ap.annotations.CaretAnnotation(
    page, ap.Rectangle(361.246, 727.908, 370.081, 735.107, True)
)
caret_annotation.flags = ap.annotations.AnnotationFlags.PRINT
caret_annotation.subject = "Inserted text 2"
caret_annotation.title = "Aspose User"
caret_annotation.color = ap.Color.blue
caret_annotation.popup = ap.annotations.PopupAnnotation(
    page, ap.Rectangle(310, 713, 410, 730, True)
)
```

#### Создать группированную аннотацию зачеркивания

Определите область зачеркивания, назначьте квадропункты и свяжите её с аннотацией каретки через `in_reply_to` и `reply_type`.

```python
strikeout_annotation = ap.annotations.StrikeOutAnnotation(
    page, ap.Rectangle(318.407, 727.826, 368.916, 740.098, True)
)
strikeout_annotation.color = ap.Color.blue
strikeout_annotation.quad_points = [
    ap.Point(321.66, 739.416),
    ap.Point(365.664, 739.416),
    ap.Point(321.66, 728.508),
    ap.Point(365.664, 728.508),
]
strikeout_annotation.subject = "Cross-out"
strikeout_annotation.in_reply_to = caret_annotation
strikeout_annotation.reply_type = ap.annotations.ReplyType.GROUP
``` 

#### Добавьте обе аннотации и сохраните PDF

```python
page.annotations.append(caret_annotation)
page.annotations.append(strikeout_annotation)

document.save(outfile)
```

#### Полный пример

```python
def replace_annotations_add(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    caret_annotation = ap.annotations.CaretAnnotation(
        page, ap.Rectangle(361.246, 727.908, 370.081, 735.107, True)
    )
    caret_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    caret_annotation.subject = "Inserted text 2"
    caret_annotation.title = "Aspose User"
    caret_annotation.color = ap.Color.blue
    caret_annotation.popup = ap.annotations.PopupAnnotation(
        page, ap.Rectangle(310, 713, 410, 730, True)
    )

    strikeout_annotation = ap.annotations.StrikeOutAnnotation(
        page, ap.Rectangle(318.407, 727.826, 368.916, 740.098, True)
    )
    strikeout_annotation.color = ap.Color.blue
    strikeout_annotation.quad_points = [
        ap.Point(321.66, 739.416),
        ap.Point(365.664, 739.416),
        ap.Point(321.66, 728.508),
        ap.Point(365.664, 728.508),
    ]
    strikeout_annotation.subject = "Cross-out"
    strikeout_annotation.in_reply_to = caret_annotation
    strikeout_annotation.reply_type = ap.annotations.ReplyType.GROUP

    page.annotations.append(caret_annotation)
    page.annotations.append(strikeout_annotation)

    document.save(outfile)
```

### Получить замену аннотаций

Чтобы определить заменяющие аннотации, найдите аннотации-зачёркивания, сгруппированные как ответы на другую аннотацию. Пример приводит каждую аннотацию-зачёркивание перед проверкой её полей отношений.

#### Загрузите документ и пройдитесь по аннотациям

```python
document = ap.Document(infile)
page = document.pages[1]
```

#### Фильтровать сгруппированные аннотации перечёркивания

```python
for annot in page.annotations:
    if annot.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT:
        sa = cast(ap.annotations.StrikeOutAnnotation, annot)
        if (
            sa.in_reply_to is not None
            and sa.reply_type == ap.annotations.ReplyType.GROUP
        ):
            print(f"Replace annotation rect: {sa.rect}")
```

#### Полный пример

```python
def replace_annotations_get(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    for annot in page.annotations:
        if annot.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT:
            sa = cast(ap.annotations.StrikeOutAnnotation, annot)
            if (
                sa.in_reply_to is not None
                and sa.reply_type == ap.annotations.ReplyType.GROUP
            ):
                print(f"Replace annotation rect: {sa.rect}")
```

### Удалить замену аннотаций

Этот рабочий процесс собирает аннотации зачёркивания, используемые для замены разметки, удаляет их со страницы и сохраняет результирующий PDF.

#### Загрузите документ и соберите заменяющие аннотации

```python
document = ap.Document(infile)
page = document.pages[1]

replace_annotations = [
    cast(ap.annotations.StrikeOutAnnotation, annot)
    for annot in page.annotations
    if annot.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
]
```

#### Удалите аннотации и сохраните документ

```python
for annot in replace_annotations:
    page.annotations.delete(annot)

document.save(outfile)
```

#### Полный пример

```python
def replace_annotations_delete(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    replace_annotations = [
        cast(ap.annotations.StrikeOutAnnotation, annot)
        for annot in page.annotations
        if annot.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
    ]

    for annot in replace_annotations:
        page.annotations.delete(annot)

    document.save(outfile)
```
