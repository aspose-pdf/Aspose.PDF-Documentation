---
title: إضافة وحذف إشارة مرجعية
linktitle: إضافة وحذف إشارة مرجعية
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
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
    "headline": "Add and Delete a Bookmark",
    "alternativeHeadline": "Manage PDF Bookmarks: Add and Delete with Ease",
    "abstract": "تتيح الميزة الجديدة للمستخدمين إدارة الإشارات المرجعية بكفاءة داخل مستندات PDF باستخدام C#. يمكنك بسهولة إضافة إشارات مرجعية جديدة أو حذف الموجودة، سواء كنت ترغب في إزالة جميع الإشارات المرجعية أو استهداف إدخالات معينة. تعزز هذه الوظيفة التنقل في المستند وتنظيمه لتحسين تجربة المستخدم",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "add bookmark, delete bookmark, PDF document, C# programming, OutlineItemCollection, OutlineCollection, child bookmark, parent bookmark",
    "wordcount": "851",
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
    "url": "/net/add-and-delete-bookmark/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-and-delete-bookmark/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكنك إضافة إشارة مرجعية إلى مستند PDF باستخدام C#. من الممكن حذف جميع الإشارات المرجعية أو إشارات مرجعية معينة من مستند PDF."
}
</script>

تعمل مقتطفات الشيفرة التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/) .

## إضافة إشارة مرجعية إلى مستند PDF

تحتفظ إشارات مرجعية في مجموعة [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) الخاصة بكائن Document، والتي توجد في مجموعة [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection) .

لإضافة إشارة مرجعية إلى PDF:

1. افتح مستند PDF باستخدام كائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) .
1. أنشئ إشارة مرجعية وحدد خصائصها.
1. أضف مجموعة [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) إلى مجموعة Outlines.

تظهر مقتطفات الشيفرة التالية كيفية إضافة إشارة مرجعية في مستند PDF.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBookmark()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddBookmark.pdf"))
    {
        // Create a bookmark object
        var pdfOutline = new Aspose.Pdf.OutlineItemCollection(document.Outlines);
        pdfOutline.Title = "Test Outline";
        pdfOutline.Italic = true;
        pdfOutline.Bold = true;

        // Set the destination page number
        pdfOutline.Action = new Aspose.Pdf.Annotations.GoToAction(document.Pages[1]);

        // Add bookmark in the document's outline collection.
        document.Outlines.Add(pdfOutline);

        // Save PDF document
        document.Save(dataDir + "AddBookmark_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBookmark()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "AddBookmark.pdf");

    // Create a bookmark object
    var pdfOutline = new Aspose.Pdf.OutlineItemCollection(document.Outlines);
    pdfOutline.Title = "Test Outline";
    pdfOutline.Italic = true;
    pdfOutline.Bold = true;

    // Set the destination page number
    pdfOutline.Action = new Aspose.Pdf.Annotations.GoToAction(document.Pages[1]);

    // Add bookmark in the document's outline collection.
    document.Outlines.Add(pdfOutline);

    // Save PDF document
    document.Save(dataDir + "AddBookmark_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## إضافة إشارة مرجعية فرعية إلى مستند PDF

يمكن أن تكون الإشارات المرجعية متداخلة، مما يشير إلى علاقة هرمية مع الإشارات المرجعية الرئيسية والفرعية. يشرح هذا المقال كيفية إضافة إشارة مرجعية فرعية، أي إشارة مرجعية من المستوى الثاني، إلى PDF.

لإضافة إشارة مرجعية فرعية إلى ملف PDF، أضف أولاً إشارة مرجعية رئيسية:

1. افتح مستندًا.
1. أضف إشارة مرجعية إلى [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) ، مع تحديد خصائصها.
1. أضف OutlineItemCollection إلى مجموعة [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection) الخاصة بكائن Document.

تُنشأ الإشارة المرجعية الفرعية تمامًا مثل الإشارة المرجعية الرئيسية، كما هو موضح أعلاه، ولكن يتم إضافتها إلى مجموعة Outlines الخاصة بالإشارة المرجعية الرئيسية.

تظهر مقتطفات الشيفرة التالية كيفية إضافة إشارة مرجعية فرعية إلى مستند PDF.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddChildBookmark()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddChildBookmark.pdf"))
    {
        // Create a parent bookmark object
        var pdfOutline = new Aspose.Pdf.OutlineItemCollection(document.Outlines);
        pdfOutline.Title = "Parent Outline";
        pdfOutline.Italic = true;
        pdfOutline.Bold = true;

        // Create a child bookmark object
        var pdfChildOutline = new Aspose.Pdf.OutlineItemCollection(document.Outlines);
        pdfChildOutline.Title = "Child Outline";
        pdfChildOutline.Italic = true;
        pdfChildOutline.Bold = true;

        // Add child bookmark in parent bookmark's collection
        pdfOutline.Add(pdfChildOutline);

        // Add parent bookmark in the document's outline collection.
        document.Outlines.Add(pdfOutline);

        // Save PDF document
        document.Save(dataDir + "AddChildBookmark_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddChildBookmark()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "AddChildBookmark.pdf");

    // Create a parent bookmark object
    var pdfOutline = new Aspose.Pdf.OutlineItemCollection(document.Outlines);
    pdfOutline.Title = "Parent Outline";
    pdfOutline.Italic = true;
    pdfOutline.Bold = true;

    // Create a child bookmark object
    var pdfChildOutline = new Aspose.Pdf.OutlineItemCollection(document.Outlines);
    pdfChildOutline.Title = "Child Outline";
    pdfChildOutline.Italic = true;
    pdfChildOutline.Bold = true;

    // Add child bookmark in parent bookmark's collection
    pdfOutline.Add(pdfChildOutline);

    // Add parent bookmark in the document's outline collection.
    document.Outlines.Add(pdfOutline);

    // Save PDF document
    document.Save(dataDir + "AddChildBookmark_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## حذف جميع الإشارات المرجعية من مستند PDF

تحتفظ جميع الإشارات المرجعية في PDF في مجموعة [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection) . يشرح هذا المقال كيفية حذف جميع الإشارات المرجعية من ملف PDF.

لحذف جميع الإشارات المرجعية من ملف PDF:

1. استدعِ طريقة Delete الخاصة بمجموعة [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection) .
1. احفظ الملف المعدل باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) الخاصة بكائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) .

تظهر مقتطفات الشيفرة التالية كيفية حذف جميع الإشارات المرجعية من مستند PDF.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteBookmarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DeleteAllBookmarks.pdf"))
    {
        // Delete all bookmarks
        document.Outlines.Delete();

        // Save PDF document
        document.Save(dataDir + "DeleteAllBookmarks_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteBookmarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "DeleteAllBookmarks.pdf");

    // Delete all bookmarks
    document.Outlines.Delete();

    // Save PDF document
    document.Save(dataDir + "DeleteAllBookmarks_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## حذف إشارة مرجعية معينة من مستند PDF

لحذف إشارة مرجعية معينة من ملف PDF:

1. مرر عنوان الإشارة المرجعية كمعامل إلى طريقة Delete الخاصة بمجموعة [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection) .
1. ثم احفظ الملف المحدث باستخدام طريقة Save الخاصة بكائن Document.

توفر فئة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) مجموعة [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection) . تقوم طريقة [Delete](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection/methods/delete) بإزالة أي إشارة مرجعية بعنوان تم تمريره إلى الطريقة.

تظهر مقتطفات الشيفرة التالية كيفية حذف إشارة مرجعية معينة من مستند PDF.

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteBookmark()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DeleteParticularBookmark.pdf"))
    {
        // Delete particular outline by Title
        document.Outlines.Delete("Child Outline");

        // Save PDF document
        document.Save(dataDir + "DeleteParticularBookmark_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteBookmark()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "DeleteParticularBookmark.pdf");

    // Delete particular outline by Title
    document.Outlines.Delete("Child Outline");

    // Save PDF document
    document.Save(dataDir + "DeleteParticularBookmark_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

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