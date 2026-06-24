---
title: Save PDF document programmatically
linktitle: Save PDF
type: docs
weight: 30
url: /java/save-pdf-document/
description: Learn how to save PDF documents in Java to a file, to a stream, or as a PDF standard using Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Saving PDF documents using the Aspose.PDF library in Java
Abstract: This article describes how to save PDF documents in Java using Aspose.PDF. It covers saving to a file path, saving to an OutputStream, and converting a document before saving it as a PDF/X standard file.
---
Aspose.PDF for Java provides several ways to save a document depending on the target destination and output requirements.

## Save a PDF document in Java

You can save a document:

1. Save the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) directly to a file on disk.
1. Save the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) to an `OutputStream`.
1. Convert the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) with [PdfFormatConversionOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) and save it in a standard format such as [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/).

## Save document to file

```java
public static void saveDocumentToFile(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString());
    document.getPages().add();
    document.save(outputFile.toString());
    document.close();
}
```

## Save document to stream

```java
public static void saveDocumentToStream(Path inputFile, Path outputFile) throws Exception {
    Document document = new Document(inputFile.toString());
    document.getPages().add();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        document.save(stream);
    } finally {
        document.close();
    }
}
```

## Save document as PDF/X

```java
public static void saveDocumentAsStandard(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString());
    document.getPages().add();
    document.convert(new PdfFormatConversionOptions(PdfFormat.PDF_X_3));
    document.save(outputFile.toString());
    document.close();
}
```
