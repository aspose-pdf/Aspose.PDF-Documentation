---
title: Add Arc Object to PDF file
linktitle: Add Arc
type: docs
weight: 10
url: /java/add-arc/
description: This article explains how to create a arc object to your PDF using Aspose.PDF for Java.
lastmod: "2025-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to add Arc objects to PDF documents
Abstract: The article provides a guide on how to add arc objects to PDF documents using Aspose.PDF for Java. It details the steps required to create and manipulate graphical elements within a PDF. The process involves creating a `Document` instance, initializing a `Drawing` object with specified dimensions, and setting a border using the `Border` class. A `Graph` object is then added to the PDF's page paragraphs. The article presents a code snippet demonstrating the creation of multiple arc objects with different colors and angles. Additionally, it covers how to create a filled arc object, showing the process of filling an arc with color and adding a line to the drawing. The final PDF file is saved with these graphical modifications. An accompanying image illustrates the result of a filled arc.
SoftwareApplication: java
---

## Add Arc object

Aspose.PDF for Java supports the feature to add graph objects (for example graph, line, rectangle etc.) to PDF documents. It also offers the feature to fill arc object with a certain color.

Follow the steps below:

1. Create [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) instance

1. Create [Drawing object](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/package-frame) with certain dimensions

1. Set [Border](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph#setBorder-com.aspose.pdf.BorderInfo-) for Drawing object

1. Add [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph) object to paragraphs collection of page

1. Save our PDF file

The following code snippet shows how to add a [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Arc) object.

```java
    public static void ExampleArc() {
        // Create Document instance
        Document pdfDocument = new Document();
        // Add page to pages collection of PDF file
        Page page = pdfDocument.getPages().add();

        // Create Drawing object with certain dimensions
        Graph graph = new Graph(400, 400);
        // Set border for Drawing object
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Arc arc1 = new Arc(100, 100, 95, 0, 90);
        arc1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().add(arc1);

        Arc arc2 = new Arc(100, 100, 90, 70, 180);
        arc2.getGraphInfo().setColor(Color.getDarkBlue());
        graph.getShapes().add(arc2);

        Arc arc3 = new Arc(100, 100, 85, 120, 210);
        arc3.getGraphInfo().setColor(Color.getRed());
        graph.getShapes().add(arc3);

        // Add Graph object to paragraphs collection of page
        page.getParagraphs().add(graph);

        // Save PDF file
        pdfDocument.save(_dataDir + "DrawingArc_out.pdf");

    }
```

## Create Filled Arc Object

Next example shows how to add a Arc object that is filled with color and certain dimensions.

```java
    public static void ExampleFilledArc() {
        // Create Document instance
        Document pdfDocument = new Document();
        // Add page to pages collection of PDF file
        Page page = pdfDocument.getPages().add();

        // Create Drawing object with certain dimensions
        Graph graph = new Graph(400, 400);
        // Set border for Drawing object
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Arc arc = new Arc(100, 100, 95, 0, 90);
        arc.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().add(arc);

        Line line = new Line(new float[] { 195, 100, 100, 100, 100, 195 });
        line.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().add(line);

        // Add Graph object to paragraphs collection of page
        page.getParagraphs().add(graph);

        // Save PDF file
        pdfDocument.save(_dataDir + "DrawingArc_out.pdf");

    }
```

Let's see the result of adding a filled Arс:

![Filled Arc](filled_arc.png)
