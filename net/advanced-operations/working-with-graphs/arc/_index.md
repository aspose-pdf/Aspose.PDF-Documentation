---
title: Add Arc Object to PDF file
linktitle: Add Arc
type: docs
weight: 10
url: /net/add-arc/
description: This article explains how to create a arc object to your PDF using Aspose.PDF for .NET.
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
    "alternativeHeadline": "How to create Arc in PDF file",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, arc in pdf",
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
    "url": "/net/add-arc/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-arc/"
    },
    "dateModified": "2022-02-04",
    "description": "This article explains how to create a arc object to your PDF using Aspose.PDF for .NET."
}
</script>

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

## Add Arc object

Aspose.PDF for .NET supports the feature to add graph objects (for example graph, line, rectangle etc.) to PDF documents. It also offers the feature to fill arc object with a certain color.

Follow the steps below:

1. Create [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) instance

1. Create [Drawing object](https://reference.aspose.com/pdf/net/aspose.pdf.drawing) with certain dimensions

1. Set [Border](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border) for Drawing object

1. Add [Graph](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) object to paragraphs collection of page

1. Save our PDF file

The following code snippet shows how to add a [Arc](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/arc) object.

```csharp
public static void Arc()
{
    // Create Document instance
    var document = new Document();

    // Add page to pages collection of PDF file
    var page = document.Pages.Add();

    // Create Drawing object with certain dimensions
    var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
    // Set border for Drawing object
    var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
    graph.Border = borderInfo;

    var arc1 = new Arc(100, 100, 95, 0, 90);
    arc1.GraphInfo.Color = Color.GreenYellow;
    graph.Shapes.Add(arc1);

    var arc2 = new Arc(100, 100, 90, 70, 180);
    arc2.GraphInfo.Color = Color.DarkBlue;
    graph.Shapes.Add(arc2);

    var arc3 = new Arc(100, 100, 85, 120, 210);
    arc3.GraphInfo.Color = Color.Red;
    graph.Shapes.Add(arc3);

    // Add Graph object to paragraphs collection of page
    page.Paragraphs.Add(graph);

    // Save PDF file
    document.Save(_dataDir + "DrawingArc_out.pdf");
}
```

## Create Filled Arc Object

Next example shows how to add a Arc object that is filled with color and certain dimensions.

```csharp
public static void ArcFilled()
{
    // Create Document instance
    var document = new Document();

    // Add page to pages collection of PDF file
    var page = document.Pages.Add();

    // Create Drawing object with certain dimensions
    var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
    // Set border for Drawing object
    var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
    graph.Border = borderInfo;

    var arc = new Arc(100, 100, 95, 0, 90);
    arc.GraphInfo.FillColor = Color.GreenYellow;
    graph.Shapes.Add(arc);

    var line = new Line(new float[] { 195, 100, 100, 100, 100, 195 });
    line.GraphInfo.FillColor = Color.GreenYellow;
    graph.Shapes.Add(line);

    // Add Graph object to paragraphs collection of page
    page.Paragraphs.Add(graph);

    // Save PDF file
    document.Save(_dataDir + "ExampleFilledArc_out.pdf");
}
```

Let's see the result of adding a filled Arс:

![Filled Arc](filled_arc.png)

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
