---
title: Convert PDF to PowerPoint in Java
linktitle: Convert PDF to PowerPoint
type: docs
weight: 30
url: /java/convert-pdf-to-powerpoint/
description: Learn how to convert PDF files to PowerPoint in Java with Aspose.PDF, including editable PPTX slides, image-based slides, and custom image resolution.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to Convert PDF to PowerPoint in Java
Abstract: This article explains how to convert PDF files into PowerPoint presentations using Aspose.PDF for Java. It covers standard PPTX conversion, slide-as-image output, and image-resolution control through `PptxSaveOptions`.
---
Aspose.PDF for Java supports exporting PDF pages into editable PowerPoint presentations with slide rendering options. Use [`PptxSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/pptxsaveoptions/) to control how PDF pages are mapped into PowerPoint slides.

## Convert PDF to PPTX

Use this example when a PDF document should be exported as a standard PowerPoint presentation.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create default [`PptxSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/pptxsaveoptions/) for editable PowerPoint export.
1. Call `document.save(outputFile.toString(), saveOptions)` so the PDF pages are serialized as a `.pptx` presentation.
1. Save the converted PPTX file.

```java
public static void convertPdfToPptx(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PptxSaveOptions saveOptions = new PptxSaveOptions();
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert PDF to PPTX with slides as images

Use this example when each PDF page should become an image-based PowerPoint slide.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`PptxSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/pptxsaveoptions/) and enable `setSlidesAsImages(true)`.
1. Call `document.save(outputFile.toString(), saveOptions)` so each PDF page is rendered as an image-backed slide in the presentation.
1. Save the generated PPTX file.

```java
public static void convertPdfToPptxSlidesAsImages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PptxSaveOptions saveOptions = new PptxSaveOptions();
        saveOptions.setSlidesAsImages(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert PDF to PPTX with custom image resolution

Use this example when the slide image quality should be controlled during PDF-to-PPTX export.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`PptxSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/pptxsaveoptions/) and set `setImageResolution(300)` for higher slide image fidelity.
1. Call `document.save(outputFile.toString(), saveOptions)` so rasterized slide content is generated at the requested resolution.
1. Save the output presentation.

```java
public static void convertPdfToPptxImageResolution(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PptxSaveOptions saveOptions = new PptxSaveOptions();
        saveOptions.setImageResolution(300);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
