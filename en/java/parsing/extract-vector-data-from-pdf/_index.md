---
title: Extract Vector Data from a PDF file using Java
linktitle: Extract Vector Data from PDF
type: docs
weight: 80
url: /java/extract-vector-data-from-pdf/
description: Aspose.PDF makes it easy to extract vector data from a PDF file. You can get the vector data, such as position, rectangle bounds, and SVG output.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
## Access vector data from a PDF document

Use `GraphicsAbsorber` to inspect vector graphic elements on a page and write their basic geometry to a text file.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create a [GraphicsAbsorber](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.vector/graphicsabsorber/) and visit the target [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/).
1. Iterate through the extracted [GraphicElement](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.vector/graphicelement/) objects.
1. Build the output text with element geometry and operator counts.
1. Write the extracted vector data to the output file.

```java
public static void extractGraphicsElements(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber absorber = new GraphicsAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        StringBuilder text = new StringBuilder();
        int index = 1;
        for (GraphicElement element : absorber.getElements()) {
            text.append("Element ").append(index)
                    .append(": Rectangle = ").append(element.getRectangle())
                    .append(", Position = ").append(element.getPosition())
                    .append(", Operators = ").append(element.getOperators().size())
                    .append("\n");
            index++;
        }
        Files.writeString(outputFile, text.toString());
    }
}
```

## Save page vector graphics to SVG

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Get the target [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) from the document.
1. Save the page vector graphics to the output SVG file.

```java
public static void saveVectorGraphicsToSvg(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        page.trySaveVectorGraphics(outputFile.toString());
    }
}
```

## Save each extracted element to a separate SVG

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create a [GraphicsAbsorber](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.vector/graphicsabsorber/) and visit the target [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/).
1. Create the output directory for the extracted subpaths.
1. Iterate through the extracted [GraphicElement](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.vector/graphicelement/) objects.
1. Save each element to a separate SVG file.

```java
public static void extractSubpathsToSvgs(Path inputFile, Path outputDir) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber absorber = new GraphicsAbsorber();
        absorber.visit(document.getPages().get_Item(1));
        Path subpathsDir = outputDir.resolve("subpaths");
        Files.createDirectories(subpathsDir);

        int index = 1;
        for (GraphicElement element : absorber.getElements()) {
            element.saveToSvg(subpathsDir.resolve("subpath_" + index + ".svg").toString());
            index++;
        }
    }
}
```

## Combine extracted elements into a single SVG

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create a [GraphicsAbsorber](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.vector/graphicsabsorber/) and visit the target [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/).
1. Create the SVG wrapper content.
1. Iterate through the extracted [GraphicElement](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.vector/graphicelement/) objects and append each SVG fragment.
1. Write the combined SVG output to the target file.

```java
public static void extractListOfElementsToSingleImage(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber absorber = new GraphicsAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        StringBuilder svg = new StringBuilder();
        svg.append("<svg xmlns=\"http://www.w3.org/2000/svg\">\n");
        for (GraphicElement element : absorber.getElements()) {
            svg.append(element.saveToSvg()).append("\n");
        }
        svg.append("</svg>\n");
        Files.writeString(outputFile, svg.toString());
    }
}
```

## Extract a single vector element

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create a [GraphicsAbsorber](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.vector/graphicsabsorber/) and visit the target [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/).
1. Get the target [GraphicElement](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.vector/graphicelement/) from the extracted elements collection.
1. Check whether the element is an [XFormPlacement](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.vector/xformplacement/) and select the nested element when needed.
1. Save the selected vector element to the output SVG file.

```java
public static void extractSingleVectorElement(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        Page page = document.getPages().get_Item(1);
        graphicsAbsorber.visit(page);
        if (graphicsAbsorber.getElements().size() > 1) {
            GraphicElement xformPlacement = graphicsAbsorber.getElements().get_Item(1);
            if (xformPlacement instanceof XFormPlacement) {
                XFormPlacement placement = (XFormPlacement) xformPlacement;
                if (placement.getElements().size() > 2) {
                    placement.getElements().get_Item(2).saveToSvg(outputFile.toString());
                }
            } else {
                xformPlacement.saveToSvg(outputFile.toString());
            }
        }
    }
}
```
