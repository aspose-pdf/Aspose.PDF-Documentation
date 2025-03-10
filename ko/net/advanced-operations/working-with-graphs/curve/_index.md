---
title: PDF 파일에 곡선 객체 추가
linktitle: 곡선 추가
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ko/net/add-curve/
description: 이 문서에서는 Aspose.PDF for .NET를 사용하여 PDF에 곡선 객체를 만드는 방법을 설명합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Curve Object to PDF file",
    "alternativeHeadline": "Create Curves in PDFs",
    "abstract": "Aspose.PDF for .NET의 새로운 기능은 개발자가 PDF 문서 내에서 곡선 객체를 생성하고 조작할 수 있도록 하며, 부드러운 그래픽을 위해 베지어 곡선을 활용합니다. 이 향상된 기능은 간단한 곡선과 채워진 곡선의 디자인을 용이하게 하여, 복잡한 시각적 표현을 생성하는 강력한 도구를 제공하면서 치수와 스타일을 제어할 수 있게 합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Curve, Curve object, Bezier curves, Aspose.PDF for .NET, PDF document generation, Drawing object, Filled Curve, Graph object, PDF manipulation, ASP.NET PDF",
    "wordcount": "500",
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
    "url": "/net/add-curve/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-curve/"
    },
    "dateModified": "2024-11-25",
    "description": "이 문서에서는 Aspose.PDF for .NET를 사용하여 PDF에 곡선 객체를 만드는 방법을 설명합니다."
}
</script>

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

## 곡선 객체 추가

그래프 [Curve](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/curve)는 각각 세 개의 다른 선과 만나는 연결된 투영선의 집합입니다.

Aspose.PDF for .NET는 그래프에서 베지어 곡선을 사용하는 방법을 보여줍니다.
베지어 곡선은 부드러운 곡선을 모델링하기 위해 컴퓨터 그래픽에서 널리 사용됩니다. 곡선은 제어 점의 볼록 껍질에 완전히 포함되며, 이 점들은 그래픽적으로 표시되고 곡선을 직관적으로 조작하는 데 사용될 수 있습니다.
전체 곡선은 네 개의 주어진 점(그들의 볼록 껍질)의 모서리를 가진 사각형에 포함됩니다.

이 문서에서는 PDF 문서에서 생성할 수 있는 간단한 그래프 곡선과 채워진 곡선을 조사할 것입니다.

아래 단계를 따르십시오:

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 인스턴스를 생성합니다.
1. 특정 치수를 가진 [Drawing object](https://reference.aspose.com/pdf/net/aspose.pdf.drawing)를 생성합니다.
1. 드로잉 객체에 대한 [Border](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border)를 설정합니다.
1. 페이지의 단락 컬렉션에 [Graph](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) 객체를 추가합니다.
1. PDF 파일을 저장합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExampleCurve()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create Drawing object with certain dimensions
        var graph = new Aspose.Pdf.Drawing.Graph(400, 200);

        // Set border for Drawing object
        var borderInfo = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Green);
        graph.Border = borderInfo;

        // Create a curve and set its properties
        var curve1 = new Aspose.Pdf.Drawing.Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120 })
        {
            GraphInfo = 
            { 
                Color = Aspose.Pdf.Color.GreenYellow 
            }
        };

        // Add the curve to the graph shapes
        graph.Shapes.Add(curve1);

        // Add Graph object to paragraphs collection of page
        page.Paragraphs.Add(graph);

        // Save PDF document
        document.Save(dataDir + "DrawingCurve1_out.pdf");
    }
}

```

다음 그림은 코드 스니펫을 실행한 결과를 보여줍니다:

![Drawing Curve](drawing_curve.png)

## 채워진 곡선 객체 만들기

이 예제는 색으로 채워진 곡선 객체를 추가하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CurveFilled()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create Drawing object with certain dimensions
        var graph = new Aspose.Pdf.Drawing.Graph(400, 200);

        // Set border for Drawing object
        var borderInfo = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Green);
        graph.Border = borderInfo;

        // Create a curve and set fill color
        var curve1 = new Aspose.Pdf.Drawing.Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120 })
        {
            GraphInfo = 
            { 
                FillColor = Aspose.Pdf.Color.GreenYellow 
            }
        };

        // Add the curve to the graph shapes
        graph.Shapes.Add(curve1);

        // Add Graph object to paragraphs collection of page
        page.Paragraphs.Add(graph);

        // Save PDF document
        document.Save(dataDir + "DrawingCurve2_out.pdf");
    }
}
```

채워진 곡선을 추가한 결과를 살펴보십시오:

![Filled Curve](filled_curve.png)

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