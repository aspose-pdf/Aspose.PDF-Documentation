---
title: 更新、删除和获取书签
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /zh/net/update-delete-and-get-bookmarks/
description: 本节解释如何使用 Aspose.PDF Facades 更新、删除和获取书签。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Update, Delete and Get Bookmarks",
    "alternativeHeadline": "Manage Bookmarks: Update, Delete, and Extract Functions",
    "abstract": "使用 Aspose.PDF Facades 管理 PDF 文件中的书签功能使用户能够轻松更新、删除和检索书签。通过 ModifyBookmarks、DeleteBookmarks 和 ExtractBookmarks 等方法，用户可以有效地操作书签，从而增强 PDF 导航和组织，提高用户体验。此功能通过简单的代码实现简化了书签管理，确保高效处理 PDF 文档。",
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
    "description": "Aspose.PDF 不仅可以执行简单易行的任务，还能应对更复杂的目标。请查看下一节以获取高级用户和开发人员的信息。"
}
</script>

## 更新 PDF 文件中的现有书签

为了更新 PDF 文件中的现有书签，您需要使用 [ModifyBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/modifybookmarks) 方法。该方法接受两个参数：源标题（要修改的书签的标题）、目标标题（要替换的标题）。您需要创建一个 [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 类的对象，并使用 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 方法绑定输入的 PDF 文件。之后，您需要调用 [ModifyBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/modifybookmarks) 方法，然后使用 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 方法保存更新后的 PDF。以下代码片段展示了如何在 PDF 文件中修改现有书签。

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

## 从 PDF 文件中删除所有书签

您可以使用不带任何参数的 [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) 方法删除 PDF 文件中的所有书签。首先，您需要创建一个 [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 类的对象，并使用 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 方法绑定输入的 PDF 文件。之后，您需要调用 [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) 方法，然后使用 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 方法保存更新后的 PDF 文件。以下代码片段展示了如何从 PDF 文件中删除所有书签。

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

## 从 PDF 文件中删除特定书签

为了删除特定书签，您需要使用字符串（标题）参数调用 [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) 方法。这里的 *title* 表示要从 PDF 中删除的书签。创建一个 [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 类的对象，并使用 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 方法绑定输入的 PDF 文件。之后，调用 [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) 方法，然后使用 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 方法保存更新后的 PDF 文件。以下代码片段展示了如何从 PDF 文件中删除特定书签。

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

## 从 PDF 文档 Facades 获取书签

[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 类提供了在现有 PDF 文件中操作书签的功能。它提供了各种属性来获取/设置与书签相关的信息。以下代码片段展示了如何获取与 PDF 文件中每个书签相关的信息。

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

## 从现有 PDF 文件中提取书签

[ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3) 方法允许您从 PDF 文件中提取书签。为了提取书签，您需要创建 [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 对象，并使用 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 方法绑定 PDF 文件。之后，您需要调用 [ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3) 方法。[ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3) 方法返回 [Bookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks/methods/index) 对象。然后，您可以遍历这些书签并获取单个 [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) 对象。最后，您可以使用 [ExportBookmarksToXML](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/exportbookmarkstoxml) 方法将书签导出到 XML 文件。以下代码片段展示了如何将书签导出到 XML 文件。

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