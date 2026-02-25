---
title: Добавление аннотаций фигур с использованием Python
linktitle: Аннотации фигур
type: docs
weight: 30
url: /ru/python-net/figures-annotation/
description: Эта статья описывает, как добавить, получить и удалить аннотации фигур из вашего PDF‑документа с помощью Aspose.PDF for Python via .NET
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Руководство по работе с аннотациями фигур в PDF
Abstract: Эта статья предоставляет всестороннее руководство по добавлению, получению и удалению квадратных, круглых, полигональных и полилинейных аннотаций в PDF‑документах с использованием Aspose.PDF for Python. Квадратные и круглые аннотации визуально выделяют определённые области на странице PDF прямоугольными и эллиптическими формами соответственно. В статье содержатся пошаговые инструкции и фрагменты кода на Python для создания этих аннотаций путём загрузки PDF‑файла, настройки свойств аннотации, таких как заголовок, цвет и непрозрачность, и добавления их на страницы PDF. Кроме того, статья описывает методы получения аннотаций по типу, вывода их прямоугольных размеров и удаления их из PDF‑документа. Также рассматриваются аннотации полигонов и полилиний, где полигоны определяются серией соединённых вершин, образующих замкнутую форму, а полилинии соединяют вершины в открытом виде. Документ содержит примеры кода, иллюстрирующие процессы добавления этих аннотаций в PDF, а также методы доступа к ним и их удаления.

---

## Добавить квадратные и круглые аннотации

В PDF‑документах аннотация квадрат представляет собой специфический тип аннотации, отображаемой в виде квадратной формы. Квадратные аннотации используются для выделения или привлечения внимания к определённой области или разделу документа.

[Квадрат](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation/) и [Круг](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/circleannotation/) аннотации отображают соответственно прямоугольник или эллипс на странице.

Шаги для создания квадратных или круглых аннотаций:

1. Загрузите PDF‑файл — новый [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Создайте новую [SquareAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation) и задайте параметры (new Rectangle, title, color, interior_color, opacity).
1. Затем добавьте квадратную аннотацию на страницу.

Следующий фрагмент кода показывает, как добавить квадратные аннотации на страницу PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    squareAnnotation = ap.annotations.SquareAnnotation(document.pages[1], ap.Rectangle(60, 600, 250, 450, True))
    squareAnnotation.title = "John Smith"
    squareAnnotation.color = ap.Color.blue
    squareAnnotation.interior_color = ap.Color.blue_violet
    squareAnnotation.opacity = 0.25

    document.pages[1].annotations.append(squareAnnotation)

    document.save(output_file)
```

Следующий фрагмент кода показывает, как добавить круглые аннотации на страницу PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_file)

    circleAnnotation = ap.annotations.CircleAnnotation(
        document.pages[1], ap.Rectangle(270, 160, 483, 383, True)
    )
    circleAnnotation.title = "John Smith"
    circleAnnotation.color = ap.Color.red
    circleAnnotation.interior_color = ap.Color.misty_rose
    circleAnnotation.opacity = 0.5
    circleAnnotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1], ap.Rectangle(842, 316, 1021, 459, True)
    )

    document.pages[1].annotations.append(circleAnnotation)
    document.save(output_file)
```

В качестве примера мы увидим следующий результат добавления квадратных и круглых аннотаций в PDF‑документ:

![Демонстрация аннотаций круга и квадрата](circle_demo.png)

### Получить аннотацию круга

Пожалуйста, попробуйте использовать следующий фрагмент кода, чтобы получить аннотацию круга из PDF‑документа.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    circleAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CIRCLE)
    ]

    for ca in circleAnnotations:
        print(ca.rect)
```

### Получить квадратную аннотацию

Пожалуйста, попробуйте использовать следующий фрагмент кода, чтобы получить квадратную аннотацию из PDF‑документа.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squareAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUARE)
    ]

    for pa in squareAnnotations:
        print(pa.rect)
```


### Удалить аннотацию круга

Следующий фрагмент кода показывает, как удалить аннотацию круга из PDF‑файла.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    circleAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CIRCLE)
    ]

    for ca in circleAnnotations:
        document.pages[1].annotations.delete(ca)

    document.save(output_file)
```

### Удалить квадратную аннотацию

Следующий фрагмент кода показывает, как удалить квадратную аннотацию из PDF‑файла.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squareAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUARE)
    ]

    for pa in squareAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```

## Добавить полигональные и полилинейные аннотации

Инструмент Polyline позволяет создавать формы и контуры с произвольным числом сторон в документе.

[Полигональные аннотации](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polygonannotation/) представляют полигоны на странице. Они могут иметь любое количество вершин, соединённых прямыми линиями.

[Полилинейные аннотации](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polylineannotation/) также похожи на полигоны, единственное отличие — первые и последние вершины не соединяются автоматически.

Шаги, с помощью которых мы создаём полигональные аннотации:

1. Загрузите PDF‑файл — новый [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Создайте новую [Polygon Annotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polygonannotation) и задайте параметры полигона (new Rectangle, new Points, title, color, interior_color и opacity).
1. Затем добавьте аннотации на страницу.

Следующий фрагмент кода показывает, как добавить полигональные аннотации в PDF‑файл:

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    polygonAnnotation = ap.annotations.PolygonAnnotation(
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
    polygonAnnotation.title = "John Smith"
    polygonAnnotation.color = ap.Color.blue
    polygonAnnotation.interior_color = ap.Color.blue_violet
    polygonAnnotation.opacity = 0.25

    document.pages[1].annotations.append(polygonAnnotation)
    document.save(output_file)
```

Следующий фрагмент кода показывает, как добавить полилинейные аннотации в PDF‑файл:

1. Загрузите PDF‑файл — новый [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Создайте новые [Polyline Annotations](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polylineannotation/) и задайте параметры полигона (new Rectangle, new Points, title, color, interior_color и opacity).
1. Затем добавьте аннотации на страницу.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    polylineAnnotation = ap.annotations.PolylineAnnotation(
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
    polylineAnnotation.title = "John Smith"
    polylineAnnotation.color = ap.Color.red
    polylineAnnotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1], ap.Rectangle(842, 196, 1021, 338, True)
    )

    document.pages[1].annotations.append(polylineAnnotation)
    document.save(output_file)
```

### Получить полигональные и полилинейные аннотации

Пожалуйста, попробуйте использовать следующий фрагмент кода, чтобы получить полигональные аннотации в PDF‑документе.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    polygonAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLYGON)
    ]

    for pa in polygonAnnotations:
        print(pa.rect)
```

Пожалуйста, попробуйте использовать следующий фрагмент кода, чтобы получить полилинейные аннотации в PDF‑документе.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    polylineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLY_LINE)
    ]

    for pa in polylineAnnotations:
        print(pa.rect)
```

### Удалить полигональные и полилинейные аннотации

Следующий фрагмент кода показывает, как удалить полигональные аннотации из PDF‑файла.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    polygonAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLYGON)
    ]

    for pa in polygonAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```

В следующем фрагменте кода показано, как удалить аннотации полилиний из PDF‑файла.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    polylineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLY_LINE)
    ]

    for pa in polylineAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```


