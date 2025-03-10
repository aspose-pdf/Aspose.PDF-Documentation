---
title: تغيير حجم صفحة PDF باستخدام C#
linktitle: تغيير حجم صفحة PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ar/net/change-page-size/
description: تغيير حجم الصفحة من مستند PDF الخاص بك باستخدام مكتبة Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Change PDF Page Size with C#",
    "alternativeHeadline": "Effortlessly Resize PDF Pages in C#",
    "abstract": "تتيح الوظيفة الجديدة في Aspose.PDF for .NET للمطورين تغيير حجم صفحة مستندات PDF برمجيًا بسهولة. مع بضع سطور من التعليمات البرمجية، يمكن للمستخدمين تعديل أبعاد PDF الحالية، مما يعزز قدراتهم في إدارة المستندات ويضمن التوافق مع متطلبات التخطيط المختلفة. تسهل هذه الميزة عملية تغيير حجم صفحات PDF إلى التنسيقات المفضلة، مثل A4، مباشرة داخل تطبيقات .NET",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "300",
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
    "url": "/net/change-page-size/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/change-page-size/"
    },
    "dateModified": "2024-11-26",
    "description": "تغيير حجم الصفحة من مستند PDF الخاص بك باستخدام مكتبة Aspose.PDF for .NET."
}
</script>

## تغيير حجم صفحة PDF

تتيح لك Aspose.PDF for .NET تغيير حجم صفحة PDF باستخدام سطور بسيطة من التعليمات البرمجية في تطبيقات .NET الخاصة بك. يشرح هذا الموضوع كيفية تحديث/تغيير أبعاد الصفحة (الحجم) لملف PDF موجود.

تعمل مقتطفات التعليمات البرمجية التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

تحتوي فئة [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) على طريقة SetPageSize(...) التي تتيح لك تعيين حجم الصفحة. يقوم مقتطف التعليمات البرمجية أدناه بتحديث أبعاد الصفحة في بضع خطوات سهلة:

1. تحميل ملف PDF المصدر.
1. الحصول على الصفحات في كائن [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. الحصول على صفحة معينة.
1. استدعاء طريقة SetPageSize(..) لتحديث أبعادها.
1. استدعاء طريقة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) لحفظ(..) لتوليد ملف PDF بأبعاد صفحة محدثة.

{{% alert color="primary" %}}

يرجى ملاحظة أن خصائص الارتفاع والعرض تستخدم النقاط كوحدة أساسية، حيث 1 بوصة = 72 نقطة و 1 سم = 1/2.54 بوصة = 0.3937 بوصة = 28.3 نقطة.

{{% /alert %}}

تظهر مقتطفات التعليمات البرمجية التالية كيفية تغيير أبعاد صفحة PDF إلى حجم A4.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangePdfPageSize()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "UpdateDimensions.pdf"))
    {
        // Get page collection
        var pageCollection = document.Pages;
        // Get particular page
        var pdfPage = pageCollection[1];
        // Set the page size as A4 (11.7 x 8.3 in) and in Aspose.Pdf, 1 inch = 72 points
        // So A4 dimensions in points will be (842.4, 597.6)
        pdfPage.SetPageSize(597.6, 842.4);
        // Save PDF document
        document.Save(dataDir + "UpdateDimensions_out.pdf"); 
    }
}
```

## الحصول على حجم صفحة PDF

يمكنك قراءة حجم صفحة PDF لملف PDF موجود باستخدام Aspose.PDF for .NET. يوضح نموذج التعليمات البرمجية التالي كيفية قراءة أبعاد صفحة PDF باستخدام C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetPdfPageSize()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "UpdateDimensions.pdf"))
    {
        // Adds a blank page to pdf document
        Page page = document.Pages.Count > 0 ? document.Pages[1] : document.Pages.Add();
        // Get page height and width information
        Console.WriteLine(page.GetPageRect(true).Width.ToString() + ":" + page.GetPageRect(true).Height);
        // Rotate page at 90 degree angle
        page.Rotate = Rotation.on90;
        // Get page height and width information
        Console.WriteLine(page.GetPageRect(true).Width.ToString() + ":" + page.GetPageRect(true).Height);
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