---
title: PDF를 프로그래밍 방식으로 분할하기
linktitle: PDF 파일 분할
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /ko/net/split-pdf-document/
description: 이 주제에서는 C#을 사용하여 .NET 애플리케이션에서 PDF 페이지를 개별 PDF 파일로 분할하는 방법을 보여줍니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Split PDF programmatically",
    "alternativeHeadline": "Effortlessly split PDF into individual files with C#",
    "abstract": "개발자가 C#을 사용하여 PDF 문서를 개별 파일로 프로그래밍 방식으로 분할할 수 있도록 합니다. 이 기능은 .NET 애플리케이션 내에서 개별 페이지를 별도의 PDF 파일로 추출할 수 있게 하여 PDF 콘텐츠 관리의 효율성을 높이고 문서 처리 능력을 향상시킵니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "326",
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
    "url": "/net/split-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/split-pdf-document/"
    },
    "dateModified": "2024-11-26",
    "description": "이 주제에서는 C#을 사용하여 .NET 애플리케이션에서 PDF 페이지를 개별 PDF 파일로 분할하는 방법을 보여줍니다."
}
</script>

## 라이브 예제

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter)는 프레젠테이션 분할 기능이 어떻게 작동하는지 조사할 수 있는 온라인 무료 웹 애플리케이션입니다.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

이 주제에서는 .NET 애플리케이션에서 PDF 페이지를 개별 PDF 파일로 분할하는 방법을 보여줍니다. C#을 사용하여 PDF 페이지를 단일 페이지 PDF 파일로 분할하려면 다음 단계를 따를 수 있습니다:

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체의 [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) 컬렉션을 통해 PDF 문서의 페이지를 반복합니다.
1. 각 반복마다 새로운 Document 객체를 생성하고 개별 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 객체를 빈 문서에 추가합니다.
1. [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) 메서드를 사용하여 새로운 PDF를 저장합니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

## PDF를 여러 파일 또는 개별 PDF로 분할하기

다음 C# 코드 스니펫은 PDF 페이지를 개별 PDF 파일로 분할하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document1 = new Aspose.Pdf.Document(dataDir + "SplitToPages.pdf"))
    {
        int pageCount = 1;

        // Loop through all the pages
        foreach (var page in document1.Pages)
        {
            // Create PDF document
            using (var document2 = new Aspose.Pdf.Document())
            {
                document2.Pages.Add(page);
                // Save PDF document
                document2.Save(dataDir + "Page_" + pageCount + "_out.pdf");
                pageCount++;
            }
        }
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