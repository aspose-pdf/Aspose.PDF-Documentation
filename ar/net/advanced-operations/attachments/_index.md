---
title: العمل مع المرفقات في PDF
linktitle: العمل مع المرفقات
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 190
url: /ar/net/attachments/
description: استخدم واجهة برمجة تطبيقات PDF بلغة C# للوصول إلى المرفقات وإضافتها وإزالتها في ملفات PDF باستخدام C# من داخل تطبيقاتك. دليل كامل مع عينات من كود C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/working-with-attachments/
    - /net/working-with-attachments-facades/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Attachments in PDF",
    "alternativeHeadline": "Effortlessly Manage PDF Attachments with C#",
    "abstract": "اكتشف كيفية إدارة المرفقات في ملفات PDF بكفاءة باستخدام واجهة برمجة تطبيقات PDF بلغة C#. تتيح هذه الميزة للمطورين الوصول إلى أنواع ملفات مختلفة مرفقة بـ PDFs، مع عينات مفصلة من كود C# للتكامل السلس في التطبيقات. عزز قدراتك في معالجة PDF من خلال الاستفادة من هذا الدليل الشامل",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "C#, PDF API, attachments in PDF, add attachments, remove attachments, extract attachments, Aspose.PDF for .NET, manipulate PDF documents, save attachment to file, delete attachment from PDF",
    "wordcount": "181",
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
    "url": "/net/attachments/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/attachments/"
    },
    "dateModified": "2024-11-25",
    "description": "استخدم واجهة برمجة تطبيقات PDF بلغة C# للوصول إلى المرفقات وإضافتها وإزالتها في ملفات PDF باستخدام C# من داخل تطبيقاتك. دليل كامل مع عينات من كود C#."
}
</script>

في هذا القسم، سنشرح كيفية العمل مع المرفقات في PDF باستخدام Aspose.PDF for .NET.
المرفق هو ملف إضافي يتم إرفاقه بمستند رئيسي، ويمكن أن يكون مجموعة متنوعة من أنواع الملفات، مثل pdf، word، صورة، أو ملفات أخرى.
ستتعلم كيفية إضافة مرفقات إلى pdf، والحصول على معلومات عن مرفق، وحفظه في ملف، وحذف المرفق من PDF برمجيًا باستخدام C#.

- [إضافة مرفق إلى مستند PDF](/pdf/net/add-attachment-to-pdf-document/)
- [استخراج وحفظ مرفق](/pdf/net/extract-and-save-an-attachment/)
- [إزالة مرفق من PDF موجود](/pdf/net/removing-attachment-from-an-existing-pdf/)
- [محفظة](/pdf/net/portfolio/)

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