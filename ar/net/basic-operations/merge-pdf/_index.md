---
title: كيفية دمج PDF باستخدام C#
linktitle: دمج ملفات PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ar/net/merge-pdf-documents/
description: تشرح هذه الصفحة كيفية دمج مستندات PDF في ملف PDF واحد باستخدام C# أو VB.NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "How to Merge PDF using C#",
    "alternativeHeadline": "Combine PDF Effortlessly Using C#",
    "abstract": "اكتشف القدرة القوية على دمج مستندات PDF متعددة في ملف واحد بسهولة باستخدام C# مع مكتبة Aspose.PDF. تتيح هذه الميزة للمطورين تبسيط سير العمل الخاص بهم من خلال دمج ملفات PDF بكفاءة، مع الحفاظ على الجودة والبنية طوال العملية. مثالي لتكامل البرمجيات، تعزز هذه الوظيفة الإنتاجية من خلال تبسيط مهام إدارة المستندات.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "411",
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
    "url": "/net/merge-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/merge-pdf-documents/"
    },
    "dateModified": "2024-11-26",
    "description": "تشرح هذه الصفحة كيفية دمج مستندات PDF في ملف PDF واحد باستخدام C# أو VB.NET."
}
</script>

## دمج أو دمج عدة PDF في PDF واحد باستخدام C#

دمج PDF في C# ليس مهمة بسيطة دون استخدام مكتبة طرف ثالث.
توضح هذه المقالة كيفية دمج عدة ملفات PDF في مستند PDF واحد باستخدام Aspose.PDF for .NET. المثال مكتوب بلغة C# ولكن يمكن استخدام واجهة برمجة التطبيقات في لغات برمجة .NET الأخرى مثل VB.NET. يتم دمج ملفات PDF بحيث يتم الانضمام إلى الأول في نهاية المستند الآخر.

تعمل مقتطفات الشيفرة التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

## دمج ملفات PDF

لدمج ملفين PDF:

1. أنشئ كائنين [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) ، يحتوي كل منهما على أحد ملفات PDF المدخلة.
1. ثم استدعِ طريقة Add لمجموعة [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) للكائن Document الذي تريد إضافة ملف PDF الآخر إليه.
1. مرر مجموعة PageCollection للكائن Document الثاني إلى طريقة Add لمجموعة PageCollection الأولى.
1. أخيرًا، احفظ ملف PDF الناتج باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

توضح مقتطفات الشيفرة التالية كيفية دمج ملفات PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MergeDocuments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "Concat1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "Concat2.pdf"))
        {
            // Add pages of second document to the first
            document1.Pages.Add(document2.Pages);

            // Save PDF document
            document1.Save(dataDir + "MergeDocuments_out.pdf");
        }
    }
}
```

## مثال حي

[دمج Aspose.PDF](https://products.aspose.app/pdf/merger) هو تطبيق ويب مجاني عبر الإنترنت يتيح لك استكشاف كيفية عمل وظيفة دمج العروض التقديمية.

[![دمج Aspose.PDF](merger.png)](https://products.aspose.app/pdf/merger)

## انظر أيضًا

- [تقسيم PDF باستخدام DOM](https://docs.aspose.com/pdf/net/split-pdf-document/)
- [دمج مستندات PDF باستخدام Facades](https://docs.aspose.com/pdf/net/concatenate-pdf-documents/)
- [تقسيم PDF باستخدام Facades](https://docs.aspose.com/pdf/net/split-pdf-pages/)

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