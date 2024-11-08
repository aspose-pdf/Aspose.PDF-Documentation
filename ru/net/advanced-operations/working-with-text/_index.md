---
title: Работа с текстом в PDF с использованием C#
linktitle: Работа с текстом
type: docs
weight: 30
url: /ru/net/working-with-text/
description: Этот раздел объясняет различные методы работы с текстом. Узнайте, как добавлять, заменять, поворачивать, искать текст с использованием Aspose.PDF и C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Работа с текстом в PDF с использованием C#",
    "alternativeHeadline": "Добавление, поворот, поиск и удаление текста в файле PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, добавление текста, поиск текста, удаление текста, манипулирование текстом в pdf",
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
    "url": "/net/working-with-text/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-text/"
    },
    "dateModified": "2022-02-04",
    "description": "Этот раздел объясняет различные методы работы с текстом. Узнайте, как добавлять, заменять, поворачивать, искать текст с использованием Aspose.PDF и C#."
}
</script>
Иногда нам всем нужно добавить текст в файл PDF. Например, когда вы хотите добавить перевод под основной текст, разместить подпись рядом с изображением или просто заполнить форму заявления. Также полезно, если все текстовые элементы можно форматировать в желаемом стиле. Самые популярные манипуляции с текстом в вашем файле PDF: добавление текста в PDF, форматирование текста внутри файла PDF, замена и поворот текста в вашем документе. **Aspose.PDF для .NET** - лучшее решение, которое имеет все необходимое для работы с содержимым PDF.

 Вы можете делать следующее:

- [Добавить текст в файл PDF](/pdf/ru/net/add-text-to-pdf-file/) - добавьте текст в ваш PDF, используйте шрифты из потока и файлов, добавьте HTML-строку, добавьте гиперссылку и т. д.
- [Всплывающая подсказка PDF](/pdf/ru/net/pdf-tooltip/) - вы можете добавить всплывающую подсказку к искомому тексту, добавив невидимую кнопку с использованием C#.
- [Форматирование текста внутри PDF](/pdf/ru/net/text-formatting-inside-pdf/) - Множество функций, которые вы можете добавить в свой документ при форматировании текста внутри него.
- [Форматирование текста внутри PDF](/pdf/ru/net/text-formatting-inside-pdf/) - Множество функций, которые вы можете добавить в свой документ, форматируя текст внутри него.
- [Замена текста в PDF](/pdf/ru/net/replace-text-in-pdf/) - для замены текста на всех страницах PDF-документа, вам сначала нужно использовать TextFragmentAbsorber.
- [Поворот текста внутри PDF](/pdf/ru/net/rotate-text-inside-pdf/) - поворот текста внутри PDF с использованием свойства поворота класса TextFragment.
- [Поиск и получение текста со страниц PDF-документа](/pdf/ru/net/search-and-get-text-from-pdf/) - вы можете использовать класс TextFragmentAbsorber для поиска и получения текста со страниц.
- [Определение переноса строк](/pdf/ru/net/determine-line-break/) - в этой теме объясняется, как отслеживать перенос строк многострочных текстовых фрагментов.

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

