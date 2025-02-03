---
title: Add Circle Object to PDF file
linktitle: Add Circle
type: docs
weight: 20
url: /java/add-circle/
description: This article explains how to create a circle object to your PDF using Aspose.PDF for Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Guide on how to add Circle objects to a PDF document using Aspose.PDF for Java
Abstract: This article provides a guide on how to add Circle objects to a PDF document using Aspose.PDF for Java. It explains the process of creating both regular and filled Circle objects within a PDF. The guide includes step-by-step instructions, starting with creating a `Document` instance and adding pages to it. A `Graph` object is then created with specified dimensions, and a border is set using the `BorderInfo` class. The article details how to add a `Circle` to the `Graph` with a specific color and, in the case of a filled circle, how to set both the border and fill colors. Code snippets demonstrate the implementation process, and visual results are shown through example images of the drawn and filled circles.
SoftwareApplication: java
---

## Add Circle object

Like bar graphs, circle graphs can be used to display data in a number of separate categories. Unlike bar graphs, however, circle graphs can be used only when you have data for all the categories that make up the whole. So let's take a look at adding a [Circle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Circle) object with Aspose.PDF for Java.

Follow the steps below:

1. Create [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) instance

1. Create [Drawing object](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/package-frame) with certain dimensions

1. Set [Border](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph#setBorder-com.aspose.pdf.BorderInfo-) for Drawing object

1. Add [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph) object to paragraphs collection of page

1. Save our PDF file

```java
public static void ExampleCircle() {
        // Create Document instance
        Document pdfDocument = new Document();
        // Add page to pages collection of PDF file
        Page page = pdfDocument.getPages().add();

        // Create Drawing object with certain dimensions
        Graph graph = new Graph(400, 200);
        // Set border for Drawing object
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Circle circle = new Circle(100,100,40);

        circle.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().add(circle);

        // Add Graph object to paragraphs collection of page
        page.getParagraphs().add(graph);

        // Save PDF file
        pdfDocument.save(_dataDir + "DrawingCircle1_out.pdf");
    }
```

Our drawn circle will look like this:

![Drawing Circle](drawing_circle.png)

## Create Filled Circle Object

This example shows how to add a Circle object that is filled with color.

```java

    public static void ExampleFilledCircle() {
        // Create Document instance
        Document pdfDocument = new Document();
        // Add page to pages collection of PDF file
        Page page = pdfDocument.getPages().add();

        // Create Drawing object with certain dimensions
        Graph graph = new Graph(400, 200);
        // Set border for Drawing object
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Circle circle = new Circle(100,100,40);
        circle.getGraphInfo().setColor(Color.getGreenYellow());       
        circle.getGraphInfo().setFillColor(Color.getGreenYellow());

        graph.getShapes().add(circle);

        // Add Graph object to paragraphs collection of page
        page.getParagraphs().add(graph);

        // Save PDF file
        pdfDocument.save(_dataDir + "DrawingCircle2_out.pdf");
    }
```

Let's see the result of adding a filled Circle:

![Filled Circle](filled_circle.png)
