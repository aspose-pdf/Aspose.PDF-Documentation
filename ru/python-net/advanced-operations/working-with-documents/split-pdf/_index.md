---
title: Разделение PDF программно на Python
linktitle: Разделение PDF файлов
type: docs
weight: 60
url: /ru/python-net/split-pdf-document/
description: Эта тема показывает, как разделить страницы PDF на отдельные PDF файлы в ваших приложениях на Python.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Разделение PDF программно",
    "alternativeHeadline": "Как разделить PDF с помощью Python",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация PDF документов",
    "keywords": "pdf, python, разделение pdf",
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
    "url": "/python-net/split-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/split-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Эта тема показывает, как разделить страницы PDF на отдельные PDF файлы в ваших приложениях на Python."
}
</script>


Разделение страниц PDF может быть полезной функцией для тех, кто хочет разделить большой файл на отдельные страницы или группы страниц.

## Живой пример

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) — это бесплатное онлайн-приложение, которое позволяет исследовать, как работает функциональность разделения презентаций.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

Эта тема показывает, как разделить страницы PDF на отдельные PDF файлы в ваших приложениях на Python. Чтобы разделить страницы PDF на файлы с одной страницей с использованием Python, можно следовать следующим шагам:

1. Переберите страницы PDF-документа через коллекцию [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) объекта [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. Для каждой итерации создайте новый объект Document и добавьте отдельный объект [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) в пустой документ

1. Сохраните новый PDF, используя метод [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)

## Разделение PDF на несколько файлов или отдельных PDF в Python

Следующий фрагмент кода на Python показывает, как разделить страницы PDF на отдельные PDF-файлы.

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf)

    page_count = 1

    # Перебрать все страницы
    for pdfPage in document.pages:
        new_document = ap.Document()
        new_document.pages.add(pdfPage)
        new_document.save(output_path + "_page_" + str(page_count) + ".pdf")
        page_count = page_count + 1
```

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
    "applicationCategory": "PDF Manipulation Library for Python",
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