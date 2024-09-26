---
title: Работа с AcroForms
linktitle: AcroForms
type: docs
weight: 10
url: /net/acroforms/
description: С помощью Aspose.PDF для .NET вы можете создать форму с нуля, заполнить поля формы в документе PDF, извлечь данные из формы и т.д.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Работа с AcroForms",
    "alternativeHeadline": "Варианты работы с AcroForms в PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, acroforms в pdf",
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
    "url": "/net/acroforms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/acroforms/"
    },
    "dateModified": "2022-02-04",
    "description": "С помощью Aspose.PDF для .NET вы можете создать форму с нуля, заполнить поля формы в документе PDF, извлечь данные из формы и т.д."
}
</script>
## Основы AcroForms

**AcroForms** — это оригинальная технология форм PDF. AcroForms ориентированы на страницы. Они были впервые представлены в 1998 году. Они принимают входные данные в формате данных форм или FDF и формате данных форм XML или xFDF. Сторонние поставщики поддерживают AcroForms. Когда Adobe ввела AcroForms, они называли их «формой PDF, которая создается с помощью Adobe Acrobat Pro/Standard и которая не является специальным типом статичной или динамичной формы XFA. AcroForms портативны и работают на всех платформах.

Вы можете использовать AcroForms для добавления дополнительных страниц в документ формы PDF. Благодаря концепции шаблонов, вы можете использовать AcroForms для заполнения формы несколькими записями базы данных.

PDF 1.7 поддерживает два различных метода интеграции данных и форм PDF.

*AcroForms (также известные как формы Acrobat)*, введены и включены в спецификацию формата PDF 1.2.

*Формы архитектуры XML Adobe (XFA)*, введены в спецификацию формата PDF 1.5 как необязательная функция (спецификация XFA не включена в спецификацию PDF, она только упоминается.
*Формы Adobe XML Forms Architecture (XFA)*, введенные в спецификации формата PDF 1.5 как необязательная функция (Спецификация XFA не включена в спецификацию PDF, она только упоминается.

Для понимания **Acroforms** против **XFA** форм, нам нужно сначала понять основы. Для начала, обе являются формами PDF, которые вы можете использовать. Acroforms - это старая версия, созданная в 1998 году, и она все еще называется классической формой PDF. Формы XFA - это веб-страницы, которые вы можете сохранить в виде PDF, и они появились в 2003 году. Понадобилось некоторое время, прежде чем PDF начал принимать формы XFA.

AcroForms обладают возможностями, которых нет в XFA, и наоборот, XFA имеет некоторые возможности, которых нет в AcroForms. Например:

- AcroForms поддерживает концепцию "Шаблоны", позволяя добавлять дополнительные страницы к документу формы PDF для заполнения формы несколькими записями базы данных.
- XFA поддерживает концепцию переформатирования документа, позволяя полю изменять размер при необходимости для размещения данных.

Для более подробного изучения возможностей Java библиотеки, смотрите следующие статьи:
Для более подробного изучения возможностей библиотеки Java ознакомьтесь со следующими статьями:

- [Создать AcroForm](/pdf/net/create-form) - создать форму с нуля с помощью C#.
- [Заполнить AcroForm](/pdf/net/fill-form) - заполнить поле формы в вашем PDF-документе.
- [Извлечь AcroForm](/pdf/net/extract-form) - получить значение из всех или отдельного поля PDF-документа.
- [Изменение AcroForm](/pdf/net/modifing-form) - получить или установить FieldLimit, установить шрифт поля формы и т.д.
- [Отправка данных AcroForm](/pdf/net/posting-acroform-data/) - импортировать и экспортировать данные формы в XML-файл и из него.
- [Импорт и экспорт данных](/pdf/net/import-and-export-data/) - импортировать и экспортировать данные с использованием класса Form.

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

