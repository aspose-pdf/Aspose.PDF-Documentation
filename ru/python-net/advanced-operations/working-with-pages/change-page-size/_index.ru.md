---
title: Изменение размера страницы PDF с помощью Python
linktitle: Изменение размера страницы PDF
type: docs
weight: 60
url: /python-net/change-page-size/
description: Измените размер страницы в вашем PDF документе с использованием библиотеки Aspose.PDF для Python через .NET.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Изменение размера страницы PDF с помощью Python",
    "alternativeHeadline": "Изменение размера страницы PDF с помощью Python",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация PDF документов",
    "keywords": "pdf, python, изменение размера pdf, изменение размера страницы pdf",
    "wordcount": "302",
    "proficiencyLevel":"Начальный",
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
    "url": "/python-net/change-page-size/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/change-page-size/"
    },
    "dateModified": "2023-04-04",
    "description": "Измените размер страницы в вашем PDF документе с использованием библиотеки Aspose.PDF для Python через .NET."
}
</script>


## Изменение размера страницы PDF

Aspose.PDF для Python через .NET позволяет изменять размер страницы PDF с помощью простых строк кода в ваших приложениях на Python. Эта тема объясняет, как обновить/изменить размеры страниц существующего PDF-файла.

Класс [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) содержит метод [set_page_size()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods), который позволяет установить размер страницы. Пример кода ниже обновляет размеры страниц в несколько простых шагов:

1. Загрузите исходный PDF-файл.
1. Получите страницы в объект [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Получите заданную страницу.
1. Вызовите метод set_page_size(), чтобы обновить ее размеры.
1. Вызовите метод [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) класса [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), чтобы сгенерировать PDF-файл с обновленными размерами страниц.

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)

    # Получить конкретную страницу
    page = document.pages[1]

    # Установить размер страницы как A4 (11.7 x 8.3 дюймов), и в Aspose.Pdf 1 дюйм = 72 точки
    # Таким образом, размеры A4 в точках будут (842.4, 597.6)
    page.set_page_size(597.6, 842.4)

    # Сохранить обновленный документ
    document.save(output_pdf)
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF для .NET Library",
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