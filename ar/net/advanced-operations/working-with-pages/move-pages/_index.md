---
title: نقل صفحات PDF برمجياً C#
linktitle: نقل صفحات PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ar/net/move-pages/
description: حاول نقل الصفحات إلى الموقع المطلوب أو إلى نهاية ملف PDF باستخدام Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Move PDF Pages programmatically C#",
    "alternativeHeadline": "Programmatically Rearrange PDF Pages with .NET",
    "abstract": "Aspose.PDF for .NET يقدم ميزة جديدة قوية تتيح للمستخدمين نقل صفحات PDF برمجياً بين المستندات أو إعادة ترتيبها داخل نفس المستند. تعزز هذه الوظيفة قدرات معالجة PDF من خلال تمكين المطورين من إدراج الصفحات في مواقع محددة وإدارة تنظيم الصفحات بسهولة مع الحفاظ على سلامة المستند.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "668",
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
    "url": "/net/move-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/move-pages/"
    },
    "dateModified": "2024-11-26",
    "description": "حاول نقل الصفحات إلى الموقع المطلوب أو إلى نهاية ملف PDF باستخدام Aspose.PDF for .NET."
}
</script>

## نقل صفحة من مستند PDF إلى آخر

تشرح هذه الموضوع كيفية نقل صفحة من مستند PDF إلى نهاية مستند آخر باستخدام C#.

تعمل مقتطفات الكود التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

لنقل صفحة يجب علينا:

1. إنشاء كائن من فئة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) مع ملف PDF المصدر.
1. إنشاء كائن من فئة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) مع ملف PDF الوجهة.
1. الحصول على الصفحة من مجموعة [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. [إضافة](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) الصفحة إلى المستند الوجهة.
1. حفظ ملف PDF الناتج باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).
1. [حذف](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/1) الصفحة في المستند المصدر.
1. حفظ ملف PDF المصدر باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

تظهر مقتطفات الكود التالية كيفية نقل صفحة واحدة.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MovingAPageFromOnePdfDocumentToAnother()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF documents
    using (var srcDocument = new Aspose.Pdf.Document(dataDir + "MovingPageInput.pdf"))
    {
        using (var dstDocument = new Aspose.Pdf.Document())
        {
            var page = srcDocument.Pages[2];
            dstDocument.Pages.Add(page);
            // Save PDF document
            dstDocument.Save(dataDir + "MovingPage_out.pdf");
            srcDocument.Pages.Delete(2);
            // Save PDF document
            srcDocument.Save(dataDir + "MovingPageInput_out.pdf");
        }
    }
}
```

## نقل مجموعة من الصفحات من مستند PDF إلى آخر

1. إنشاء كائن من فئة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) مع ملف PDF المصدر.
1. إنشاء كائن من فئة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) مع ملف PDF الوجهة.
1. تعريف مصفوفة بأرقام الصفحات التي سيتم نقلها.
1. تشغيل حلقة عبر المصفوفة:
    1. الحصول على الصفحة من مجموعة [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
    1. [إضافة](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) الصفحة إلى المستند الوجهة.
1. حفظ ملف PDF الناتج باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).
1. [حذف](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/2) الصفحة في المستند المصدر باستخدام المصفوفة.
1. حفظ ملف PDF المصدر باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

تظهر مقتطفات الكود التالية كيفية نقل مجموعة من الصفحات من مستند PDF إلى آخر.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MovingBunchOfPagesFromOnePdfDocumentToAnother()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF documents
    using (var srcDocument = new Aspose.Pdf.Document(dataDir + "MovingBunchOfPagesInput.pdf"))
    {
        using (var dstDocument = new Aspose.Pdf.Document())
        {
            var pages = new[] { 1, 3 };
            foreach (int pageIndex in pages)
            {
                var page = srcDocument.Pages[pageIndex];
                dstDocument.Pages.Add(page);
            }
            // Save PDF document
            dstDocument.Save(dataDir + "MovingBunchOfPages_out.pdf");
            srcDocument.Pages.Delete(pages);
            // Save PDF document
            srcDocument.Save(dataDir + "MovingBunchOfPagesInput_out.pdf";
        }
    }
}
```

## نقل صفحة إلى موقع جديد في مستند PDF الحالي

1. إنشاء كائن من فئة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) مع ملف PDF المصدر.
1. الحصول على الصفحة من مجموعة [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. [إضافة](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) الصفحة إلى الموقع الجديد (على سبيل المثال إلى النهاية).
1. [حذف](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/1) الصفحة في الموقع السابق.
1. حفظ ملف PDF الناتج باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MovingAPageInNewLocationInTheCurrentPdfDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "MovingAPageInNewLocationInTheCurrentPdfDocumentInput.pdf"))
    {
        var page = document.Pages[2];
        document.Pages.Add(page);
        document.Pages.Delete(2);
        // Save PDF document
        document.Save(dataDir + "MovingAPageInNewLocationInTheCurrentPdfDocument_out.pdf");
    }
}
```

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