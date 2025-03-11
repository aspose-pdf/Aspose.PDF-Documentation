---
title: .NET에서 아티팩트 작업하기
linktitle: 아티팩트 작업하기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 170
url: /ko/net/artifacts/
description: Aspose.PDF for .NET은 PDF 페이지에 배경 이미지를 추가하고 Artifact 클래스를 사용하여 각 워터마크를 가져올 수 있게 해줍니다.
lastmod: "2024-01-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Artifacts in .NET",
    "alternativeHeadline": "Add and Manage Artifacts in PDF Documents",
    "abstract": "Aspose.PDF for .NET은 Artifact 클래스를 소개하여 개발자가 PDF 문서 내에서 배경 이미지 및 워터마크와 같은 비콘텐츠 요소를 효율적으로 관리할 수 있도록 합니다. 이 기능은 문서 구조를 향상시키고 접근성을 개선하며, 아티팩트는 보조 기술에 의해 무시될 수 있습니다. 유형 및 속성에 대한 사용자 정의 옵션을 통해 사용자는 이러한 요소를 쉽게 조작하여 시각적으로 매력적인 PDF를 생성할 수 있습니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Artifacts, PDF document generation, Aspose.PDF for .NET, BackgroundArtifact, WatermarkArtifact, Artifact class, PDF artifacts, Artifact types, Accessibility in PDF, PDF watermark handling",
    "wordcount": "779",
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
    "url": "/net/artifacts/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/artifacts/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF for .NET은 PDF 페이지에 배경 이미지를 추가하고 Artifact 클래스를 사용하여 각 워터마크를 가져올 수 있게 해줍니다."
}
</script>

PDF의 아티팩트는 문서의 실제 콘텐츠에 포함되지 않는 그래픽 객체 또는 기타 요소입니다. 일반적으로 장식, 레이아웃 또는 배경 용도로 사용됩니다. 아티팩트의 예로는 페이지 헤더, 바닥글, 구분선 또는 의미를 전달하지 않는 이미지가 있습니다.

PDF에서 아티팩트의 목적은 콘텐츠와 비콘텐츠 요소를 구분할 수 있게 하는 것입니다. 이는 접근성에 중요하며, 화면 판독기 및 기타 보조 기술이 아티팩트를 무시하고 관련 콘텐츠에 집중할 수 있게 해줍니다. 아티팩트는 인쇄, 검색 또는 복사에서 생략될 수 있으므로 PDF 문서의 성능과 품질을 향상시킬 수 있습니다.

PDF에서 요소를 아티팩트로 만들려면 [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact) 클래스를 사용해야 합니다.
다음과 같은 유용한 속성을 포함합니다:

- **Artifact.Type** – 아티팩트 유형을 가져옵니다 (Artifact.ArtifactType 열거형의 값, 값에는 Background, Layout, Page, Pagination 및 Undefined가 포함됩니다).
- **Artifact.Subtype** – 아티팩트 하위 유형을 가져옵니다 (Artifact.ArtifactSubtype 열거형의 값, 값에는 Background, Footer, Header, Undefined, Watermark가 포함됩니다).
- **Artifact.Image** – 아티팩트의 이미지를 가져옵니다 (이미지가 존재하면, 그렇지 않으면 null).
- **Artifact.Text** – 아티팩트의 텍스트를 가져옵니다.
- **Artifact.Contents** – 아티팩트 내부 연산자의 컬렉션을 가져옵니다. 지원되는 유형은 System.Collections.ICollection입니다.
- **Artifact.Form** – 아티팩트의 XForm을 가져옵니다 (XForm이 사용되는 경우). 워터마크, 헤더 및 바닥글 아티팩트는 모든 아티팩트 내용을 보여주는 XForm을 포함합니다.
- **Artifact.Rectangle** – 페이지에서 아티팩트의 위치를 가져옵니다.
- **Artifact.Rotation** – 아티팩트의 회전을 가져옵니다 (도 단위, 양수 값은 반시계 방향 회전을 나타냅니다).
- **Artifact.Opacity** – 아티팩트의 불투명도를 가져옵니다. 가능한 값은 0...1 범위에 있으며, 1은 완전히 불투명합니다.

다음 클래스도 아티팩트 작업에 유용할 수 있습니다:

- [ArtifactCollection](https://reference.aspose.com/pdf/net/aspose.pdf/artifactcollection)
- [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact/)
- [HeaderArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/headerartifact/)
- [FooterArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/footerartifact/)
- [WatermarkArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/watermarkartifact/)

## 기존 워터마크 작업하기

Adobe Acrobat으로 생성된 워터마크는 아티팩트라고 합니다 (PDF 사양의 14.8.2.2 실제 콘텐츠 및 아티팩트에서 설명됨).

특정 페이지의 모든 워터마크를 가져오려면 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 클래스의 Artifacts 속성을 사용합니다.

다음 코드 스니펫은 PDF 파일의 첫 페이지에서 모든 워터마크를 가져오는 방법을 보여줍니다.

_참고:_ 이 코드는 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와도 작동합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractWatermarkFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample-w.pdf"))
    {
        // Get the watermarks from the first page artifacts
        var watermarks = document.Pages[1].Artifacts
            .Where(artifact =>
                artifact.Type == Aspose.Pdf.Artifact.ArtifactType.Pagination
                && artifact.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Watermark);

        // Iterate through the found watermark artifacts and print details
        foreach (Aspose.Pdf.WatermarkArtifact item in watermarks.Cast<Aspose.Pdf.WatermarkArtifact>())
        {
            Console.WriteLine($"{item.Text} {item.Rectangle}");
        }
    }
}
```

## 아티팩트로서 배경 작업하기

배경 이미지는 문서에 워터마크 또는 다른 미세한 디자인을 추가하는 데 사용할 수 있습니다. Aspose.PDF for .NET에서는 각 PDF 문서가 페이지의 컬렉션이며 각 페이지는 아티팩트의 컬렉션을 포함합니다. [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact) 클래스를 사용하여 페이지 객체에 배경 이미지를 추가할 수 있습니다.

다음 코드 스니펫은 BackgroundArtifact 객체를 사용하여 PDF 페이지에 배경 이미지를 추가하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBackgroundImageToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
    {
        // Create a new BackgroundArtifact and set the background image
        var background = new Aspose.Pdf.BackgroundArtifact()
        {
            BackgroundImage = File.OpenRead(dataDir + "background.jpg")
        };

        // Add the background image to the first page's artifacts
        document.Pages[1].Artifacts.Add(background);

        // Save PDF document with the added background
        document.Save(dataDir + "SampleArtifactsBackground_out.pdf");
    }
}
```

어떤 이유로든 단색 배경을 사용하고 싶다면, 이전 코드를 다음과 같이 변경하십시오:

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

 private static void AddBackgroundColorToPDF()
 {
    // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Open PDF document
     using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
     {
         // Create a new BackgroundArtifact and set the background color
         var background = new Aspose.Pdf.BackgroundArtifact()
         {
             BackgroundColor = Aspose.Pdf.Color.DarkKhaki
         };

         // Add the background color to the first page's artifacts
         document.Pages[1].Artifacts.Add(background);

         // Save PDF document
         document.Save(dataDir + "SampleArtifactsBackground_out.pdf");
     }
 }
```

## 특정 유형의 아티팩트 수 계산하기

특정 유형의 아티팩트(예: 워터마크의 총 수)를 계산하려면 다음 코드를 사용하십시오:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CountPDFArtifacts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
    {
        // Get pagination artifacts from the first page
        var paginationArtifacts = document.Pages[1].Artifacts
            .Where(artifact => artifact.Type == Aspose.Pdf.Artifact.ArtifactType.Pagination);

        // Count and display the number of each artifact type
        Console.WriteLine("Watermarks: {0}",
            paginationArtifacts.Count(a => a.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Watermark));
        Console.WriteLine("Backgrounds: {0}",
            paginationArtifacts.Count(a => a.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Background));
        Console.WriteLine("Headers: {0}",
            paginationArtifacts.Count(a => a.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Header));
        Console.WriteLine("Footers: {0}",
            paginationArtifacts.Count(a => a.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Footer));
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