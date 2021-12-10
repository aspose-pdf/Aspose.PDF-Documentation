---
title: Add Ellipse Object to PDF file
linktitle: Add Ellipse
type: docs
weight: 60
url: /java/add-ellipse/
description: This article explains how to create a Ellipse object to your PDF using Aspose.PDF for Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Add Ellipse object

Aspose.PDF for Java supports to add [Ellipse](https://apireference.aspose.com/pdf/java/com.aspose.pdf.drawing/Ellipse) objects to PDF documents. It also offers the feature to fill ellipse  object with a certain color.

```java
public static void ExampleEllipse() {
        // Create Document instance
        Document pdfDocument = new Document();
        // Add page to pages collection of PDF file
        Page page = pdfDocument.getPages().add();

        // Create Drawing object with certain dimensions
        Graph graph = new Graph(400, 400);
        // Set border for Drawing object
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Ellipse ellipse1 = new Ellipse(150, 100, 120, 60);
        ellipse1.getGraphInfo().setColor(Color.getGreenYellow());
        ellipse1.setText(new TextFragment("Ellipse"));
        graph.getShapes().add(ellipse1);

        Ellipse ellipse2 = new Ellipse(50, 50, 18, 300);
        ellipse2.getGraphInfo().setColor(Color.getDarkRed());

        graph.getShapes().add(ellipse2);

        // Add Graph object to paragraphs collection of page
        page.getParagraphs().add(graph);

        // Save PDF file
        pdfDocument.save(_dataDir + "DrawingEllipse_out.pdf");
    }
```

![Add Ellipse](ellipse.png)

## Create Filled Ellipse Object

The following code snippet shows how to add a [Ellipse](https://apireference.aspose.com/pdf/java/com.aspose.pdf.drawing/Ellipse) object that is filled with color.

```java
    public static void ExampleFilledEllipse() {
        // Create Document instance
        Document pdfDocument = new Document();
        // Add page to pages collection of PDF file
        Page page = pdfDocument.getPages().add();

        // Create Drawing object with certain dimensions
        Graph graph = new Graph(400, 400);
        // Set border for Drawing object
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Ellipse ellipse1 = new Ellipse(100, 100, 120, 180);
        ellipse1.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().add(ellipse1);

        Ellipse ellipse2 = new Ellipse(200, 150, 180, 120);
        ellipse2.getGraphInfo().setFillColor(Color.getDarkRed());
        graph.getShapes().add(ellipse2);

        // Add Graph object to paragraphs collection of page
        page.getParagraphs().add(graph);

        // Save PDF file
        pdfDocument.save(_dataDir + "DrawingEllipse_out.pdf");

    }
```

![Filled Ellipse](fill_ellipse.png)

## Add Text inside the Ellipse

Aspose.PDF for Java supports to add text inside the Graph Object. Text property of Graph Object provides option to set text of the Graph Object. The following code snippet shows how to add text inside a Rectangle object.

```java

public static void ExampleEllipseWithText() {
        // Create Document instance
        Document pdfDocument = new Document();
        // Add page to pages collection of PDF file
        Page page = pdfDocument.getPages().add();

        // Create Drawing object with certain dimensions
        Graph graph = new Graph(400, 400);
        // Set border for Drawing object
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        TextFragment textFragment = new TextFragment("Ellipse");
        textFragment.getTextState().setFont(FontRepository.findFont("Helvetica"));
        textFragment.getTextState().setFontSize(24);

        Ellipse ellipse1 = new Ellipse(100, 100, 120, 180);
        ellipse1.getGraphInfo().setFillColor(Color.getGreenYellow());
        ellipse1.setText(textFragment);
        graph.getShapes().add(ellipse1);
        

        Ellipse ellipse2 = new Ellipse(200, 150, 180, 120);
        ellipse2.getGraphInfo().setFillColor(Color.getDarkRed());        
        ellipse2.setText(textFragment);
        graph.getShapes().add(ellipse2);

        // Add Graph object to paragraphs collection of page
        page.getParagraphs().add(graph);

        // Save PDF file
        pdfDocument.save(_dataDir + "DrawingEllipseText_out.pdf");

    }
 ```

![Text inside Ellipse](text_ellipse.png)
