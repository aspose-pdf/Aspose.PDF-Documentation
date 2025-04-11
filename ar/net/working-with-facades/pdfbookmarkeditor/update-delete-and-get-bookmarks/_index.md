---
title: تحديث، حذف والحصول على العلامات المرجعية
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ar/net/update-delete-and-get-bookmarks/
description: يشرح هذا القسم كيفية تحديث، حذف والحصول على العلامات المرجعية باستخدام Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Update, Delete and Get Bookmarks",
    "alternativeHeadline": "Manage Bookmarks: Update, Delete, and Extract Functions",
    "abstract": "تتيح ميزة إدارة العلامات المرجعية داخل ملفات PDF باستخدام Aspose.PDF Facades للمستخدمين تحديث، حذف، واسترجاع العلامات المرجعية بسهولة. مع طرق مثل ModifyBookmarks و DeleteBookmarks و ExtractBookmarks، يمكن للمستخدمين التلاعب بالعلامات المرجعية بفعالية، مما يعزز التنقل والتنظيم في PDF لتحسين تجربة المستخدم. تعمل هذه الوظيفة على تبسيط إدارة العلامات المرجعية من خلال تنفيذ كود بسيط، مما يضمن التعامل الفعال مع مستندات PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "761",
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
    "url": "/net/update-delete-and-get-bookmarks/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/update-delete-and-get-bookmarks/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة ولكن أيضًا التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## تحديث علامة مرجعية موجودة في ملف PDF

لتحديث علامة مرجعية موجودة في ملف PDF، تحتاج إلى استخدام [ModifyBookmarks](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfbookmarkeditor/methods/modifybookmarks) method. تأخذ هذه الطريقة وسيطين: عنوان المصدر (عنوان العلامة المرجعية التي سيتم تعديلها)، عنوان الوجهة (العنوان الذي سيتم استبداله). تحتاج إلى إنشاء كائن من [PdfBookmarkEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfbookmarkeditor) class وربط ملف PDF المدخل باستخدام [BindPdf](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. بعد ذلك، تحتاج إلى استدعاء [ModifyBookmarks](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfbookmarkeditor/methods/modifybookmarks) method، ثم حفظ ملف PDF المحدث باستخدام [Save](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document/methods/save) method. يوضح مقتطف الكود التالي كيفية تعديل علامة مرجعية موجودة في ملف PDF.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void UpdateExistingBookmark()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "UpdateBookmark.pdf");

        // Modify the existing bookmark, assigning a new title
        bookmarkEditor.ModifyBookmarks("New Bookmark", "New Title");

        // Save PDF document
        bookmarkEditor.Save(dataDir + "UpdateBookmark_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void UpdateExistingBookmark()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor();

    // Bind PDF document
    bookmarkEditor.BindPdf(dataDir + "UpdateBookmark.pdf");

    // Modify the existing bookmark, assigning a new title
    bookmarkEditor.ModifyBookmarks("New Bookmark", "New Title");

    // Save PDF document
    bookmarkEditor.Save(dataDir + "UpdateBookmark_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## حذف جميع العلامات المرجعية من ملف PDF

يمكنك حذف جميع العلامات المرجعية من ملف PDF باستخدام [DeleteBookmarks](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) method بدون أي معلمات. أولاً، تحتاج إلى إنشاء كائن من [PdfBookmarkEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfbookmarkeditor) class وربط ملف PDF المدخل باستخدام [BindPdf](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. بعد ذلك، تحتاج إلى استدعاء [DeleteBookmarks](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) method ثم حفظ ملف PDF المحدث باستخدام [Save](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document/methods/save) method. يوضح مقتطف الكود التالي كيفية حذف جميع العلامات المرجعية من ملف PDF.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void DeleteAllBookmarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "DeleteAllBookmarks.pdf");

        // Delete all bookmarks in the document
        bookmarkEditor.DeleteBookmarks();

        // Save PDF document
        bookmarkEditor.Save(dataDir + "DeleteAllBookmarks_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void DeleteAllBookmarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor();

    // Bind PDF document
    bookmarkEditor.BindPdf(dataDir + "DeleteAllBookmarks.pdf");

    // Delete all bookmarks in the document
    bookmarkEditor.DeleteBookmarks();

    // Save PDF document
    bookmarkEditor.Save(dataDir + "DeleteAllBookmarks_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## حذف علامة مرجعية معينة من ملف PDF

لحذف علامة مرجعية معينة، تحتاج إلى استدعاء [DeleteBookmarks](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) method مع وسيط سلسلة (العنوان). *العنوان* هنا يمثل العلامة المرجعية التي سيتم حذفها من PDF. أنشئ كائنًا من [PdfBookmarkEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfbookmarkeditor) class واربط ملف PDF المدخل باستخدام [BindPdf](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. بعد ذلك، استدعِ [DeleteBookmarks](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) method ثم احفظ ملف PDF المحدث باستخدام [Save](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document/methods/save) method. يوضح مقتطف الكود التالي كيفية حذف علامة مرجعية معينة من ملف PDF.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void DeleteParticularBookmark()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "DeleteABookmark.pdf");

        // Delete a bookmark with the title "Page2"
        bookmarkEditor.DeleteBookmarks("Page2");

        // Save PDF document
        bookmarkEditor.Save(dataDir + "DeleteABookmark_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void DeleteParticularBookmark()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor();

   // Bind PDF document
    bookmarkEditor.BindPdf(dataDir + "DeleteABookmark.pdf");

    // Delete a bookmark with the title "Page2"
    bookmarkEditor.DeleteBookmarks("Page2");

    // Save PDF document
    bookmarkEditor.Save(dataDir + "DeleteABookmark_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## الحصول على العلامات المرجعية من واجهات مستند PDF

توفر [PdfBookmarkEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfbookmarkeditor) class ميزة التلاعب بالعلامات المرجعية في ملف PDF الموجود. توفر خصائص مختلفة للحصول على/تعيين المعلومات المتعلقة بالعلامات المرجعية. يوضح مقتطف الكود التالي كيفية الحصول على معلومات تتعلق بكل علامة مرجعية في ملف PDF.

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void GetBookmarksFromDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "GetFromPDF.PDF");

        // Extract all bookmarks from the document
        Aspose.Pdf.Facades.Bookmarks bookmarks = bookmarkEditor.ExtractBookmarks();

        // Iterate through each bookmark and display information
        foreach (Aspose.Pdf.Facades.Bookmark bookmark in bookmarks)
        {
            // Get the title information of bookmark item
            Console.WriteLine("Title: {0}", bookmark.Title);

            // Get the destination page for bookmark
            Console.WriteLine("Page Number: {0}", bookmark.PageNumber);

            // Get the information related to associated action with bookmark
            Console.WriteLine("Bookmark Action: " + bookmark.Action);
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void GetBookmarksFromDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor();

    // Bind PDF document
    bookmarkEditor.BindPdf(dataDir + "GetFromPDF.PDF");

    // Extract all bookmarks from the document
    Aspose.Pdf.Facades.Bookmarks bookmarks = bookmarkEditor.ExtractBookmarks();

    // Iterate through each bookmark and display information
    foreach (Aspose.Pdf.Facades.Bookmark bookmark in bookmarks)
    {
        // Get the title information of bookmark item
        Console.WriteLine("Title: {0}", bookmark.Title);

        // Get the destination page for bookmark
        Console.WriteLine("Page Number: {0}", bookmark.PageNumber);

        // Get the information related to associated action with bookmark
        Console.WriteLine("Bookmark Action: " + bookmark.Action);
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## استخراج العلامات المرجعية من ملف PDF موجود

تسمح لك [ExtractBookmarks](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3) method باستخراج العلامات المرجعية من ملف PDF. لاستخراج العلامات المرجعية، تحتاج إلى إنشاء كائن [PdfBookmarkEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfbookmarkeditor) وربط ملف PDF باستخدام [BindPdf](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. بعد ذلك، تحتاج إلى استدعاء [ExtractBookmarks](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3) method. ترجع [ExtractBookmarks](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3) method كائن [Bookmarks](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/bookmarks/methods/index). يمكنك بعد ذلك التكرار عبر هذه العلامات المرجعية والحصول على كائنات [Bookmark](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/bookmark) الفردية. أخيرًا، يمكنك تصدير العلامات المرجعية إلى ملف XML باستخدام [ExportBookmarksToXML](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfbookmarkeditor/exportbookmarkstoxml) method. يوضح مقتطف الكود التالي كيفية تصدير العلامات المرجعية إلى ملف XML.

{{< tabs tabID="5" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ExtractBookmarksFromPDFFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "ExtractBookmarks.pdf");

        // Extract bookmarks from the document
        Aspose.Pdf.Facades.Bookmarks bookmarks = bookmarkEditor.ExtractBookmarks();

        // Iterate through each extracted bookmark
        foreach (Aspose.Pdf.Facades.Bookmark bookmark in bookmarks)
        {
            // Get the title information of bookmark item
            Console.WriteLine("Title: {0}", bookmark.Title);

            // Get the destination page for bookmark
            Console.WriteLine("Page Number: {0}", bookmark.PageNumber);
        }

        // Export bookmarks to an XML file
        bookmarkEditor.ExportBookmarksToXML(dataDir + "bookmarks.xml");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ExtractBookmarksFromPDFFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor();

    // Bind PDF document
    bookmarkEditor.BindPdf(dataDir + "ExtractBookmarks.pdf");

    // Extract bookmarks from the document
    Aspose.Pdf.Facades.Bookmarks bookmarks = bookmarkEditor.ExtractBookmarks();

    // Iterate through each extracted bookmark
    foreach (Aspose.Pdf.Facades.Bookmark bookmark in bookmarks)
    {
        // Get the title information of bookmark item
        Console.WriteLine("Title: {0}", bookmark.Title);

        // Get the destination page for bookmark
        Console.WriteLine("Page Number: {0}", bookmark.PageNumber);
    }

    // Export bookmarks to an XML file
    bookmarkEditor.ExportBookmarksToXML(dataDir + "bookmarks.xml");
}
```
{{< /tab >}}
{{< /tabs >}}