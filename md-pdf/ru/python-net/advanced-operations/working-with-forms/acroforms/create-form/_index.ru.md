---
title: Создание AcroForm - Создание заполняемого PDF на Python
linktitle: Создание AcroForm
type: docs
weight: 10
url: /python-net/create-form/
description: С Aspose.PDF для Python вы можете создать форму с нуля в вашем PDF файле
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Создание AcroForm на Python",
    "alternativeHeadline": "Как создать AcroForm в PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация PDF документов",
    "keywords": "pdf, python, создание acroform",
    "wordcount": "302",
    "proficiencyLevel":"Начинающий",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Документальная команда",
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
    "url": "/python-net/create-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/create-form/"
    },
    "dateModified": "2022-02-04",
    "description": "С Aspose.PDF для Python вы можете создать форму с нуля в вашем PDF файле"
}
</script>


## Создание формы с нуля

### Добавление поля формы в PDF документ

Класс [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) предоставляет коллекцию под названием [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/), которая помогает управлять полями формы в PDF документе.

Чтобы добавить поле формы:

1. Создайте поле формы, которое вы хотите добавить.
2. Вызовите метод [add](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/#methods) коллекции Form.

### Добавление TextBoxField

Пример ниже показывает, как добавить [TextBoxField](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/).

```python

    import aspose.pdf as ap

    # Открыть документ
    pdfDocument = ap.Document(input_file)

    # Создать поле
    textBoxField = ap.forms.TextBoxField(pdfDocument.pages[1], ap.Rectangle(100, 200, 300, 300, True))
    textBoxField.partial_name = "textbox1"
    textBoxField.value = "Text Box"

    border = ap.annotations.Border(textBoxField)
    border.width = 5
    border.dash = ap.annotations.Dash(1, 1)
    textBoxField.border = border

    textBoxField.color = ap.Color.green

    # Добавить поле в документ
    pdfDocument.form.add(textBoxField, 1)

    # Сохранить измененный PDF
    pdfDocument.save(output_pdf)
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF для библиотеки Python",
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
    "applicationCategory": "Библиотека для работы с PDF для Python",
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