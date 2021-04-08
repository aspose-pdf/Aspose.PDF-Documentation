---
title: Add Rectangle Object to PDF file
linktitle: Add Rectangle
type: docs
weight: 50
url: /java/add-rectangle/
description: This article explains how to create a Rectangle object to your PDF using Aspose.PDF for Java.
lastmod: "2021-04-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
Aspose.PDF for Java supports the feature to add graph objects (for example graph, line, rectangle etc.) to PDF documents. You also get the leverage to add [Rectangle](https://apireference.aspose.com/pdf/java/com.aspose.pdf.drawing/Rectangle) object where you also offers the feature to fill rectangle object with a certain color, control Z-Order, add gradiant color fill and etc.

First, let's look at the possibility of creating a Rectangle object.

Follow the steps below:

1. Create a new PDF Document

1. Add page to pages collection of PDF file

1. Add text fragment to paragraphs collection of page instance

1. Create Graph instance

1. Set border for Drawing object

1. Create Rectangle instance

1. Add rectangle object to shapes collection of Graph object

1. Add graph object to paragraphs collection of page instance

1. Add text fragment to paragraphs collection of page instance

1. And save your PDF file

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.BorderInfo;
import com.aspose.pdf.BorderSide;
import com.aspose.pdf.Color;
import com.aspose.pdf.Document;
import com.aspose.pdf.Page;
import com.aspose.pdf.Point;
import com.aspose.pdf.TextFragment;
import com.aspose.pdf.drawing.*;

public class WorkingWithGraphs {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    public static void ExampleRectangle() {

        // Create a new PDF document
        Document pdfDocument = new Document();

        // Add page to pages collection of PDF file
        Page page = pdfDocument.getPages().add();

        // Add text fragment to paragraphs collection of page instance
        page.getParagraphs().add(new TextFragment("Text before Graph object"));

        // Create Graph instance
        Graph graph = new Graph(400, 200);

        // Set border for Drawing object
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getRed());
        graph.setBorder(borderInfo);

        // Create Rectangle instance
        Rectangle rect = new Rectangle(10, 10, 380, 180);

        // Add rectangle object to shapes collection of Graph object
        graph.getShapes().add(rect);

        // Add graph object to paragraphs collection of page instance
        page.getParagraphs().add(graph);

        // Add text fragment to paragraphs collection of page instance
        page.getParagraphs().add(new TextFragment("Text after Graph object"));

        // Save PDF file
        pdfDocument.save(_dataDir + "CreateRectangle_out.pdf");
    }
```