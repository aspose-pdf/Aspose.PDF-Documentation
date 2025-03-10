---
title: C#를 사용하여 PDF 병합하는 방법
linktitle: PDF 파일 병합
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ko/net/merge-pdf-documents/
description: 이 페이지에서는 C# 또는 VB.NET을 사용하여 PDF 문서를 단일 PDF 파일로 병합하는 방법을 설명합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "How to Merge PDF using C#",
    "alternativeHeadline": "Combine PDF Effortlessly Using C#",
    "abstract": "Aspose.PDF 라이브러리를 사용하여 여러 PDF 문서를 단일 파일로 손쉽게 병합하는 강력한 기능을 발견하십시오. 이 기능은 개발자가 PDF를 효율적으로 결합하여 작업 흐름을 간소화하고, 과정 전반에 걸쳐 품질과 구조를 유지할 수 있도록 합니다. 소프트웨어 통합에 적합하며, 이 기능은 문서 관리 작업을 단순화하여 생산성을 향상시킵니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "411",
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
    "url": "/net/merge-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/merge-pdf-documents/"
    },
    "dateModified": "2024-11-26",
    "description": "이 페이지에서는 C# 또는 VB.NET을 사용하여 PDF 문서를 단일 PDF 파일로 병합하는 방법을 설명합니다."
}
</script>

## C#에서 여러 PDF를 단일 PDF로 병합 또는 결합하기

C#에서 PDF를 병합하는 것은 3rd 파티 라이브러리를 사용하지 않고는 간단한 작업이 아닙니다.
이 문서에서는 Aspose.PDF for .NET를 사용하여 여러 PDF 파일을 단일 PDF 문서로 병합하는 방법을 보여줍니다. 예제는 C#로 작성되었지만 API는 VB.NET과 같은 다른 .NET 프로그래밍 언어에서도 사용할 수 있습니다. PDF 파일은 첫 번째 파일이 다른 문서의 끝에 추가되도록 병합됩니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

## PDF 파일 병합

두 개의 PDF 파일을 연결하려면:

1. 입력 PDF 파일 중 하나를 포함하는 두 개의 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체를 생성합니다.
1. 그런 다음 다른 PDF 파일을 추가할 Document 객체에 대해 [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) 컬렉션의 Add 메서드를 호출합니다.
1. 두 번째 Document 객체의 PageCollection 컬렉션을 첫 번째 PageCollection 컬렉션의 Add 메서드에 전달합니다.
1. 마지막으로 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) 메서드를 사용하여 출력 PDF 파일을 저장합니다.

다음 코드 스니펫은 PDF 파일을 연결하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MergeDocuments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "Concat1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "Concat2.pdf"))
        {
            // Add pages of second document to the first
            document1.Pages.Add(document2.Pages);

            // Save PDF document
            document1.Save(dataDir + "MergeDocuments_out.pdf");
        }
    }
}
```

## 라이브 예제

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger)는 프레젠테이션 병합 기능이 어떻게 작동하는지 조사할 수 있는 온라인 무료 웹 애플리케이션입니다.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)

## 참조

- [DOM을 사용하여 PDF 분할](https://docs.aspose.com/pdf/net/split-pdf-document/)
- [Facade를 사용하여 PDF 문서 연결](https://docs.aspose.com/pdf/net/concatenate-pdf-documents/)
- [Facade를 사용하여 PDF 분할](https://docs.aspose.com/pdf/net/split-pdf-pages/)

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