---
title: PDF 파일에 아크 객체 추가
linktitle: 아크 추가
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ko/net/add-arc/
description: 이 문서에서는 Aspose.PDF for .NET을 사용하여 PDF에 아크 객체를 만드는 방법을 설명합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Arc Object to PDF file",
    "alternativeHeadline": "Add Colorful Arc Shapes to  PDF Documents",
    "abstract": "Aspose.PDF for .NET의 새로운 기능은 사용자가 아크 객체를 PDF 문서에 원활하게 통합할 수 있도록 하여 다양한 색상과 치수로 아크를 그릴 수 있는 기능을 제공하여 그래픽 기능을 향상시킵니다. 이 기능은 개발자가 채워진 아크와 속성(예: 테두리 및 채우기 색상)에 대한 정밀한 제어를 통해 보다 시각적으로 매력적이고 맞춤화된 PDF 파일을 만들 수 있도록 합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Arc Object, PDF file, Aspose.PDF for .NET, create Arc, graph objects, filled Arc object",
    "wordcount": "472",
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
    "url": "/net/add-arc/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-arc/"
    },
    "dateModified": "2024-11-25",
    "description": "이 문서에서는 Aspose.PDF for .NET을 사용하여 PDF에 아크 객체를 만드는 방법을 설명합니다."
}
</script>

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

## 아크 객체 추가

Aspose.PDF for .NET은 PDF 문서에 그래프 객체(예: 그래프, 선, 사각형 등)를 추가하는 기능을 지원합니다. 또한 특정 색상으로 아크 객체를 채우는 기능도 제공합니다.

아래 단계를 따르세요:

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 인스턴스를 생성합니다.
1. 특정 치수로 [Drawing object](https://reference.aspose.com/pdf/net/aspose.pdf.drawing)를 생성합니다.
1. Drawing object에 대한 [Border](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border)를 설정합니다.
1. 페이지의 단락 컬렉션에 [Graph](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) 객체를 추가합니다.
1. PDF 파일을 저장합니다.

다음 코드 스니펫은 [Arc](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/arc) 객체를 추가하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Arc()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create Drawing object with certain dimensions
        var graph = new Aspose.Pdf.Drawing.Graph(400, 400);

        // Set border for Drawing object
        var borderInfo = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Green);
        graph.Border = borderInfo;

        // Create arcs and set their properties
        var arc1 = new Aspose.Pdf.Drawing.Arc(100, 100, 95, 0, 90)
        {
            GraphInfo = 
            { 
                Color = Aspose.Pdf.Color.GreenYellow 
            }
        };
        graph.Shapes.Add(arc1);

        var arc2 = new Aspose.Pdf.Drawing.Arc(100, 100, 90, 70, 180)
        {
            GraphInfo = 
            { 
                Color = Aspose.Pdf.Color.DarkBlue 
            }
        };
        graph.Shapes.Add(arc2);

        var arc3 = new Aspose.Pdf.Drawing.Arc(100, 100, 85, 120, 210)
        {
            GraphInfo = 
            { 
                Color = Aspose.Pdf.Color.Red 
            }
        };
        graph.Shapes.Add(arc3);

        // Add Graph object to paragraphs collection of page
        page.Paragraphs.Add(graph);

        // Save PDF document
        document.Save(dataDir + "DrawingArc_out.pdf");
    }
}
```

## 채워진 아크 객체 생성

다음 예제는 색상과 특정 치수로 채워진 아크 객체를 추가하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ArcFilled()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create Drawing object with certain dimensions
        var graph = new Aspose.Pdf.Drawing.Graph(400, 400);

        // Set border for Drawing object
        var borderInfo = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Green);
        graph.Border = borderInfo;

        // Create an arc and set fill color
        var arc = new Aspose.Pdf.Drawing.Arc(100, 100, 95, 0, 90)
        {
            GraphInfo = 
            { 
                FillColor = Aspose.Pdf.Color.GreenYellow 
            }
        };
        graph.Shapes.Add(arc);

        // Create a line and set fill color
        var line = new Aspose.Pdf.Drawing.Line(new float[] { 195, 100, 100, 100, 100, 195 })
        {
            GraphInfo = 
            { 
                FillColor = Aspose.Pdf.Color.GreenYellow 
            }
        };
        graph.Shapes.Add(line);

        // Add Graph object to the paragraphs collection of page
        page.Paragraphs.Add(graph);

        // Save PDF document
        document.Save(dataDir + "ExampleFilledArc_out.pdf");
    }
}
```

채워진 아크 추가 결과를 봅시다:

![채워진 아크](filled_arc.png)

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