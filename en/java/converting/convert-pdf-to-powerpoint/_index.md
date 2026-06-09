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
## Convert PDF to PPTX

1. Create [PptxSaveOptions](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/pptxsaveoptions/) for the conversion.
1. Convert the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) by using the PowerPoint save options.

```java
public static void convertPdfToPptx(Path inputFile, Path outputFile) {
    saveDocument(inputFile, outputFile, new PptxSaveOptions());
}
```

## Save slides as images or control resolution

1. Create [PptxSaveOptions](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/pptxsaveoptions/) for the conversion.
1. Enable image-based slides in the PowerPoint output.
1. Convert the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) by using the configured save options.

```java
public static void convertPdfToPptxSlidesAsImages(Path inputFile, Path outputFile) {
    PptxSaveOptions saveOptions = new PptxSaveOptions();
    saveOptions.setSlidesAsImages(true);
    saveDocument(inputFile, outputFile, saveOptions);
}
```

1. Create [PptxSaveOptions](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/pptxsaveoptions/) for the conversion.
1. Set the image resolution for the PowerPoint output.
1. Convert the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) by using the configured save options.

```java
public static void convertPdfToPptxImageResolution(Path inputFile, Path outputFile) {
    PptxSaveOptions saveOptions = new PptxSaveOptions();
    saveOptions.setImageResolution(300);
    saveDocument(inputFile, outputFile, saveOptions);
}
```
