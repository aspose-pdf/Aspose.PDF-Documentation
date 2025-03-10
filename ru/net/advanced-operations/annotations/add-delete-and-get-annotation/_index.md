---
title: Добавление, удаление и получение аннотаций
linktitle: Добавление, удаление и получение аннотаций
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ru/net/add-delete-and-get-annotation/
description: С помощью Aspose.PDF for .NET вы можете добавлять, удалять и получать аннотации из вашего PDF-файла. Проверьте все списки аннотаций, чтобы решить вашу задачу.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add, Delete and Get Annotation",
    "alternativeHeadline": "Manage PDF Annotations with Aspose.PDF for .NET",
    "abstract": "Улучшите свои возможности манипуляции PDF с новой функцией добавления, удаления и получения аннотаций в Aspose.PDF for .NET. Эта мощная функциональность позволяет пользователям без труда управлять аннотациями в своих PDF-файлах, предлагая упрощенное редактирование и улучшенное взаимодействие с контентом. Узнайте, как работать с различными типами аннотаций, чтобы удовлетворить ваши конкретные потребности в документах.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "add annotation, delete annotation, get annotation, Aspose.PDF for .NET, PDF document generation, PDF annotations, multimedia annotation, PDF text annotation, highlights annotation, PDF manipulation library",
    "wordcount": "174",
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
    "url": "/net/add-delete-and-get-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-delete-and-get-annotation/"
    },
    "dateModified": "2024-11-25",
    "description": "С помощью Aspose.PDF for .NET вы можете добавлять, удалять и получать аннотации из вашего PDF-файла. Проверьте все списки аннотаций, чтобы решить вашу задачу."
}
</script>

**Что такое аннотации в PDF-документах?**

Это дополнительные объекты, которые вы добавляете в свой файл, чтобы расширить содержание текста, внести правки, комментарии для других пользователей. Также возможно сделать текст в документе более читаемым, выделить его, подчеркнуть или добавить совершенно новый текст.

Мы объединили различные виды аннотаций, доступные для библиотеки Aspose.PDF for .NET, в группы:

- [PDF Текстовая аннотация](/pdf/ru/net/text-annotation/)
- [PDF Аннотация выделения](/pdf/ru/net/highlights-annotation/)
- [PDF Аннотация фигур](/pdf/ru/net/figures-annotation/)
- [Мультимедийная аннотация](/pdf/ru/net/multimedia-annotation/)
- [PDF Липкие аннотации](/pdf/ru/net/sticky-annotations/)
- [Аннотации ссылок](/pdf/ru/net/link-annotations/)
- [Дополнительные аннотации](/pdf/ru/net/extra-annotations/)

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