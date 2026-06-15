---
title: Convert PDF to PowerPoint in Java
linktitle: Convert PDF to PowerPoint
type: docs
weight: 30
url: /java/convert-pdf-to-powerpoint/
description: Learn how to convert PDF files to PowerPoint in Java with Aspose.PDF, including editable PPTX slides, image-based slides, and custom image resolution.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to Convert PDF to PowerPoint in Java
Abstract: This article explains how to convert PDF files into PowerPoint presentations using Aspose.PDF for Java. It covers standard PPTX conversion, slide-as-image output, and image-resolution control through `PptxSaveOptions`.
---
Aspose.PDF for Java supports exporting PDF pages into editable PowerPoint presentations with slide rendering options.

## Convert PDF to PPTX

Use this example when a PDF document should be exported as a standard PowerPoint presentation.

1. Open the source PDF document.
1. Configure the PowerPoint save options.
1. Save the converted PPTX file.

```java
public static void convertPdfToPptx(Path inputFile, Path outputFile) {
       saveDocument(inputFile, outputFile, new PptxSaveOptions());
   }
```

## Convert PDF to PPTX with slides as images

Use this example when each PDF page should become an image-based PowerPoint slide.

1. Open the source PDF document.
1. Configure the PPTX save options to render slides as images.
1. Save the generated PPTX file.

```java
public static void convertPdfToPptxSlidesAsImages(Path inputFile, Path outputFile) {
    PptxSaveOptions saveOptions = new PptxSaveOptions();
    saveOptions.setSlidesAsImages(true);
    saveDocument(inputFile, outputFile, saveOptions);
}
```

## Convert PDF to PPTX with custom image resolution

Use this example when the slide image quality should be controlled during PDF-to-PPTX export.

1. Open the source PDF document.
1. Set the PPTX save options with the required image resolution.
1. Save the output presentation.

```java
public static void convertPdfToPptxImageResolution(Path inputFile, Path outputFile) {
    PptxSaveOptions saveOptions = new PptxSaveOptions();
    saveOptions.setImageResolution(300);
    saveDocument(inputFile, outputFile, saveOptions);
}
```

## Reuse a shared PowerPoint save helper

Use this helper when multiple PowerPoint conversion examples should share the same save routine.

1. Open the source PDF document.
1. Pass the prepared `PptxSaveOptions` to the helper.
1. Save the converted PPTX output.

```java
private static void saveDocument(Path inputFile, Path outputFile, PptxSaveOptions saveOptions) {
    try (Document document = new Document(inputFile.toString())) {
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
