---
title: Add Line Object to PDF file
linktitle: Add Line
type: docs
weight: 40
url: /java/add-line/
description: This article explains how to create a line object to your PDF using Aspose.PDF for Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF for Java supports the feature to add graph objects (for example graph, line, rectangle etc.) to PDF documents. You also get the leverage to add [Line](https://apireference.aspose.com/pdf/java/com.aspose.pdf.drawing/Line) object where you can also specify the dash pattern, color and other formatting for Line element.

Follow the steps below:

1. Create [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Document) instance.

1. Add [Page](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Page) to pages collection of PDF file.

1. Create [Graph](https://apireference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph) instance.

1. Add Graph object to paragraphs collection of page instance.

1. Create [Rectangle](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) instance.

1. Set line width.

1. Add [Rectangle](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) object to shapes collection of Graph object.

1. Save your PDF file.

The following code snippet shows how to add a [Rectangle](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) object that is filled with color.

```java
 public static void ExampleLine() {
        // Create Document instance
        Document pdfDocument = new Document();
        // Add page to pages collection of PDF file
        Page page = pdfDocument.getPages().add();
        // Create Graph instance
        Graph graph = new Graph(100, 400);

        // Add graph object to paragraphs collection of page instance
        page.getParagraphs().add(graph);

        // Create Rectangle instance
        Line line = new Line(new float[] { 100, 100, 200, 100 });
        
        line.getGraphInfo().setLineWidth(5);
        
        // Add rectangle object to shapes collection of Graph object
        graph.getShapes().add(line);

        // Save PDF file
        pdfDocument.save(_dataDir + "LineAdded.pdf");
    }
```

![Add Line](add_line.png)

## How to add Dotted Dashed Line to your PDF document

```java
public static void ExampleDashedLine() {
        // Create Document instance
        Document pdfDocument = new Document();
        // Add page to pages collection of PDF file
        Page page = pdfDocument.getPages().add();

        // Create Drawing object with certain dimensions
        Graph canvas = new Graph(100, 400);
        // Add drawing object to paragraphs collection of page instance
        page.getParagraphs().add(canvas);

        // Create Line object
        Line line = new Line(new float[] { 100, 100, 200, 100 });

        // Set color for Line object
        line.getGraphInfo().setColor(Color.getRed());
        // Specify dash array for line object
        line.getGraphInfo().setDashArray(new int[] { 0, 1, 0 });
        // Set the dash phase for Line instance
        line.getGraphInfo().setDashPhase(1);
        // Add line to shapes collection of drawing object
        canvas.getShapes().add(line);
        // Save PDF document
        pdfDocument.save(_dataDir + "DashLength_out.pdf");
    }
```

Let's check the result:

![Dashed Line](dash_line.png)

## Draw Line Across the Page

We can also use line object to draw a cross starting from Left-Bottom to Right-Upper corner and Left-Top corner to Bottom-Right corner.

Please take a look over following code snippet to accomplish this requirement.

```java
    public static void ExampleLineAcrossPage() {
        // Create Document instance
        Document pdfDocument = new Document();
        // Add page to pages collection of PDF file
        Page page = pdfDocument.getPages().add();
        // Set page margin on all sides as 0

        page.getPageInfo().getMargin().setLeft(0);
        page.getPageInfo().getMargin().setRight(0);
        page.getPageInfo().getMargin().setBottom(0);
        page.getPageInfo().getMargin().setTop(0);

        // Create Graph object with Width and Height equal to page dimensions
        Graph graph = new Graph((float) page.getPageInfo().getWidth(), (float) page.getPageInfo().getHeight());

        // Create first line object starting from Lower-Left to Top-Right corner of page
        Line line = new Line(new float[] { (float) page.getRect().getLLX(), 0, (float) page.getPageInfo().getWidth(),
                (float) page.getRect().getURY() });

        // Add line to shapes collection of Graph object
        graph.getShapes().add(line);
        // Draw line from Top-Left corner of page to Bottom-Right corner of page
        Line line2 = new Line(new float[] { 0, (float) page.getRect().getURY(), (float) page.getPageInfo().getWidth(),
                (float) page.getRect().getLLX() });

        // Add line to shapes collection of Graph object
        graph.getShapes().add(line2);
        // Add Graph object to paragraphs collection of page
        page.getParagraphs().add(graph);

        // Save PDF file
        pdfDocument.save(_dataDir + "DrawingLine_out.pdf");
    }
```

![Drawing Line](draw_line.png)
