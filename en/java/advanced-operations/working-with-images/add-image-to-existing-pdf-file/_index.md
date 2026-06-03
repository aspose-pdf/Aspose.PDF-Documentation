---
title: Add Image to PDF using Java
linktitle: Add Image
type: docs
weight: 10
url: /java/add-image-to-existing-pdf-file/
description: Learn how to add images to existing PDF files in Java.
lastmod: "2026-05-27"
TechArticle: true
AlternativeHeadline: Add images to existing PDF files with Java
Abstract: This article shows how to add images to PDF documents using Aspose.PDF for Java. It covers placing an image at fixed coordinates, adding images through low-level page operators, setting alternative text for accessibility, and embedding image data with Flate compression.
---
Aspose.PDF for Java supports both high-level image placement and low-level operator-based drawing.

## Add an image at a fixed rectangle

1. Open or create the PDF document used in this example.
2. Configure the Aspose.PDF objects needed to add an image at a fixed rectangle.
3. Save the result to apply the change.

```java
public static void addImage(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.addImage(imageFile.toString(), new Rectangle(20, 730, 120, 830, true));
        document.save(outputFile.toString());
    }
}
```

## Add an image with page operators

`addImageUsingOperators` adds the image to the page resource collection, calculates a target rectangle from the image size, applies a transformation matrix, and draws the image with `Do`.

## Set alternative text for an image

1. Load the PDF document or object that will be updated.
2. Apply the settings shown in the example to set alternative text for an image.
3. Save the document if the change should persist.

```java
public static void addImageSetAlternativeTextForImage(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.setPageSize(842, 595);

        page.addImage(imageFile.toString(), new Rectangle(0, 0, 842, 595, true));

        XImage xImage = page.getResources().getImages().get_Item(1);
        xImage.trySetAlternativeText("Alternative text for image", page);
        document.save(outputFile.toString());
    }
}
```