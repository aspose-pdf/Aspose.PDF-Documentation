---
title: Как объединить PDF с использованием Python
linktitle: Объединение PDF файлов
type: docs
weight: 50
url: /ru/python-net/merge-pdf-documents/
keywords: "объединить несколько pdf в один pdf python, комбинировать несколько pdf в один python, объединить несколько pdf в один python"
description: Эта страница объясняет, как объединить PDF документы в один PDF файл с помощью Python.
lastmod: "2023-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Как объединить PDF с использованием Python",
    "alternativeHeadline": "Комбинирование PDF документов с помощью Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "манипуляция pdf документами",
    "keywords": "pdf, python, объединение pdf, конкатенация, комбинирование pdf",
    "wordcount": "212",
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
    "url": "https://docs.aspose.com/pdf/python-net/merge-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://docs.aspose.com/pdf/python-net/merge-pdf-documents/"
    },
    "dateModified": "2023-04-14",
    "description": "Эта страница объясняет, как объединить PDF документы в один PDF файл с помощью Python через .NET."
}
</script>


## Объединение или комбинирование нескольких PDF в один PDF на Python

Объединение PDF файлов является очень популярным запросом среди пользователей. Это может быть полезно, когда у вас есть несколько PDF файлов, которые вы хотите поделиться или сохранить вместе как единый документ.

Объединение PDF файлов может помочь вам организовать ваши документы, освободить место для хранения на вашем ПК и поделиться несколькими PDF файлами с другими, объединив их в один документ.

Объединение PDF в Python через .NET не является простой задачей без использования сторонней библиотеки. Эта статья показывает, как объединить несколько PDF файлов в один PDF документ, используя Aspose.PDF для Python через .NET.

## Объединение PDF файлов с использованием Python и DOM

Чтобы соединить два PDF файла:

1. Создайте два объекта [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), каждый из которых содержит один из входных PDF файлов.

1. Затем вызовите метод [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) коллекции [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) для объекта Document, к которому вы хотите добавить другой PDF файл.
1. Передайте коллекцию PageCollection второго объекта Document в метод [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) первой коллекции PageCollection.
1. Наконец, сохраните выходной PDF файл, используя метод [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

Следующий код показывает, как объединить PDF файлы.

```python

    import aspose.pdf as ap

    # Открыть первый документ
    document1 = ap.Document(input_pdf_1)
    # Открыть второй документ
    document2 = ap.Document(input_pdf_2)

    # Добавить страницы второго документа в первый
    document1.pages.add(document2.pages)

    # Сохранить объединенный выходной файл
    document1.save(output_pdf)
```


## Live Example

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) — это бесплатное веб-приложение, которое позволяет исследовать, как работает функциональность слияния презентаций.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)

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