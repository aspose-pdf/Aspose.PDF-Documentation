---
title: 将椭圆对象添加到PDF文件
linktitle: 添加椭圆
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /zh/net/add-ellipse/
description: 本文解释了如何使用Aspose.PDF for .NET将椭圆对象创建到您的PDF中。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Ellipse Object to PDF file",
    "alternativeHeadline": "Add Ellipse Objects in PDF Files Effortlessly",
    "abstract": "介绍Aspose.PDF在.NET中的新椭圆对象功能，使开发人员能够轻松将椭圆形状纳入其PDF文档中。此功能支持添加填充椭圆，甚至在形状内添加文本，增强PDF文件的视觉呈现和自定义。通过丰富的图形元素优化文档生成，提高用户参与度。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Ellipse, PDF manipulation, Aspose.PDF for .NET, create ellipse object, filled ellipse, text inside ellipse, drawing object, color fill, PDF document generation",
    "wordcount": "541",
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
    "url": "/net/add-ellipse/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-ellipse/"
    },
    "dateModified": "2024-11-25",
    "description": "本文解释了如何使用Aspose.PDF for .NET将椭圆对象创建到您的PDF中。"
}
</script>

以下代码片段也适用于[Aspose.PDF.Drawing](/pdf/zh/net/drawing/)库。

## 添加椭圆对象

Aspose.PDF for .NET支持将[椭圆](https://reference.aspose.com/pdf/zh/net/aspose.pdf.drawing/ellipse)对象添加到PDF文档中。它还提供用特定颜色填充椭圆对象的功能。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Ellipse()
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

        // Create first ellipse with specified coordinates and radii
        var ellipse1 = new Aspose.Pdf.Drawing.Ellipse(150, 100, 120, 60)
        {
            GraphInfo = { Color = Aspose.Pdf.Color.GreenYellow },
            Text = new Aspose.Pdf.Text.TextFragment("Ellipse")
        };
        graph.Shapes.Add(ellipse1);

        // Create second ellipse with different dimensions and color
        var ellipse2 = new Aspose.Pdf.Drawing.Ellipse(50, 50, 18, 300)
        {
            GraphInfo = { Color = Aspose.Pdf.Color.DarkRed }
        };
        graph.Shapes.Add(ellipse2);

        // Add Graph object to paragraphs collection of page
        page.Paragraphs.Add(graph);

        // Save PDF document
        document.Save(dataDir + "DrawingEllipse_out.pdf");
    }
}
```

![添加椭圆](ellipse.png)

## 创建填充椭圆对象

以下代码片段演示如何添加一个用颜色填充的[椭圆](https://reference.aspose.com/pdf/zh/net/aspose.pdf.drawing/ellipse)对象。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EllipseFilled()
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

        // Create first ellipse and set its fill color
        var ellipse1 = new Aspose.Pdf.Drawing.Ellipse(100, 100, 120, 180)
        {
            GraphInfo = 
            { 
                FillColor = Aspose.Pdf.Color.GreenYellow 
            }
        };
        graph.Shapes.Add(ellipse1);

        // Create second ellipse and set its fill color
        var ellipse2 = new Aspose.Pdf.Drawing.Ellipse(200, 150, 180, 120)
        {
            GraphInfo = 
            { 
                FillColor = Aspose.Pdf.Color.DarkRed 
            }
        };
        graph.Shapes.Add(ellipse2);

        // Add Graph object to paragraphs collection of page
        page.Paragraphs.Add(graph);

        // Save PDF document
        document.Save(dataDir + "DrawingEllipse_out.pdf");
    }
}
```

![填充椭圆](fill_ellipse.png)

## 在椭圆内添加文本

Aspose.PDF for .NET支持在图形对象内添加文本。图形对象的文本属性提供设置图形对象文本的选项。以下代码片段演示如何在矩形对象内添加文本。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EllipseWithText()
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

        // Create TextFragment for adding text to shapes
        var textFragment = new Aspose.Pdf.Text.TextFragment("Ellipse")
        {
            TextState =
            {
                Font = Aspose.Pdf.Text.FontRepository.FindFont("Helvetica"),
                FontSize = 24
            }
        };

        // Create first ellipse and set properties
        var ellipse1 = new Aspose.Pdf.Drawing.Ellipse(100, 100, 120, 180)
        {
            GraphInfo = 
            { 
                FillColor = Aspose.Pdf.Color.GreenYellow 
            },
            Text = textFragment
        };
        graph.Shapes.Add(ellipse1);

        // Create second ellipse and set properties
        var ellipse2 = new Aspose.Pdf.Drawing.Ellipse(200, 150, 180, 120)
        {
            GraphInfo = 
            { 
                FillColor = Aspose.Pdf.Color.DarkRed 
            },
            Text = textFragment
        };
        graph.Shapes.Add(ellipse2);

        // Add Graph object to paragraphs collection of page
        page.Paragraphs.Add(graph);

        // Save PDF document
        document.Save(dataDir + "DrawingEllipseText_out.pdf");
    }
}
 ```

![椭圆内的文本](text_ellipse.png)

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