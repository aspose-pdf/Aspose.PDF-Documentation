---
title: Работа с текстом в PDF с помощью C#
linktitle: Работа с текстом
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ru/net/working-with-text/
description: В этом разделе объясняются различные методы работы с текстом. Узнайте, как добавлять, заменять, поворачивать и искать текст с помощью Aspose.PDF и C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Text in PDF using C#",
    "alternativeHeadline": "Enhanced Text Manipulation Features in PDF with C#",
    "abstract": "Откройте для себя мощные возможности работы с текстом в PDF-файлах с помощью Aspose.PDF для .NET. Эта функция позволяет пользователям легко добавлять, заменять, поворачивать и форматировать текст в PDF-документах, улучшая интерактивность и настройку документов. Обогатите свои приложения эффективными функциями поиска и гибкими методами обработки текста, разработанными специально для разработчиков на C#",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF manipulation, add text to PDF, rotate text in PDF, search text in PDF, replace text in PDF, text formatting inside PDF, Aspose.PDF for .NET, text handling techniques, PDF document generation, Floating Box tool",
    "wordcount": "371",
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
    "url": "/net/working-with-text/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-text/"
    },
    "dateModified": "2024-11-26",
    "description": "Этот раздел объясняет различные методы работы с текстом. Узнайте, как добавлять, заменять, поворачивать, искать текст с помощью Aspose.PDF и C#."
}
</script>

Всем нам иногда нужно было добавить текст в файл PDF. Например, когда вы хотите добавить перевод под основным текстом, разместить подпись рядом с изображением или просто заполнить форму заявления. Также полезно, если все текстовые элементы можно отформатировать по своему вкусу. Самые популярные операции с текстом в вашем PDF-файле: добавление текста в PDF, форматирование текста в файле PDF, замена и поворот текста в документе. **Aspose.PDF for .NET** — лучшее решение, в котором есть всё необходимое для работы с содержимым PDF.

Вы можете:

- [Добавить текст в PDF-файл](/pdf/ru/net/add-text-to-pdf-file/) — добавляйте текст в свой PDF-файл, используйте шрифты из потока и файлов, добавляйте HTML-строку, добавляйте гиперссылку и т. д.
- [Всплывающая подсказка PDF](/pdf/ru/net/pdf-tooltip/) — вы можете добавить всплывающую подсказку к искомому тексту, добавив невидимую кнопку с помощью C#.
- [Форматирование текста внутри PDF](/pdf/ru/net/text-formatting-inside-pdf/) — множество функций, которые вы можете добавить в свой документ при форматировании текста внутри него. Добавьте отступ строки, добавьте границу текста, добавьте подчёркивание текста, добавьте перенос строки с помощью библиотеки Aspose.PDF.
- [Использование FloatingBox](/pdf/ru/net/floating-box/) — инструмент Floating Box — это специальный инструмент для размещения текста и другого содержимого на странице PDF.
- [Замена текста в PDF](/pdf/ru/net/replace-text-in-pdf/) — для замены текста на всех страницах PDF-документа. Сначала вам нужно использовать TextFragmentAbsorber.
- [Поворот текста внутри PDF](/pdf/ru/net/rotate-text-inside-pdf/) — поворачивайте текст внутри PDF с помощью свойства поворота класса TextFragment.
- [Поиск и получение текста со страниц PDF-документа](/pdf/ru/net/search-and-get-text-from-pdf/) — вы можете использовать класс TextFragmentAbsorber для поиска и получения текста со страниц.
- [Определение переноса строки](/pdf/ru/net/determine-line-break/) — в этой теме объясняется, как отслеживать перенос строк многострочных текстовых фрагментов.

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