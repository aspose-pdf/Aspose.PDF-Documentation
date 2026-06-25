---
title: Convert Image Formats to PDF in Java
linktitle: Convert Images to PDF
type: docs
weight: 60
url: /java/convert-images-format-to-pdf/
lastmod: "2026-06-16"
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

1. Create an empty [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) to hold the output PDF.
1. Add a [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) and place the BMP with `page.addImage(...)`.
1. Define the target image rectangle with [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) so the raster content fills the PDF page area.
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

1. Open the CGM source by passing the file path and [`CgmLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/cgmloadoptions/) into the [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) constructor.
1. Let Aspose.PDF interpret the CGM graphics stream during document loading.
1. Save the converted PDF to the target output path.

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

1. Create an empty [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) for the PDF output.
1. Create an [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) object, set its [`ImageFileType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagefiletype/) to `Dicom`, and assign the source file path.
1. Add a [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) and append the DICOM image to the page paragraphs collection.
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

1. Create an empty [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) and open the EMF source as a binary stream.
1. Add a [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) and clear its margins so the EMF artwork can occupy the full page area.
1. Create an [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/), bind the EMF stream to it, and add it to the page paragraphs collection.
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

1. Load the EMF source with Aspose.Imaging and render it to an in-memory PNG stream before PDF placement.
1. Create an empty [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) and add a [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Create an [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) from the intermediate byte stream and add it to the page.
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

1. Create an empty [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) for the PDF output.
1. Add a [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) and place the GIF with `page.addImage(...)`.
1. Define the placement bounds with [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) so the image fills the page area.
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

1. Create an empty [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) for the output PDF.
1. Add a [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) and insert the JPEG image with `page.addImage(...)`.
1. Use [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) to control how the raster image is mapped to page coordinates.
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

1. Create an empty [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) for the conversion output.
1. Add a [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) and place the PNG image on it with `page.addImage(...)`.
1. Use [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) to size the image against the page canvas.
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

1. Open the SVG source by passing the file path and [`SvgLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgloadoptions/) into the [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) constructor.
1. Let Aspose.PDF parse the SVG markup and create the corresponding PDF graphics model during loading.
1. Save the PDF output to the target file path.

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

1. Create an empty [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) for the PDF output.
1. Add a [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) and place the TIFF image with `page.addImage(...)`.
1. Define the placement area with [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) so the TIFF content is mapped to page coordinates.
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

1. Open the CDR source by passing the file path and `CdrLoadOptions` into the [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) constructor.
1. Let Aspose.PDF load the CorelDRAW content into the PDF document model.
1. Save the converted PDF file to the requested output path.

```java
public static void convertCdrToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new CdrLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
