---
title: PDF 페이지를 프로그래밍 방식으로 이동 C#
linktitle: PDF 페이지 이동
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ko/net/move-pages/
description: Aspose.PDF for .NET을 사용하여 원하는 위치 또는 PDF 파일의 끝으로 페이지를 이동해 보세요.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Move PDF Pages programmatically C#",
    "alternativeHeadline": "Programmatically Rearrange PDF Pages with .NET",
    "abstract": "Aspose.PDF for .NET은 사용자가 문서 간에 PDF 페이지를 프로그래밍 방식으로 이동하거나 동일한 문서 내에서 재배열할 수 있는 강력한 새로운 기능을 소개합니다. 이 기능은 개발자가 지정된 위치에 페이지를 삽입하고 문서 무결성을 유지하면서 페이지 구성을 쉽게 관리할 수 있도록 하여 PDF 조작 기능을 향상시킵니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "668",
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
    "url": "/net/move-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/move-pages/"
    },
    "dateModified": "2024-11-26",
    "description": "Aspose.PDF for .NET을 사용하여 원하는 위치 또는 PDF 파일의 끝으로 페이지를 이동해 보세요."
}
</script>

## 한 PDF 문서에서 다른 PDF 문서로 페이지 이동

이 주제에서는 C#을 사용하여 한 PDF 문서의 페이지를 다른 문서의 끝으로 이동하는 방법을 설명합니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

페이지를 이동하려면 다음을 수행해야 합니다:

1. 소스 PDF 파일로 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스 객체를 생성합니다.
1. 대상 PDF 파일로 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스 객체를 생성합니다.
1. [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) 컬렉션에서 페이지를 가져옵니다.
1. [Add](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) 메서드를 사용하여 페이지를 대상 문서에 추가합니다.
1. [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) 메서드를 사용하여 출력 PDF를 저장합니다.
1. 소스 문서에서 [Delete](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/1) 메서드를 사용하여 페이지를 삭제합니다.
1. [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) 메서드를 사용하여 소스 PDF를 저장합니다.

다음 코드 스니펫은 한 페이지를 이동하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MovingAPageFromOnePdfDocumentToAnother()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF documents
    using (var srcDocument = new Aspose.Pdf.Document(dataDir + "MovingPageInput.pdf"))
    {
        using (var dstDocument = new Aspose.Pdf.Document())
        {
            var page = srcDocument.Pages[2];
            dstDocument.Pages.Add(page);
            // Save PDF document
            dstDocument.Save(dataDir + "MovingPage_out.pdf");
            srcDocument.Pages.Delete(2);
            // Save PDF document
            srcDocument.Save(dataDir + "MovingPageInput_out.pdf");
        }
    }
}
```

## 여러 페이지를 한 PDF 문서에서 다른 PDF 문서로 이동

1. 소스 PDF 파일로 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스 객체를 생성합니다.
1. 대상 PDF 파일로 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스 객체를 생성합니다.
1. 이동할 페이지 번호로 배열을 정의합니다.
1. 배열을 통해 루프를 실행합니다:
    1. [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) 컬렉션에서 페이지를 가져옵니다.
    1. [Add](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) 메서드를 사용하여 페이지를 대상 문서에 추가합니다.
1. [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) 메서드를 사용하여 출력 PDF를 저장합니다.
1. 배열을 사용하여 소스 문서에서 [Delete](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/2) 메서드를 사용하여 페이지를 삭제합니다.
1. [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) 메서드를 사용하여 소스 PDF를 저장합니다.

다음 코드 스니펫은 여러 페이지를 한 PDF 문서에서 다른 PDF 문서로 이동하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MovingBunchOfPagesFromOnePdfDocumentToAnother()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF documents
    using (var srcDocument = new Aspose.Pdf.Document(dataDir + "MovingBunchOfPagesInput.pdf"))
    {
        using (var dstDocument = new Aspose.Pdf.Document())
        {
            var pages = new[] { 1, 3 };
            foreach (int pageIndex in pages)
            {
                var page = srcDocument.Pages[pageIndex];
                dstDocument.Pages.Add(page);
            }
            // Save PDF document
            dstDocument.Save(dataDir + "MovingBunchOfPages_out.pdf");
            srcDocument.Pages.Delete(pages);
            // Save PDF document
            srcDocument.Save(dataDir + "MovingBunchOfPagesInput_out.pdf";
        }
    }
}
```

## 현재 PDF 문서에서 새로운 위치로 페이지 이동

1. 소스 PDF 파일로 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스 객체를 생성합니다.
1. [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) 컬렉션에서 페이지를 가져옵니다.
1. 새로운 위치(예: 끝)에 [Add](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) 메서드를 사용하여 페이지를 추가합니다.
1. 이전 위치에서 [Delete](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/1) 메서드를 사용하여 페이지를 삭제합니다.
1. [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) 메서드를 사용하여 출력 PDF를 저장합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MovingAPageInNewLocationInTheCurrentPdfDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "MovingAPageInNewLocationInTheCurrentPdfDocumentInput.pdf"))
    {
        var page = document.Pages[2];
        document.Pages.Add(page);
        document.Pages.Delete(2);
        // Save PDF document
        document.Save(dataDir + "MovingAPageInNewLocationInTheCurrentPdfDocument_out.pdf");
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