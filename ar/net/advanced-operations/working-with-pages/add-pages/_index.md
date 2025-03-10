---
title: إضافة صفحات إلى مستند PDF
linktitle: إضافة صفحات
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ar/net/add-pages/
description: استكشف كيفية إضافة صفحات إلى PDF موجود في .NET باستخدام Aspose.PDF لتعزيز وتوسيع مستنداتك.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Pages to PDF Document",
    "alternativeHeadline": "Insert and Manage Pages in PDF Easily with C#",
    "abstract": "تتيح الميزة في Aspose.PDF for .NET للمستخدمين إدراج الصفحات بسهولة في مستند PDF في أي موقع محدد، مما يعزز مرونة المستند وتنظيمه. لا تدعم هذه الوظيفة إضافة الصفحات فحسب، بل تشمل أيضًا خيارات لنقل أو إزالة الصفحات الموجودة باستخدام C#. قم بتبسيط إدارة PDF الخاصة بك مع هذه الإضافة البديهية إلى مجموعة أدوات التطوير الخاصة بك",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Pages to PDF, insert PDF page, empty page PDF, C# PDF manipulation, PDF document generation, PageCollection, Aspose.PDF for .NET, move PDF pages, remove PDF pages, add pages to PDF",
    "wordcount": "651",
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
    "url": "/net/add-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-pages/"
    },
    "dateModified": "2024-11-26",
    "description": "تعلّم في هذه المقالة كيفية إدراج (إضافة) صفحة في الموقع المطلوب من ملف PDF. تعلم كيفية نقل وإزالة (حذف) الصفحات من ملف PDF باستخدام C#."
}
</script>

Aspose.PDF for .NET API يوفر مرونة كاملة للعمل مع الصفحات في مستند PDF باستخدام C# أو أي لغة .NET أخرى. يحتفظ بجميع صفحات مستند PDF في [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) التي يمكن استخدامها للعمل مع صفحات PDF.
تتيح لك Aspose.PDF for .NET إدراج صفحة في مستند PDF في أي موقع في الملف بالإضافة إلى إضافة صفحات إلى نهاية ملف PDF.
توضح هذه القسم كيفية إضافة صفحات إلى PDF باستخدام C#.

## إضافة أو إدراج صفحة في ملف PDF

تتيح لك Aspose.PDF for .NET إدراج صفحة في مستند PDF في أي موقع في الملف بالإضافة إلى إضافة صفحات إلى نهاية ملف PDF.

تعمل مقتطفات الكود التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

### إدراج صفحة فارغة في ملف PDF في الموقع المطلوب

لإدراج صفحة فارغة في ملف PDF:

1. أنشئ كائن من فئة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) باستخدام ملف PDF المدخل.
1. استدعِ طريقة [Insert](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection/methods/insert) لمجموعة [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) مع الفهرس المحدد.
1. احفظ ملف PDF الناتج باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

توضح مقتطفات الكود التالية كيفية إدراج صفحة في ملف PDF.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertAnEmptyPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "InsertEmptyPage.pdf"))
    {
       // Insert an empty page in a PDF
       document.Pages.Insert(2);
        // Save PDF document
       document.Save(dataDir + "InsertEmptyPage_out.pdf");
    }
}
```

في المثال أعلاه، أضفنا صفحة فارغة مع المعلمات الافتراضية. إذا كنت بحاجة إلى جعل حجم الصفحة مماثلاً لصفحة أخرى في المستند، يجب عليك إضافة
بضع سطور من الكود:

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertAnEmptyPageWithParameters()
{
    var page = document.Pages.Insert(2);
    //copy page parameters from page 1
    page.ArtBox = document.Pages[1].ArtBox;
    page.BleedBox = document.Pages[1].BleedBox;
    page.CropBox = document.Pages[1].CropBox;
    page.MediaBox = document.Pages[1].MediaBox;
    page.TrimBox = document.Pages[1].TrimBox;
}
```

### إضافة صفحة فارغة في نهاية ملف PDF

أحيانًا، تريد التأكد من أن المستند ينتهي بصفحة فارغة. تشرح هذه الموضوع كيفية إدراج صفحة فارغة في نهاية مستند PDF.

لإدراج صفحة فارغة في نهاية ملف PDF:

1. أنشئ كائن من فئة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) باستخدام ملف PDF المدخل.
1. استدعِ طريقة [Add](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) لمجموعة [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) بدون أي معلمات.
1. احفظ ملف PDF الناتج باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

توضح مقتطفات الكود التالية كيفية إدراج صفحة فارغة في نهاية ملف PDF.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertAnEmptyPageAtTheEnd()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "InsertEmptyPageAtEnd.pdf"))
    {
        // Insert an empty page at the end of a PDF file
        document.Pages.Add();
        // Save PDF document
        document.Save(dataDir + "InsertEmptyPageAtEnd_out.pdf");
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