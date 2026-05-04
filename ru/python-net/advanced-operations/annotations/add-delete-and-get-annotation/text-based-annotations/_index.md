---
title: Текстовые аннотации с использованием Python
linktitle: Текстовые аннотации
type: docs
weight: 10
url: /python-net/text-based-Annotations/
description: Узнайте, как добавлять, просматривать и удалять аннотации свободного текста, выделения, подчеркивания, волнистого подчеркивания и зачёркивания в PDF‑документах с использованием Aspose.PDF for Python via .NET.
lastmod: "2026-04-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Работайте с текстовыми и разметочными PDF‑аннотациями в Python.
Abstract: В этой статье объясняется, как создавать, читать и удалять текстовые аннотации в PDF‑документах с использованием Aspose.PDF for Python via .NET. Она охватывает свободные текстовые аннотации и аннотации разметки текста, такие как highlight, underline, squiggly и strikeout, включая расширенные процессы underline, такие как flattening, quad points и извлечение отмеченного текста.
---

В этой статье показано, как работать с аннотациями на основе текста в PDF‑документах с использованием Aspose.PDF for Python via .NET.

Пример скрипта демонстрирует несколько рабочих процессов текстовых аннотаций:

- аннотации свободного текста
- Выделить аннотации
- аннотации подчеркивания
- волнистые аннотации
- аннотации зачеркивания

## Аннотации FreeText

### Добавить аннотации FreeText 

Свободные текстовые аннотации позволяют размещать видимые текстовые комментарии непосредственно на странице PDF. В этом примере добавляется простая свободная текстовая аннотация на первую страницу.

#### Откройте исходный PDF

```python
document = ap.Document(infile)
```

#### Создайте и настройте аннотацию свободного текста

```python
free_text_annotation = ap.annotations.FreeTextAnnotation(
    document.pages[1],
    ap.Rectangle(299, 713, 308, 720, True),
    ap.annotations.DefaultAppearance(),
)
free_text_annotation.title = "Aspose User"
free_text_annotation.color = ap.Color.light_green
```

#### Добавьте аннотацию и сохраните PDF

```python
document.pages[1].annotations.append(free_text_annotation)
document.save(outfile)
```

#### Полный пример

```python
def free_text_annotation_add(infile, outfile):
    document = ap.Document(infile)

    free_text_annotation = ap.annotations.FreeTextAnnotation(
        document.pages[1],
        ap.Rectangle(299, 713, 308, 720, True),
        ap.annotations.DefaultAppearance(),
    )
    free_text_annotation.title = "Aspose User"
    free_text_annotation.color = ap.Color.light_green

    document.pages[1].annotations.append(free_text_annotation)
    document.save(outfile)
```

### Получить аннотации FreeText 

Чтобы проверить аннотации свободного текста, отфильтруйте аннотации первой страницы по `FREE_TEXT` введите и распечатайте каждый прямоугольник аннотации.

#### Загрузите документ и соберите аннотации свободного текста

```python
document = ap.Document(infile)
free_text_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.FREE_TEXT
]
```

#### Вывести прямоугольники аннотаций

```python
for annotation in free_text_annotations:
    print(annotation.rect)
```

#### Полный пример

```python
def free_text_annotation_get(infile, outfile):
    document = ap.Document(infile)
    free_text_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.FREE_TEXT
    ]

    for annotation in free_text_annotations:
        print(annotation.rect)
```

### Удалить аннотации FreeText 

Этот рабочий процесс удаляет все аннотации свободного текста с первой страницы и сохраняет обновлённый PDF.

#### Найти и удалить аннотации свободного текста

```python
document = ap.Document(infile)
free_text_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.FREE_TEXT
]

for annotation in free_text_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### Полный пример

```python
def free_text_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    free_text_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.FREE_TEXT
    ]

    for annotation in free_text_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```


## Текстовые разметочные аннотации

### Выделить аннотации

#### Добавить выделение текста

Аннотации выделения подчёркивают части документа, не изменяя исходное содержимое. В этом примере добавляется аннотация выделения на первую страницу.

```python
document = ap.Document(infile)

highlight_annotation = ap.annotations.HighlightAnnotation(
    document.pages[1],
    ap.Rectangle(300, 750, 320, 770, True),
)

document.pages[1].annotations.append(highlight_annotation)
document.save(outfile)
```

```python
def text_highlight_annotation_add(infile, outfile):
    document = ap.Document(infile)

    highlight_annotation = ap.annotations.HighlightAnnotation(
        document.pages[1],
        ap.Rectangle(300, 750, 320, 770, True),
    )

    document.pages[1].annotations.append(highlight_annotation)
    document.save(outfile)
```

#### Получить выделение текста

Чтобы проверить выделения, отфильтруйте аннотации страницы по `HIGHLIGHT` введите тип и выведите их прямоугольники.

```python
document = ap.Document(infile)
highlight_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT
]

for annotation in highlight_annotations:
    print(annotation.rect)
```

```python
def text_highlight_annotation_get(infile, outfile):
    document = ap.Document(infile)
    highlight_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT
    ]

    for annotation in highlight_annotations:
        print(annotation.rect)
```

#### Удалить выделение текста

Этот рабочий процесс удаляет все аннотации выделения с первой страницы и сохраняет результирующий PDF.

```python
document = ap.Document(infile)
highlight_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT
]

for annotation in highlight_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

```python
def text_highlight_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    highlight_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT
    ]

    for annotation in highlight_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```


### Подчёркнутые аннотации

#### Добавить аннотации подчёркивания текста

Аннотации подчеркивания отмечают текст видимым подчеркиванием. В этом примере добавляется простая аннотация подчеркивания и задаются её метаданные и цвет.

```python
document = ap.Document(infile)

underline_annotation = ap.annotations.UnderlineAnnotation(
    document.pages[1],
    ap.Rectangle(299.988, 713.664, 308.708, 720.769, True),
)
underline_annotation.title = "Aspose User"
underline_annotation.subject = "Inserted Underline 1"
underline_annotation.flags = ap.annotations.AnnotationFlags.PRINT
underline_annotation.color = ap.Color.blue

document.pages[1].annotations.append(underline_annotation)
document.save(outfile)
```

```python
def text_underline_annotation_add(infile, outfile):
    document = ap.Document(infile)

    underline_annotation = ap.annotations.UnderlineAnnotation(
        document.pages[1],
        ap.Rectangle(299.988, 713.664, 308.708, 720.769, True),
    )
    underline_annotation.title = "Aspose User"
    underline_annotation.subject = "Inserted Underline 1"
    underline_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    underline_annotation.color = ap.Color.blue

    document.pages[1].annotations.append(underline_annotation)
    document.save(outfile)
```

#### Добавить подчеркивание текста в аннотации, сплющить 

Если вы хотите, чтобы подчеркивание стало частью содержимого страницы, а не оставалось интерактивной аннотацией, вы можете сплющить его после добавления.

```python
document = ap.Document(infile)

underline_annotation = ap.annotations.UnderlineAnnotation(
    document.pages[1],
    ap.Rectangle(299.988, 713.664, 308.708, 720.769, True),
)
underline_annotation.title = "Aspose User"
underline_annotation.subject = "Inserted Underline to Flatten"
underline_annotation.flags = ap.annotations.AnnotationFlags.PRINT
underline_annotation.color = ap.Color.blue

document.pages[1].annotations.append(underline_annotation)
underline_annotation.flatten()

document.save(outfile)
```

```python
def text_underline_flatten_add(infile, outfile):
    document = ap.Document(infile)

    underline_annotation = ap.annotations.UnderlineAnnotation(
        document.pages[1],
        ap.Rectangle(299.988, 713.664, 308.708, 720.769, True),
    )
    underline_annotation.title = "Aspose User"
    underline_annotation.subject = "Inserted Underline to Flatten"
    underline_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    underline_annotation.color = ap.Color.blue

    document.pages[1].annotations.append(underline_annotation)
    underline_annotation.flatten()

    document.save(outfile)
```

#### Добавить аннотации подчеркивания текста с Quad Points

Quad points позволяют задать точную отмеченную область для аннотации подчёркивания. Это полезно, когда вам нужен больший контроль, чем простой прямоугольник.

```python
document = ap.Document(infile)
rect = ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)

underline_annotation = ap.annotations.UnderlineAnnotation(document.pages[1], rect)
underline_annotation.title = "Aspose User"
underline_annotation.subject = "Inserted Underline with Quad Points"
underline_annotation.flags = ap.annotations.AnnotationFlags.PRINT
underline_annotation.color = ap.Color.blue
underline_annotation.quad_points = [
    ap.Point(rect.llx, rect.lly),
    ap.Point(rect.urx, rect.lly),
    ap.Point(rect.urx, rect.ury),
    ap.Point(rect.llx, rect.ury),
]

document.pages[1].annotations.append(underline_annotation)
document.save(outfile)
```

```python
def text_underline_with_quad_points_add(infile, outfile):
    document = ap.Document(infile)
    rect = ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)

    underline_annotation = ap.annotations.UnderlineAnnotation(document.pages[1], rect)
    underline_annotation.title = "Aspose User"
    underline_annotation.subject = "Inserted Underline with Quad Points"
    underline_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    underline_annotation.color = ap.Color.blue
    underline_annotation.quad_points = [
        ap.Point(rect.llx, rect.lly),
        ap.Point(rect.urx, rect.lly),
        ap.Point(rect.urx, rect.ury),
        ap.Point(rect.llx, rect.ury),
    ]

    document.pages[1].annotations.append(underline_annotation)
    document.save(outfile)
```

#### Удалить аннотации подчеркивания текста

Этот рабочий процесс удаляет все аннотации подчеркивания с первой страницы и сохраняет обновлённый документ.

```python
document = ap.Document(infile)
underline_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
]

for annotation in underline_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

```python
def text_underline_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    underline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
    ]

    for annotation in underline_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

#### Удалить аннотации подчеркивания текста по названию

Этот рабочий процесс показывает, как выборочно удалять аннотации подчёркивания после проверки их заголовка.

```python
document = ap.Document(infile)

underline_annotations = [
    cast(ap.annotations.UnderlineAnnotation, annotation)
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
]

for annotation in underline_annotations:
    if annotation.title.startswith("a"):
        document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

```python
def text_underline_by_title_delete(infile, outfile):
    document = ap.Document(infile)

    underline_annotations = [
        cast(ap.annotations.UnderlineAnnotation, annotation)
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
    ]

    for annotation in underline_annotations:
        if annotation.title.startswith("a"):
            document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

#### Получить аннотации подчеркивания текста

Чтобы просмотреть аннотации подчеркивания, отфильтруйте аннотации первой страницы по `UNDERLINE` введите и распечатайте каждый прямоугольник.

```python
document = ap.Document(infile)
underline_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
]

for annotation in underline_annotations:
    print(annotation.rect)
```

```python
def text_underline_annotation_get(infile, outfile):
    document = ap.Document(infile)
    underline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
    ]

    for annotation in underline_annotations:
        print(annotation.rect)
```

#### Получить отмеченный текст подчеркивающих анноций

Этот рабочий процесс преобразует каждую аннотацию подчеркивания в `UnderlineAnnotation` объект и извлекает помеченный текст.

```python
document = ap.Document(infile)

underline_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
]

for annotation in underline_annotations:
    ua = cast(ap.annotations.UnderlineAnnotation, annotation)
    print(f"Marked text: {ua.get_marked_text()}")
```

```python
def text_underline_marked_text_get(infile, outfile):
    document = ap.Document(infile)

    underline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
    ]

    for annotation in underline_annotations:
        ua = cast(ap.annotations.UnderlineAnnotation, annotation)
        print(f"Marked text: {ua.get_marked_text()}")
```

#### Получить фрагменты, отмеченные аннотациями подчёркнутого текста

Если вам нужен каждый отмеченный фрагмент отдельно, вы можете итерировать коллекцию, возвращаемую `get_marked_text_fragments()`.

```python
document = ap.Document(infile)

underline_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
]

for annotation in underline_annotations:
    ua = cast(ap.annotations.UnderlineAnnotation, annotation)
    for fragment in ua.get_marked_text_fragments():
        print(f"Fragment text: {fragment.text}")
```

```python
def text_underline_marked_fragments_get(infile, outfile):
    document = ap.Document(infile)

    underline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
    ]

    for annotation in underline_annotations:
        ua = cast(ap.annotations.UnderlineAnnotation, annotation)
        for fragment in ua.get_marked_text_fragments():
            print(f"Fragment text: {fragment.text}")
```


### Волнистые аннотации

#### Добавить волнообразные аннотации

Волнистые аннотации часто используются для выделения ошибок правописания, грамматики или областей, требующих внимания, в тексте. В данном примере добавляется волнистая аннотация на первую страницу.

```python
document = ap.Document(infile)
page = document.pages[1]

squiggly_annotation = ap.annotations.SquigglyAnnotation(
    page,
    ap.Rectangle(67, 317, 261, 459, True),
)
squiggly_annotation.title = "John Smith"
squiggly_annotation.color = ap.Color.blue

page.annotations.append(squiggly_annotation)
document.save(outfile)
```

```python
def text_squiggly_annotation_add(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    squiggly_annotation = ap.annotations.SquigglyAnnotation(
        page,
        ap.Rectangle(67, 317, 261, 459, True),
    )
    squiggly_annotation.title = "John Smith"
    squiggly_annotation.color = ap.Color.blue

    page.annotations.append(squiggly_annotation)
    document.save(outfile)
```

#### Получить волнистые аннотации

Чтобы просмотреть волнистые аннотации, отфильтруйте аннотации страницы по `SQUIGGLY` введите тип и выведите их прямоугольники.

```python
document = ap.Document(infile)
squiggly_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.SQUIGGLY
]

for annotation in squiggly_annotations:
    print(annotation.rect)
```

```python
def text_squiggly_annotation_get(infile, outfile):
    document = ap.Document(infile)
    squiggly_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.SQUIGGLY
    ]

    for annotation in squiggly_annotations:
        print(annotation.rect)
```

#### Удалить волнистые аннотации

Этот рабочий процесс удаляет все волнообразные аннотации с первой страницы и сохраняет результат.

```python
document = ap.Document(infile)
squiggly_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.SQUIGGLY
]

for annotation in squiggly_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

```python
def text_squiggly_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    squiggly_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.SQUIGGLY
    ]

    for annotation in squiggly_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```


### Аннотации зачеркивания

#### Добавить аннотации зачёркивания текста

Аннотации зачёркивания помечают текст, который следует считать удалённым или перечёркнутым. В этом примере добавляется аннотация зачёркивания, и задаются её метаданные и цвет.

```python
document = ap.Document(infile)

strikeout_annotation = ap.annotations.StrikeOutAnnotation(
    document.pages[1],
    ap.Rectangle(299.988, 713.664, 308.708, 720.769, True),
)
strikeout_annotation.title = "Aspose User"
strikeout_annotation.subject = "Inserted text 1"
strikeout_annotation.flags = ap.annotations.AnnotationFlags.PRINT
strikeout_annotation.color = ap.Color.blue

document.pages[1].annotations.append(strikeout_annotation)
document.save(outfile)
```

```python
def text_strikeout_annotation_add(infile, outfile):
    document = ap.Document(infile)

    strikeout_annotation = ap.annotations.StrikeOutAnnotation(
        document.pages[1],
        ap.Rectangle(299.988, 713.664, 308.708, 720.769, True),
    )
    strikeout_annotation.title = "Aspose User"
    strikeout_annotation.subject = "Inserted text 1"
    strikeout_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    strikeout_annotation.color = ap.Color.blue

    document.pages[1].annotations.append(strikeout_annotation)
    document.save(outfile)
```

#### Получить аннотации зачёркнутого текста

Чтобы проверить аннотации зачёркивания, отфильтруйте аннотации страниц по `STRIKE_OUT` введите тип и выведите их прямоугольники.

```python
document = ap.Document(infile)
strikeout_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
]

for annotation in strikeout_annotations:
    print(annotation.rect)
```

```python
def text_strikeout_annotation_get(infile, outfile):
    document = ap.Document(infile)
    strikeout_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
    ]

    for annotation in strikeout_annotations:
        print(annotation.rect)
```

#### Удалить текстовые аннотации зачёркивания

Этот рабочий процесс удаляет все аннотации типа зачеркивания с первой страницы и сохраняет обновлённый документ.

```python
document = ap.Document(infile)
strikeout_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
]

for annotation in strikeout_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

```python
def text_strikeout_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    strikeout_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
    ]

    for annotation in strikeout_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

## Связанные темы

- [Импорт и экспорт аннотаций](/python-net/import-export-annotations/)
- [Интерактивные аннотации](/python-net/interactive-annotations/)
- [Разметка аннотаций](/python-net/markup-annotations/)
- [Медиа-аннотации](/python-net/media-annotations/)
- [Аннотации безопасности](/python-net/security-annotations/)
- [Фигурные аннотации](/python-net/shape-annotations/)
- [Аннотации водяного знака](/python-net/watermark-annotations/)
