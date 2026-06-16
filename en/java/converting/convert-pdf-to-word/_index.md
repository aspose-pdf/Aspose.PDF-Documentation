---
title: Convert PDF to Word in Java
linktitle: Convert PDF to Word
type: docs
weight: 10
url: /java/convert-pdf-to-word/
lastmod: "2026-06-16"
description: Learn how to convert PDF files to DOC and DOCX in Java with Aspose.PDF for easier document editing and reuse.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to Convert PDF to Word in Java
Abstract: This article explains how to convert PDF files to Microsoft Word formats using Aspose.PDF for Java. It covers DOC output, DOCX output, enhanced-flow DOCX conversion, preserved line breaks, bullet recognition, and image-resolution control through `DocSaveOptions`.
---
Aspose.PDF for Java can export PDF documents to Microsoft Word formats with different recognition and layout options. Use [`DocSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/docsaveoptions/) to control how PDF text, lists, and images are mapped into Word output.

## Convert PDF to DOC

Use this example when a PDF document should be exported to the legacy DOC format.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`DocSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/docsaveoptions/) and set the format to `Doc`.
1. Call `document.save(outputFile.toString(), saveOptions)` so the PDF is exported to the Microsoft Word binary document format.
1. Save the converted DOC file.

```java
public static void convertPdfToDoc(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.Doc);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert PDF to DOCX

Use this example when a PDF document should be exported as a DOCX file.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`DocSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/docsaveoptions/) and set the format to `DocX`.
1. Call `document.save(outputFile.toString(), saveOptions)` so the PDF content is exported as an Office Open XML Word document.
1. Save the resulting DOCX file.

```java
public static void convertPdfToDocx(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert PDF to DOCX with enhanced flow recognition

Use this example when the Word export should favor flowing editable content instead of fixed visual layout.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`DocSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/docsaveoptions/) for `DocX` output.
1. Enable `setMode(DocSaveOptions.RecognitionMode.EnhancedFlow)` so the converter uses enhanced flow recognition during DOCX generation.
1. Call `document.save(outputFile.toString(), saveOptions)` and save the converted DOCX output.

```java
public static void convertPdfToDocxAdvanced(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setMode(DocSaveOptions.RecognitionMode.EnhancedFlow);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert PDF to DOCX with preserved line breaks

Use this example when line endings from the source PDF should be retained in the Word output.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`DocSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/docsaveoptions/) for `DocX` export.
1. Enable `setAddReturnToLineEnd(true)` so explicit line breaks are preserved during conversion.
1. Call `document.save(outputFile.toString(), saveOptions)` and save the DOCX file.

```java
public static void convertPdfToDocxWithLineBreaks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setAddReturnToLineEnd(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert PDF to DOCX with bullet recognition

Use this example when list bullets from the source PDF should be recognized and preserved as list structures in Word.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`DocSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/docsaveoptions/) for `DocX` export.
1. Enable `setRecognizeBullets(true)` so list-like PDF content is recognized as bullet lists during conversion.
1. Call `document.save(outputFile.toString(), saveOptions)` and save the DOCX file.

```java
public static void convertPdfToDocxWithBulletRecognition(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setRecognizeBullets(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert PDF to DOCX with custom image resolution

Use this example when image fidelity inside the generated DOCX should be controlled during conversion.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`DocSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/docsaveoptions/) for `DocX` export.
1. Set `setImageResolutionX(300)` and `setImageResolutionY(300)` so raster content is generated at the requested resolution.
1. Call `document.save(outputFile.toString(), saveOptions)` and save the DOCX output.

```java
public static void convertPdfToDocxWithImageResolution(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setImageResolutionX(300);
        saveOptions.setImageResolutionY(300);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
