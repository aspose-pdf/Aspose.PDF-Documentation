---
title: Convert PDF to PDF/A, PDF/E, and PDF/X in Java
linktitle: Convert PDF to PDF/A, PDF/E, and PDF/X
type: docs
weight: 120
url: /java/convert-pdf-to-pdf_x/
lastmod: "2026-06-16"
description: Learn how to convert PDF files to PDF/A, PDF/E, and PDF/X in Java with Aspose.PDF for archival, engineering, accessibility, and print workflows.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: How to convert PDF to PDF/x formats
Abstract: This article explains how to validate and convert PDF documents to PDF/A, PDF/E, and PDF/X formats using Aspose.PDF for Java. It covers log generation, attachment preservation for PDF/A-3, missing-font substitution, auto-tagging, ICC profile configuration, and output intent settings.
---
Aspose.PDF for Java can validate and convert standard PDF files into archival and exchange-oriented PDF standards.

## Convert PDF to PDF/A

Use this example when a standard PDF should be converted into a PDF/A-compliant archival document.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Call `document.convert(...)` with [`PdfFormat`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/pdfformat/) `PDF_A_1B` and [`ConvertErrorAction`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/converterroraction/) `Delete`.
1. Write the validation log to a sidecar XML file so compliance issues are recorded during conversion.
1. Save the validated PDF/A output.

```java
public static void convertPdfToPdfA(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.convert(logFile(outputFile, "-log.xml").toString(), PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);
        document.save(outputFile.toString());
    }
}
```

## Convert PDF to PDF/E

Use this example when a PDF should be converted into the engineering-oriented PDF/E standard.

1. Create [`PdfFormatConversionOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/pdfformatconversionoptions/) for [`PdfFormat`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/pdfformat/) `PDF_E_1` and the desired log-file path.
1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Call `document.convert(options)` so the compliance conversion is executed with the prepared options object.
1. Save the resulting compliant PDF file.

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

## Convert PDF to PDF/X

Use this example when a PDF should be converted into the print-oriented PDF/X standard.

1. Create [`PdfFormatConversionOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/pdfformatconversionoptions/) for [`PdfFormat`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/pdfformat/) `PDF_X_4` and the desired log-file path.
1. Configure an [`OutputIntent`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/outputintent/) such as `FOGRA39` so the print-target color profile is embedded into the conversion settings.
1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance and call `document.convert(options)`.
1. Save the converted PDF/X output.

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
