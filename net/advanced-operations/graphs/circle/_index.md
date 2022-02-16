---
title: Add Circle Object to PDF file
linktitle: Add Circle
type: docs
weight: 20
url: /net/add-circle/
description: This article explains how to create a circle object to your PDF using Aspose.PDF for .NET.
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
    "alternativeHeadline": "Add Circle Object to PDF file",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, document generation",
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
    "url": "/net/add-circle/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-circle/"
    },
    "dateModified": "2022-02-04",
    "description": "This article explains how to create a circle object to your PDF using Aspose.PDF for .NET."
}
</script>

## Add Circle object

Like bar graphs, circle graphs can be used to display data in a number of separate categories. Unlike bar graphs, however, circle graphs can be used only when you have data for all the categories that make up the whole. So let's take a look at adding a [Circle](https://apireference.aspose.com/pdf/net/aspose.pdf.drawing/circle) object with Aspose.PDF for .NET.

Follow the steps below:

1. Create [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) instance

1. Create [Drawing object](https://apireference.aspose.com/pdf/net/aspose.pdf.drawing) with certain dimensions

1. Set [Border](https://apireference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border) for Drawing object

1. Add [Graph](https://apireference.aspose.com/pdf/net/aspose.pdf.drawing/graph) object to paragraphs collection of page

1. Save our PDF file

```csharp
        public static void Circle()
        {
            // Create Document instance
            var document = new Document();

            // Add page to pages collection of PDF file
            var page = document.Pages.Add();

            // Create Drawing object with certain dimensions
            var graph = new Aspose.Pdf.Drawing.Graph(400, 200);
            // Set border for Drawing object
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var circle = new Circle(100, 100, 40);

            circle.GraphInfo.Color = Color.GreenYellow;
            graph.Shapes.Add(circle);

            // Add Graph object to paragraphs collection of page
            page.Paragraphs.Add(graph);

            // Save PDF file
            document.Save(_dataDir + "DrawingCircle1_out.pdf");
        }
```

Our drawn circle will look like this:

![Drawing Circle](drawing_circle.png)

## Create Filled Circle Object

This example shows how to add a Circle object that is filled with color.

```csharp
        public static void CircleFilled()
        {
            // Create Document instance
            var document = new Document();

            // Add page to pages collection of PDF file
            var page = document.Pages.Add();

            // Create Drawing object with certain dimensions
            var graph = new Aspose.Pdf.Drawing.Graph(400, 200);

            // Set border for Drawing object
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var circle = new Circle(100, 100, 40);
            circle.GraphInfo.Color = Color.GreenYellow;
            circle.GraphInfo.FillColor = Color.Green;
            circle.Text = new TextFragment("Circle");

            graph.Shapes.Add(circle);

            // Add Graph object to paragraphs collection of page
            page.Paragraphs.Add(graph);

            // Save PDF file
            document.Save(_dataDir + "DrawingCircle2_out.pdf");
        }
```

Let's see the result of adding a filled Circle:

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
