---
title: Convert PDF/A and PDF/UA to PDF in Java
linktitle: Convert PDF/A and PDF/UA to PDF
type: docs
weight: 120
url: /java/convert-pdf_x-to-pdf/
lastmod: "2026-06-04"
description: Learn how to remove PDF/A and PDF/UA compliance from standards-based PDF files in Java and save them as standard PDF documents.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: How to convert PDF/A and PDF/UA to standard PDF in Java
Abstract: This article explains how to remove PDF/A and PDF/UA compliance from standards-based PDF documents using Aspose.PDF for Java, then save the result as a standard PDF file.
---
## Convert PDF/A to standard PDF

1. Open the source PDF/A document.
1. Remove PDF/A compliance from the document.
1. Save the output PDF document.

```java
public static void convertPdfAToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.removePdfaCompliance();
        document.save(outputFile.toString());
    }
}
```

## Convert PDF/UA to standard PDF

1. Open the source PDF/UA document.
1. Remove PDF/UA compliance from the document.
1. Save the output PDF document.

```java
public static void convertPdfUaToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.removePdfUaCompliance();
        document.save(outputFile.toString());
    }
}
```
