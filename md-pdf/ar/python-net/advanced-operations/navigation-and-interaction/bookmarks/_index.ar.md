---
title: العمل مع الإشارات المرجعية في PDF باستخدام Python
linktitle: الإشارات المرجعية
type: docs
weight: 30
url: /python-net/bookmarks/
description: يشرح هذا القسم كيفية إضافة وحذف والحصول على الإشارات المرجعية باستخدام Aspose.PDF لـ Python عبر .NET.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "العمل مع الإشارات المرجعية في PDF باستخدام Python",
    "alternativeHeadline": "كيفية إضافة إشارات مرجعية في PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستندات pdf",
    "keywords": "pdf, python, الإشارات المرجعية في pdf",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق مستندات Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "url": "/python-net/bookmarks/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/bookmarks/"
    },
    "dateModified": "2023-02-04",
    "description": "يشرح هذا القسم كيفية إضافة وحذف والحصول على الإشارات المرجعية باستخدام Aspose.PDF لـ Python عبر .NET."
}
</script>


استخدام العلامات المرجعية في PDF هو ميزة مفيدة جداً. معها، يمكنك إعداد التنقل في مستنداتك، وتنظيم وهيكلة ملفات PDF، وجعل هذه الملفات أكثر سهولة في الوصول. فهي تعمل كروابط تفاعلية في المستند، مما يسمح للمستخدمين بالتنقل بسرعة إلى أقسام أو صفحات محددة.

تعد العلامات المرجعية في PDF أداة مفيدة وأساسية عندما يتعلق الأمر بقراءة ملفات PDF. فهي تتيح للمستخدمين القفز بسرعة إلى أماكن أخرى في مستند PDF، والتنقل عبر الصفحات، ومشاهدة محتويات ملف PDF بسرعة، تماماً كما هو الحال في جدول المحتويات.
في هذا القسم، سوف تتعلم كيفية:

- [إضافة وحذف علامة مرجعية](/pdf/python-net/add-and-delete-bookmark/)
- [الحصول على، تحديث وتوسيع علامة مرجعية](/pdf/python-net/get-update-and-expand-bookmark/)

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "applicationCategory": "PDF Manipulation Library for Python",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>