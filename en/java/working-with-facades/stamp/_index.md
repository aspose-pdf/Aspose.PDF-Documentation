---
title: Stamp Class
type: docs
weight: 150
url: /java/stamp-class/
description: Learn how to work with the Stamp class in Java to add image, PDF, and text-based stamps to PDF documents.
lastmod: "2026-06-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add image, PDF, and text stamps to PDF documents in Java
Abstract: This section explains how to use the Stamp class together with PdfFileStamp in Aspose.PDF for Java to add reusable stamp content to PDF documents. The current Java examples cover image stamps, PDF-page stamps, text stamps with a custom TextState, page-specific stamps, and background image stamps with opacity, size, and rotation settings.
---
The Java `StampExamples` class demonstrates the main stamp-building workflows available through the Facades API.

## Add an image stamp

Use this workflow when an image file should be placed on the PDF as a stamp.

### Steps

1. Create a `PdfFileStamp` instance and bind the source PDF.
2. Create a `Stamp` object and bind it to the image file.
3. Set the stamp identifier and placement origin.
4. Add the stamp to the document.
5. Save the result and close the facade object.

### Java example

```java
public static void addImageStamp(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        stamp.setStampId(1);
        stamp.setOrigin(36, 520);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## Add a PDF page as a stamp

Use this workflow when content from another PDF page should be reused as stamp content.

### Steps

1. Create a `PdfFileStamp` instance and bind the target PDF.
2. Create a `Stamp` object.
3. Bind the stamp to a specific page from another PDF file.
4. Set the target page number and origin for placement.
5. Add the stamp, save the output, and close the facade object.

### Java example

```java
public static void addPdfPageAsStamp(Path inputFile, Path stampPdf, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindPdf(stampPdf.toString(), 1);
        stamp.setPageNumber(1);
        stamp.setOrigin(36, 250);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## Add a text stamp with TextState

Use this workflow when the stamp should contain styled text rather than an image.

### Steps

1. Create a `PdfFileStamp` instance and bind the source PDF.
2. Create a `Stamp` object.
3. Bind a `FormattedText` logo and a custom `TextState` to the stamp.
4. Set the stamp origin and rotation.
5. Add the stamp, save the output, and close the facade object.

### Java example

```java
public static void addTextStampWithTextState(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindLogo(createTextLogo("Approved by signing workflow"));
        stamp.bindTextState(createTextState());
        stamp.setOrigin(36, 700);
        stamp.setRotation(15.0f);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## Add a stamp to specific pages

Use this workflow when the stamp should appear only on selected pages instead of the whole document.

### Steps

1. Create a `PdfFileStamp` instance and bind the source PDF.
2. Create a `Stamp` object and bind it to an image file.
3. Set the target page list, origin, and image size.
4. Add the stamp to the document.
5. Save the result and close the facade object.

### Java example

```java
public static void addStampToSpecificPages(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        stamp.setPages(new int[] {1});
        stamp.setOrigin(400, 40);
        stamp.setImageSize(120, 60);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## Add a background image stamp

Use this workflow when the stamp should appear behind page content with controlled opacity and rotation.

### Steps

1. Create a `PdfFileStamp` instance and bind the source PDF.
2. Create a `Stamp` object and bind it to the image file.
3. Mark the stamp as background content.
4. Configure opacity, quality, rotation, size, and origin.
5. Add the stamp, save the output, and close the facade object.

### Java example

```java
public static void addBackgroundImageStamp(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        stamp.setBackground(true);
        stamp.setOpacity(0.35f);
        stamp.setQuality(90);
        stamp.setRotation(45.0f);
        stamp.setImageSize(160, 80);
        stamp.setOrigin(200, 300);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```
