---
title: 북마크 만들기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ko/net/create-bookmarks/
description: 이 섹션에서는 PdfBookmarkEditor 클래스를 사용하여 Aspose.PDF Facades로 PDF 파일에 북마크를 만드는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Create Bookmarks",
    "alternativeHeadline": "Effortlessly Manage PDF Bookmarks with PdfBookmarkEditor",
    "abstract": "Aspose.PDF for .NET에서 북마크 기능을 소개합니다. 이 기능은 사용자가 전체 페이지, 특정 페이지 또는 사용자 정의 속성을 가진 페이지 범위에 대한 북마크를 생성할 수 있도록 하여 PDF 탐색을 향상시킵니다. 이 기능은 PDF 문서의 원활한 조직을 가능하게 하여 콘텐츠에 효과적으로 접근하고 관리할 수 있도록 합니다. 간단한 북마크를 추가하든 복잡한 자식 북마크를 추가하든, Aspose.PDF PdfBookmarkEditor 클래스는 PDF 경험을 향상시키기 위한 도구를 제공합니다.",
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
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

## 모든 페이지의 북마크 만들기

모든 페이지의 북마크를 만들기 위해서는 매개변수 없이 [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) 메서드를 사용해야 합니다. [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 클래스는 PDF 파일의 모든 페이지에 대한 북마크를 생성할 수 있도록 합니다. 먼저, [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 클래스의 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 메서드를 사용하여 입력 PDF를 바인딩해야 합니다. 그런 다음 [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) 메서드를 호출하고 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 메서드를 사용하여 출력 PDF 파일을 저장해야 합니다. 다음 코드 스니펫은 북마크를 만드는 방법을 보여줍니다.

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

## 속성이 있는 모든 페이지의 북마크 만들기

[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 클래스는 PDF 파일의 모든 페이지에 대한 북마크를 생성하고 속성(색상, 굵게, 기울임꼴)을 지정할 수 있도록 합니다. 이는 [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) 메서드를 통해 가능합니다. 먼저, [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 클래스의 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 메서드를 사용하여 입력 PDF를 바인딩해야 합니다. 그런 다음 [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) 메서드를 호출하고 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 메서드를 사용하여 출력 PDF 파일을 저장해야 합니다. 다음 코드 스니펫은 속성이 있는 모든 페이지의 북마크를 만드는 방법을 보여줍니다.

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

## 특정 페이지의 북마크 만들기

기존 PDF 파일에서 특정 페이지의 북마크를 만들기 위해서는 [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) 메서드를 사용할 수 있습니다. 이 메서드는 두 개의 인수를 받습니다: 북마크 제목과 페이지 번호. 먼저, [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 클래스의 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 메서드를 사용하여 입력 PDF 파일을 바인딩해야 합니다. 그런 다음 [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) 메서드를 호출하고 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 메서드를 사용하여 출력 PDF 파일을 저장해야 합니다. 다음 코드 스니펫은 특정 페이지의 북마크를 만드는 방법을 보여줍니다.

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

## 페이지 범위의 북마크 만들기

[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 클래스는 페이지 범위의 북마크를 생성할 수 있도록 합니다. [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) 메서드를 두 개의 매개변수와 함께 사용할 수 있습니다: 북마크 목록(북마크 제목 목록)과 페이지 목록(북마크할 페이지 목록). 먼저, [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 클래스의 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 메서드를 사용하여 입력 PDF 파일을 바인딩해야 합니다. 그런 다음 [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) 메서드를 호출하고 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 메서드를 사용하여 출력 PDF를 저장해야 합니다. 다음 코드 스니펫은 페이지 범위의 북마크를 만드는 방법을 보여줍니다.

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

## 기존 PDF 파일에 북마크 추가하기

기존 PDF 파일에 북마크를 추가하기 위해서는 [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 클래스를 사용할 수 있습니다. 북마크를 만들기 위해서는 [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) 객체를 생성하고 북마크의 필수 속성을 설정해야 합니다. 그 후, [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) 객체를 [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 클래스의 [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) 메서드에 전달해야 합니다. 마지막으로, [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 메서드를 사용하여 업데이트된 PDF 파일을 저장해야 합니다. 다음 코드 스니펫은 기존 PDF 파일에 북마크를 추가하는 방법을 보여줍니다.

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

## 기존 PDF 파일에 자식 북마크 추가하기

기존 PDF 파일에 자식 북마크를 추가하기 위해서는 [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 클래스를 사용할 수 있습니다. 자식 북마크를 추가하기 위해서는 [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) 객체를 생성해야 합니다. 개별 [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) 객체를 [Bookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks) 객체에 추가할 수 있습니다. 또한 [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) 객체를 생성하고 그 [ChildItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark/properties/childitem) 속성을 [Bookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks) 객체로 설정해야 합니다. 그런 다음 이 [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) 객체를 [ChildItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark/properties/childitem)과 함께 [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) 메서드에 전달해야 합니다. 마지막으로, [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 클래스의 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 메서드를 사용하여 업데이트된 PDF를 저장해야 합니다. 다음 코드 스니펫은 기존 PDF 파일에 자식 북마크를 추가하는 방법을 보여줍니다.

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