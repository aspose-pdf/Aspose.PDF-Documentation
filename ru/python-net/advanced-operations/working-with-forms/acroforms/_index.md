---
title: Работа с AcroForms с использованием Python
linktitle: AcroForms
type: docs
weight: 10
url: /ru/python-net/acroforms/
description: С помощью Aspose.PDF для Python вы можете создать форму с нуля, заполнить поле формы в PDF-документе, извлечь данные из формы и т.д.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Работа с AcroForms с использованием Python",
    "alternativeHeadline": "Опции работы с AcroForms в PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация pdf документов",
    "keywords": "pdf, python, acroforms в pdf",
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
    "url": "/python-net/acroforms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/acroforms/"
    },
    "dateModified": "2023-02-04",
    "description": "С помощью Aspose.PDF для Python вы можете создать форму с нуля, заполнить поле формы в PDF-документе, извлечь данные из формы и т.д."
}
</script>


## Основы AcroForms

**AcroForms** - уникальная технология форм PDF от Adobe. AcroForms представляет собой формулу ориентированную на страницы. Они впервые появились в 1998 году. Они принимают ввод в виде формата данных или FDF и XML формата данных или xFDF. AcroForms поддерживаются сторонними поставщиками. Когда Adobe представила AcroForms, они называли их "PDF формой, автором которой является Adobe Acrobat Pro/Standard и которая не является специальным типом статической или динамической формы XFA. AcroForms портативны и работают на всех платформах.

Вы можете использовать AcroForms для добавления дополнительных страниц в документ формы PDF. Благодаря концепции шаблонов, вы можете использовать AcroForms для поддержки заполнения формы несколькими записями из базы данных.

PDF 1.7 поддерживает два различных метода интеграции данных и форм PDF.

*AcroForms (также известные как формы Acrobat)*, введенные и включенные в спецификацию формата PDF 1.2.

Для более подробного изучения возможностей Java-библиотеки, см. следующие статьи:

- [Создание AcroForm](/pdf/ru/python-net/create-form) - создание формы с нуля с помощью Python.
- [Заполнить AcroForm](/pdf/ru/python-net/fill-form) - заполните поле формы в вашем PDF документе.
- [Извлечь AcroForm](/pdf/ru/python-net/extract-form) - получите значение из всех или отдельного поля PDF документа.

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python Library",
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
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>