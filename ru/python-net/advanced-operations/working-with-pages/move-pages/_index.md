---
title: Перемещение страниц PDF программно с помощью Python
linktitle: Перемещение страниц PDF
type: docs
weight: 100
url: ru/python-net/move-pages/
description: Попробуйте переместить страницы в нужное место или в конец PDF файла, используя Aspose.PDF для Python через .NET.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Перемещение страниц PDF программно Python",
    "alternativeHeadline": "Как перемещать страницы PDF с помощью Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация PDF документов",
    "keywords": "pdf, python, перемещение страниц pdf",
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
    "url": "/python-net/move-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/move-pages/"
    },
    "dateModified": "2023-04-04",
    "description": "Попробуйте переместить страницы в нужное место или в конец PDF файла, используя Aspose.PDF для Python через .NET."
}
</script>


## Перемещение страницы из одного PDF документа в другой

Эта тема объясняет, как переместить страницу из одного PDF документа в конец другого документа, используя Python. Чтобы переместить страницу, мы должны:

1. Создать объект класса [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) с исходным PDF файлом.
1. Создать объект класса [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) с целевым PDF файлом.
1. Получить страницу из коллекции [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) страницу в целевой документ.
1. Сохранить выходной PDF, используя метод [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).
1. [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) страницу в исходном документе.

1. Сохраните исходный PDF, используя метод [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

Следующий фрагмент кода показывает, как переместить одну страницу.

```python

    import aspose.pdf as ap

    srcDocument = ap.Document(src_file_name)
    dstDocument = ap.Document(dst_File_name)
    page = srcDocument.pages[2]
    dstDocument.pages.add(page)
    # Сохранить выходной файл
    dstDocument.save(dst_File_name_new)
    srcDocument.pages.delete(2)
    srcDocument.save(src_file_name_new)
```

## Перемещение нескольких страниц из одного PDF документа в другой

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) с исходным PDF файлом.
1. Создайте объект класса [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) с целевым PDF файлом.
1. Определите массив с номерами страниц, которые нужно переместить.
1. Запустите цикл по массиву:

1. Получите страницу из [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) коллекции.
1. [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) страницу в целевой документ.
1. Сохраните выходной PDF, используя метод [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).
1. Удалите [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) страницу в исходном документе, используя массив.
1. Сохраните исходный PDF, используя метод [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

Следующий фрагмент кода показывает, как вставить пустую страницу в конец PDF файла.

```python

    import aspose.pdf as ap

    srcDocument = ap.Document(input_pdf)
    dstDocument = ap.Document()
    pages = [1, 3]
    for page_index in pages:
        page = srcDocument.pages[page_index]
        dstDocument.pages.add(page)
    # Сохранить выходные файлы
    dstDocument.save(output_pdf_1)
    srcDocument.pages.delete(pages)
    srcDocument.save(output_pdf_2)
```


## Перемещение страницы в новое место в текущем PDF документе

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) с исходным PDF файлом.
1. Получите страницу из коллекции [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) страница в новое место (например, в конец).
1. [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) страница в предыдущем месте.
1. Сохраните выходной PDF, используя метод [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    import aspose.pdf as ap

    srcDocument = ap.Document(input_pdf)

    page = srcDocument.pages[2]
    srcDocument.pages.add(page)
    srcDocument.pages.delete(2)

    # Сохранить выходной файл
    srcDocument.save(output_pdf)