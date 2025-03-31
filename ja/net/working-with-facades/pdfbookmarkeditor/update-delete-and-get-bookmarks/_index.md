---
title: ブックマークの更新、削除、取得
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ja/net/update-delete-and-get-bookmarks/
description: このセクションでは、Aspose.PDF Facadesを使用してブックマークを更新、削除、取得する方法について説明します。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Update, Delete and Get Bookmarks",
    "alternativeHeadline": "Manage Bookmarks: Update, Delete, and Extract Functions",
    "abstract": "Aspose.PDF Facadesを使用してPDFファイル内のブックマークを管理する機能により、ユーザーはブックマークを簡単に更新、削除、取得できます。ModifyBookmarks、DeleteBookmarks、ExtractBookmarksなどのメソッドを使用することで、ユーザーはブックマークを効果的に操作し、PDFのナビゲーションと整理を向上させ、より良いユーザー体験を提供します。この機能は、簡単なコード実装を通じてブックマーク管理を効率化し、PDFドキュメントの効率的な取り扱いを保証します。",
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
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## PDFファイル内の既存のブックマークを更新する

PDFファイル内の既存のブックマークを更新するには、[ModifyBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/modifybookmarks)メソッドを使用する必要があります。このメソッドは、2つの引数を取ります: ソースタイトル（変更するブックマークのタイトル）、宛先タイトル（置き換えるタイトル）。[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor)クラスのオブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3)メソッドを使用して入力PDFファイルをバインドする必要があります。その後、[ModifyBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/modifybookmarks)メソッドを呼び出し、[Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save)メソッドを使用して更新されたPDFを保存します。以下のコードスニペットは、PDFファイル内の既存のブックマークを変更する方法を示しています。

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

## PDFファイルからすべてのブックマークを削除する

[DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks)メソッドを使用して、パラメータなしでPDFファイルからすべてのブックマークを削除できます。まず、[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor)クラスのオブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3)メソッドを使用して入力PDFファイルをバインドする必要があります。その後、[DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks)メソッドを呼び出し、[Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save)メソッドを使用して更新されたPDFファイルを保存します。以下のコードスニペットは、PDFファイルからすべてのブックマークを削除する方法を示しています。

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

## PDFファイルから特定のブックマークを削除する

特定のブックマークを削除するには、文字列（タイトル）パラメータを持つ[DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks)メソッドを呼び出す必要があります。ここでの*タイトル*は、PDFから削除されるブックマークを表します。[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor)クラスのオブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3)メソッドを使用して入力PDFファイルをバインドします。その後、[DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks)メソッドを呼び出し、[Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save)メソッドを使用して更新されたPDFファイルを保存します。以下のコードスニペットは、PDFファイルから特定のブックマークを削除する方法を示しています。

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

## PDFドキュメントファサードからブックマークを取得する

[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor)クラスは、既存のPDFファイル内のブックマークを操作する機能を提供します。ブックマークに関する情報を取得/設定するためのさまざまなプロパティを提供します。以下のコードスニペットは、PDFファイル内の各ブックマークに関連する情報を取得する方法を示しています。

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

## 既存のPDFファイルからブックマークを抽出する

[ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3)メソッドを使用すると、PDFファイルからブックマークを抽出できます。ブックマークを抽出するには、[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor)オブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3)メソッドを使用してPDFファイルをバインドする必要があります。その後、[ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3)メソッドを呼び出す必要があります。[ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3)メソッドは[Bookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks/methods/index)オブジェクトを返します。これらのブックマークをループして、個々の[Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark)オブジェクトを取得できます。最後に、[ExportBookmarksToXML](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/exportbookmarkstoxml)メソッドを使用して、ブックマークをXMLファイルにエクスポートできます。以下のコードスニペットは、ブックマークをXMLファイルにエクスポートする方法を示しています。

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