---
title: Work with Vector Graphics in Java
linktitle: Working with Vector Graphics
type: docs
weight: 100
url: /java/working-with-vector-graphics/
description: Learn how to extract, move, remove, copy, and export vector graphics in PDF documents using Java.
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Use GraphicsAbsorber to inspect and manipulate PDF vector graphics in Java
Abstract: This article explains how to work with vector graphics in Aspose.PDF for Java using the GraphicsAbsorber class. Learn how to inspect vector elements on a page, move or remove them, copy graphics between pages, and export vector content to SVG.
---
Aspose.PDF for Java exposes vector content through `GraphicsAbsorber` and `GraphicElement` objects. This lets you inspect low-level vector elements on a page and then update, remove, copy, or export them.

## Inspect vector graphics on a page

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Access the target [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/).
1. Create the [GraphicsAbsorber](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.vector/graphicsabsorber/) and visit the page.
1. Inspect the returned [GraphicElement](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.vector/graphicelement/) objects and read their properties.

```java
public static void usingGraphicsAbsorber(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page = document.getPages().get_Item(1);
            graphicsAbsorber.visit(page);
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                System.out.println("Page Number: " + element.getSourcePage().getNumber());
                System.out.println("Position: (" + element.getPosition().getX() + ", "
                        + element.getPosition().getY() + ")");
                System.out.println("Number of Operators: " + element.getOperators().size());
            }
        } finally {
            graphicsAbsorber.dispose();
        }
    }
}
```

## Move vector graphics

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Access the target [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) and visit it with [GraphicsAbsorber](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.vector/graphicsabsorber/).
1. Update the position of each [GraphicElement](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.vector/graphicelement/) using a new [Point](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/point/).
1. Save the updated PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

```java
public static void moveGraphics(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page = document.getPages().get_Item(1);
            graphicsAbsorber.visit(page);
            graphicsAbsorber.suppressUpdate();
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                Point position = element.getPosition();
                element.setPosition(new Point(position.getX() + 150, position.getY() - 10));
            }
            graphicsAbsorber.resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
}
```
