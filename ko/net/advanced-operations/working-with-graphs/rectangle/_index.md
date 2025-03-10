---
title: PDF 파일에 사각형 객체 추가
linktitle: 사각형 추가
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ko/net/add-rectangle/
description: 이 문서에서는 Aspose.PDF for .NET을 사용하여 PDF에 사각형 객체를 만드는 방법을 설명합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Rectangle Object to PDF file",
    "alternativeHeadline": "Add Rectangle to PDF file",
    "abstract": "Aspose.PDF for .NET의 새로운 기능은 사용자가 PDF 문서에 사각형 객체를 원활하게 추가할 수 있도록 합니다. 이 기능은 사각형을 단색, 그라디언트 채우기 및 투명도로 사용자 정의할 수 있는 옵션을 포함하여 PDF 콘텐츠에 대한 향상된 시각적 사용자 정의 및 레이어링 제어를 제공합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Rectangle, PDF document generation, Aspose.PDF for .NET, Rectangle object, fill rectangle, gradient color fill, Z-Order control, alpha channel color, graph objects in PDF, create filled rectangle",
    "wordcount": "1263",
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
    "url": "/net/add-rectangle/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-rectangle/"
    },
    "dateModified": "2024-11-25",
    "description": "이 문서에서는 Aspose.PDF for .NET을 사용하여 PDF에 사각형 객체를 만드는 방법을 설명합니다."
}
</script>

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

## 사각형 객체 추가

Aspose.PDF for .NET은 PDF 문서에 그래프 객체(예: 그래프, 선, 사각형 등)를 추가하는 기능을 지원합니다. 또한 특정 색상으로 사각형 객체를 채우고, Z-순서를 제어하고, 그라디언트 색상 채우기를 추가하는 기능을 제공합니다.

먼저, 사각형 객체를 만드는 가능성을 살펴보겠습니다.

아래 단계를 따르세요:

1. 새 PDF [문서](https://reference.aspose.com/pdf/net/aspose.pdf/document) 생성.
1. PDF 파일의 페이지 컬렉션에 [페이지](https://reference.aspose.com/pdf/net/aspose.pdf/page) 추가.
1. 페이지 인스턴스의 단락 컬렉션에 [텍스트 조각](https://reference.aspose.com/pdf/net/aspose.pdf/texfragment) 추가.
1. [그래프](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) 인스턴스 생성.
1. [그리기 객체](https://reference.aspose.com/pdf/net/aspose.pdf.drawing)에 테두리 설정.
1. 사각형 인스턴스 생성.

1. [사각형](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) 객체를 그래프 객체의 도형 컬렉션에 추가.
1. 페이지 인스턴스의 단락 컬렉션에 그래프 객체 추가.
1. 페이지 인스턴스의 단락 컬렉션에 [텍스트 조각](https://reference.aspose.com/pdf/net/aspose.pdf/texfragment) 추가.

1. 그리고 PDF 파일을 저장하세요.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddRectangle(Aspose.Pdf.Page page, float x, float y, float width, float height, Aspose.Pdf.Color color, int zIndex)
{
    // Create a Graph object with dimensions matching the specified rectangle
    var graph = new Aspose.Pdf.Drawing.Graph(width, height)
    {
        // Prevent the graph from repositioning automatically
        IsChangePosition = false,
        // Set the Left coordinate position for the Graph instance
        Left = x,
        // Set the Top coordinate position for the Graph instance
        Top = y
    };

    // Create a Rectangle object inside the Graph
    var rect = new Aspose.Pdf.Drawing.Rectangle(0, 0, width, height)
    {
        // Set the fill color of the rectangle
        GraphInfo =
        {
            FillColor = color,
            // Set the border color of the rectangle
            Color = color
        }
    };

    // Add the rectangle to the Shapes collection of the Graph
    graph.Shapes.Add(rect);

    // Set the Z-Index for the Graph object to control layering
    graph.ZIndex = zIndex;

    // Add the Graph object to the Paragraphs collection of the page
    page.Paragraphs.Add(graph);
}
```

![사각형 만들기](create_rectangle.png)

## 채워진 사각형 객체 만들기

Aspose.PDF for .NET은 특정 색상으로 사각형 객체를 채우는 기능도 제공합니다.

다음 코드 스니펫은 색상으로 채워진 [사각형](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) 객체를 추가하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RectangleFilled()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create Graph instance
        var graph = new Aspose.Pdf.Drawing.Graph(100, 400);

        // Add graph object to paragraphs collection of page instance
        page.Paragraphs.Add(graph);

        // Create Rectangle instance with specified dimensions
        var rect = new Aspose.Pdf.Drawing.Rectangle(100, 100, 200, 120)
        {
            // Specify fill color for the Rectangle object
            GraphInfo = 
            { 
                FillColor = Aspose.Pdf.Color.Red 
            }
        };

        // Add rectangle object to shapes collection of Graph object
        graph.Shapes.Add(rect);

        // Save PDF document
        document.Save(dataDir + "CreateFilledRectangle_out.pdf");
    }
}
```

단색으로 채워진 사각형의 결과를 살펴보세요:

![채워진 사각형](fill_rectangle.png)

## 그라디언트 채우기로 그리기 추가

Aspose.PDF for .NET은 PDF 문서에 그래프 객체를 추가하는 기능을 지원하며, 때때로 그래프 객체를 그라디언트 색상으로 채워야 할 필요가 있습니다. 그래프 객체를 그라디언트 색상으로 채우기 위해서는 gradientAxialShading 객체와 함께 setPatterColorSpace를 설정해야 합니다.

다음 코드 스니펫은 그라디언트 색상으로 채워진 [사각형](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) 객체를 추가하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateFilledRectangleGradientFill()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create Graph instance
        var graph = new Aspose.Pdf.Drawing.Graph(400, 400);

        // Add graph object to paragraphs collection of page instance
        page.Paragraphs.Add(graph);

        // Create Rectangle instance
        var rect = new Aspose.Pdf.Drawing.Rectangle(0, 0, 300, 300);

        // Create a gradient fill color
        var gradientColor = new Aspose.Pdf.Color();
        var gradientSettings = new Aspose.Pdf.Drawing.GradientAxialShading(Aspose.Pdf.Color.Red, Aspose.Pdf.Color.Blue)
        {
            Start = new Aspose.Pdf.Point(0, 0),
            End = new Aspose.Pdf.Point(350, 350)
        };
        gradientColor.PatternColorSpace = gradientSettings;

        // Apply gradient fill color to the rectangle
        rect.GraphInfo.FillColor = gradientColor;

        // Add rectangle object to shapes collection of Graph object
        graph.Shapes.Add(rect);

        // Save PDF document
        document.Save(dataDir + "CreateFilledRectangleGradient_out.pdf");
    }
}
```

![그라디언트 사각형](gradient.png)

## 알파 색상 채널로 사각형 만들기

Aspose.PDF for .NET은 특정 색상으로 사각형 객체를 채우는 기능을 지원합니다. 사각형 객체는 투명한 외관을 제공하기 위해 알파 색상 채널을 가질 수도 있습니다. 다음 코드 스니펫은 알파 색상 채널이 있는 [사각형](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) 객체를 추가하는 방법을 보여줍니다.

이미지의 픽셀은 색상 값과 함께 불투명도에 대한 정보를 저장할 수 있습니다. 이를 통해 투명하거나 반투명한 영역이 있는 이미지를 만들 수 있습니다.

색상을 투명하게 만드는 대신, 각 픽셀은 얼마나 불투명한지를 저장합니다. 이 불투명도 데이터는 알파 채널이라고 하며 일반적으로 픽셀의 색상 채널 뒤에 저장됩니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RectangleFilled_AlphaChannel()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create Graph instance
        var graph = new Aspose.Pdf.Drawing.Graph(100, 400);

        // Add graph object to paragraphs collection of page instance
        page.Paragraphs.Add(graph);

        // Create first rectangle with alpha channel fill color
        var rect = new Aspose.Pdf.Drawing.Rectangle(100, 100, 200, 120)
        {
            GraphInfo = 
            { 
                FillColor = Aspose.Pdf.Color.FromArgb(128, 244, 180, 0) 
            }
        };

        // Add the first rectangle to the shapes collection of the Graph object
        graph.Shapes.Add(rect);

        // Create second rectangle with different alpha channel fill color
        var rect1 = new Aspose.Pdf.Drawing.Rectangle(200, 150, 200, 100)
        {
            GraphInfo = 
            { 
                FillColor = Aspose.Pdf.Color.FromArgb(160, 120, 0, 120) 
            }
        };

        // Add the second rectangle to the shapes collection of the Graph object
        graph.Shapes.Add(rect1);

        // Save PDF document
        document.Save(dataDir + "CreateFilledRectangle_out.pdf");
    }
}
```

![사각형 알파 채널 색상](rectangle_color.png)

## 사각형의 Z-순서 제어

Aspose.PDF for .NET은 PDF 문서에 그래프 객체(예: 그래프, 선, 사각형 등)를 추가하는 기능을 지원합니다. PDF 파일 내에서 동일한 객체의 여러 인스턴스를 추가할 때, Z-순서를 지정하여 렌더링을 제어할 수 있습니다. Z-순서는 객체를 서로 위에 렌더링해야 할 때도 사용됩니다.

다음 코드 스니펫은 서로 위에 렌더링하는 [사각형](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) 객체의 단계를 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddRectangleZOrder()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Set size of PDF page
        page.SetPageSize(375, 300);

        // Set left and top margins for the page object as 0
        page.PageInfo.Margin.Left = 0;
        page.PageInfo.Margin.Top = 0;

        // Create rectangles with different colors and Z-Order values
        AddRectangle(page, 50, 40, 60, 40, Aspose.Pdf.Color.Red, 2);
        AddRectangle(page, 20, 20, 30, 30, Aspose.Pdf.Color.Blue, 1);
        AddRectangle(page, 40, 40, 60, 30, Aspose.Pdf.Color.Green, 0);

        // Save PDF document
        document.Save(dataDir + "ControlRectangleZOrder_out.pdf");
    }
}
```

![Z 순서 제어](control.png)

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