---
title: Аннотации фигур через Python
linktitle: Аннотации фигур
type: docs
weight: 20
url: /python-net/shape-annotations/
description: Узнайте, как добавлять, проверять и удалять аннотации линий, квадратов, кругов, полигонов и полилиний в PDF‑документах с помощью Aspose.PDF for Python via .NET.
lastmod: "2026-04-21"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true 
AlternativeHeadline: Работайте с геометрическими PDF‑аннотациями в Python.
Abstract: В этой статье объясняется, как создавать, читать и удалять аннотации фигур в PDF‑документах с использованием Aspose.PDF for Python via .NET. Описываются аннотации линий, квадратов, кругов, полигонов и полилиний, при этом каждый рабочий процесс разбит на небольшие шаги и содержит полные примеры кода.
---

В этой статье показано, как работать с аннотациями фигур в PDF‑документах с использованием Aspose.PDF for Python via .NET.

Пример сценария демонстрирует несколько геометрически‑ориентированных рабочих процессов аннотирования:

- аннотации линий
- аннотации квадрата
- аннотации круга
- аннотации полигон
- аннотации полилиний

## Аннотация линий

### Добавить аннотацию линий

Этот пример добавляет аннотацию линий на первую страницу и настраивает стили стрелок, толщину линии и всплывающее окно.

#### Открыть исходный PDF

```python
document = ap.Document(infile)
```

#### Создать и настроить аннотацию линий

```python
line_annotation = ap.annotations.LineAnnotation(
    document.pages[1],
    ap.Rectangle(550, 93, 562, 439, True),
    ap.Point(556, 99),
    ap.Point(556, 443),
)

line_annotation.title = "John Smith"
line_annotation.color = ap.Color.red
line_annotation.width = 3
line_annotation.starting_style = ap.annotations.LineEnding.OPEN_ARROW
line_annotation.ending_style = ap.annotations.LineEnding.OPEN_ARROW
```

#### Прикрепить всплывающее окно и сохранить PDF

```python
popup = ap.annotations.PopupAnnotation(
    document.pages[1],
    ap.Rectangle(842, 124, 1021, 266, True),
)
line_annotation.popup = popup

document.pages[1].annotations.append(line_annotation)
document.save(outfile)
```

#### Полный пример

```python
def line_annotation_add(infile, outfile):
    document = ap.Document(infile)

    line_annotation = ap.annotations.LineAnnotation(
        document.pages[1],
        ap.Rectangle(550, 93, 562, 439, True),
        ap.Point(556, 99),
        ap.Point(556, 443),
    )

    line_annotation.title = "John Smith"
    line_annotation.color = ap.Color.red
    line_annotation.width = 3
    line_annotation.starting_style = ap.annotations.LineEnding.OPEN_ARROW
    line_annotation.ending_style = ap.annotations.LineEnding.OPEN_ARROW

    popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(842, 124, 1021, 266, True),
    )
    line_annotation.popup = popup

    document.pages[1].annotations.append(line_annotation)
    document.save(outfile)
```

### Получить аннотацию линии

Чтобы проверить аннотации линий, отфильтруйте коллекцию аннотаций на первой странице и приведите каждый результат к `LineAnnotation` чтобы вы могли прочитать его начальные и конечные точки.

#### Загрузить PDF и собрать аннотации линий

```python
document = ap.Document(infile)

line_annotation = [
    cast(ap.annotations.LineAnnotation, annotation)
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.LINE
]
```

#### Вывести координаты линии

```python
for annotation in line_annotation:
    print(
        f"[{annotation.starting.x},{annotation.starting.y}]"
        f"-[{annotation.ending.x},{annotation.ending.y}]"
    )
```

#### Полный пример

```python
def line_annotations_get(infile, outfile):
    document = ap.Document(infile)

    line_annotation = [
        cast(ap.annotations.LineAnnotation, annotation)
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.LINE
    ]

    for annotation in line_annotation:
        print(
            f"[{annotation.starting.x},{annotation.starting.y}]"
            f"-[{annotation.ending.x},{annotation.ending.y}]"
        )
```

### Удалить аннотацию линий

Этот процесс удаляет все аннотации линий с первой страницы и сохраняет обновлённый PDF.

#### Найти аннотацию линий для удаления

```python
document = ap.Document(infile)
page = document.pages[1]

line_annotations = [
    annotation
    for annotation in page.annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.LINE
]
```

#### Удалить аннотации и сохранить PDF

```python
for annotation in line_annotations:
    page.annotations.delete(annotation)

document.save(outfile)
```

#### Полный пример

```python
def line_annotations_delete(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    line_annotations = [
        annotation
        for annotation in page.annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.LINE
    ]

    for annotation in line_annotations:
        page.annotations.delete(annotation)

    document.save(outfile)
```

## Аннотации квадратов и кругов

### Добавить аннотацию квадрата

Аннотации квадрата полезны для обозначения прямоугольных областей в документе. В этом примере создаётся аннотация квадрата с настройками границы, заливки и прозрачности.

#### Открыть PDF и создать аннотацию квадрата

```python
document = ap.Document(infile)

square_annotation = ap.annotations.SquareAnnotation(
    document.pages[1],
    ap.Rectangle(60, 600, 250, 450, True),
)
square_annotation.title = "John Smith"
square_annotation.color = ap.Color.blue
square_annotation.interior_color = ap.Color.blue_violet
square_annotation.opacity = 0.25
```

#### Добавить аннотацию и сохранить PDF

```python
document.pages[1].annotations.append(square_annotation)
document.save(outfile)
```

#### Полный пример

```python
def square_annotation_add(infile, outfile):
    document = ap.Document(infile)

    square_annotation = ap.annotations.SquareAnnotation(
        document.pages[1],
        ap.Rectangle(60, 600, 250, 450, True),
    )
    square_annotation.title = "John Smith"
    square_annotation.color = ap.Color.blue
    square_annotation.interior_color = ap.Color.blue_violet
    square_annotation.opacity = 0.25

    document.pages[1].annotations.append(square_annotation)
    document.save(outfile)
```

### Получить аннотацию квадрата

Чтобы просмотреть аннотации квадрата, отфильтруйте аннотации первой страницы по `SQUARE` введите и распечатайте каждый прямоугольник.

#### Загрузить документ и собрать аннотации квадрата

```python
document = ap.Document(infile)
square_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.SQUARE
]
```

#### Печать прямоугольников аннотаций

```python
for annotation in square_annotations:
    print(annotation.rect)
```

#### Полный пример

```python
def square_annotation_get(infile, outfile):
    document = ap.Document(infile)
    square_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.SQUARE
    ]

    for annotation in square_annotations:
        print(annotation.rect)
```

### Удалить квадратную аннотацию

Этот рабочий процесс удаляет все квадратные аннотации с первой страницы и сохраняет документ.

#### Найти и удалить квадратные аннотации

```python
document = ap.Document(infile)
square_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.SQUARE
]

for annotation in square_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### Полный пример

```python
def square_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    square_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.SQUARE
    ]

    for annotation in square_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

### Добавить круговую аннотацию 

Круговые аннотации обозначают закруглённые области в PDF. В этом примере добавляется круговая аннотация с цветом заливки, непрозрачностью и всплывающей аннотацией.

#### Открыть PDF и создать круговую аннотацию

```python
document = ap.Document(infile)

circle_annotation = ap.annotations.CircleAnnotation(
    document.pages[1],
    ap.Rectangle(270, 160, 483, 383, True),
)
circle_annotation.title = "John Smith"
circle_annotation.color = ap.Color.red
circle_annotation.interior_color = ap.Color.misty_rose
circle_annotation.opacity = 0.5
```

#### Прикрепить всплывающее окно и сохранить PDF

```python
circle_annotation.popup = ap.annotations.PopupAnnotation(
    document.pages[1],
    ap.Rectangle(842, 316, 1021, 459, True),
)

document.pages[1].annotations.append(circle_annotation)
document.save(outfile)
```

#### Полный пример

```python
def circle_annotation_add(infile, outfile):
    document = ap.Document(infile)

    circle_annotation = ap.annotations.CircleAnnotation(
        document.pages[1],
        ap.Rectangle(270, 160, 483, 383, True),
    )
    circle_annotation.title = "John Smith"
    circle_annotation.color = ap.Color.red
    circle_annotation.interior_color = ap.Color.misty_rose
    circle_annotation.opacity = 0.5
    circle_annotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(842, 316, 1021, 459, True),
    )

    document.pages[1].annotations.append(circle_annotation)
    document.save(outfile)
```

### Получить круговую аннотацию

Чтобы просмотреть круговые аннотации, отфильтруйте аннотации страницы по `CIRCLE` введите и выведите их прямоугольники.

#### Загрузить документ и собрать круговые аннотации

```python
document = ap.Document(infile)
circle_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.CIRCLE
]
```

#### Печать прямоугольников аннотаций

```python
for annotation in circle_annotations:
    print(annotation.rect)
```

#### Полный пример

```python
def circle_annotation_get(infile, outfile):
    document = ap.Document(infile)
    circle_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.CIRCLE
    ]

    for annotation in circle_annotations:
        print(annotation.rect)
```

### Удалить круговую аннотацию 

Этот рабочий процесс удаляет все круговые аннотации с первой страницы и сохраняет результирующий PDF.

#### Найти и удалить круглые аннотации

```python
document = ap.Document(infile)
circle_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.CIRCLE
]

for annotation in circle_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### Полный пример

```python
def circle_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    circle_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.CIRCLE
    ]

    for annotation in circle_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

## Аннотации многоугольников и полилиний

### Добавить полигональную аннотацию 

Полигональные аннотации определяют замкнутую многоточечную форму. В этом примере создаётся полигональная аннотация из прямоугольника и списка точек.

#### Открыть PDF и создать полигональную аннотацию

```python
document = ap.Document(infile)

polygon_annotation = ap.annotations.PolygonAnnotation(
    document.pages[1],
    ap.Rectangle(200, 300, 400, 400, True),
    [
        ap.Point(200, 300),
        ap.Point(220, 300),
        ap.Point(250, 330),
        ap.Point(300, 304),
        ap.Point(300, 400),
    ],
)
polygon_annotation.title = "John Smith"
polygon_annotation.color = ap.Color.blue
polygon_annotation.interior_color = ap.Color.blue_violet
polygon_annotation.opacity = 0.25
```

#### Добавить аннотацию и сохранить PDF

```python
document.pages[1].annotations.append(polygon_annotation)
document.save(outfile)
```

#### Полный пример

```python
def polygon_annotation_add(infile, outfile):
    document = ap.Document(infile)

    polygon_annotation = ap.annotations.PolygonAnnotation(
        document.pages[1],
        ap.Rectangle(200, 300, 400, 400, True),
        [
            ap.Point(200, 300),
            ap.Point(220, 300),
            ap.Point(250, 330),
            ap.Point(300, 304),
            ap.Point(300, 400),
        ],
    )
    polygon_annotation.title = "John Smith"
    polygon_annotation.color = ap.Color.blue
    polygon_annotation.interior_color = ap.Color.blue_violet
    polygon_annotation.opacity = 0.25

    document.pages[1].annotations.append(polygon_annotation)
    document.save(outfile)
```

### Получить полигональную аннотацию 

Чтобы просмотреть аннотации полигонов, отфильтруйте аннотации первой страницы по `POLYGON` введите и распечатайте каждый прямоугольник аннотации.

#### Загрузить документ и собрать полигональные аннотации

```python
document = ap.Document(infile)
polygon_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.POLYGON
]
```

#### Печать прямоугольников аннотаций

```python
for annotation in polygon_annotations:
    print(annotation.rect)
```

#### Полный пример

```python
def polygon_annotation_get(infile, outfile):
    document = ap.Document(infile)
    polygon_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLYGON
    ]

    for annotation in polygon_annotations:
        print(annotation.rect)
```

### Удалить полигональную аннотацию 

Этот рабочий процесс удаляет все полигональные аннотации с первой страницы и сохраняет обновлённый PDF.

#### Найти и удалить аннотации полигонов

```python
document = ap.Document(infile)
polygon_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.POLYGON
]

for annotation in polygon_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### Полный пример

```python
def polygon_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    polygon_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLYGON
    ]

    for annotation in polygon_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

### Добавить аннотацию полилинии 

Полилинейные аннотации определяют открытый путь через несколько точек. В этом примере создаётся полилинейная аннотация с всплывающей заметкой.

#### Открыть PDF и создать аннотацию полилинии

```python
document = ap.Document(infile)

polyline_annotation = ap.annotations.PolylineAnnotation(
    document.pages[1],
    ap.Rectangle(270, 193, 571, 383, True),
    [
        ap.Point(545, 150),
        ap.Point(545, 190),
        ap.Point(667, 190),
        ap.Point(667, 110),
        ap.Point(626, 111),
    ],
)
polyline_annotation.title = "John Smith"
polyline_annotation.color = ap.Color.red
```

#### Прикрепить всплывающее окно и сохранить PDF

```python
polyline_annotation.popup = ap.annotations.PopupAnnotation(
    document.pages[1],
    ap.Rectangle(842, 196, 1021, 338, True),
)

document.pages[1].annotations.append(polyline_annotation)
document.save(outfile)
```

#### Полный пример

```python
def polyline_annotation_add(infile, outfile):
    document = ap.Document(infile)

    polyline_annotation = ap.annotations.PolylineAnnotation(
        document.pages[1],
        ap.Rectangle(270, 193, 571, 383, True),
        [
            ap.Point(545, 150),
            ap.Point(545, 190),
            ap.Point(667, 190),
            ap.Point(667, 110),
            ap.Point(626, 111),
        ],
    )
    polyline_annotation.title = "John Smith"
    polyline_annotation.color = ap.Color.red
    polyline_annotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(842, 196, 1021, 338, True),
    )

    document.pages[1].annotations.append(polyline_annotation)
    document.save(outfile)
```

### Получить аннотацию PolyLine 

Чтобы просмотреть аннотации полилиний, отфильтруйте аннотации страницы по `POLY_LINE` введите и выведите их прямоугольники.

#### Загрузить документ и собрать аннотации полилиний

```python
document = ap.Document(infile)
polyline_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.POLY_LINE
]
```

#### Печать прямоугольников аннотаций

```python
for annotation in polyline_annotations:
    print(annotation.rect)
```

#### Полный пример

```python
def polyline_annotation_get(infile, outfile):
    document = ap.Document(infile)
    polyline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLY_LINE
    ]

    for annotation in polyline_annotations:
        print(annotation.rect)
```

### Удалить аннотацию PolyLine 

Этот рабочий процесс удаляет все аннотации полилиний с первой страницы и сохраняет результирующий PDF.

#### Найти и удалить аннотации полилиний

```python
document = ap.Document(infile)
polyline_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.POLY_LINE
]

for annotation in polyline_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### Полный пример

```python
def polyline_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    polyline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLY_LINE
    ]

    for annotation in polyline_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

## Связанные темы

- [Импорт и экспорт аннотаций](/python-net/import-export-annotations/)
- [Интерактивные аннотации](/python-net/interactive-annotations/)
- [Разметка аннотаций](/python-net/markup-annotations/)
- [Медиа аннотации](/python-net/media-annotations/)
- [Аннотации безопасности](/python-net/security-annotations/)
- [Текстовые аннотации](/python-net/text-based-Annotations/)
- [Аннотации водяного знака](/python-net/watermark-annotations/)
