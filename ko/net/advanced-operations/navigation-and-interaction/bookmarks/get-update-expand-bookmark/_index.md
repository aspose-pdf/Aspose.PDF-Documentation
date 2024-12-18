---
title: 북마크 추가 및 삭제
linktitle: 북마크 추가 및 삭제
type: docs
weight: 10
url: /ko/net/add-and-delete-bookmark/
description: PDF 문서에 C#을 사용하여 북마크를 추가할 수 있습니다. PDF 문서에서 모든 북마크 또는 특정 북마크를 삭제할 수 있습니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/add-and-delete-a-bookmark/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "북마크 추가 및 삭제",
    "alternativeHeadline": "PDF에서 북마크 추가 및 삭제 방법",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, c#, 북마크 삭제, 북마크 추가",
    "wordcount": "302",
    "proficiencyLevel":"초급",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF 문서 팀",
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
    "description": "PDF 문서에 C#을 사용하여 북마크를 추가할 수 있습니다. PDF 문서에서 모든 북마크 또는 특정 북마크를 삭제할 수 있습니다."
}
</script>
다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

## PDF 문서에 즐겨찾기 추가하기

즐겨찾기는 [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) 컬렉션의 [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection) 컬렉션에 저장됩니다.

PDF에 즐겨찾기를 추가하려면:

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체를 사용하여 PDF 문서를 엽니다.
1. 즐겨찾기를 생성하고 그 속성을 정의합니다.
1. [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) 컬렉션을 Outlines 컬렉션에 추가합니다.

다음 코드 조각은 PDF 문서에 즐겨찾기를 추가하는 방법을 보여줍니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// 문서 열기
Document pdfDocument = new Document(dataDir + "AddBookmark.pdf");

// 즐겨찾기 객체 생성
OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.Outlines);
pdfOutline.Title = "Test Outline";
pdfOutline.Italic = true;
pdfOutline.Bold = true;
// 목적지 페이지 번호 설정
pdfOutline.Action = new GoToAction(pdfDocument.Pages[1]);
// 문서의 즐겨찾기 컬렉션에 추가
pdfDocument.Outlines.Add(pdfOutline);

dataDir = dataDir + "AddBookmark_out.pdf";
// 출력 저장
pdfDocument.Save(dataDir);
```
## PDF 문서에 자식 즐겨찾기 추가

즐겨찾기는 중첩될 수 있으며, 부모 즐겨찾기와 자식 즐겨찾기 간의 계층적 관계를 나타낼 수 있습니다. 이 문서에서는 PDF에 두 번째 수준의 즐겨찾기인 자식 즐겨찾기를 추가하는 방법을 설명합니다.

PDF 파일에 자식 즐겨찾기를 추가하려면 먼저 부모 즐겨찾기를 추가하세요:

1. 문서를 엽니다.
1. [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection)에 즐겨찾기를 추가하고, 그 속성을 정의합니다.
1. OutlineItemCollection을 문서 객체의 [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection) 컬렉션에 추가합니다.

자식 즐겨찾기는 위에서 설명한 부모 즐겨찾기와 같은 방식으로 생성되지만, 부모 즐겨찾기의 Outlines 컬렉션에 추가됩니다.

다음 코드 스니펫은 PDF 문서에 자식 즐겨찾기를 추가하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// Open document
Document pdfDocument = new Document(dataDir + "AddChildBookmark.pdf");

// Create a parent bookmark object
OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.Outlines);
pdfOutline.Title = "Parent Outline";
pdfOutline.Italic = true;
pdfOutline.Bold = true;

// Create a child bookmark object
OutlineItemCollection pdfChildOutline = new OutlineItemCollection(pdfDocument.Outlines);
pdfChildOutline.Title = "Child Outline";
pdfChildOutline.Italic = true;
pdfChildOutline.Bold = true;

// Add child bookmark in parent bookmark's collection
pdfOutline.Add(pdfChildOutline);
// Add parent bookmark in the document's outline collection.
pdfDocument.Outlines.Add(pdfOutline);

dataDir = dataDir + "AddChildBookmark_out.pdf";
// Save output
pdfDocument.Save(dataDir);
```
## PDF 문서에서 모든 북마크 삭제하기

PDF의 모든 북마크는 [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection) 컬렉션에 저장됩니다. 이 문서는 PDF 파일에서 모든 북마크를 삭제하는 방법을 설명합니다.

PDF 파일에서 모든 북마크를 삭제하려면:

1. [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection) 컬렉션의 Delete 메서드를 호출합니다.
1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체의 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) 메서드를 사용하여 수정된 파일을 저장합니다.

다음 코드 스니펫은 PDF 문서에서 모든 북마크를 삭제하는 방법을 보여줍니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인해 주세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// 문서 열기
Document pdfDocument = new Document(dataDir + "DeleteAllBookmarks.pdf");

// 모든 북마크 삭제
pdfDocument.Outlines.Delete();

dataDir = dataDir + "DeleteAllBookmarks_out.pdf";
// 업데이트된 파일 저장
pdfDocument.Save(dataDir);
```
## PDF 문서에서 특정 북마크 삭제하기

PDF 파일에서 특정 북마크를 삭제하려면:

1. 북마크의 제목을 매개변수로 [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection) 컬렉션의 Delete 메소드에 전달합니다.
1. 그 다음, Document 객체의 Save 메소드로 업데이트된 파일을 저장합니다.

[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스는 [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection) 컬렉션을 제공합니다. [Delete](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection/methods/delete) 메소드는 메소드에 전달된 제목을 가진 북마크를 제거합니다.

다음 코드 스니펫은 PDF 문서에서 특정 북마크를 삭제하는 방법을 보여줍니다.

```csharp
// 전체 예제 및 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인할 수 있습니다.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// 문서 열기
Document pdfDocument = new Document(dataDir + "DeleteParticularBookmark.pdf");

// 제목으로 특정 개요 삭제
pdfDocument.Outlines.Delete("Child Outline");

// 업데이트된 파일 저장
pdfDocument.Save(dataDir + "DeleteParticularBookmark_out.pdf");
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET 라이브러리",
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
                "contactType": "영업",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "영업",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "영업",
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
    "applicationCategory": ".NET용 PDF 조작 라이브러리",
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

