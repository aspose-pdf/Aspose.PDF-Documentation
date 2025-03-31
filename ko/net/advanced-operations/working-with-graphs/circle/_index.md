---
title: PDF 파일에 원 객체 추가
linktitle: 원 추가
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ko/net/add-circle/
description: 이 문서에서는 Aspose.PDF for .NET을 사용하여 PDF에 원 객체를 만드는 방법을 설명합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Circle Object to PDF file",
    "alternativeHeadline": "Add Interactive Circle Objects in PDFs with Ease",
    "abstract": "Aspose.PDF for .NET의 새로운 기능을 통해 사용자는 PDF 파일 내에서 원 객체를 손쉽게 생성할 수 있습니다. 이 기능은 일반 및 채워진 원 그래픽을 추가할 수 있게 하여 데이터 시각화를 향상시키며, 개발자에게 문서에서 정보를 그래픽적으로 표현하는 직관적인 방법을 제공합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Circle Object, Circle in PDF, Aspose.PDF for .NET, PDF document generation, Create filled Circle, Graph object, PDF file manipulation, C# PDF library",
    "wordcount": "441",
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
    "url": "/net/add-circle/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-circle/"
    },
    "dateModified": "2024-11-25",
    "description": "이 문서에서는 Aspose.PDF for .NET을 사용하여 PDF에 원 객체를 만드는 방법을 설명합니다."
}
</script>

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

## 원 객체 추가

막대 그래프와 마찬가지로 원 그래프는 여러 개의 개별 카테고리에서 데이터를 표시하는 데 사용할 수 있습니다. 그러나 막대 그래프와 달리 원 그래프는 전체를 구성하는 모든 카테고리에 대한 데이터가 있을 때만 사용할 수 있습니다. 그러므로 Aspose.PDF for .NET을 사용하여 [원](https://reference.aspose.com/pdf/ko/net/aspose.pdf.drawing/circle) 객체를 추가하는 방법을 살펴보겠습니다.

아래 단계를 따르세요:

1. [Document](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document) 인스턴스를 생성합니다.
1. 특정 크기로 [Drawing object](https://reference.aspose.com/pdf/ko/net/aspose.pdf.drawing)를 생성합니다.
1. Drawing object에 대한 [Border](https://reference.aspose.com/pdf/ko/net/aspose.pdf.drawing/graph/properties/border)를 설정합니다.
1. 페이지의 단락 컬렉션에 [Graph](https://reference.aspose.com/pdf/ko/net/aspose.pdf.drawing/graph) 객체를 추가합니다.
1. PDF 파일을 저장합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Circle()
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

        // Create a circle with the specified coordinates and radius
        var circle = new Aspose.Pdf.Drawing.Circle(100, 100, 40);

        // Set the circle's color
        circle.GraphInfo.Color = Aspose.Pdf.Color.GreenYellow;

        // Add the circle to the graph shapes
        graph.Shapes.Add(circle);

        // Add Graph object to paragraphs collection of page
        page.Paragraphs.Add(graph);

        // Save PDF document
        document.Save(dataDir + "DrawingCircle1_out.pdf");
    }
}
```

그림으로 그린 원은 다음과 같이 보일 것입니다:

![Drawing Circle](drawing_circle.png)

## 채워진 원 객체 만들기

이 예제는 색으로 채워진 원 객체를 추가하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CircleFilled()
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

        // Create a filled circle
        var circle = new Aspose.Pdf.Drawing.Circle(100, 100, 40)
        {
            GraphInfo = 
            { 
                Color = Aspose.Pdf.Color.GreenYellow, 
                FillColor = Aspose.Pdf.Color.Green 
            },
            Text = new Aspose.Pdf.Text.TextFragment("Circle")
        };

        // Add the circle to the graph shapes
        graph.Shapes.Add(circle);

        // Add Graph object to paragraphs collection of page
        page.Paragraphs.Add(graph);

        // Save PDF document
        document.Save(dataDir + "DrawingCircle2_out.pdf");
    }
}
```

채워진 원을 추가한 결과를 살펴보겠습니다:

![Filled Circle](filled_circle.png)

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