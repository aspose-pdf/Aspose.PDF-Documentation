---
title: Добавить Номер Страницы в PDF с помощью Python
linktitle: Добавить Номер Страницы
type: docs
weight: 30
url: /ru/python-net/add-page-number/
description: Aspose.PDF для Python через .NET позволяет добавлять штамп номера страницы в ваш PDF файл, используя класс PageNumberStamp.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Добавить Номер Страницы в PDF с помощью Python",
    "alternativeHeadline": "Как добавить штамп номера страницы в PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "создание PDF документов",
    "keywords": "pdf, python, штамп номера страницы",
    "wordcount": "302",
    "proficiencyLevel":"Начинающий",
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
    "url": "/python-net/add-page-number/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-page-number/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF для Python через .NET позволяет добавлять штамп номера страницы в ваш PDF файл, используя класс PageNumberStamp."
}
</script>


Все документы должны содержать номера страниц. Номер страницы облегчает читателю поиск различных частей документа. **Aspose.PDF для Python через .NET** позволяет добавлять номера страниц с помощью [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/).

Вы можете использовать класс [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) для добавления штампа номера страницы в PDF-файл.
 [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) класс предоставляет свойства, необходимые для создания штампа с номером страницы, такие как формат, поля, выравнивание, начальный номер и т.д. Для того чтобы добавить штамп с номером страницы, необходимо создать объект [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) и объект [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) с использованием необходимых свойств. После этого можно вызвать метод [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) класса [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) для добавления штампа в PDF. Также можно установить атрибуты шрифта для штампа с номером страницы. Следующий фрагмент кода показывает, как добавить номера страниц в PDF файл.

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf)

    # Создать штамп с номером страницы
    page_number_stamp = ap.PageNumberStamp()
    # Является ли штамп фоном
    page_number_stamp.background = False
    page_number_stamp.format = "Страница # из " + str(len(document.pages))
    page_number_stamp.bottom_margin = 10
    page_number_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    page_number_stamp.starting_number = 1
    # Установить свойства текста
    page_number_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    page_number_stamp.text_state.font_size = 14.0
    page_number_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    page_number_stamp.text_state.font_style = ap.text.FontStyles.ITALIC
    page_number_stamp.text_state.foreground_color = ap.Color.aqua

    # Добавить штамп на конкретную страницу
    document.pages[1].add_stamp(page_number_stamp)

    # Сохранить выходной документ
    document.save(output_pdf)
```

## Пример в реальном времени

[Добавить номера страниц в PDF](https://products.aspose.app/pdf/page-number) — это бесплатное веб-приложение, которое позволяет вам исследовать, как работает функциональность добавления номеров страниц.

[![Как добавить номер страницы в PDF с помощью Python](page_number.png)](https://products.aspose.app/pdf/page-number)

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
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
    "applicationCategory": "Библиотека для манипуляции PDF для Python",
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