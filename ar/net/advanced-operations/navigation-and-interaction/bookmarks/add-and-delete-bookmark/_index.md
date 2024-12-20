---
title: إضافة وحذف إشارة مرجعية
linktitle: إضافة وحذف إشارة مرجعية
type: docs
weight: 10
url: /ar/net/add-and-delete-bookmark/
description: يمكنك إضافة إشارة مرجعية إلى مستند PDF باستخدام C#. من الممكن حذف جميع الإشارات المرجعية أو إشارات مرجعية معينة من مستند PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "إضافة وحذف إشارة مرجعية",
    "alternativeHeadline": "كيفية إضافة وحذف إشارة مرجعية من PDF",
    "author": {
        "@type": "Person",
        "name":"أندري أندروخوفسكي",
        "givenName": "أندري",
        "familyName": "أندروخوفسكي",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "توليد مستند PDF",
    "keywords": "pdf, c#, حذف إشارة مرجعية, إضافة إشارة مرجعية",
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
    "url": "/net/add-and-delete-bookmark/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-and-delete-bookmark/"
    },
    "dateModified": "2022-02-04",
    "description": "يمكنك إضافة إشارة مرجعية إلى مستند PDF باستخدام C#. من الممكن حذف جميع الإشارات المرجعية أو إشارات مرجعية معينة من مستند PDF."
}
</script>
يعمل الجزء التالي من الكود أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

## إضافة إشارة مرجعية إلى مستند PDF

تُحفظ الإشارات المرجعية في مجموعة [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) الخاصة بكائن الوثيقة، وهي ضمن مجموعة [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection).

لإضافة إشارة مرجعية إلى مستند PDF:

1. افتح مستند PDF باستخدام كائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. قم بإنشاء إشارة مرجعية وحدد خصائصها.
1. أضف مجموعة [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) إلى مجموعة العناوين.

يوضح الجزء التالي من الكود كيفية إضافة إشارة مرجعية في مستند PDF.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// فتح المستند
Document pdfDocument = new Document(dataDir + "AddBookmark.pdf");

// إنشاء كائن الإشارة المرجعية
OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.Outlines);
pdfOutline.Title = "Test Outline";
pdfOutline.Italic = true;
pdfOutline.Bold = true;
// تحديد رقم صفحة الوجهة
pdfOutline.Action = new GoToAction(pdfDocument.Pages[1]);
// إضافة الإشارة المرجعية في مجموعة عناوين الوثيقة.
pdfDocument.Outlines.Add(pdfOutline);

dataDir = dataDir + "AddBookmark_out.pdf";
// حفظ الناتج
pdfDocument.Save(dataDir);
```

## إضافة إشارة مرجعية فرعية إلى مستند PDF

يمكن تداخل الإشارات المرجعية، مما يشير إلى علاقة تسلسلية بين الإشارات المرجعية الأبوية والفرعية. يشرح هذا المقال كيفية إضافة إشارة مرجعية فرعية، أي إشارة مرجعية من المستوى الثاني، إلى ملف PDF.

لإضافة إشارة مرجعية فرعية إلى ملف PDF، أولاً أضف إشارة مرجعية أبوية:

1. افتح مستندًا.
1. أضف إشارة مرجعية إلى [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection)، مع تحديد خصائصها.
1. أضف مجموعة OutlineItemCollection إلى مجموعة [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection) الخاصة بكائن المستند.

تُنشأ الإشارة المرجعية الفرعية بنفس طريقة الإشارة المرجعية الأبوية، كما هو موضح أعلاه، لكن يتم إضافتها إلى مجموعة الإشارات المرجعية للإشارة الأبوية

تظهر الأجزاء التالية من الكود كيفية إضافة إشارة مرجعية فرعية إلى مستند PDF.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// فتح المستند
Document pdfDocument = new Document(dataDir + "AddChildBookmark.pdf");

// إنشاء كائن إشارة مرجعية أبوية
OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.Outlines);
pdfOutline.Title = "Parent Outline";
pdfOutline.Italic = true;
pdfOutline.Bold = true;

// إنشاء كائن إشارة مرجعية فرعية
OutlineItemCollection pdfChildOutline = new OutlineItemCollection(pdfDocument.Outlines);
pdfChildOutline.Title = "Child Outline";
pdfChildOutline.Italic = true;
pdfChildOutline.Bold = true;

// إضافة الإشارة المرجعية الفرعية في مجموعة الإشارة الأبوية
pdfOutline.Add(pdfChildOutline);
// إضافة الإشارة المرجعية الأبوية في مجموعة الإشارات المرجعية للمستند.
pdfDocument.Outlines.Add(pdfOutline);

dataDir = dataDir + "AddChildBookmark_out.pdf";
// حفظ الناتج
pdfDocument.Save(dataDir);
```
## حذف جميع العلامات المرجعية من مستند PDF

جميع العلامات المرجعية في ملف PDF موجودة في مجموعة [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection). يشرح هذا المقال كيفية حذف جميع العلامات المرجعية من ملف PDF.

لحذف جميع العلامات المرجعية من ملف PDF:

1. استدعاء طريقة الحذف لمجموعة [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection).
1. حفظ الملف المعدل باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) لكائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

تظهر الأجزاء التالية من الشفرة كيفية حذف جميع العلامات المرجعية من مستند PDF.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// فتح المستند
Document pdfDocument = new Document(dataDir + "DeleteAllBookmarks.pdf");

// حذف جميع العلامات المرجعية
pdfDocument.Outlines.Delete();

dataDir = dataDir + "DeleteAllBookmarks_out.pdf";
// حفظ الملف المحدث
pdfDocument.Save(dataDir);
```
## حذف علامة مرجعية معينة من مستند PDF

لحذف علامة مرجعية معينة من ملف PDF:

1. قم بتمرير عنوان العلامة المرجعية كمعامل إلى طريقة حذف مجموعة [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection).
1. ثم احفظ الملف المُحدث باستخدام طريقة حفظ الكائن Document.

توفر فئة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) مجموعة [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection). تقوم طريقة [Delete](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection/methods/delete) بإزالة أي علامة مرجعية يتم تمرير عنوانها إلى الطريقة.

توضح أجزاء الكود التالية كيفية حذف علامة مرجعية معينة من مستند PDF.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، الرجاء التوجه إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// فتح المستند
Document pdfDocument = new Document(dataDir + "DeleteParticularBookmark.pdf");

// حذف علامة مرجعية معينة بالعنوان
pdfDocument.Outlines.Delete("Child Outline");

// حفظ الملف المُحدث
pdfDocument.Save(dataDir + "DeleteParticularBookmark_out.pdf");
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
```

