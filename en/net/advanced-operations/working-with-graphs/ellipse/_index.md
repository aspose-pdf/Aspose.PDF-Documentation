---
title: Add Ellipse Object to PDF file
linktitle: Add Ellipse
type: docs
weight: 60
url: /net/add-ellipse/
description: This article explains how to create a Ellipse object to your PDF using Aspose.PDF for .NET.
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
    "abstract": "Introducing the new Ellipse Object feature for Aspose.PDF in .NET, which allows developers to effortlessly incorporate ellipse shapes into their PDF documents. This functionality supports adding filled ellipses and even text within the shapes, enhancing the visual presentation and customization of PDF files. Optimize your document generation with rich graphical elements that elevate user engagement",
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
    "description": "This article explains how to create a Ellipse object to your PDF using Aspose.PDF for .NET."
}
</script>

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

## Add Ellipse object

Aspose.PDF for .NET supports to add [Ellipse](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/ellipse) objects to PDF documents. It also offers the feature to fill ellipse  object with a certain color.

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

![Add Ellipse](ellipse.png)

## Create Filled Ellipse Object

The following code snippet shows how to add a [Ellipse](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/ellipse)  object that is filled with color.

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

![Filled Ellipse](fill_ellipse.png)

## Add Text inside the Ellipse

Aspose.PDF for .NET supports to add text inside the Graph Object. Text property of Graph Object provides option to set text of the Graph Object. The following code snippet shows how to add text inside a Rectangle object.

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

![Text inside Ellipse](text_ellipse.png)

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
