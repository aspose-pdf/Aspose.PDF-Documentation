---
title: Работа с аннотациями
linktitle: Аннотации в PDF
type: docs
weight: 100
url: /ru/net/annotations/
description: Этот раздел демонстрирует, как использовать все виды аннотаций в вашем PDF-файле с помощью библиотеки Aspose.PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/working-with-annotations/
    - /net/annotation/
    - /net/working-with-annotations-facades/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Аннотации PDF",
    "alternativeHeadline": "Работа с аннотациями в PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голубь",
        "givenName": "Анастасия",
        "familyName": "Голубь",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, аннотации",
    "wordcount": "302",
    "proficiencyLevel":"Начинающий",
    "publisher": {
        "@type": "Organization",
        "name": "Команда документации Aspose.PDF",
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
                "contactType": "продажи",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/annotations/"
    },
    "dateModified": "2022-02-04",
    "description": "Этот раздел демонстрирует, как использовать все виды аннотаций в вашем PDF-файле с помощью библиотеки Aspose.PDF."
}
</script>
Содержимое внутри страницы PDF трудно редактировать, но спецификация PDF определяет полный набор объектов, которые можно добавлять на страницы PDF без изменения содержимого страницы.

Эти объекты называются аннотациями, и их цель варьируется от разметки содержимого страницы до реализации интерактивных функций, таких как формы.

Просмотрщики PDF обычно позволяют создавать и редактировать различные типы аннотаций, например, выделения текста, заметки, линии или фигуры. Независимо от типов аннотаций, которые могут быть созданы, просмотрщики PDF, соответствующие спецификации PDF, также должны поддерживать отображение всех типов аннотаций.

Аннотация является важной частью файла PDF. Используя Aspose.PDF для .NET, вы можете добавить новую аннотацию, отредактировать существующую аннотацию и удалить аннотации и так далее. В этом разделе рассматривается следующая тема:

Вы можете делать следующее:

- [Обзор аннотаций](/pdf/ru/net/overview-of-annotations/) - узнайте, какие типы аннотаций определены спецификацией PDF, и что поддерживает Aspose.PDF.
- [Добавить, удалить и получить аннотацию](/pdf/ru/net/add-delete-and-get-annotation/) - этот раздел объясняет, как работать со всеми типами разрешенных аннотаций.
- [Добавление, удаление и получение аннотаций](/pdf/ru/net/add-delete-and-get-annotation/) - этот раздел объясняет, как работать со всеми типами разрешенных аннотаций.
- [Импорт и экспорт аннотаций в формате XFDF](/pdf/ru/net/import-export-xfdf/) - библиотека Aspose.PDF предоставляет методы для импорта и экспорта данных аннотаций в файлы XFDF.

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

