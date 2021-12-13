---
title: Add Curve Object to PDF file
linktitle: Add Curve
type: docs
weight: 30
url: /java/add-curve/
description: This article explains how to create a curve object to your PDF using Aspose.PDF for Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Add Curve object

A graph [Curve](https://apireference.aspose.com/pdf/java/com.aspose.pdf.drawing/Curve) is a connected union of projective lines, each line meeting three others in ordinary double points.

Aspose.PDF for Java shows how to use Bézier curves in your Graphs.
Bézier curves are widely used in computer graphics to model smooth curves. The curve is completely contained in the convex hull of its control points, the points may be graphically displayed and used to manipulate the curve intuitively.
The entire curve is contained in the quadrilateral whose corners are the four given points (their convex hull).

In this article, we will investigate  simply graph curves, and filled curves, that you can create in your PDF document.

Follow the steps below:

1. Create [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Document) instance.

1. Create [Drawing object](https://apireference.aspose.com/pdf/java/com.aspose.pdf.drawing/package-frame) with certain dimensions.

1. Set [Border](https://apireference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph#setBorder-com.aspose.pdf.BorderInfo-) for Drawing object.

1. Add [Graph](https://apireference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph) object to paragraphs collection of page.

1. Save your PDF file

```java
    public static void ExampleCurve() {
        // Create Document instance
        Document pdfDocument = new Document();
        // Add page to pages collection of PDF file
        Page page = pdfDocument.getPages().add();

        // Create Drawing object with certain dimensions
        Graph graph = new Graph(400, 200);
        // Set border for Drawing object
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Curve curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120});

        curve1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().add(curve1);

        // Add Graph object to paragraphs collection of page
        page.getParagraphs().add(graph);

        // Save PDF file
        pdfDocument.save(_dataDir + "DrawingCurve1_out.pdf");
    }
```

The following picture shows the result executed with our code snippet:

![Drawing Curve](drawing_curve.png)

## Create Filled Curve Object

This example shows how to add a Curve object that is filled with color.

```java
    public static void ExampleFilledCurve() {
        // Create Document instance
        Document pdfDocument = new Document();
        // Add page to pages collection of PDF file
        Page page = pdfDocument.getPages().add();

        // Create Drawing object with certain dimensions
        Graph graph = new Graph(400, 200);
        // Set border for Drawing object
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Curve curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120});
        curve1.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().add(curve1);

        // Add Graph object to paragraphs collection of page
        page.getParagraphs().add(graph);

        // Save PDF file
        pdfDocument.save(_dataDir + "DrawingCurve2_out.pdf");
    }
```

Look at the result of adding a filled Curve:

![Filled Curve](filled_curve.png)
