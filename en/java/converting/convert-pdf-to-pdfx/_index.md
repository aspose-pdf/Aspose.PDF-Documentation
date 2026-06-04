---
title: Convert PDF to PDF/A, PDF/E, and PDF/X in Java
linktitle: Convert PDF to PDF/A, PDF/E, and PDF/X
type: docs
weight: 120
url: /java/convert-pdf-to-pdf_x/
lastmod: "2026-06-04"
description: Learn how to convert PDF files to PDF/A, PDF/E, and PDF/X in Java with Aspose.PDF for archival, engineering, accessibility, and print workflows.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: How to convert PDF to PDF/x formats
Abstract: This article explains how to validate and convert PDF documents to PDF/A, PDF/E, and PDF/X formats using Aspose.PDF for Java. It covers log generation, attachment preservation for PDF/A-3, missing-font substitution, auto-tagging, ICC profile configuration, and output intent settings.
---
## Convert PDF to PDF/A

1. Open the source PDF document.
1. Convert the document to the PDF/A target format and write the conversion log file.
1. Save the converted PDF document.

```java
public static void convertPdfToPdfA(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.convert(logFile(outputFile, "-log.xml").toString(), PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);
        document.save(outputFile.toString());
    }
}
```

## Convert PDF to PDF/E or PDF/X

1. Create PDF format conversion options for PDF/E output.
1. Set the conversion log file, target format, and error handling mode.
1. Open the source PDF document.
1. Convert the document by using the configured options.
1. Save the converted PDF document.

```java
public static void convertPdfToPdfE(Path inputFile, Path outputFile) {
    PdfFormatConversionOptions options = new PdfFormatConversionOptions(
            logFile(outputFile, "-log.xml").toString(), PdfFormat.PDF_E_1, ConvertErrorAction.Delete);

    try (Document document = new Document(inputFile.toString())) {
        document.convert(options);
        document.save(outputFile.toString());
    }
}
```

1. Create PDF format conversion options for PDF/X output.
1. Set the conversion log file, target format, and error handling mode.
1. Configure the required output intent.
1. Open the source PDF document.
1. Convert the document by using the configured options.
1. Save the converted PDF document.

```java
public static void convertPdfToPdfX(Path inputFile, Path outputFile) {
    PdfFormatConversionOptions options = new PdfFormatConversionOptions(
            logFile(outputFile, "-log.xml").toString(), PdfFormat.PDF_X_4, ConvertErrorAction.Delete);
    options.setOutputIntent(new OutputIntent("FOGRA39"));

    try (Document document = new Document(inputFile.toString())) {
        document.convert(options);
        document.save(outputFile.toString());
    }
}
```
