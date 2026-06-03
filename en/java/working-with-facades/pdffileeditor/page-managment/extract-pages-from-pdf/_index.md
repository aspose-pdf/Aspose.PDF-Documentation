---
title: Extract Pages from PDF
type: docs
weight: 30
url: /java/extract-pages-from-pdf/
description: Extract selected pages from a PDF in Java with the PdfFileEditor facade.
lastmod: "2026-06-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extract selected PDF pages into a new document with Java
Abstract: Learn how to extract pages from a PDF with Aspose.PDF for Java. The Java example uses PdfFileEditor to collect specific page numbers and write them into a separate output PDF.
---
## Extract pages from a PDF

The Java sample extracts pages 1, 4, and 3 into a new PDF document.

### Steps

1. Create a `PdfFileEditor` instance.
2. Define the page numbers to extract.
3. Call `extract` with the source file, page array, and output file.
4. Save the extracted pages as a new PDF.

### Java example

```java
public static void extractPagesFromPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.extract(inputFile.toString(), new int[] {1, 4, 3}, outputFile.toString());
}
```
