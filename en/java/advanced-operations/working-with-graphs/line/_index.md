---
title: Add Line Shapes to PDF in Java
linktitle: Add Line
type: docs
weight: 40
url: /java/add-line/
description: Learn how to draw line shapes and styled lines in PDF files in Java.
lastmod: "2026-06-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Draw line shapes in PDF files using Java
Abstract: This article shows how to add line shapes to PDF documents using Aspose.PDF for Java. It covers creating lines from coordinate arrays, applying dashed styling and color, and drawing lines across the full page area.
---
## Add a dashed line

1. Create a new PDF document.
1. Add a page to the document.
1. Create a Graph container and add it to the page.
1. Create the line shape and configure its coordinates.
1. Add the shape to the Graph container.
1. Save the output PDF document.

```java
public static void addLine(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(100.0, 400.0);
        page.getParagraphs().add(graph);

        Line line = new Line(new float[]{100, 100, 200, 100});
        line.getGraphInfo().setDashArray(new int[]{0, 1, 0});
        line.getGraphInfo().setDashPhase(1);
        graph.getShapes().addItem(line);

        document.save(outputFile.toString());
    }
}
```

## Add a colored dotted or dashed line

`addDottedDashedLine` uses the same coordinates and dash settings, but also applies `Color.getRed()`.

## Draw lines across the page

1. Create a new PDF document.
1. Add a page to the document.
1. Create a Graph container and add it to the page.
1. Create the line shape and configure its coordinates.
1. Add the shape to the Graph container.
1. Save the output PDF document.

```java
public static void drawLineAcrossPage(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getPageInfo().getMargin().setLeft(0);
        page.getPageInfo().getMargin().setRight(0);
        page.getPageInfo().getMargin().setBottom(0);
        page.getPageInfo().getMargin().setTop(0);

        Graph graph = new Graph(page.getPageInfo().getWidth(), page.getPageInfo().getHeight());
        Line line = new Line(new float[]{
                (float) page.getRect().getLLX(),
                0,
                (float) page.getPageInfo().getWidth(),
                (float) page.getRect().getURY()
        });
        graph.getShapes().addItem(line);
        page.getParagraphs().add(graph);

        document.save(outputFile.toString());
    }
}
```
