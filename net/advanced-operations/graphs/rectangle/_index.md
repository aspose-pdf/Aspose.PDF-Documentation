---
title: Add Rectangle Object to PDF file
linktitle: Add Rectangle
type: docs
weight: 50
url: /net/add-rectangle/
description: This article explains how to create a Rectangle object to your PDF using Aspose.PDF for .NET.
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
    "alternativeHeadline": "How to create Rectangle Object in PDF file",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, rectangle in pdf",
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
    "url": "/net/add-rectangle/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-rectangle/"
    },
    "dateModified": "2022-02-04",
    "description": "This article explains how to create a Rectangle object to your PDF using Aspose.PDF for .NET."
}
</script>

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

## Add Rectangle object

Aspose.PDF for .NET supports the feature to add graph objects (for example graph, line, rectangle etc.) to PDF documents. You also get the leverage to add [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) object where you also offers the feature to fill rectangle object with a certain color, control Z-Order, add gradiant color fill and etc.

First, let's look at the possibility of creating a Rectangle object.

Follow the steps below:

1. Create a new PDF [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)

1. Add [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) to pages collection of PDF file

1. Add [Text fragment](https://reference.aspose.com/pdf/net/aspose.pdf/texfragment) to paragraphs collection of page instance

1. Create [Graph](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) instance

1. Set border for [Drawing object](https://reference.aspose.com/pdf/net/aspose.pdf.drawing)

1. Create Rectangle instance

1. Add [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) object to shapes collection of Graph object

1. Add graph object to paragraphs collection of page instance

1. Add [Text fragment](https://reference.aspose.com/pdf/net/aspose.pdf/texfragment) to paragraphs collection of page instance

1. And save your PDF file

```csharp
 private static void AddRectangle(Page page, float x, float y, float width, float height, Color color, int zindex)
        {
            // Create graph object with dimensions same as specified for Rectangle object
            Aspose.Pdf.Drawing.Graph graph = new Aspose.Pdf.Drawing.Graph(width, height)
            {
                // Can we change the position of graph instance
                IsChangePosition = false,
                // Set Left coordinate position for Graph instance
                Left = x,
                // Set Top coordinate position for Graph object
                Top = y
            };
            // Add a rectangle inside the "graph"
            Rectangle rect = new Rectangle(0, 0, width, height);
            // Set rectangle fill color
            rect.GraphInfo.FillColor = color;
            // Color of graph object
            rect.GraphInfo.Color = color;
            // Add rectangle to shapes collection of graph instance
            graph.Shapes.Add(rect);
            // Set Z-Index for rectangle object
            graph.ZIndex = zindex;
            // Add graph to paragraphs collection of page object
            page.Paragraphs.Add(graph);
        }
```

![Create Rectangle](create_rectangle.png)

## Create Filled Rectangle Object

Aspose.PDF for .NET also offers the feature to fill rectangle object with a certain color.

The following code snippet shows how to add a [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) object that is filled with color.

```csharp
    {
        private const string _dataDir = "C:\\Samples\\";
        public static void RectangleFilled()
        {
            // Create Document instance
            var doc = new Document();

            // Add page to pages collection of PDF file
            var page = doc.Pages.Add();
            // Create Graph instance
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);

            // Add graph object to paragraphs collection of page instance
            page.Paragraphs.Add(graph);

            // Create Rectangle instance
            var rect = new Rectangle(100, 100, 200, 120);

            // Specify fill color for Graph object
            rect.GraphInfo.FillColor = Color.Red;

            // Add rectangle object to shapes collection of Graph object
            graph.Shapes.Add(rect);

            // Save PDF file
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```

Look at the result of rectangle filled solid color:

![Filled Rectangle](fill_rectangle.png)

## Add Drawing with Gradient Fill

Aspose.PDF for .NET supports the feature to add graph objects to PDF documents and sometimes it is required to fill graph objects with Gradient Color. To Fill graph objects with Gradient Color, We need to set setPatterColorSpace with gradientAxialShading object as following.

The following code snippet shows how to add a [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) object that is filled with Gradient Color.

```csharp
 public static void CreateFilledRectangletGradientFill()
        {
            // Create Document instance
            var doc = new Document();

            // Add page to pages collection of PDF file
            var page = doc.Pages.Add();
            // Create Graph instance
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // Add graph object to paragraphs collection of page instance
            page.Paragraphs.Add(graph);
            // Create Rectangle instance
            var rect = new Rectangle(0, 0, 300, 300);
            // Specify fill color for Graph object
            var gradientColor = new Color();
            var gradientSettings = new GradientAxialShading(Color.Red, Color.Blue)
            {
                Start = new Point(0, 0),
                End = new Point(350, 350)
            };
            gradientColor.PatternColorSpace = gradientSettings;
            rect.GraphInfo.FillColor = gradientColor;

            // Add rectangle object to shapes collection of Graph object
            graph.Shapes.Add(rect);

            // Save PDF file
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```

![Gradient Rectangle](gradient.png)

## Create Rectangle with Alpha color channel

Aspose.PDF for .NET supports to fill rectangle object with a certain color. A rectangle object can also have Alpha color channel to give transparent appearance. The following code snippet shows how to add a [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) object with Alpha color channel.

Pixels of the image can store information about their opacity along with color value. This allows creating images with transparent or semi-transparent areas.

Instead of making a color transparent, each pixel stores information on how opaque it is. This opacity data is called alpha channel and is typically stored after the color channels of the pixel.

```csharp
     public static void RectangleFilled_AlphaChannel()
        {
            // Create Document instance
            var doc = new Document();

            // Add page to pages collection of PDF file
            var page = doc.Pages.Add();
            // Create Graph instance
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);
            // Add graph object to paragraphs collection of page instance
            page.Paragraphs.Add(graph);
            // Create Rectangle instance
            var rect = new Rectangle(100, 100, 200, 120);
            // Specify fill color for Graph object
            rect.GraphInfo.FillColor = Color.FromArgb(128, 244, 180, 0);

            // Add rectangle object to shapes collection of Graph object
            graph.Shapes.Add(rect);

            // Create second rectangle object
            var rect1 = new Rectangle(200, 150, 200, 100);
            rect1.GraphInfo.FillColor = Color.FromArgb(160, 120, 0, 120);
            graph.Shapes.Add(rect1);

            // Add graph instance to paragraph collection of page object
            page.Paragraphs.Add(graph);

            // Save PDF file
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```

![Rectangle Alpha Channel Color](rectangle_color.png)

## Control Z-Order of Rectangle

Aspose.PDF for .NET supports the feature to add graph objects (for example graph, line, rectangle etc.) to PDF documents. When adding more than one instance of same object inside PDF file, we can control their rendering by specifying the Z-Order. Z-Order is also used when we need to render objects on top of each other.

The following code snippet shows the steps to render [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) objects on top of each other.

```csharp
 public static void AddRectangleZOrder()
        {
            // Instantiate Document class object
            Document doc1 = new Document();
            /// Add page to pages collection of PDF file
            Page page1 = doc1.Pages.Add();
            // Set size of PDF page
            page1.SetPageSize(375, 300);
            // Set left margin for page object as 0
            page1.PageInfo.Margin.Left = 0;
            // Set top margin of page object as 0
            page1.PageInfo.Margin.Top = 0;
            // Create a new rectangle with Color as Red, Z-Order as 0 and certain dimensions
            AddRectangle(page1, 50, 40, 60, 40, Color.Red, 2);
            // Create a new rectangle with Color as Blue, Z-Order as 0 and certain dimensions
            AddRectangle(page1, 20, 20, 30, 30, Color.Blue, 1);
            // Create a new rectangle with Color as Green, Z-Order as 0 and certain dimensions
            AddRectangle(page1, 40, 40, 60, 30, Color.Green, 0);
            // Save resultant PDF file
            doc1.Save(_dataDir + "ControlRectangleZOrder_out.pdf");
        }
```

![Controlling Z Order](control.png)

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
