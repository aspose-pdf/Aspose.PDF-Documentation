---
title: Дополнительные аннотации с использованием Python
linktitle: Дополнительные аннотации
type: docs
weight: 60
url: ru/python-net/extra-annotations/
description: Этот раздел описывает, как добавлять, получать и удалять дополнительные виды аннотаций из вашего PDF документа.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Дополнительные аннотации с использованием Python",
    "alternativeHeadline": "Как добавить дополнительные аннотации в PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "создание PDF документов",
    "keywords": "pdf, python, аннотация ссылки, аннотация каретки",
    "wordcount": "302",
    "proficiencyLevel":"Начальный",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/python-net/extra-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/extra-annotations/"
    },
    "dateModified": "2023-02-04",
    "description": "Этот раздел описывает, как добавлять, получать и удалять дополнительные виды аннотаций из вашего PDF документа с помощью Python."
}
</script>


## Как добавить аннотацию каретки в существующий PDF файл с помощью Python

Аннотация каретки — это символ, который указывает на редактирование текста. Аннотация каретки также является аннотацией разметки, поэтому класс Caret наследуется от класса Markup и также предоставляет функции для получения или установки свойств аннотации каретки и сброса потока отображения аннотации каретки. Аннотации каретки часто используются для предложения изменений, дополнений или изменений в тексте.

Шаги, с помощью которых мы создаем аннотацию каретки:

1. Загрузите PDF файл - новый [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Создайте новую [CaretAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/caretannotation/) и установите параметры каретки (новый прямоугольник, заголовок, тема, флаги, цвет). Эта аннотация используется для указания вставки текста.
1. Как только мы сможем добавить аннотации на страницу.

Следующий фрагмент кода показывает, как добавить аннотацию каретки в PDF файл:

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_file)

    caretAnnotation1 = ap.annotations.CaretAnnotation(
        document.pages[1], ap.Rectangle(200, 700.664, 308.708, 740.769, True)
    )
    caretAnnotation1.title = "Пользователь Aspose"
    caretAnnotation1.subject = "Вставленный текст 1"
    caretAnnotation1.flags = ap.annotations.AnnotationFlags.PRINT
    caretAnnotation1.color = ap.Color.blue

    document.pages[1].annotations.append(caretAnnotation1)
    document.save(output_file)
```


### Получение аннотации каретки

Пожалуйста, попробуйте использовать следующий фрагмент кода для получения аннотации каретки в PDF документе

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    caretAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CARET)
    ]

    for ca in caretAnnotations:
        print(ca.rect)
```

### Удаление аннотации каретки

Следующий фрагмент кода показывает, как удалить аннотацию каретки из PDF файла с использованием Python.

```python

    import aspose.pdf as ap

    # Загрузите PDF файл
    document = ap.Document(input_file)
    caretAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CARET)
    ]

    for ca in caretAnnotations:
        document.pages[1].annotations.delete(ca)

    document.save(output_file)
```

## Добавление аннотации ссылки

[Ссылки](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/linkannotation/) — это аннотации, которые открывают URL-адреса или перемещаются к определённым позициям внутри того же или внешнего документа при клике.

A Link Annotations — это прямоугольная область, которую можно разместить в любом месте страницы. Каждая ссылка имеет соответствующее действие PDF, связанное с ней. Это действие выполняется, когда пользователь щелкает в области этой ссылки.

Следующий фрагмент кода показывает, как добавить аннотацию ссылки в PDF-файл, используя пример с номером телефона:

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    # Создать объект TextFragmentAbsorber для поиска номера телефона
    textFragmentAbsorber = ap.text.TextFragmentAbsorber("file")

    # Применить поглотитель только для 1-й страницы
    document.pages[1].accept(textFragmentAbsorber)

    phoneNumberFragment = textFragmentAbsorber.text_fragments[1]

    # Создать аннотацию ссылки и установить действие для вызова номера телефона
    linkAnnotation = ap.annotations.LinkAnnotation(document.pages[1], phoneNumberFragment.rectangle)
    linkAnnotation.action = ap.annotations.GoToURIAction("www.aspose.com")

    # Добавить аннотацию на страницу
    document.pages[1].annotations.append(linkAnnotation)
    document.save(output_file)
```


### Получение Аннотации Ссылки

Пожалуйста, попробуйте использовать следующий фрагмент кода, чтобы получить [LinkAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/linkannotation/) из PDF-документа.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    linkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in linkAnnotations:
        print(la.rect)
```

### Удаление Аннотации Ссылки

Следующий фрагмент кода показывает, как удалить аннотацию ссылки из PDF-файла. Для этого нам нужно найти и удалить все аннотации ссылок на первой странице. После этого мы сохраним документ с удаленной аннотацией.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for hs in highlightAnnotations:
        document.pages[1].annotations.delete(hs)

    document.save(output_file)
```


## Редактирование определенного региона страницы с помощью аннотации редактирования с использованием Aspose.PDF для Python

Aspose.PDF для Python через .NET поддерживает возможность добавления и изменения аннотаций в существующем PDF-файле. Аннотации редактирования в PDF-документах служат для окончательного удаления или скрытия конфиденциальной информации в документе. Процесс редактирования информации включает в себя покрытие или затенение определенного контента, такого как текст, изображения или графика, таким образом, чтобы ограничить его видимость и доступность для других. Это гарантирует, что конфиденциальная информация остается скрытой и защищенной в документе. Для выполнения этого требования предоставляется класс под названием [RedactionAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/redactionannotation/), который может использоваться для редактирования определенных регионов страницы или может использоваться для управления существующими RedactionAnnotations и их редактирования (т.е. сглаживания аннотации и удаления текста под ней).

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    page = document.pages[1]
    redactionAnnotation = ap.annotations.RedactionAnnotation(page, ap.Rectangle(270, 190, 371, 250, True))
    redactionAnnotation.title = "John Smith"
    redactionAnnotation.fill_color = ap.Color.light_gray
    redactionAnnotation.color = ap.Color.red
    redactionAnnotation.redact()

    page.annotations.append(redactionAnnotation)
    document.save(output_file)
```


### Получить Аннотацию Сокрытия

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    redactionAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.REDACTION)
    ]

    for pa in redactionAnnotations:
        print(pa.rect)
```    

### Удалить Аннотацию Сокрытия

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    redactionAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.REDACTION)
    ]

    for pa in redactionAnnotations:
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