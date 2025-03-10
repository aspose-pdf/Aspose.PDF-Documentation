---
title: C#를 사용하여 PDF에 워터마크 추가
linktitle: 워터마크 추가
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 90
url: /ko/net/add-watermarks/
description: 이 문서에서는 C#을 사용하여 프로그래밍 방식으로 PDF에서 아티팩트 작업 및 워터마크 가져오기 기능을 설명합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/working-with-existing-watermarks/
    - /net/adding-multi-line-watermark-to-existing-pdf/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add watermark to PDF using C#",
    "alternativeHeadline": "Add Custom Watermarks to PDF with C#",
    "abstract": "Aspose.PDF for .NET의 새로운 기능은 개발자가 아티팩트 기능을 사용하여 PDF 문서에 프로그래밍 방식으로 사용자 정의 가능한 워터마크를 추가할 수 있도록 합니다. 이 기능은 유형, 불투명도, 회전 및 텍스트 사용자 정의를 포함한 다양한 아티팩트 속성을 지원하여 사용자가 전문적이고 식별 가능한 PDF 파일을 쉽게 생성할 수 있도록 문서 관리를 향상시킵니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "462",
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
    "url": "/net/add-watermarks/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-watermarks/"
    },
    "dateModified": "2024-11-26",
    "description": "이 문서에서는 C#을 사용하여 프로그래밍 방식으로 PDF에서 아티팩트 작업 및 워터마크 가져오기 기능을 설명합니다."
}
</script>

**Aspose.PDF for .NET**은 아티팩트를 사용하여 PDF 문서에 워터마크를 추가할 수 있습니다. 이 문서를 확인하여 작업을 해결하십시오.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

Adobe Acrobat으로 생성된 워터마크는 아티팩트라고 하며( PDF 사양의 14.8.2.2 실제 콘텐츠 및 아티팩트에 설명됨), 아티팩트와 함께 작업하기 위해 Aspose.PDF에는 두 개의 클래스가 있습니다: [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact) 및 [ArtifactCollection](https://reference.aspose.com/pdf/net/aspose.pdf/artifactcollection).

특정 페이지의 모든 아티팩트를 가져오기 위해 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 클래스에는 Artifacts 속성이 있습니다. 이 주제에서는 PDF 파일에서 아티팩트와 함께 작업하는 방법을 설명합니다.

## 아티팩트 작업하기

[Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact) 클래스에는 다음과 같은 속성이 포함되어 있습니다:

- **Artifact.Type**: 아티팩트 유형을 가져옵니다(Artifact.ArtifactType 열거형의 값으로 배경, 레이아웃, 페이지, 페이지 매김 및 정의되지 않음 지원).
- **Artifact.Subtype**: 아티팩트 하위 유형을 가져옵니다(Artifact.ArtifactSubtype 열거형의 값으로 배경, 바닥글, 머리글, 정의되지 않음, 워터마크 지원).

{{% alert color="primary" %}}

Adobe Acrobat으로 생성된 워터마크는 유형이 페이지 매김이고 하위 유형이 워터마크임을 유의하십시오.

{{% /alert %}}

- **Artifact.Contents**: 아티팩트 내부 연산자의 컬렉션을 가져옵니다. 지원되는 유형은 System.Collections.ICollection입니다.
- **Artifact.Form**: 아티팩트의 XForm을 가져옵니다( XForm이 사용되는 경우). 워터마크, 머리글 및 바닥글 아티팩트는 모든 아티팩트 내용을 보여주는 XForm을 포함합니다.
- **Artifact.Image**: 아티팩트의 이미지를 가져옵니다(이미지가 있는 경우, 그렇지 않으면 null).
- **Artifact.Text**: 아티팩트의 텍스트를 가져옵니다.
- **Artifact.Rectangle**: 페이지에서 아티팩트의 위치를 가져옵니다.
- **Artifact.Rotation**: 아티팩트의 회전을 가져옵니다(도 단위, 양수 값은 반시계 방향 회전을 나타냅니다).
- **Artifact.Opacity**: 아티팩트의 불투명도를 가져옵니다. 가능한 값은 0…1 범위에 있으며, 1은 완전히 불투명합니다.

## PDF 파일에 워터마크 추가하는 방법

다음 코드 스니펫은 C#을 사용하여 PDF 파일의 첫 페이지에서 각 워터마크를 가져오는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddWatermarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddWatermarksInput.pdf"))
    {
        // Create a new watermark artifact
        var artifact = new Aspose.Pdf.WatermarkArtifact();
        artifact.SetTextAndState(
            "WATERMARK",
            new Aspose.Pdf.Text.TextState()
            {
                FontSize = 72,
                ForegroundColor = Aspose.Pdf.Color.Blue,
                Font = Aspose.Pdf.Text.FontRepository.FindFont("Courier")
            });
        // Set watermark properties
        artifact.ArtifactHorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        artifact.ArtifactVerticalAlignment = Aspose.Pdf.VerticalAlignment.Center;
        artifact.Rotation = 45;
        artifact.Opacity = 0.5;
        artifact.IsBackground = true;
        // Add watermark artifact to the first page
        document.Pages[1].Artifacts.Add(artifact);
        // Save PDF document
        document.Save(dataDir + "AddWatermarks_out.pdf");
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