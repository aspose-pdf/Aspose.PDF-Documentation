---
title: Crop PDF Pages in Java
linktitle: Cropping PDF Pages
type: docs
weight: 70
url: /java/crop-pages/
description: Learn how to crop PDF pages and adjust crop, trim, bleed, and media boxes in Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Crop pages and adjust page boxes in PDF files with Java
Abstract: This article explains how to crop PDF pages using Aspose.PDF for Java. It covers assigning a new crop rectangle to the crop, trim, art, and bleed boxes, and cropping a page automatically based on detected image content.
---
Aspose.PDF for Java lets you crop pages either by explicit box coordinates or based on detected content.

## Crop a page by setting page boxes

Use this example when you need to apply the same crop area to the main page boxes.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Create the new crop [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/).
1. Apply the rectangle to the crop-related page boxes and save the document.

```java
public static void cropPage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Rectangle newBox = new Rectangle(200, 220, 2170, 1520, true);
        document.getPages().get_Item(1).setCropBox(newBox);
        document.getPages().get_Item(1).setTrimBox(newBox);
        document.getPages().get_Item(1).setArtBox(newBox);
        document.getPages().get_Item(1).setBleedBox(newBox);
        document.save(outputFile.toString());
    }
}
```

## Crop a page by detected content

Use this example when the crop area should be derived from the first detected image on the page.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Use [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) to detect image placements.
1. Set the crop box to the image rectangle if one is found, then save the document.

```java
public static void cropPageByContent(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);
        if (absorber.getImagePlacements().size() > 0) {
            document.getPages().get_Item(1).setCropBox(absorber.getImagePlacements().get_Item(1).getRectangle());
        } else {
            System.out.println("No images found on the first page");
        }
        document.save(outputFile.toString());
    }
}
```
