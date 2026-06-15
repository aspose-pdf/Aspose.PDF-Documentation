---
title: Convert Image Formats to PDF in Java
linktitle: Convert Images to PDF
type: docs
weight: 60
url: /java/convert-images-format-to-pdf/
lastmod: "2026-06-09"
description: Learn how to convert BMP, CGM, DICOM, PNG, TIFF, EMF, SVG, CDR, and other image formats to PDF in Java with Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: How to Convert Images to PDF in Java
Abstract: This article explains how to convert multiple image formats to PDF using Aspose.PDF for Java. It covers direct image placement into a new PDF page as well as file-type-specific load options for CGM, SVG, and CDR inputs.
---
Aspose.PDF for Java can convert many raster and vector image formats into PDF documents.

## Convert BMP to PDF

Use this example when a BMP image should be placed into a PDF document.

1. Open the BMP source image.
1. Create a PDF document and add the image to a page.
1. Save the output PDF file.

```java
public static void convertBmpToPdf(Path inputFile, Path outputFile) {
        try (Document document = new Document()) {
            try (Page page = document.getPages().add()) {
                page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
            }
            document.save(outputFile.toString());
        }
        System.out.println(inputFile + " converted into " + outputFile);
    }
```

## Convert CGM to PDF

Use this example when a CGM graphics file should be converted into PDF.

1. Open the CGM input file.
1. Create the PDF document from the CGM source.
1. Save the converted PDF.

```java
public static void convertCgmToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new CgmLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert DICOM to PDF

Use this example when a medical DICOM image should be wrapped into a PDF document.

1. Open the DICOM input file.
1. Create a PDF document and place the DICOM image on a page.
1. Save the result as PDF.

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
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert EMF to PDF with direct document loading

Use this example when an EMF file should be converted to PDF through the primary EMF load path.

1. Open the EMF source with the required load options.
1. Create the PDF document from the EMF input.
1. Save the output PDF file.

```java
public static void convertEmfToPdf01(Path inputFile, Path outputFile) throws IOException {
    try (Document document = new Document();
         FileInputStream imageStream = new FileInputStream(inputFile.toFile())) {
        try (Page page = document.getPages().add()) {
            page.getPageInfo().getMargin().setBottom(0);
            page.getPageInfo().getMargin().setTop(0);
            page.getPageInfo().getMargin().setLeft(0);
            page.getPageInfo().getMargin().setRight(0);

            Image image = new Image();
            image.setFileType(ImageFileType.Unknown);
            image.setImageStream(imageStream);
            page.getParagraphs().add(image);
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert EMF to PDF with an alternative workflow

Use this example when the EMF content should be converted using an alternative setup or page composition flow.

1. Open the EMF source.
1. Configure the destination PDF page and place the EMF content.
1. Save the converted PDF.

```java
public static void convertEmfToPdf02(Path inputFile, Path outputFile) throws IOException {
    try (Document document = new Document();
         com.aspose.imaging.Image emfImage = com.aspose.imaging.Image.load(inputFile.toString());
         ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream()) {
        emfImage.save(byteArrayOutputStream, new PngOptions());

        try (Page page = document.getPages().add()) {
            Image image = new Image();
            image.setImageStream(new ByteArrayInputStream(byteArrayOutputStream.toByteArray()));
            page.getParagraphs().add(image);
        }

        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert GIF to PDF

Use this example when a GIF image should be added to a PDF page.

1. Open the GIF source image.
1. Create a PDF document and insert the image.
1. Save the output PDF.

```java
public static void convertGifToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert JPEG to PDF

Use this example when a JPEG image should be converted into a one-page PDF.

1. Open the JPEG source image.
1. Create a PDF document and add the image to a page.
1. Save the generated PDF file.

```java
public static void convertJpegToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert PNG to PDF

Use this example when a PNG image should be wrapped into a PDF document.

1. Open the PNG input image.
1. Create the PDF page and add the PNG content.
1. Save the output file.

```java
public static void convertPngToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert SVG to PDF

Use this example when SVG artwork should be rendered inside a PDF document.

1. Open the SVG source file.
1. Convert the SVG content into a PDF document.
1. Save the PDF output.

```java
public static void convertSvgToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new SvgLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert TIFF to PDF

Use this example when a TIFF image should be converted into PDF.

1. Open the TIFF source image.
1. Create the PDF document and add the TIFF content.
1. Save the result as PDF.

```java
public static void convertTiffToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert CDR to PDF

Use this example when a CorelDRAW CDR file should be converted into PDF.

1. Open the CDR input file.
1. Create the PDF document from the CDR source.
1. Save the converted PDF file.

```java
public static void convertCdrToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new CdrLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
