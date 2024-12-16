---
title: Добавить страницы в PDF с помощью Python
linktitle: Добавить страницы
type: docs
weight: 10
url: /ru/python-net/add-pages/
description: Эта статья учит, как вставить (добавить) страницу в нужное место в PDF-файле. Узнайте, как перемещать, удалять (удалять) страницы из PDF-файла с использованием C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Добавить страницы в PDF с помощью Python",
    "alternativeHeadline": "Как добавить страницы в PDF-документ",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация PDF-документов",
    "keywords": "pdf, python, добавить страницу в pdf, вставить страницу в pdf",
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
    "url": "/python-net/add-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "Эта статья учит, как вставить (добавить) страницу в нужное место в PDF-файле. Узнайте, как перемещать, удалять (удалять) страницы из PDF-файла с использованием Python."
}
</script>


Aspose.PDF for Python via .NET API предоставляет полную гибкость для работы со страницами в PDF-документе с использованием Python. Он поддерживает все страницы PDF-документа в [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/), который можно использовать для работы со страницами PDF. Aspose.PDF for Python via .NET позволяет вставить страницу в PDF-документ в любое место в файле, а также добавлять страницы в конец PDF-файла. Этот раздел показывает, как добавлять страницы в PDF с использованием Python.

## Добавить или вставить страницу в PDF-файл

Aspose.PDF for Python via .NET позволяет вставить страницу в PDF-документ в любое место в файле, а также добавлять страницы в конец PDF-файла.

### Вставить пустую страницу в PDF-файл в желаемое место

Чтобы вставить пустую страницу в PDF-файл:

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) с входным PDF-файлом.

1. Вызовите метод [insert](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection/methods/insert) коллекции [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) с указанным индексом.
1. Сохраните выходной PDF, используя метод [save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

Следующий фрагмент кода показывает, как вставить страницу в PDF файл.

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf)
    # Вставить пустую страницу в PDF
    document.pages.insert(2)
    # Сохранить выходной файл
    document.save(output_pdf)
```

### Добавить пустую страницу в конец PDF файла

Иногда необходимо, чтобы документ заканчивался пустой страницей. Эта тема объясняет, как вставить пустую страницу в конец PDF документа.

Чтобы вставить пустую страницу в конец PDF файла:

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) с входным PDF файлом.

1. Вызовите метод [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) коллекции [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/), без параметров.
1. Сохраните выходной PDF, используя метод [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

Следующий фрагмент кода показывает, как вставить пустую страницу в конец PDF-файла.

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf)

    # Вставить пустую страницу в конец PDF-файла
    document.pages.add()

    # Сохранить выходной файл
    document.save(output_pdf)