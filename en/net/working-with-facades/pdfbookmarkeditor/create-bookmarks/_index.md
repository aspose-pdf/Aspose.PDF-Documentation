---
title: Create Bookmarks
type: docs
weight: 10
url: /net/create-bookmarks/
description: This section explains how to create bookmarks to your PDF file with Aspose.PDF Facades using PdfBookmarEditor Class.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Create Bookmarks",
    "alternativeHeadline": "Effortlessly Manage PDF Bookmarks with PdfBookmarkEditor",
    "abstract": "Introducing the bookmarking functionality in Aspose.PDF for .NET, designed to enhance PDF navigation by allowing users to create bookmarks for entire pages, specific pages, or ranges of pages with customizable properties. This feature enables seamless organization of PDF documents, making it easier to access and manage content effectively. Whether you need to add simple bookmarks or intricate child bookmarks, Aspose.PDF PdfBookmarkEditor class provides the tools to elevate your PDF experience",
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
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Create Bookmarks of All Pages

In order to create bookmarks of all the pages, you need to use [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) method without any parameters . [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) class allows you to create bookmarks of all the pages of a PDF file. First, you need to create an object of [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) class and bind the input PDF using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. Then, you have to call [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) method and save the output PDF file using [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method. The following code snippet shows you how to create Bookmarks.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateBookmarksOfAllPages()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

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

## Create Bookmarks of All Pages with Properties

[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) class allows you to create bookmarks of all the pages of a PDF file and specify the properties (Color, Bold, Italic). You can do that with the help of [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) method. First, you need to create an object of [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) class and bind the input PDF using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. Then, you have to call [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) method and save the output PDF file using [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method. The following code snippet shows you how to create bookmarks of all the pages with properties.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateBookmarksOfAllPagesWithProperties()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

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

## Create Bookmark of a Particular Page

You can create a bookmark of a particular page in an existing PDF file using [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) method. This method takes two arguments: bookmark title and page number. First, you need to create an object of [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) class and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. Then, you have to call the [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) method and save the output PDF file using [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method. The following code snippet shows you how to create bookmark of a particular page.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateBookmarkOfAParticularPage()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

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

## Create Bookmarks of a Range of Pages

[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) class allows you to create bookmarks of a range of pages. You can use [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) method with two parameters: bookmark list (the list of the bookmark titles) and page list (the list of the pages to bookmark). First, you need to create an object of [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) class and bind the input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. Then, you have to call [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) method and save the output PDF using [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method. The following code snippet shows you how to create bookmarks of a range of pages.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateBookmarksOfARangeOfPages()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

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

## Add Bookmark in an Existing PDF File

You can add bookmark in an existing PDF file using [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) class. In order to create the bookmark, you need to create [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) object and set the required attributes of the bookmark. After that, you need to pass the [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) object to the [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) method of [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) class. Finally, you need to save the updated PDF file using [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method. The following code snippet shows you how to add the bookmark in an existing PDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBookmarkInAnExistingPdfFile()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();
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

## Add Child Bookmark in an Existing PDF File

You can add child bookmarks in an existing PDF file using [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) class. In order to add child bookmarks, you need to create [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) objects. You can add individual [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) objects into [Bookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks) object. You also need to create a [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) object and set its [ChildItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark/properties/childitem) property to [Bookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks) object. You then need to pass this [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) object with [ChildItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark/properties/childitem) to the [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) method. Finally, you need to save the updated PDF using [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method of the [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) class. The following code snippet shows you how to add child bookmarks in an existing PDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddChildBookmarkInAnExistingPdfFile()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();
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

## See also

Try to compare and find a way to work with bookmarks that suits you. Lets learn [Working with Bookmarks in PDF](/pdf/net/bookmarks/) section.