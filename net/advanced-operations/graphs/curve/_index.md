---
title: Add Curve Object to PDF file
linktitle: Add Curve
type: docs
weight: 30
url: /net/add-curve/
description: This article explains how to create a curve object to your PDF using Aspose.PDF for .NET.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

A graph [Curve](https://apireference.aspose.com/pdf/net/aspose.pdf.drawing/curve) is a connected union of projective lines, each line meeting three others in ordinary double points.

Aspose.PDF for .NET shows how to use Bézier curves in your Graphs.
Bézier curves are widely used in computer graphics to model smooth curves. The curve is completely contained in the convex hull of its control points, the points may be graphically displayed and used to manipulate the curve intuitively.
The entire curve is contained in the quadrilateral whose corners are the four given points (their convex hull).

In this article, we will investigate  simply graph curves, and filled curves, that you can create in your PDF document.

Follow the steps below:

1. Create [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) instance

1. Create [Drawing object](https://apireference.aspose.com/pdf/net/aspose.pdf.drawing) with certain dimensions

1. Set [Border](https://apireference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border) for Drawing object

1. Add [Graph](https://apireference.aspose.com/pdf/net/aspose.pdf.drawing/graph) object to paragraphs collection of page

1. Save our PDF file

```csharp
 public static void ExampleCurve()
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

            var curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120 });
            curve1.GraphInfo.Color = Color.GreenYellow;
            graph.Shapes.Add(curve1);

            // Add Graph object to paragraphs collection of page
            page.Paragraphs.Add(graph);

            // Save PDF file
            document.Save(_dataDir + "DrawingCurve1_out.pdf");
        }
```

The following picture shows the result executed with our code snippet:

![Drawing Curve](drawing_curve.png)

## Create Filled Curve Object

This example shows how to add a Curve object that is filled with color.

```csharp
      public static void CurveFilled()
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

            var curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120 });
            curve1.GraphInfo.FillColor = Color.GreenYellow;
            graph.Shapes.Add(curve1);

            // Add Graph object to paragraphs collection of page
            page.Paragraphs.Add(graph);

            // Save PDF file
            document.Save(_dataDir + "DrawingCurve2_out.pdf");
        }
```

Look at the result of adding a filled Curve:

![Filled Curve](filled_curve.png)
