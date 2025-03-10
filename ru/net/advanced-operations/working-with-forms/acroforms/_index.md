---
title: Работа с AcroForms
linktitle: АкроФормы
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ru/net/acroforms/
description: С помощью Aspose.PDF for .NET вы можете создать форму с нуля, заполнить поля формы в PDF-документе, извлечь данные из формы и т. д.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with AcroForms",
    "alternativeHeadline": "Enhance PDF forms with flexible AcroForms functionality",
    "abstract": "Aspose.PDF для .NET предоставляет расширенные возможности для работы с AcroForms, позволяя пользователям эффективно создавать формы с нуля, заполнять поля PDF и без проблем извлекать данные. Эта мощная функция поддерживает интеграцию нескольких записей базы данных, обеспечивая динамическое управление формами и оптимизированный пользовательский интерфейс.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "AcroForms, PDF forms technology, create a form, fill form fields, extract data, database records, Templates, modify AcroForms, posting AcroForm data, import and export data",
    "wordcount": "484",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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
    "url": "/net/acroforms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/acroforms/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и лёгкие задачи, но и справляться с более сложными целями. Ознакомьтесь со следующим разделом для опытных пользователей и разработчиков."
}
</script>

## Основы AcroForms

**AcroForms** — это оригинальная технология форм PDF. AcroForms — это форма, ориентированная на страницу. Они были впервые представлены в 1998 году. Они принимают входные данные в формате Forms Data Format (FDF) и XML Forms Data Format (xFDF). Сторонние поставщики поддерживают AcroForms. Когда Adobe представила AcroForms, они назвали их «PDF-формой, созданной с помощью Adobe Acrobat Pro/Standard и не являющейся особым типом статической или динамической формы XFA». Acroforms переносимы и работают на всех платформах.

Вы можете использовать AcroForms для добавления дополнительных страниц в документ PDF-формы. Благодаря концепции шаблонов вы можете использовать AcroForms для поддержки заполнения формы несколькими записями базы данных.

PDF 1.7 поддерживает два различных метода интеграции данных и PDF-форм.

*AcroForms (также известные как формы Acrobat)*, представленные и включённые в спецификацию формата PDF 1.2.

*Формы Adobe XML Forms Architecture (XFA)*, представленные в спецификации формата PDF 1.5 в качестве дополнительной функции (спецификация XFA не включена в спецификацию PDF, на неё только ссылаются).

Чтобы понять разницу между **Acroforms** и формами **XFA**, сначала нужно разобраться в основах. Начнём с того, что и то, и другое — это PDF-формы, которые вы можете использовать. Acroforms — более старая версия, созданная ещё в 1998 году, и до сих пор называется классической PDF-формой. Формы XFA — это веб-страницы, которые можно сохранить в виде PDF-файла, появились в 2003 году. Прошло некоторое время, прежде чем PDF начал поддерживать формы XFA.

У AcroForms есть возможности, которых нет у XFA, и наоборот, у XFA есть некоторые возможности, которых нет у AcroForms. Например:

- AcroForms поддерживает концепцию «Шаблонов», позволяя добавлять дополнительные страницы к документу PDF-формы для поддержки заполнения формы несколькими записями базы данных.
- XFA поддерживает концепцию переформатирования документа, позволяя при необходимости изменять размер поля для размещения данных.

Для более детального изучения возможностей библиотеки Java см. следующие статьи:

- [Создание AcroForm](/pdf/net/create-form) — создайте форму с нуля с помощью C#.
- [Заполнение AcroForm](/pdf/net/fill-form) — заполните поля формы в вашем PDF-документе.
- [Извлечение AcroForm](/pdf/net/extract-form) — получите значение из всех полей или отдельного поля PDF-документа.
- [Изменение AcroForm](/pdf/net/modifing-form) — получение или установка FieldLimit, установка шрифта поля формы и т.д.
- [Размещение данных AcroForm](/pdf/net/posting-acroform-data/) — импорт и экспорт данных формы в файл XML.
- [Импорт и экспорт данных](/pdf/net/import-and-export-data/) —  импорт и экспорт данных с использованием класса Form.
- [Удаление форм из PDF](/pdf/net/remove-form/) — удаление текста на основе подтипа/формы, удаление всех форм.
- [Импорт и экспорт данных в JSON](/pdf/net/import-export-json/) — импорт и экспорт данных с помощью JSON.

<!-- 2316813259 -->
<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "Программное приложение",
    "название": "Библиотека Aspose.PDF for .NET",
    "изображение": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "издательство": {
        "@type": "Организация",
        "название": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "логотип": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com
<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>