---
title: ブックマークの作成
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ja/net/create-bookmarks/
description: このセクションでは、PdfBookmarkEditorクラスを使用してAspose.PDFファサードでPDFファイルにブックマークを作成する方法を説明します。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Create Bookmarks",
    "alternativeHeadline": "Effortlessly Manage PDF Bookmarks with PdfBookmarkEditor",
    "abstract": "PDFナビゲーションを向上させるために設計されたAspose.PDF for .NETのブックマーク機能を紹介します。これにより、ユーザーはカスタマイズ可能なプロパティを持つ全ページ、特定のページ、またはページ範囲のブックマークを作成できます。この機能により、PDFドキュメントのシームレスな整理が可能になり、コンテンツに効果的にアクセスし管理することが容易になります。シンプルなブックマークを追加する必要がある場合でも、複雑な子ブックマークを追加する必要がある場合でも、Aspose.PDF PdfBookmarkEditorクラスはPDF体験を向上させるためのツールを提供します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1124",
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
    "url": "/net/create-bookmarks/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-bookmarks/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、シンプルで簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーや開発者向けの情報を確認してください。"
}
</script>

## すべてのページのブックマークを作成

すべてのページのブックマークを作成するには、パラメーターなしで[CreateBookmarks](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2)メソッドを使用する必要があります。[PdfBookmarkEditor](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfbookmarkeditor)クラスを使用すると、PDFファイルのすべてのページのブックマークを作成できます。まず、[PdfBookmarkEditor](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfbookmarkeditor)クラスのオブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades.facade/bindpdf/methods/3)メソッドを使用して入力PDFをバインドする必要があります。その後、[CreateBookmarks](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2)メソッドを呼び出し、[Save](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document/methods/save)メソッドを使用して出力PDFファイルを保存する必要があります。以下のコードスニペットは、ブックマークを作成する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateBookmarksOfAllPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "CreateBookmarksAll.pdf");
        // Create bookmark of all pages
        bookmarkEditor.CreateBookmarks();
        // Save PDF document
        bookmarkEditor.Save(dataDir + "CreateBookmarksOfAllPages_out.pdf");
    }
} 
```

## プロパティ付きのすべてのページのブックマークを作成

[PdfBookmarkEditor](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfbookmarkeditor)クラスを使用すると、PDFファイルのすべてのページのブックマークを作成し、プロパティ（色、太字、イタリック）を指定できます。これは、[CreateBookmarks](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2)メソッドを使用して行うことができます。まず、[PdfBookmarkEditor](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfbookmarkeditor)クラスのオブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades.facade/bindpdf/methods/3)メソッドを使用して入力PDFをバインドする必要があります。その後、[CreateBookmarks](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2)メソッドを呼び出し、[Save](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document/methods/save)メソッドを使用して出力PDFファイルを保存する必要があります。以下のコードスニペットは、プロパティ付きのすべてのページのブックマークを作成する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateBookmarksOfAllPagesWithProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "CreateBookmarks-PagesProperties.pdf");
        // Create bookmark of all pages
        bookmarkEditor.CreateBookmarks(System.Drawing.Color.Green, true, true);
        // Save PDF document
        bookmarkEditor.Save(dataDir + "CreateBookmarks-PagesProperties_out.pdf");
    }
}
```

## 特定のページのブックマークを作成

既存のPDFファイルの特定のページのブックマークを作成するには、[CreateBookmarkOfPage](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1)メソッドを使用します。このメソッドは、ブックマークタイトルとページ番号の2つの引数を取ります。まず、[PdfBookmarkEditor](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfbookmarkeditor)クラスのオブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades.facade/bindpdf/methods/3)メソッドを使用して入力PDFファイルをバインドする必要があります。その後、[CreateBookmarkOfPage](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1)メソッドを呼び出し、[Save](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document/methods/save)メソッドを使用して出力PDFファイルを保存する必要があります。以下のコードスニペットは、特定のページのブックマークを作成する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateBookmarkOfAParticularPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "CreateBookmark-Page.pdf");
        // Create bookmark of a particular page
        bookmarkEditor.CreateBookmarkOfPage("Bookmark Name", 2);
        // Save PDF document
        bookmarkEditor.Save(dataDir + "CreateBookmark-Page_out.pdf");
    }
}
```

## ページ範囲のブックマークを作成

[PdfBookmarkEditor](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfbookmarkeditor)クラスを使用すると、ページ範囲のブックマークを作成できます。[CreateBookmarkOfPage](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1)メソッドを使用して、ブックマークリスト（ブックマークタイトルのリスト）とページリスト（ブックマークするページのリスト）の2つのパラメーターを指定できます。まず、[PdfBookmarkEditor](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfbookmarkeditor)クラスのオブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades.facade/bindpdf/methods/3)メソッドを使用して入力PDFファイルをバインドする必要があります。その後、[CreateBookmarkOfPage](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1)メソッドを呼び出し、[Save](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document/methods/save)メソッドを使用して出力PDFを保存する必要があります。以下のコードスニペットは、ページ範囲のブックマークを作成する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateBookmarksOfARangeOfPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "CreateBookmark-Page.pdf");
        // Bookmark name list
        string[] bookmarkList = { "First" };
        // Page list
        int[] pageList = { 1 };
        // Create bookmark of a range of pages
        bookmarkEditor.CreateBookmarkOfPage(bookmarkList, pageList);
        // Save PDF document
        bookmarkEditor.Save(dataDir + "CreateBookmarkPageRange_out.pdf");
    }
}
```

## 既存のPDFファイルにブックマークを追加

既存のPDFファイルにブックマークを追加するには、[PdfBookmarkEditor](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfbookmarkeditor)クラスを使用します。ブックマークを作成するには、[Bookmark](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/bookmark)オブジェクトを作成し、ブックマークの必要な属性を設定する必要があります。その後、[Bookmark](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/bookmark)オブジェクトを[CreateBookmarks](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2)メソッドに渡す必要があります。最後に、[Save](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document/methods/save)メソッドを使用して更新されたPDFファイルを保存する必要があります。以下のコードスニペットは、既存のPDFファイルにブックマークを追加する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBookmarkInAnExistingPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();
    // Create bookmark
    var bookmark = new Aspose.Pdf.Facades.Bookmark();
    bookmark.PageNumber = 1;
    bookmark.Title = "New Bookmark";
    // Create PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "AddBookmark.pdf");
        // Create bookmarks
        bookmarkEditor.CreateBookmarks(bookmark);
        // Save PDF document
        bookmarkEditor.Save(dataDir + "AddBookmark_out.pdf");
    }
}
```

## 既存のPDFファイルに子ブックマークを追加

既存のPDFファイルに子ブックマークを追加するには、[PdfBookmarkEditor](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfbookmarkeditor)クラスを使用します。子ブックマークを追加するには、[Bookmark](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/bookmark)オブジェクトを作成する必要があります。個々の[Bookmark](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/bookmark)オブジェクトを[Bookmarks](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/bookmarks)オブジェクトに追加できます。また、[Bookmark](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/bookmark)オブジェクトを作成し、その[ChildItem](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/bookmark/properties/childitem)プロパティを[Bookmarks](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/bookmarks)オブジェクトに設定する必要があります。この[Bookmark](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/bookmark)オブジェクトを[ChildItem](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/bookmark/properties/childitem)とともに[CreateBookmarks](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2)メソッドに渡す必要があります。最後に、[PdfBookmarkEditor](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfbookmarkeditor)クラスの[Save](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document/methods/save)メソッドを使用して更新されたPDFを保存する必要があります。以下のコードスニペットは、既存のPDFファイルに子ブックマークを追加する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddChildBookmarkInAnExistingPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();
    // Create bookmarks
    var bookmarks = new Aspose.Pdf.Facades.Bookmarks();
    var childBookmark1 = new Aspose.Pdf.Facades.Bookmark();
    childBookmark1.PageNumber = 1;
    childBookmark1.Title = "First Child";
    var childBookmark2 = new Aspose.Pdf.Facades.Bookmark();
    childBookmark2.PageNumber = 2;
    childBookmark2.Title = "Second Child";
    bookmarks.Add(childBookmark1);
    bookmarks.Add(childBookmark2);
    var bookmark = new Aspose.Pdf.Facades.Bookmark();
    bookmark.Action = "GoTo";
    bookmark.PageNumber = 1;
    bookmark.Title = "Parent";
    bookmark.ChildItems = bookmarks;
    // Create PdfBookmarkEditor class
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "AddChildBookmark.pdf");
        // Create bookmarks
        bookmarkEditor.CreateBookmarks(bookmark);
        // Save PDF document
        bookmarkEditor.Save(dataDir + "AddChildBookmark_out.pdf");
    }
}
```