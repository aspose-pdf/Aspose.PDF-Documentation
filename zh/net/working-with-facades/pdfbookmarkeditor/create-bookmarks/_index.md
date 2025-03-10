---
title: 创建书签
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /zh/net/create-bookmarks/
description: 本节解释如何使用 Aspose.PDF Facades 的 PdfBookmarEditor 类为 PDF 文件创建书签。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Create Bookmarks",
    "alternativeHeadline": "Effortlessly Manage PDF Bookmarks with PdfBookmarkEditor",
    "abstract": "介绍 Aspose.PDF for .NET 中的书签功能，旨在通过允许用户为整个页面、特定页面或页面范围创建具有可自定义属性的书签来增强 PDF 导航。此功能使 PDF 文档的组织变得无缝，更容易有效地访问和管理内容。无论您需要添加简单书签还是复杂的子书签，Aspose.PDF PdfBookmarkEditor 类都提供了提升您的 PDF 体验的工具。",
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
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一节以获取高级用户和开发人员的信息。"
}
</script>

## 创建所有页面的书签

为了创建所有页面的书签，您需要使用 [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) 方法而不带任何参数。[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 类允许您为 PDF 文件的所有页面创建书签。首先，您需要创建一个 [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 类的对象，并使用 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 方法绑定输入 PDF。然后，您必须调用 [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) 方法，并使用 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 方法保存输出 PDF 文件。以下代码片段向您展示如何创建书签。

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

## 创建具有属性的所有页面的书签

[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 类允许您为 PDF 文件的所有页面创建书签并指定属性（颜色、粗体、斜体）。您可以借助 [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) 方法来实现。首先，您需要创建一个 [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 类的对象，并使用 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 方法绑定输入 PDF。然后，您必须调用 [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) 方法，并使用 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 方法保存输出 PDF 文件。以下代码片段向您展示如何创建具有属性的所有页面的书签。

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

## 创建特定页面的书签

您可以使用 [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) 方法在现有 PDF 文件中创建特定页面的书签。此方法接受两个参数：书签标题和页面编号。首先，您需要创建一个 [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 类的对象，并使用 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 方法绑定输入 PDF 文件。然后，您必须调用 [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) 方法，并使用 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 方法保存输出 PDF 文件。以下代码片段向您展示如何创建特定页面的书签。

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

## 创建页面范围的书签

[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 类允许您创建页面范围的书签。您可以使用 [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) 方法，传入两个参数：书签列表（书签标题的列表）和页面列表（要书签的页面列表）。首先，您需要创建一个 [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 类的对象，并使用 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 方法绑定输入 PDF 文件。然后，您必须调用 [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) 方法，并使用 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 方法保存输出 PDF。以下代码片段向您展示如何创建页面范围的书签。

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

## 在现有 PDF 文件中添加书签

您可以使用 [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 类在现有 PDF 文件中添加书签。为了创建书签，您需要创建 [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) 对象并设置书签的所需属性。之后，您需要将 [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) 对象传递给 [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 类的 [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) 方法。最后，您需要使用 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 方法保存更新后的 PDF 文件。以下代码片段向您展示如何在现有 PDF 文件中添加书签。

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

## 在现有 PDF 文件中添加子书签

您可以使用 [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 类在现有 PDF 文件中添加子书签。为了添加子书签，您需要创建 [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) 对象。您可以将单个 [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) 对象添加到 [Bookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks) 对象中。您还需要创建一个 [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) 对象，并将其 [ChildItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark/properties/childitem) 属性设置为 [Bookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks) 对象。然后，您需要将此 [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) 对象与 [ChildItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark/properties/childitem) 一起传递给 [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) 方法。最后，您需要使用 [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 类的 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 方法保存更新后的 PDF。以下代码片段向您展示如何在现有 PDF 文件中添加子书签。

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