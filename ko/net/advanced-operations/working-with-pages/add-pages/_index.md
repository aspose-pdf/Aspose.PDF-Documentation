---
title: PDF 문서에 페이지 추가
linktitle: 페이지 추가
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ko/net/add-pages/
description: Aspose.PDF를 사용하여 .NET에서 기존 PDF에 페이지를 추가하는 방법을 탐색하여 문서를 향상하고 확장합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Pages to PDF Document",
    "alternativeHeadline": "Insert and Manage Pages in PDF Easily with C#",
    "abstract": "Aspose.PDF for .NET의 기능은 사용자가 지정된 위치에 PDF 문서에 페이지를 쉽게 삽입할 수 있도록 하여 문서의 유연성과 조직을 향상시킵니다. 이 기능은 페이지 추가를 지원할 뿐만 아니라 C#을 사용하여 기존 페이지를 이동하거나 제거하는 옵션도 포함됩니다. 이 직관적인 추가 기능으로 PDF 관리를 간소화하세요.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Pages to PDF, insert PDF page, empty page PDF, C# PDF manipulation, PDF document generation, PageCollection, Aspose.PDF for .NET, move PDF pages, remove PDF pages, add pages to PDF",
    "wordcount": "651",
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
    "url": "/net/add-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-pages/"
    },
    "dateModified": "2024-11-26",
    "description": "이 문서에서는 원하는 위치에 PDF 파일에 페이지를 삽입(추가)하는 방법을 설명합니다. C#을 사용하여 PDF 파일에서 페이지를 이동하고 제거(삭제)하는 방법을 배우세요."
}
</script>

Aspose.PDF for .NET API는 C# 또는 기타 .NET 언어를 사용하여 PDF 문서의 페이지를 작업할 수 있는 완전한 유연성을 제공합니다. PDF 문서의 모든 페이지는 [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection)에서 유지되며, 이를 사용하여 PDF 페이지를 작업할 수 있습니다.
Aspose.PDF for .NET은 PDF 문서의 파일 내의 원하는 위치에 페이지를 삽입할 수 있을 뿐만 아니라 PDF 파일의 끝에 페이지를 추가할 수 있습니다.
이 섹션에서는 C#을 사용하여 PDF에 페이지를 추가하는 방법을 보여줍니다.

## PDF 파일에 페이지 추가 또는 삽입

Aspose.PDF for .NET은 PDF 문서의 파일 내의 원하는 위치에 페이지를 삽입할 수 있을 뿐만 아니라 PDF 파일의 끝에 페이지를 추가할 수 있습니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

### 원하는 위치에 PDF 파일에 빈 페이지 삽입

PDF 파일에 빈 페이지를 삽입하려면:

1. 입력 PDF 파일로 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스 객체를 생성합니다.
1. 지정된 인덱스와 함께 [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) 컬렉션의 [Insert](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection/methods/insert) 메서드를 호출합니다.
1. [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) 메서드를 사용하여 출력 PDF를 저장합니다.

다음 코드 스니펫은 PDF 파일에 페이지를 삽입하는 방법을 보여줍니다.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertAnEmptyPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "InsertEmptyPage.pdf"))
    {
       // Insert an empty page in a PDF
       document.Pages.Insert(2);
        // Save PDF document
       document.Save(dataDir + "InsertEmptyPage_out.pdf");
    }
}
```

위의 예에서는 기본 매개변수로 빈 페이지를 추가했습니다. 문서의 다른 페이지와 동일한 페이지 크기를 원한다면 몇 줄의 코드를 추가해야 합니다:

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertAnEmptyPageWithParameters()
{
    var page = document.Pages.Insert(2);
    //copy page parameters from page 1
    page.ArtBox = document.Pages[1].ArtBox;
    page.BleedBox = document.Pages[1].BleedBox;
    page.CropBox = document.Pages[1].CropBox;
    page.MediaBox = document.Pages[1].MediaBox;
    page.TrimBox = document.Pages[1].TrimBox;
}
```

### PDF 파일 끝에 빈 페이지 추가

때때로 문서가 빈 페이지로 끝나도록 보장하고 싶습니다. 이 주제에서는 PDF 문서의 끝에 빈 페이지를 삽입하는 방법을 설명합니다.

PDF 파일 끝에 빈 페이지를 삽입하려면:

1. 입력 PDF 파일로 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스 객체를 생성합니다.
1. 매개변수 없이 [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) 컬렉션의 [Add](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) 메서드를 호출합니다.
1. [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) 메서드를 사용하여 출력 PDF를 저장합니다.

다음 코드 스니펫은 PDF 파일 끝에 빈 페이지를 삽입하는 방법을 보여줍니다.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertAnEmptyPageAtTheEnd()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "InsertEmptyPageAtEnd.pdf"))
    {
        // Insert an empty page at the end of a PDF file
        document.Pages.Add();
        // Save PDF document
        document.Save(dataDir + "InsertEmptyPageAtEnd_out.pdf");
    }
}
```

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