---
title: Convert PDF to Word in Java
linktitle: Convert PDF to Word
type: docs
weight: 10
url: /java/convert-pdf-to-word/
lastmod: "2026-06-09"
description: Learn how to convert PDF files to DOC and DOCX in Java with Aspose.PDF for easier document editing and reuse.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to Convert PDF to Word in Java
Abstract: This article explains how to convert PDF files to Microsoft Word formats using Aspose.PDF for Java. It covers DOC output, DOCX output, and enhanced-flow DOCX conversion with `DocSaveOptions`.
---
Aspose.PDF for Java can export PDF documents to Microsoft Word formats with different recognition and layout options.

## Convert PDF to DOC

Use this example when a PDF document should be exported to the legacy DOC format.

1. Open the source PDF document.
1. Configure the Word save options for DOC output.
1. Save the converted DOC file.

```java
public static void convertPdfToDoc(Path inputFile, Path outputFile) {
       DocSaveOptions saveOptions = new DocSaveOptions();
       saveOptions.setFormat(DocSaveOptions.DocFormat.Doc);
       saveDocument(inputFile, outputFile, saveOptions);
   }
```

## Convert PDF to DOCX

Use this example when a PDF document should be exported as a DOCX file.

1. Open the source PDF document.
1. Configure the Word save options for DOCX output.
1. Save the resulting DOCX file.

```java
public static void convertPdfToDocx(Path inputFile, Path outputFile) {
    DocSaveOptions saveOptions = new DocSaveOptions();
    saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
    saveDocument(inputFile, outputFile, saveOptions);
}
```

## Convert PDF to DOCX with advanced options

Use this example when the Word export should use advanced recognition or layout settings.

1. Open the source PDF document.
1. Configure the advanced DOCX save options.
1. Save the converted DOCX output.

```java
public static void convertPdfToDocxAdvanced(Path inputFile, Path outputFile) {
    DocSaveOptions saveOptions = new DocSaveOptions();
    saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
    saveOptions.setMode(DocSaveOptions.RecognitionMode.EnhancedFlow);
    saveDocument(inputFile, outputFile, saveOptions);
}
```

## Reuse a shared Word save helper

Use this helper when several PDF-to-Word examples should save through one common method.

1. Open the source PDF document.
1. Pass the prepared `DocSaveOptions` to the helper.
1. Save the converted Word file.

```java
private static void saveDocument(Path inputFile, Path outputFile, DocSaveOptions saveOptions) {
    try (Document document = new Document(inputFile.toString())) {
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
