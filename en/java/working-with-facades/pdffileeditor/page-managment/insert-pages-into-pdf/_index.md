---
title: Insert Pages into PDF
linktitle: Insert Pages into PDF
type: docs
weight: 40
url: /java/insert-pages-into-pdf/
description: Insert selected pages from one PDF into another in Java with the PdfFileEditor facade.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Insert pages from another PDF at a chosen position with Java
Abstract: Learn how to insert pages into a PDF with Aspose.PDF for Java. The Java example uses PdfFileEditor to insert selected pages from a second document after a given page number in the target PDF.
---
## Insert pages into a PDF

The Java sample inserts pages 1 and 2 from the secondary document after page 2 of the target PDF.

### Steps

1. Create a `PdfFileEditor` instance.
2. Choose the insertion point in the target document.
3. Select the page numbers to copy from the source document.
4. Call `insert` with the target file, insertion point, source file, page array, and output file.
5. Save the updated PDF.

### Java example

```java
public static void insertPagesIntoPdf(Path inputFile, Path sampleFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.insert(inputFile.toString(), 2, sampleFile.toString(), new int[] {1, 2}, outputFile.toString());
}
```
