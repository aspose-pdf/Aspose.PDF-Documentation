---
title: Изменение размера страницы PDF с помощью C#
linktitle: Изменение размера страницы PDF
type: docs
weight: 40
url: /ru/net/change-page-size/
description: Измените размер страницы вашего PDF-документа с помощью библиотеки Aspose.PDF для .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Изменение размера страницы PDF с помощью C#",
    "alternativeHeadline": "Изменение размера страницы PDF с помощью .NET",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голубь",
        "givenName": "Анастасия",
        "familyName": "Голубь",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, изменение размера pdf, изменение размера pdf",
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
    "url": "/net/change-page-size/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/change-page-size/"
    },
    "dateModified": "2022-02-04",
    "description": "Измените размер страницы вашего PDF-документа с помощью библиотеки Aspose.PDF для .NET."
}
</script>

## Изменение размера страницы PDF

Aspose.PDF для .NET позволяет изменять размер страницы PDF с помощью нескольких строк кода в ваших .NET приложениях. Эта тема объясняет, как обновить/изменить размеры страницы (размер) существующего PDF файла.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

Класс [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) содержит метод SetPageSize(...), который позволяет установить размер страницы. Приведенный ниже фрагмент кода обновляет размеры страницы в несколько простых шагов:

1. Загрузите исходный PDF-файл.
1. Получите страницы в объект [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. Получите данную страницу.
1. Вызовите метод SetPageSize(..), чтобы обновить его размеры.
1. Вызовите метод Save(..) класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document), чтобы сгенерировать PDF-файл с обновленными размерами страниц.

{{% alert color="primary" %}}

Обратите внимание, что свойства высоты и ширины используют точки как основную единицу, где 1 дюйм = 72 точки и 1 см = 1/2.54 дюйма = 0.3937 дюйма = 28.3 точки.
Обратите внимание, что свойства высоты и ширины используют пункты в качестве базовой единицы, где 1 дюйм = 72 пункта, а 1 см = 1/2.54 дюйма = 0.3937 дюйма = 28.3 пункта.

{{% /alert %}}

Следующий фрагмент кода показывает, как изменить размеры страницы PDF на размер A4.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-UpdateDimensions-UpdateDimensions.cs" >}}

## Получить размер страницы PDF

Вы можете прочитать размер страницы PDF существующего файла PDF, используя Aspose.PDF для .NET. Следующий пример кода показывает, как считать размеры страницы PDF с помощью C#.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetDimensions-GetDimensions.cs" >}}

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


