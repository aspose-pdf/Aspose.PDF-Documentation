---
title: Add Image Stamps to PDF in Java
linktitle: Image stamps in PDF File
type: docs
weight: 10
url: /java/image-stamps-in-pdf-page/
description: Learn how to add image stamps to PDF pages in Java.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add image stamps and image backgrounds to PDF pages with Java
Abstract: This article explains how to add image stamps to PDF files using Aspose.PDF for Java. It covers image stamps with positioning, rotation, opacity, and quality control, and using an image as the background of a floating box.
---
## Add an image stamp

```java
public static void addImageStamp(Path inputFile, Path imageFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImageStamp imageStamp = new ImageStamp(imageFile.toString());
        imageStamp.setBackground(true);
        imageStamp.setXIndent(100);
        imageStamp.setYIndent(100);
        imageStamp.setHeight(300);
        imageStamp.setWidth(300);
        imageStamp.setRotate(Rotation.on270);
        imageStamp.setOpacity(0.5);

        document.getPages().get_Item(1).addStamp(imageStamp);
        document.save(outputFile.toString());
    }
}
```

## Control image stamp quality

`addImageStampWithQualityControl` sets `imageStamp.setQuality(10)` before adding the stamp.

## Use an image as a floating box background

`addImageAsBackgroundInFloatingBox` creates a `FloatingBox`, adds text to it, then assigns an `Image` as the background image.
