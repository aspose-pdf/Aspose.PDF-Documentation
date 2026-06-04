---
title: Convert Image Formats to PDF in Java
linktitle: Convert Images to PDF
type: docs
weight: 60
url: /java/convert-images-format-to-pdf/
lastmod: "2026-06-04"
description: Learn how to convert BMP, CGM, DICOM, PNG, TIFF, EMF, SVG, CDR, and other image formats to PDF in Java with Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: How to Convert Images to PDF in Java
Abstract: This article explains how to convert multiple image formats to PDF using Aspose.PDF for Java. It covers direct image placement into a new PDF page as well as file-type-specific load options for CGM, SVG, and CDR inputs.
---
Aspose.PDF for Java supports several approaches for image-to-PDF conversion depending on the source format.

## Convert bitmap-style images to PDF

BMP, GIF, JPEG, PNG, and TIFF examples all follow the same core pattern: create a new `Document`, add a page, place the image on the page, and save the result.

1. Create a new PDF document.
1. Add a page to the document.
1. Place the source image on the page in the target rectangle.
1. Save the output PDF document.

```java
public static void convertBmpToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
}
```

## Convert SVG, CGM, or CDR to PDF

1. Open the source SVG file with SVG load options.
1. Create the PDF document from the source file.
1. Save the output PDF document.

```java
public static void convertSvgToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new SvgLoadOptions())) {
        document.save(outputFile.toString());
    }
}
```

1. Open the source CGM file with CGM load options.
1. Create the PDF document from the source file.
1. Save the output PDF document.

```java
public static void convertCgmToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new CgmLoadOptions())) {
        document.save(outputFile.toString());
    }
}
```

## Convert DICOM to PDF

1. Create a new PDF document.
1. Create an image object and set its file type to DICOM.
1. Set the source DICOM file for the image object.
1. Add a page to the document and append the image to the page paragraphs.
1. Save the output PDF document.

```java
public static void convertDicomToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        Image image = new Image();
        image.setFileType(ImageFileType.Dicom);
        image.setFile(inputFile.toString());

        try (Page page = document.getPages().add()) {
            page.getParagraphs().add(image);
        }

        document.save(outputFile.toString());
    }
}
```
