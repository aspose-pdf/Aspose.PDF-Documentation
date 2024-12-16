---
title: Программное удаление страниц PDF на Python
linktitle: Удаление страниц PDF
type: docs
weight: 80
url: /ru/python-net/delete-pages/
description: Вы можете удалить страницы из вашего PDF-файла, используя библиотеку Aspose.PDF для Python через .NET.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Программное удаление страниц PDF на Python",
    "alternativeHeadline": "Как удалить страницы PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "создание PDF-документов",
    "keywords": "pdf, python, удаление страниц pdf, удаление страниц из pdf",
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
    "url": "/python-net/delete-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/delete-pages/"
    },
    "dateModified": "2023-04-04",
    "description": "Вы можете удалить страницы из вашего PDF-файла, используя библиотеку Aspose.PDF для Python через .NET."
}
</script>


Вы можете удалить страницы из PDF-файла, используя Aspose.PDF для Python через .NET. Чтобы удалить определённую страницу из коллекции [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).

## Удалить страницу из PDF-файла

1. Вызовите метод [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) и укажите индекс страницы
1. Вызовите метод [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) для сохранения обновленного PDF-файла
Следующий фрагмент кода показывает, как удалить определённую страницу из PDF-файла, используя Python.

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf)

    # Удалить определённую страницу
    document.pages.delete(2)

    # Сохранить обновленный PDF
    document.save(output_pdf)