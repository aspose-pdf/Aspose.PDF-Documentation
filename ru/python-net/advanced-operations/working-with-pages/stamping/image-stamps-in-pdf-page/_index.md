---
title: Добавление штампов изображений в PDF с использованием Python
linktitle: Штампы изображений в PDF файле
type: docs
weight: 10
url: ru/python-net/image-stamps-in-pdf-page/
description: Добавьте штамп изображения в ваш PDF документ, используя класс ImageStamp с библиотекой Aspose.PDF для Python.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Добавление штампов изображений в PDF с использованием Python",
    "alternativeHeadline": "Добавление штампов изображений в PDF с использованием Python",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "генерация документов pdf",
    "keywords": "pdf, python, генерация документов",
    "wordcount": "302",
    "proficiencyLevel":"Начинающий",
    "publisher": {
        "@type": "Organization",
        "name": "Команда документации Aspose.PDF",
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
    "url": "/python-net/image-stamps-in-pdf-page/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/image-stamps-in-pdf-page/"
    },
    "dateModified": "2023-04-04",
    "description": "Добавьте штамп изображения в ваш PDF документ, используя класс ImageStamp с библиотекой Aspose.PDF для Python."
}
</script>


## Добавление изображения штампа в PDF файл

Вы можете использовать класс [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) для добавления изображения штампа в PDF файл. Класс [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) предоставляет свойства, необходимые для создания штампа на основе изображения, такие как высота, ширина, непрозрачность и так далее.

Чтобы добавить изображение штампа:

1. Создайте объект Document и объект ImageStamp с использованием необходимых свойств.
1. Вызовите метод [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) класса [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) для добавления штампа в PDF.

Следующий фрагмент кода показывает, как добавить изображение штампа в PDF файл.

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf)

    # Создать штамп изображения
    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.background = True
    image_stamp.x_indent = 100
    image_stamp.y_indent = 100
    image_stamp.height = 300
    image_stamp.width = 300
    image_stamp.rotate = ap.Rotation.ON270
    image_stamp.opacity = 0.5
    # Добавить штамп на конкретную страницу
    document.pages[1].add_stamp(image_stamp)

    # Сохранить выходной документ
    document.save(output_pdf)
```


## Контроль качества изображения при добавлении штампа

При добавлении изображения в качестве штампа вы можете контролировать качество изображения. Свойство [quality](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/#properties) класса [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) используется для этой цели. Оно указывает качество изображения в процентах (допустимые значения от 0 до 100).

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf)

    # Создать штамп изображения
    image_stamp = ap.ImageStamp(input_jpg)
    image_stamp.quality = 10
    # Добавить штамп на определенную страницу
    document.pages[1].add_stamp(image_stamp)

    # Сохранить выходной документ
    document.save(output_pdf)
```

## Штамп изображения как фон в плавающей рамке

Aspose.PDF для Python API позволяет добавить штамп изображения как фон в плавающую рамку.
 The [background](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/#properties) свойство класса [FloatingBox](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) может быть использовано для установки фонового изображения для плавающего блока, как показано в следующем примере кода.

```python

    import aspose.pdf as ap

    # Создать объект Document
    document = ap.Document()
    # Добавить страницу в PDF документ
    page = document.pages.add()
    # Создать объект FloatingBox
    box = ap.FloatingBox(200.0, 100.0)
    # Установить левую позицию для FloatingBox
    box.left = 40
    # Установить верхнюю позицию для FloatingBox
    box.top = 80
    # Установить горизонтальное выравнивание для FloatingBox
    box.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Добавить текстовый фрагмент в коллекцию параграфов FloatingBox
    box.paragraphs.add(ap.text.TextFragment("основной текст"))
    # Установить границу для FloatingBox
    box.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)

    img = ap.Image()
    img.file = input_image_file
    # Добавить фоновое изображение
    box.background_image = img
    # Установить фоновый цвет для FloatingBox
    box.background_color = ap.Color.yellow
    # Добавить FloatingBox в коллекцию параграфов объекта страницы
    page.paragraphs.add(box)
    # Сохранить PDF документ
    document.save(output_pdf)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF для Python через .NET Библиотека",
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
                "contactType": "продажи",
                "areaServed": "США",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "Великобритания",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "Австралия",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Библиотека манипуляции PDF для Python",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>