---
title: Convert PDF/A and PDF/UA to PDF in Java
linktitle: Convert PDF/A and PDF/UA to PDF
type: docs
weight: 120
url: /java/convert-pdf_x-to-pdf/
lastmod: "2026-06-16"
description: Learn how to remove PDF/A and PDF/UA compliance from standards-based PDF files in Java and save them as standard PDF documents.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: How to convert PDF/A and PDF/UA to standard PDF in Java
Abstract: This article explains how to remove PDF/A and PDF/UA compliance from standards-based PDF documents using Aspose.PDF for Java, then save the result as a standard PDF file.
---
Aspose.PDF for Java can convert standards-compliant PDF variants back to a regular PDF document.

## Convert PDF/A to standard PDF

Use this example when an archival PDF/A document should be downgraded to a standard PDF.

1. Open the source PDF/A file in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Call `removePdfaCompliance()` to detach the archival compliance profile from the loaded document.
1. Save the resulting standard PDF file without the PDF/A restriction set.

```java
public static void convertPdfAToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.removePdfaCompliance();
        document.save(outputFile.toString());
    }
}
```

## Convert PDF/UA to standard PDF

Use this example when an accessible PDF/UA document should be converted back to a standard PDF.

1. Open the source PDF/UA file in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Call `removePdfUaCompliance()` to remove the accessibility compliance profile from the document metadata and structure requirements.
1. Save the resulting PDF document as a regular PDF file.

```java
public static void convertPdfUaToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.removePdfUaCompliance();
        document.save(outputFile.toString());
    }
}
```
