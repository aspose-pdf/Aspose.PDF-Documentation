---
title: Add Circle Object to PDF file
linktitle: Add Circle
type: docs
weight: 20
url: /net/add-circle/
description: This article explains how to create a circle object to your PDF using Aspose.PDF for .NET.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

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
