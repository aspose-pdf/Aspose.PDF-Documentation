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
Abstract: This article explains how to convert PDF files to Microsoft Word formats using Aspose.PDF for Java. It covers DOC output, DOCX output, and enhanced-flow DOCX conversion with `DocSaveOptions`.
---
Aspose.PDF for Java can export PDF documents to Microsoft Word formats with different recognition and layout options. Use [DocSaveOptions](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/docsaveoptions/) to choose the output format and control how PDF page content is reconstructed in Word.

The common choices are:

- DOC for compatibility with older Microsoft Word workflows.
- DOCX for modern editable Word documents.
- DOCX with enhanced flow when the output should prioritize editable, flowing content over fixed page positioning.

PDF-to-Word conversion reconstructs a document from fixed PDF pages. Complex layouts, tables, images, columns, and custom fonts can affect how closely the Word output matches the source file, so choose the conversion mode according to whether editing or visual fidelity is more important.

## Convert PDF to DOC

Use this example when a PDF document should be exported to the legacy DOC format. The code creates `DocSaveOptions`, sets the format to `Doc`, and passes the options to a shared save method.

1. Create [DocSaveOptions](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/docsaveoptions/) to define how the PDF should be exported to a Word-processing format.
1. Set `DocSaveOptions.DocFormat.Doc` with `setFormat(...)` so the output is written as a legacy DOC file.
1. Pass the input path, output path, and configured save options to the shared method.
1. Save the converted DOC file by calling `Document.save(String, DocSaveOptions)` inside the method.

```java
public static void convertPdfToDoc(Path inputFile, Path outputFile) {
    DocSaveOptions saveOptions = new DocSaveOptions();
    saveOptions.setFormat(DocSaveOptions.DocFormat.Doc);
    saveDocument(inputFile, outputFile, saveOptions);
}
```

## Convert PDF to DOCX

Use this example when a PDF document should be exported as a DOCX file. DOCX is the preferred format for most new Word-processing workflows because it is widely supported and easier to edit.

1. Create [DocSaveOptions](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/docsaveoptions/) for the Word conversion settings.
1. Set `DocSaveOptions.DocFormat.DocX` with `setFormat(...)` to generate a DOCX file.
1. Pass the prepared options to the shared method so the same document-loading and saving logic can be reused.
1. Save the resulting DOCX file through `Document.save(String, DocSaveOptions)`.

```java
public static void convertPdfToDocx(Path inputFile, Path outputFile) {
    DocSaveOptions saveOptions = new DocSaveOptions();
    saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
    saveDocument(inputFile, outputFile, saveOptions);
}
```

## Convert PDF to DOCX with advanced options

Use this example when the Word export should use advanced recognition or layout settings. `RecognitionMode.EnhancedFlow` helps create a more editable Word document by reconstructing text flow instead of preserving every PDF page element as fixed-position content.

1. Create [DocSaveOptions](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/docsaveoptions/) for DOCX conversion.
1. Set `DocSaveOptions.DocFormat.DocX` with `setFormat(...)` so the result uses the modern Word format.
1. Set `DocSaveOptions.RecognitionMode.EnhancedFlow` with `setMode(...)` to improve editable text flow in the generated document.
1. Pass the configured options to the shared method.
1. Save the converted DOCX output through the loaded `Document` instance.

```java
public static void convertPdfToDocxAdvanced(Path inputFile, Path outputFile) {
    DocSaveOptions saveOptions = new DocSaveOptions();
    saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
    saveOptions.setMode(DocSaveOptions.RecognitionMode.EnhancedFlow);
    saveDocument(inputFile, outputFile, saveOptions);
}
```

## Reuse a shared Word save method

Use this method when several PDF-to-Word examples should save through one common code path. It opens the source [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) and saves it with the prepared `DocSaveOptions`.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) from `inputFile.toString()`.
1. Keep the `Document` inside a try-with-resources block so the PDF resources are released after conversion.
1. Pass the prepared `DocSaveOptions` to `Document.save(...)` so the method can save either DOC or DOCX output.
1. Write the converted Word file to `outputFile.toString()`.

```java
private static void saveDocument(Path inputFile, Path outputFile, DocSaveOptions saveOptions) {
    try (Document document = new Document(inputFile.toString())) {
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
