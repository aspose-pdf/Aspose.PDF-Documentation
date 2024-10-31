---
title: Add Line Object to PDF file
linktitle: Add Line
type: docs
weight: 40
url: /net/add-line/
description: This article explains how to create a line object to your PDF using Aspose.PDF for .NET.
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
    "alternativeHeadline": "How to create Line Object in PDF file",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, line in pdf",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "dateModified": "2022-02-04",
    "description": "This article explains how to create a line object to your PDF using Aspose.PDF for .NET."
}
</script>

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

## Add Line object

Aspose.PDF for .NET supports the feature to add graph objects (for example graph, line, rectangle etc.) to PDF documents. You also get the leverage to add [Line](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/line) object where you can also specify the dash pattern, color and other formatting for Line element.

Follow the steps below:

1. Create a new PDF [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)

1. Add [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) to pages collection of PDF file

1. Create [Graph](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) instance.

1. Add Graph object to paragraphs collection of page instance.

1. Create [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) instance.

1. Set line width.

1. Add [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) object to shapes collection of Graph object.

1. Save your PDF file.

The following code snippet shows how to add a [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) object that is filled with color.

```csharp
public static void AddLineObjectToPDF()
{
    // Create Document instance
    var document = new Document();

    // Add page to pages collection of PDF file
    var page = document.Pages.Add();

    // Create Graph instance
    var graph = new Aspose.Pdf.Drawing.Graph(100, 400);

    // Add graph object to paragraphs collection of page instance
    page.Paragraphs.Add(graph);

    // Create Rectangle instance
    var line = new Line(new float[] { 100, 100, 200, 100 });

    // Specify fill color for Graph object
    line.GraphInfo.DashArray = new int[] { 0, 1, 0 };
    line.GraphInfo.DashPhase = 1;

    // Add rectangle object to shapes collection of Graph object
    graph.Shapes.Add(line);

    // Save PDF file
    document.Save(_dataDir + "AddLineObject_out.pdf");
}
```

![Add Line](add_line.png)

## How to add Dotted Dashed Line to your PDF document

```csharp
public static void DashLengthInBlackAndDashLengthInWhite()
{
    // Create Document instance
    var document = new Document();

    // Add page to pages collection of PDF file
    var page = document.Pages.Add();

    // Create Drawing object with certain dimensions
    var canvas = new Aspose.Pdf.Drawing.Graph(100, 400);
    // Add drawing object to paragraphs collection of page instance
    page.Paragraphs.Add(canvas);

    // Create Line object
    var line = new Line(new float[] { 100, 100, 200, 100 });
    // Set color for Line object
    line.GraphInfo.Color = Color.Red;
    // Specify dash array for line object
    line.GraphInfo.DashArray = new int[] { 0, 1, 0 };
    // Set the dash phase for Line instance
    line.GraphInfo.DashPhase = 1;
    // Add line to shapes collection of drawing object
    canvas.Shapes.Add(line);
    // Save PDF file
    document.Save(_dataDir + "DashLengthInBlackAndDashLengthInWhite_out.pdf");
}
```

Let's check the result:

![Dashed Line](dash_line.png)

## Draw Line Across the Page

We can also use line object to draw a cross starting from Left-Bottom to Right-Upper corner and Left-Top corner to Bottom-Right corner.

Please take a look over following code snippet to accomplish this requirement.

```csharp
public static void ExampleLineAcrossPage()
{

    // Create Document instance
    var document = new Document();

    // Add page to pages collection of PDF file
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
    var line = new Line(
            new float[]{
                (float)page.Rect.LLX, 0,
                (float)page.PageInfo.Width,
                (float)page.Rect.URY });

    // Add line to shapes collection of Graph object
    graph.Shapes.Add(line);
    // Draw line from Top-Left corner of page to Bottom-Right corner of page
    var line2 = new Line(
        new float[]{ 0,
            (float) page.Rect.URY,
            (float) page.PageInfo.Width,
            (float) page.Rect.LLX });

    // Add line to shapes collection of Graph object
    graph.Shapes.Add(line2);

    // Add Graph object to paragraphs collection of page
    page.Paragraphs.Add(graph);

    // Save PDF file
    document.Save(_dataDir + "ExampleLineAcrossPage_out.pdf");
}
```

![Drawing Line](draw_line.png)

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
