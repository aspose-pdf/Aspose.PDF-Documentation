---
title: Как создать PDF с использованием Python
linktitle: Создание PDF документа
type: docs
weight: 10
url: /python-net/create-pdf-document/
description: Создавайте и форматируйте PDF документы с помощью Aspose.PDF для Python через .NET.
lastmod: "2023-04-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Как создать PDF с использованием Python",
    "alternativeHeadline": "Создание PDF документа с нуля через Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация PDF документов",
    "keywords": "pdf, python, dotnet, создание PDF документа",
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
    "url": "/python-net/create-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/create-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Создавайте и форматируйте PDF документы с помощью Aspose.PDF для Python через .NET."
}
</script>


**Aspose.PDF для Python через .NET** — это API для работы с PDF, который позволяет разработчикам создавать, загружать, изменять и конвертировать PDF-файлы непосредственно из Python для .NET приложений, используя всего несколько строк кода.

## Как создать простой PDF файл

Чтобы создать PDF с использованием Python через .NET с Aspose.PDF, выполните следующие шаги:

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. Добавьте объект [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) в коллекцию [pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) объекта Document
1. Добавьте [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) в коллекцию [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) страницы
1. Сохраните результирующий PDF документ

```python

    import aspose.pdf as ap

    # Инициализировать объект документа
    document = ap.Document()
    # Добавить страницу
    page = document.pages.add()
    # Добавить текст на новую страницу
    page.paragraphs.add(ap.text.TextFragment("Hello World!"))
    # Сохранить обновленный PDF
    document.save(output_pdf)
```