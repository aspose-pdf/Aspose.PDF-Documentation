---
title: C#로 PDF 페이지 크기 변경
linktitle: PDF 페이지 크기 변경
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ko/net/change-page-size/
description: Aspose.PDF for .NET 라이브러리를 사용하여 PDF 문서의 페이지 크기를 변경합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Change PDF Page Size with C#",
    "alternativeHeadline": "Effortlessly Resize PDF Pages in C#",
    "abstract": "Aspose.PDF for .NET의 새로운 기능을 통해 개발자는 프로그래밍 방식으로 PDF 문서의 페이지 크기를 쉽게 변경할 수 있습니다. 몇 줄의 코드만으로 사용자는 기존 PDF 치수를 수정하여 문서 관리 기능을 향상시키고 다양한 레이아웃 요구 사항과의 호환성을 보장할 수 있습니다. 이 기능은 .NET 애플리케이션 내에서 A4와 같은 선호하는 형식으로 PDF 페이지 크기를 조정하는 프로세스를 간소화합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "300",
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
    "url": "/net/change-page-size/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/change-page-size/"
    },
    "dateModified": "2024-11-26",
    "description": "Aspose.PDF for .NET 라이브러리를 사용하여 PDF 문서의 페이지 크기를 변경합니다."
}
</script>

## C#로 PDF 페이지 크기 변경

Aspose.PDF for .NET을 사용하면 .NET 애플리케이션에서 간단한 코드로 PDF 페이지 크기를 변경할 수 있습니다. 이 주제에서는 기존 PDF 파일의 페이지 치수(크기)를 업데이트/변경하는 방법을 설명합니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 클래스에는 페이지 크기를 설정할 수 있는 SetPageSize(...) 메서드가 포함되어 있습니다. 아래의 코드 스니펫은 몇 가지 간단한 단계로 페이지 치수를 업데이트합니다:

1. 소스 PDF 파일을 로드합니다.
1. [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) 객체에 페이지를 가져옵니다.
1. 주어진 페이지를 가져옵니다.
1. SetPageSize(..) 메서드를 호출하여 치수를 업데이트합니다.
1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스의 Save(..) 메서드를 호출하여 업데이트된 페이지 치수로 PDF 파일을 생성합니다.

{{% alert color="primary" %}}

높이와 너비 속성은 기본 단위로 포인트를 사용하며, 1인치 = 72 포인트, 1cm = 1/2.54 인치 = 0.3937 인치 = 28.3 포인트임을 유의하시기 바랍니다.

{{% /alert %}}

다음 코드 스니펫은 PDF 페이지 치수를 A4 크기로 변경하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangePdfPageSize()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "UpdateDimensions.pdf"))
    {
        // Get page collection
        var pageCollection = document.Pages;
        // Get particular page
        var pdfPage = pageCollection[1];
        // Set the page size as A4 (11.7 x 8.3 in) and in Aspose.Pdf, 1 inch = 72 points
        // So A4 dimensions in points will be (842.4, 597.6)
        pdfPage.SetPageSize(597.6, 842.4);
        // Save PDF document
        document.Save(dataDir + "UpdateDimensions_out.pdf"); 
    }
}
```

## PDF 페이지 크기 가져오기

Aspose.PDF for .NET을 사용하여 기존 PDF 파일의 PDF 페이지 크기를 읽을 수 있습니다. 다음 코드 샘플은 C#을 사용하여 PDF 페이지 치수를 읽는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetPdfPageSize()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "UpdateDimensions.pdf"))
    {
        // Adds a blank page to pdf document
        Page page = document.Pages.Count > 0 ? document.Pages[1] : document.Pages.Add();
        // Get page height and width information
        Console.WriteLine(page.GetPageRect(true).Width.ToString() + ":" + page.GetPageRect(true).Height);
        // Rotate page at 90 degree angle
        page.Rotate = Rotation.on90;
        // Get page height and width information
        Console.WriteLine(page.GetPageRect(true).Width.ToString() + ":" + page.GetPageRect(true).Height);
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