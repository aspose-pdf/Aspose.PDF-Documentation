---
title: العمل مع العلامات المرجعية في PDF باستخدام C#
linktitle: العلامات المرجعية
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ar/net/bookmarks/
description: اكتشف كيفية العمل مع العلامات المرجعية في PDF في .NET باستخدام Aspose.PDF لتسهيل التنقل وتنظيم الوثائق.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/working-with-bookmarks/
    - /net/working-with-bookmarks-facades/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Bookmarks in PDF using C#",
    "alternativeHeadline": "Effortlessly Manage PDF Bookmarks with C#",
    "abstract": "اكتشف القدرات الجديدة لـ Aspose.PDF for .NET، مما يمكّن المستخدمين من إدارة العلامات المرجعية في مستندات PDF بكفاءة. تتيح هذه الميزة إضافة وحذف واسترجاع العلامات المرجعية بسلاسة، مما يعزز التنقل والوصول داخل ملفات PDF",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Bookmarks, PDF, C#, Aspose.PDF, add bookmark, delete bookmark, get bookmark, update bookmark, expand bookmark, PDF manipulation",
    "wordcount": "130",
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
    "url": "/net/bookmarks/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/bookmarks/"
    },
    "dateModified": "2024-11-25",
    "description": "تشرح هذه القسم كيفية إضافة وحذف والحصول على علامة مرجعية مع Aspose.PDF for .NET."
}
</script>

تعتبر العلامات المرجعية في PDF أداة مفيدة وأساسية عند قراءة ملفات PDF. تتيح للمستخدمين القفز بسرعة إلى أماكن أخرى في مستند PDF، والتنقل عبر الصفحات، وعرض محتويات PDF بسرعة، تمامًا مثل جدول المحتويات.
في هذا القسم، ستتعلم كيفية:

- [إضافة وحذف علامة مرجعية](/pdf/net/add-and-delete-bookmark/)
- [الحصول على، تحديث وتوسيع علامة مرجعية](/pdf/net/get-update-and-expand-bookmark/)

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