---
title: 将线对象添加到PDF文件
linktitle: 添加线
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /zh/net/add-line/
description: 本文解释了如何使用Aspose.PDF for .NET将线对象创建到您的PDF中。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Line Object to PDF file",
    "alternativeHeadline": "Enhance PDFs with Custom Line Objects Using .NET",
    "abstract": "通过无缝添加线对象来增强您的PDF文档，使用Aspose.PDF for .NET。此新功能允许精确控制线条属性，包括虚线模式和颜色，使用户能够在PDF文件中创建视觉上吸引人的图形表示。了解如何通过全面的代码示例和清晰的逐步说明轻松实现此功能。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Line Object, PDF manipulation, Aspose.PDF for .NET, Line object, Drawing in PDF, Graph object, Rectangle in PDF, Dotted Dashed Line, Draw Line Across the Page, PDF document generation",
    "wordcount": "729",
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
    "url": "/net/add-line/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-line/"
    },
    "dateModified": "2024-11-25",
    "description": "本文解释了如何使用Aspose.PDF for .NET将线对象创建到您的PDF中。"
}
</script>

以下代码片段也适用于[Aspose.PDF.Drawing](/pdf/net/drawing/)库。

## 添加线对象

Aspose.PDF for .NET支持将图形对象（例如图形、线条、矩形等）添加到PDF文档的功能。您还可以添加[线](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/line)对象，在其中您还可以指定虚线模式、颜色和其他线元素的格式。

请按照以下步骤操作：

1. 创建一个新的PDF [文档](https://reference.aspose.com/pdf/net/aspose.pdf/document)。
1. 将[页面](https://reference.aspose.com/pdf/net/aspose.pdf/page)添加到PDF文件的页面集合中。
1. 创建[图形](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph)实例。
1. 将图形对象添加到页面实例的段落集合中。
1. 创建[矩形](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle)实例。
1. 设置线宽。
1. 将[矩形](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle)对象添加到图形对象的形状集合中。

1. 保存您的PDF文件。

以下代码片段演示了如何添加一个填充颜色的[矩形](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle)对象。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddLineObjectToPDF()
{
    // The path to the document directory
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

        // Create Line instance with specified coordinates
        var line = new Aspose.Pdf.Drawing.Line(new float[] { 100, 100, 200, 100 });

        // Specify dash settings for the line
        line.GraphInfo.DashArray = new int[] { 0, 1, 0 };
        line.GraphInfo.DashPhase = 1;

        // Add line object to shapes collection of Graph object
        graph.Shapes.Add(line);

        // Save PDF document
        document.Save(dataDir + "AddLineObject_out.pdf");
    }
}
```

![添加线](add_line.png)

## 如何将虚线添加到您的PDF文档

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DashLengthInBlackAndDashLengthInWhite()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create Drawing object with certain dimensions
        var canvas = new Aspose.Pdf.Drawing.Graph(100, 400);

        // Add drawing object to paragraphs collection of page instance
        page.Paragraphs.Add(canvas);

        // Create Line object
        var line = new Aspose.Pdf.Drawing.Line(new float[] { 100, 100, 200, 100 });

        // Set color for Line object
        line.GraphInfo.Color = Aspose.Pdf.Color.Red;

        // Specify dash array for line object
        line.GraphInfo.DashArray = new int[] { 3, 2 }; // Dash and gap lengths in points

        // Set the dash phase for Line instance
        line.GraphInfo.DashPhase = 1;

        // Add line to shapes collection of drawing object
        canvas.Shapes.Add(line);

        // Save PDF document
        document.Save(dataDir + "DashLengthInBlackAndDashLengthInWhite_out.pdf");
    }
}
```

让我们检查一下结果：

![虚线](dash_line.png)

## 在页面上绘制线条

我们还可以使用线对象绘制一条从左下角到右上角的交叉线，以及从左上角到右下角的交叉线。

请查看以下代码片段以实现此要求。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExampleLineAcrossPage()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Set page margin on all sides as 0
        page.PageInfo.Margin.Left = 0;
        page.PageInfo.Margin.Right = 0;
        page.PageInfo.Margin.Bottom = 0;
        page.PageInfo.Margin.Top = 0;

        // Create Graph object with Width and Height equal to page dimensions
        var graph = new Aspose.Pdf.Drawing.Graph(
            (float)page.PageInfo.Width,
            (float)page.PageInfo.Height);

        // Create first line object starting from Lower-Left to Top-Right corner of page
        var line1 = new Aspose.Pdf.Drawing.Line(new float[]
        {
            (float)page.Rect.LLX, 0,
            (float)page.PageInfo.Width,
            (float)page.Rect.URY
        });

        // Add line to shapes collection of Graph object
        graph.Shapes.Add(line1);

        // Create second line object starting from Top-Left corner to Bottom-Right corner of page
        var line2 = new Aspose.Pdf.Drawing.Line(new float[]
        {
            0, (float)page.Rect.URY,
            (float)page.PageInfo.Width, (float)page.Rect.LLX
        });

        // Add line to shapes collection of Graph object
        graph.Shapes.Add(line2);

        // Add Graph object to paragraphs collection of page
        page.Paragraphs.Add(graph);

        // Save PDF document
        document.Save(dataDir + "ExampleLineAcrossPage_out.pdf");
    }
}
```

![绘制线条](draw_line.png)

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