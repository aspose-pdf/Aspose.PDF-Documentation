---
title: Добавление Аннотаций Фигур с использованием Python
linktitle: Аннотации Фигур
type: docs
weight: 30
url: ru/python-net/figures-annotation/
description: Эта статья описывает, как добавлять, получать и удалять аннотации фигур из вашего PDF-документа с помощью Aspose.PDF для Python через .NET
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Добавление Аннотаций Фигур с использованием Python",
    "alternativeHeadline": "Как добавить Аннотации Фигур в PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация pdf документов",
    "keywords": "pdf, python, аннотации фигур, аннотация многоугольника, аннотация линии, аннотация квадрата, аннотация круга",
    "wordcount": "302",
    "proficiencyLevel":"Начинающий",
    "publisher": {
        "@type": "Organization",
        "name": "Команда Документации Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/figures-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/figures-annotation/"
    },
    "dateModified": "2023-02-04",
    "description": "Эта статья описывает, как добавлять, получать и удалять аннотации фигур из вашего PDF-документа с помощью Aspose.PDF для Python"
}
</script>


## Добавление квадратных и круглых аннотаций

В PDF документах квадратная аннотация относится к специфическому типу аннотаций, которые представлены квадратной формой. Квадратные аннотации используются для выделения или привлечения внимания к определенной области или разделу в документе.

[Квадратные](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation/) и [Круглые](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/circleannotation/) аннотации отображают, соответственно, прямоугольник или эллипс на странице.

Шаги для создания квадратных или круглых аннотаций:

1. Загрузите PDF файл - новый [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
2. Создайте новую [SquareAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation) и установите параметры (новый Rectangle, заголовок, цвет, внутренний_цвет, непрозрачность).
3. После этого необходимо добавить квадратную аннотацию на страницу.

Следующий фрагмент кода показывает, как добавить квадратные аннотации на страницу PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    squareAnnotation = ap.annotations.SquareAnnotation(document.pages[1], ap.Rectangle(60, 600, 250, 450, True))
    squareAnnotation.title = "Джон Смит"
    squareAnnotation.color = ap.Color.blue
    squareAnnotation.interior_color = ap.Color.blue_violet
    squareAnnotation.opacity = 0.25

    document.pages[1].annotations.append(squareAnnotation)

    document.save(output_file)
```

Следующий фрагмент кода показывает, как добавить круговые аннотации на страницу PDF.

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_file)

    circleAnnotation = ap.annotations.CircleAnnotation(
        document.pages[1], ap.Rectangle(270, 160, 483, 383, True)
    )
    circleAnnotation.title = "Джон Смит"
    circleAnnotation.color = ap.Color.red
    circleAnnotation.interior_color = ap.Color.misty_rose
    circleAnnotation.opacity = 0.5
    circleAnnotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1], ap.Rectangle(842, 316, 1021, 459, True)
    )

    document.pages[1].annotations.append(circleAnnotation)
    document.save(output_file)
```


Как пример, мы увидим следующий результат добавления аннотаций Квадрат и Круг в PDF документ:

![Демонстрация аннотаций Круг и Квадрат](circle_demo.png)

### Получить аннотацию Круга

Пожалуйста, попробуйте использовать следующий фрагмент кода для получения аннотации Круга из PDF документа.

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

### Получить аннотацию Квадрата

Пожалуйста, попробуйте использовать следующий фрагмент кода для получения аннотации Квадрата из PDF документа.

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

### Удалить аннотацию Круга

Следующий фрагмент кода показывает, как удалить аннотацию круга из PDF файла.

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

### Удалить аннотацию квадрата

Следующий фрагмент кода показывает, как удалить аннотацию квадрата из PDF файла.

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

## Добавление аннотаций многоугольника и полилинии

Инструмент Polyline позволяет создавать формы и контуры с произвольным количеством сторон на документе.

[Аннотации Полигонов](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polygonannotation/) представляют собой многоугольники на странице. Они могут иметь любое количество вершин, соединенных прямыми линиями.

[Аннотации Полилиний](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polylineannotation/) также похожи на многоугольники, единственное отличие - это то, что первая и последняя вершины не соединены неявно.

Шаги, с помощью которых мы создаем аннотации Полигонов:

1. Загрузите PDF файл - новый [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Создайте новую [Аннотацию Полигона](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polygonannotation) и установите параметры Полигона (новый Прямоугольник, новые Точки, заголовок, цвет, внутренний_цвет и непрозрачность).
1. После этого мы можем добавить аннотации на страницу.

Следующий фрагмент кода показывает, как добавить Аннотации Полигонов в PDF файл:

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


Следующий фрагмент кода показывает, как добавить аннотации полилинии в PDF-файл:

1. Загрузите PDF-файл - новый [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Создайте новые [Polyline Annotations](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polylineannotation/) и установите параметры многоугольника (новый Rectangle, новые Points, title, color, interior_color и opacity).
1. После этого мы можем добавить аннотации на страницу.

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


### Получить аннотации полигонов и полилиний

Пожалуйста, попробуйте использовать следующий фрагмент кода, чтобы получить аннотации полигонов в PDF-документе.

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

Пожалуйста, попробуйте использовать следующий фрагмент кода, чтобы получить аннотации полилиний в PDF-документе.

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

### Удалить аннотации полигонов и полилиний

Следующий фрагмент кода показывает, как удалить аннотации полигонов из PDF-файла.

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


Следующий фрагмент кода показывает, как удалить аннотации полилинии из PDF файла.

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

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for Python",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>