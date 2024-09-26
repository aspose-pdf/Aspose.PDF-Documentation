---
title: Работа с PDF документами с использованием C#
linktitle: Работа с документами
type: docs
weight: 10
url: /net/working-with-documents/
description: В этой статье описано, какие манипуляции можно выполнить с документом с помощью библиотеки Aspose.PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/working-with-document/
    - /net/working-with-document-facades/
    - /net/create-document/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Работа с PDF документами с использованием C#",
    "alternativeHeadline": "Манипуляции с PDF документами",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация PDF документов",
    "keywords": "pdf, c#, pdf документы",
    "wordcount": "302",
    "proficiencyLevel":"Начальный",
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
    "url": "/net/working-with-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-documents/"
    },
    "dateModified": "2022-02-04",
    "description": "В этой статье описано, какие манипуляции можно выполнить с документом с помощью библиотеки Aspose.PDF."
}
</script>

PDF означает Переносимый Формат Документов, используемый для отображения документов в электронном виде независимо от программного обеспечения, оборудования или операционной системы, на которых они просматриваются.

PDF является открытым стандартом, сегодня его поддерживает Международная организация по стандартизации (ISO).

Первоначальная цель заключалась в сохранении и защите содержания и макета документа - независимо от платформы или программы, на которой он просматривается. Именно поэтому PDF-файлы трудно редактировать, а иногда даже извлечение информации из них представляет собой проблему.

Но **Aspose.PDF для .NET** может помочь справиться с большинством задач, возникающих при работе с PDF-документом.

Вы можете выполнять следующие действия:

- [Форматирование PDF-документа](/pdf/net/formatting-pdf-document/) - создание документа, получение и установка свойств документа, встраивание шрифтов и другие операции с PDF-файлами.
- [Манипулирование PDF-документом](/pdf/net/manipulate-pdf-document/) - проверка PDF-документа на соответствие стандарту PDF A, работа с оглавлением, установка срока действия PDF и т.д.
- [Оптимизация PDF](/pdf/net/optimize-pdf/) - оптимизация содержимого страницы, оптимизация размера файла, удаление неиспользуемых объектов, сжатие всех изображений для успешной оптимизации документа.
- [Оптимизация PDF](/pdf/net/optimize-pdf/) - оптимизация содержимого страницы, оптимизация размера файла, удаление неиспользуемых объектов, сжатие всех изображений для успешной оптимизации документа.
- [Слияние PDF](/pdf/net/merge-pdf-documents/) - объединение нескольких PDF-файлов в один PDF-документ с использованием C#.
- [Разделение PDF](/pdf/net/split-document/) - разделение страниц PDF на отдельные PDF-файлы в ваших .NET приложениях.
- [Конкатенация PDF-файлов в папке](/pdf/net/concatenating-all-pdf-files-in-particular-folder/) - конкатенация всех PDF-файлов в определенной папке с использованием класса PdfFileEditor.
- [Конкатенация нескольких PDF-файлов с использованием MemoryStreams](/pdf/net/concatenate-pdf-documents/) - вы научитесь объединять несколько PDF-файлов с использованием MemoryStreams на C#.
- [Работа с заголовками](/pdf/net/working-with-headings/) - вы можете создать нумерацию в заголовках вашего PDF-документа с помощью C#.

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

