---
title: Convert PDF to Word in Java
linktitle: Convert PDF to Word
type: docs
weight: 10
url: /java/convert-pdf-to-word/
lastmod: "2026-05-27"
description: Learn how to convert PDF files to DOC and DOCX in Java with Aspose.PDF for easier document editing and reuse.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to Convert PDF to Word in Java
Abstract: This article explains how to convert PDF files to Microsoft Word formats using Aspose.PDF for Java. It covers DOC output, DOCX output, and enhanced-flow DOCX conversion with `DocSaveOptions`.
---
## Convert PDF to DOC or DOCX

Use `DocSaveOptions` to choose the target Word format.

```java
public static void convertPdfToDoc(Path inputFile, Path outputFile) {
    DocSaveOptions saveOptions = new DocSaveOptions();
    saveOptions.setFormat(DocSaveOptions.DocFormat.Doc);
    saveDocument(inputFile, outputFile, saveOptions);
}
```

```java
public static void convertPdfToDocx(Path inputFile, Path outputFile) {
    DocSaveOptions saveOptions = new DocSaveOptions();
    saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
    saveDocument(inputFile, outputFile, saveOptions);
}
```

## Use enhanced-flow recognition for DOCX

```java
public static void convertPdfToDocxAdvanced(Path inputFile, Path outputFile) {
    DocSaveOptions saveOptions = new DocSaveOptions();
    saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
    saveOptions.setMode(DocSaveOptions.RecognitionMode.EnhancedFlow);
    saveDocument(inputFile, outputFile, saveOptions);
}
```
