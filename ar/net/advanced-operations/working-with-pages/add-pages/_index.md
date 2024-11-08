---
title: إضافة صفحات إلى مستند PDF
linktitle: إضافة صفحات
type: docs
weight: 10
url: /ar/net/add-pages/
description: هذا المقال يعلم كيفية إدراج (إضافة) صفحة في الموقع المطلوب في ملف PDF. تعلم كيفية نقل، إزالة (حذف) الصفحات من ملف PDF باستخدام C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/insert-pdf-pages/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "إضافة صفحات في PDF باستخدام C#",
    "alternativeHeadline": "كيفية إضافة صفحات في مستند PDF",
    "author": {
        "@type": "Person",
        "name":"أناستاسيا هولوب",
        "givenName": "أناستاسيا",
        "familyName": "هولوب",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستند PDF",
    "keywords": "pdf, c#, إضافة صفحة pdf, إدراج صفحة pdf",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق Aspose.PDF Doc",
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
    "dateModified": "2022-02-04",
    "description": "هذا المقال يعلم كيفية إدراج (إضافة) صفحة في الموقع المطلوب في ملف PDF. تعلم كيفية نقل، إزالة (حذف) الصفحات من ملف PDF باستخدام C#."
}
</script>

Aspose.PDF لـ .NET API يوفر مرونة كاملة للعمل مع الصفحات في مستند PDF باستخدام C# أو أي لغة .NET أخرى. يحافظ على جميع صفحات مستند PDF في [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) التي يمكن استخدامها للعمل مع صفحات PDF.
Aspose.PDF لـ .NET يتيح لك إدراج صفحة في مستند PDF في أي مكان في الملف بالإضافة إلى إضافة صفحات إلى نهاية ملف PDF.
هذا القسم يوضح كيفية إضافة صفحات إلى PDF باستخدام C#.

## إضافة أو إدراج صفحة في ملف PDF

Aspose.PDF لـ .NET يتيح لك إدراج صفحة في مستند PDF في أي مكان في الملف بالإضافة إلى إضافة صفحات إلى نهاية ملف PDF.

الشفرة التالية تعمل أيضاً مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

### إدراج صفحة فارغة في ملف PDF في الموقع المطلوب

لإدراج صفحة فارغة في ملف PDF:

1. إنشاء كائن الفئة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) مع ملف PDF المدخل.
1.
1. احفظ ملف PDF الناتج باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

يوضح الجزء التالي من الشفرة كيف يمكنك إدراج صفحة في ملف PDF.

```cs
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// فتح المستند
Document pdfDocument = new Document(dataDir + "InsertEmptyPage.pdf");

// إدراج صفحة فارغة في PDF
pdfDocument.Pages.Insert(2);
// حفظ الملف الناتج
pdfDocument.Save(dataDir + "InsertEmptyPage_out.pdf");
```

في المثال أعلاه، أضفنا صفحة فارغة بالمعايير الافتراضية. إذا كنت بحاجة لجعل حجم الصفحة مماثل لصفحة أخرى في المستند يجب إضافة بعض الأسطر من الشفرة:

```cs
var page = pdfDocument.Pages.Insert(2);
// نسخ معايير الصفحة من الصفحة 1
page.ArtBox = pdfDocument.Pages[1].ArtBox;
page.BleedBox = pdf.Document.Pages[1].BleedBox;
page.CropBox = pdf.Document.Pages[1].CropBox;
page.MediaBox = pdf.Document.Pages[1].MediaBox;
page.TrimBox = pdf.Document.Pages[1].TrimBox;
```
### إضافة صفحة فارغة في نهاية ملف PDF

أحيانًا، قد ترغب في التأكد من أن المستند ينتهي بصفحة فارغة. يشرح هذا الموضوع كيفية إدراج صفحة فارغة في نهاية مستند PDF.

لإدراج صفحة فارغة في نهاية ملف PDF:

1. قم بإنشاء كائن من فئة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) مع ملف PDF المدخل.
1. استدعي طريقة [Add](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) من مجموعة [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection)، بدون أي معاملات.
1. احفظ ملف PDF الناتج باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

يوضح الجزء التالي من الشفرة كيفية إدراج صفحة فارغة في نهاية ملف PDF.

```cs
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// فتح المستند
Document pdfDocument = new Document(dataDir + "InsertEmptyPageAtEnd.pdf");

// إدراج صفحة فارغة في نهاية ملف PDF
pdfDocument.Pages.Add();

// حفظ الملف الناتج
pdfDocument.Save(dataDir + "InsertEmptyPageAtEnd_out.pdf");
```
<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "مكتبة Aspose.PDF لـ .NET",
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
                "contactType": "مبيعات",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "مبيعات",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "مبيعات",
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
    "applicationCategory": "مكتبة التلاعب بملفات PDF لـ .NET",
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

