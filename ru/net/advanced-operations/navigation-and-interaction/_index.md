---
title: Навигация и взаимодействие в PDF
linktitle: Навигация и взаимодействие
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 140
url: /ru/net/navigation-and-interaction/
description: Этот раздел описывает функции работы со ссылками, действиями и закладками.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Links in PDF programmatically",
    "alternativeHeadline": "Programmatically Add Links to PDF Files in C#",
    "abstract": "Откройте для себя новую возможность программно управлять ссылками в PDF документах с помощью C#. Эта функция позволяет вам без усилий добавлять внутренние ссылки на страницы и внешние гиперссылки на веб-сайты, улучшая навигацию и интерактивность в ваших PDF. Идеально подходит для разработчиков, стремящихся оптимизировать свои процессы управления PDF!",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Working with Links, PDF programmatically, internal page link, external website hyperlink, C# language, PDF document generation, create links in PDF, extract links from PDF, update link destinations, Aspose.PDF for .NET",
    "wordcount": "118",
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
    "url": "/net/navigation-and-interaction/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/navigation-and-interaction/"
    },
    "dateModified": "2024-11-25",
    "description": "Этот раздел описывает функции работы со ссылками, действиями и закладками."
}
</script>

- [Ссылки](/pdf/ru/net/links/) - вы можете легко создавать, обновлять и извлекать ссылки с помощью C#.
- [Действия](/pdf/ru/net/actions/) - возможно добавление и получение, создание гиперссылок на PDF файлы. Также в этой статье вы узнаете, как удалить действие открытия документа из PDF файла и как указать страницу PDF при просмотре документа.
- [Закладки](/pdf/ru/net/bookmarks/) - крупные публикации обычно включают структуру закладок, которую можно легко просматривать и выбирать в панели закладок, позволяя вам щелкнуть по закладке, чтобы перейти на страницу или главу, которую она представляет. Панель закладок является элементом, осознающим содержимое, и видима в боковой панели только если открытый PDF документ содержит структуру закладок.

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