---
title: Add Rectangle Shapes to PDF in Java
linktitle: Add Rectangle
type: docs
weight: 50
url: /java/add-rectangle/
description: Learn how to draw and fill rectangle shapes in PDF files in Java.
lastmod: "2026-06-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Draw rectangle shapes in PDF files using Java
Abstract: This article shows how to add rectangle shapes to PDF documents using Aspose.PDF for Java. It covers outlined rectangles, solid fills, gradient fills, alpha transparency, and z-order control for overlapping shapes.
---
## Add a rectangle outline

1. Create a new PDF document.
1. Add a page to the document.
1. Create a Graph container and add it to the page.
1. Create the rectangle shape and configure its geometry.
1. Add the shape to the Graph container.
1. Save the output PDF document.

```java
public static void addRectangle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 300.0);
        page.getParagraphs().add(graph);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getRed()));

        Rectangle rectangle = new Rectangle(20, 20, 350, 250);
        graph.getShapes().addItem(rectangle);

        document.save(outputFile.toString());
    }
}
```

## Fill a rectangle with solid or gradient color

The rectangle examples include:

- `createRectangleFilled` for a solid fill with `Color.getRed()`
- `addDrawingWithGradientFill` for a `GradientAxialShading` fill

## Use alpha transparency

`createRectangleWithAlphaColorChannel` applies translucent colors with `Color.fromArgb(...)` so overlapping rectangles remain visible.

## Control z-order of rectangles

1. Create a new PDF document.
1. Add a page to the document.
1. Set the page size required by the example.
1. Save the output PDF document.

```java
public static void controlZOrderOfRectangle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.setPageSize(375, 300);
        page.getPageInfo().getMargin().setLeft(0);
        page.getPageInfo().getMargin().setTop(0);

        addRectangleToPage(page, 50, 40, 60, 40, Color.getRed(), 2);
        addRectangleToPage(page, 20, 20, 30, 30, Color.getBlue(), 1);
        addRectangleToPage(page, 40, 40, 60, 30, Color.getGreen(), 0);

        document.save(outputFile.toString());
    }
}
```
