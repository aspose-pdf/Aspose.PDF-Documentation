---
title: Delete Pages from PDF
type: docs
weight: 20
url: /java/delete-pages-from-pdf/
description: Delete selected pages from a PDF in Java with the PdfFileEditor facade.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remove specific pages from a PDF document with Java
Abstract: Learn how to delete pages from a PDF with Aspose.PDF for Java. The Java example uses PdfFileEditor to remove a defined set of page numbers and save the remaining pages as a new document.
---
## Delete pages from a PDF

The Java sample removes pages 2 and 4 from the source document.

### Steps

1. Create a `PdfFileEditor` instance.
2. Build an array with the page numbers to remove.
3. Call `delete` with the input file, page array, and output file.
4. Save the resulting PDF.

### Java example

```java
public static void deletePagesFromPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.delete(inputFile.toString(), new int[] {2, 4}, outputFile.toString());
}
```
