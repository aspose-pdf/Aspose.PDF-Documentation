---
title: نقل صفحات PDF برمجيًا باستخدام C#
linktitle: نقل صفحات PDF
type: docs
weight: 20
url: ar/net/move-pages/
description: حاول نقل الصفحات إلى الموقع المطلوب أو في نهاية ملف PDF باستخدام Aspose.PDF لـ .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "نقل صفحات PDF برمجيًا باستخدام C#",
    "alternativeHeadline": "كيفية نقل صفحات PDF باستخدام .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد وثيقة PDF",
    "keywords": "pdf, c#, نقل صفحة pdf",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق وثائق Aspose.PDF",
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
    "dateModified": "2022-02-04",
    "description": "حاول نقل الصفحات إلى الموقع المطلوب أو في نهاية ملف PDF باستخدام Aspose.PDF لـ .NET."
}
</script>
## نقل صفحة من مستند PDF إلى آخر

هذا الموضوع يشرح كيفية نقل صفحة من مستند PDF إلى نهاية مستند آخر باستخدام C#.

الشفرة التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

لنقل صفحة يجب أن:

1. ننشئ كائن فئة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) بملف PDF المصدر.
1. ننشئ كائن فئة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) بملف PDF الوجهة.
1. نحصل على صفحة من مجموعة [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. [نضيف](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) الصفحة إلى المستند الوجهة.
1. نحفظ ملف PDF الناتج باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).
1. [نحذف](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/1) الصفحة في مستند المصدر.
1.
1.

الشفرة التالية توضح لك كيفية نقل صفحة واحدة.

```csharp
var srcFileName = "<أدخل اسم الملف>";
var dstFileName = "<أدخل اسم الملف>";
var srcDocument = new Document(srcFileName);
var dstDocument = new Document();
var page = srcDocument.Pages[2];
dstDocument.Pages.Add(page);
// حفظ الملف الناتج
dstDocument.Save(srcFileName);
srcDocument.Pages.Delete(2);
srcDocument.Save(dstFileName);
```

## نقل مجموعة صفحات من مستند PDF إلى آخر

1. إنشاء كائن فئة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) بملف PDF المصدر.
1. إنشاء كائن فئة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) بملف PDF الوجهة.
1. تعريف مصفوفة بأرقام الصفحات المراد نقلها.
1. تشغيل حلقة عبر المصفوفة:
    1. الحصول على الصفحة من مجموعة [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. احفظ ملف PDF الناتج باستخدام طريقة [الحفظ](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).
1. [احذف](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/2) صفحة في المستند المصدر باستخدام مصفوفة.
1. احفظ ملف PDF المصدر باستخدام طريقة [الحفظ](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

يوضح الكود التالي كيفية نقل مجموعة من الصفحات من مستند PDF إلى آخر.

```csharp
var srcFileName = "<أدخل اسم الملف>";
var dstFileName = "<أدخل اسم الملف>";
var srcDocument = new Aspose.Pdf.Document(srcFileName);
var dstDocument = new Aspose.Pdf.Document();
var pages = new []{ 1, 3 };
foreach (var pageIndex in pages)
{
    var page = srcDocument.Pages[pageIndex];
    dstDocument.Pages.Add(page);
}                       
// احفظ الملفات الناتجة
dstDocument.Save(dstFileName);
srcDocument.Pages.Delete(pages);
srcDocument.Save(srcFileName);
```

## نقل صفحة في موقع جديد في مستند PDF الحالي

1.
1. الحصول على صفحة من مجموعة [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. [إضافة](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) الصفحة إلى موقع جديد (مثلاً إلى النهاية).
1. [حذف](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/1) الصفحة في الموقع السابق.
1. حفظ ملف PDF الناتج باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

```csharp
var srcFileName = "<enter file name>";
var dstFileName = "<enter file name>";
var srcDocument = new Aspose.Pdf.Document(srcFileName);

var page = srcDocument.Pages[2];
srcDocument.Pages.Add(page);
srcDocument.Pages.Delete(2);          

// Save output file
srcDocument.Save(dstFileName);
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

