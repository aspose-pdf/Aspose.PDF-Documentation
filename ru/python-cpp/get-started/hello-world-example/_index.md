---
title: Пример Hello World на языке Python
linktitle: Пример Hello World
type: docs
weight: 20
url: ru/python-cpp/hello-world-example/
description: Этот пример демонстрирует, как создать простой PDF-документ "Hello, World!" с использованием Aspose.PDF для Python
lastmod: "2023-07-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Пример Hello World на языке Python",
    "alternativeHeadline": "Пример Aspose.PDF Python (через C++)",
    "author": {
        "@type": "Person",
        "givenName": "Андрий",
        "familyName": "Андруховский",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "генерация PDF-документов",
    "keywords": "pdf, Python, генерация документов",
    "wordcount": "302",
    "proficiencyLevel":"Начинающий",
    "publisher": {
        "@type": "Organization",
        "name": "Команда документации Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-cpp.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://https://www.youtube.com/@AsposePDF",
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
    "url": "http://docs.aspose.com/pdf/python-cpp/hello-world-example/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "http://docs.aspose.com/pdf/python-cpp/hello-world-example/"
    },
    "dateModified": "2022-02-04",
    "description": "Этот пример демонстрирует, как создать простой PDF-документ с использованием Aspose.PDF для Python.",
    "articleBody": "Простой пример может помочь продемонстрировать возможности языка программирования или программного обеспечения. Обычно это делается с помощью примера \"Hello World\".\n\nAspose.PDF для Python через C++ — это мощный API для работы с PDF, который позволяет разработчикам создавать, изменять и конвертировать PDF-документы в своих Python-приложениях. Он поддерживает работу с различными форматами файлов, такими как PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX и форматами изображений. В этой статье мы покажем, как создать PDF-документ с текстом \"Hello World!\" с использованием Aspose.PDF API. Вам необходимо установить Aspose.PDF для Python через C++ в вашей среде перед запуском следующего примера кода.\n1. Импортируйте модуль AsposePdfPython.\n2. Создайте новый объект PDF-документа с использованием функции document_create.\n3. Получите коллекцию страниц документа с использованием функции document_get_pages.\n4. Добавьте новую страницу в коллекцию страниц с использованием функции page_collection_add_page.\n5. Получите коллекцию абзацев страницы с использованием функции page_get_paragraphs.\n6. Создайте новый объект изображения с использованием функции image_create.\n7. Установите имя файла объекта изображения в \"sample.jpg\" с использованием функции image_set_file.\n8. Добавьте объект изображения в коллекцию абзацев с использованием функции paragraphs_add_image.\n9. Сохраните документ в файл с именем \"document.pdf\" с использованием функции document_save.\n10. Закройте дескриптор документа с использованием функции close_handle."
}
</script>


A simple use case can help to demonstrate the features of a programming language or software. This is usually done with a "Hello World" example.

Простой пример использования может помочь продемонстрировать возможности языка программирования или программного обеспечения. Обычно это делается с примером "Hello World".

Aspose.PDF for Python via C++ is a powerful PDF API that enables the developers to create, manipulate and convert PDF documents in their Python applications. It supports working with various file formats such as PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX and image file formats. In this article, we will show you how to create a PDF document with the text "Hello World!" using Aspose.PDF API. You need to install Aspose.PDF for Python via C++ in your environment before running the following code sample.

Aspose.PDF для Python через C++ — это мощный API для работы с PDF, который позволяет разработчикам создавать, изменять и конвертировать PDF-документы в их Python-приложениях. Он поддерживает работу с различными форматами файлов, такими как PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX и форматы изображений. В этой статье мы покажем вам, как создать PDF-документ с текстом "Hello World!" используя Aspose.PDF API. Вам необходимо установить Aspose.PDF для Python через C++ в вашей среде перед запуском следующего примера кода.

1. Import the `AsposePdfPython` module.
1. Create a new PDF document object using the `document_create` function.
1. Get the pages collection of the document using the `document_get_pages` function.
1. Add a new page to the pages collection using the `page_collection_add_page` function.

1. Импортируйте модуль `AsposePdfPython`.
1. Создайте новый объект PDF-документа, используя функцию `document_create`.
1. Получите коллекцию страниц документа, используя функцию `document_get_pages`.
1. Добавьте новую страницу в коллекцию страниц, используя функцию `page_collection_add_page`.

1. Получите коллекцию абзацев страницы с помощью функции `page_get_paragraphs`.
1. Создайте новый объект изображения с помощью функции `image_create`.
1. Установите имя файла объекта изображения в "sample.jpg" с помощью функции `image_set_file`.
1. Добавьте объект изображения в коллекцию абзацев с помощью функции `paragraphs_add_image`.
1. Сохраните документ в файл с именем "document.pdf" с помощью функции `document_save`.
1. Закройте дескриптор документа с помощью функции `close_handle`.

Следующий фрагмент кода - это программа Hello World, демонстрирующая работу Aspose.PDF для Python через C++.

```python
from AsposePdfPython import *
 
doc = document_create()
pages = document_get_pages(doc)
page = page_collection_add_page(pages)
paragraphs = page_get_paragraphs(page)
image = image_create()
image_set_file(image,"sample.jpg")
paragraphs_add_image(paragraphs,image)
 
document_save(doc, "document.pdf")
close_handle(doc)
```