---
title: Work with Vector Graphics in Java
linktitle: Working with Vector Graphics
type: docs
weight: 100
url: /java/working-with-vector-graphics/
description: Learn how to extract, move, remove, copy, and export vector graphics in PDF documents using Java.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Use GraphicsAbsorber to inspect and manipulate PDF vector graphics in Java
Abstract: This article explains how to work with vector graphics in Aspose.PDF for Java using the GraphicsAbsorber class. Learn how to inspect vector elements on a page, move or remove them, copy graphics between pages, and export vector content to SVG.
---
Aspose.PDF for Java exposes vector content through `GraphicsAbsorber` and `GraphicElement` objects. This lets you inspect low-level vector elements on a page and then update, remove, copy, or export them.

## Inspect vector graphics on a page

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

## Remove or copy vector graphics

The example set also includes:

- `removeGraphicsMethod1` to remove matching elements individually with `element.remove()`
- `removeGraphicsMethod2` to collect matching elements and delete them from the page in one step
- `addToAnotherPageMethod1` to add each element to another page one by one
- `addToAnotherPageMethod2` to copy the full element collection to another page

## Export vector content to SVG

The related parsing examples also show how to export vector graphics:

- `saveVectorGraphicsToSvg` saves page vector graphics directly to an SVG file.
- `extractSubpathsToSvgs` saves each `GraphicElement` to its own SVG.
- `extractSingleVectorElement` exports a selected element or nested XForm element to SVG.
