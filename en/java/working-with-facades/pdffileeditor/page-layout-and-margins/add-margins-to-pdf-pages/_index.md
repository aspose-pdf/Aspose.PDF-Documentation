---
title: Add Margins to PDF Pages
linktitle: Add Margins to PDF Pages
type: docs
weight: 10
url: /java/add-margins-to-pdf-pages/
description: Add margins to selected PDF pages in Java with the PdfFileEditor facade.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add margins to specific pages in a PDF document with Java
Abstract: Learn how to add margins to selected pages with Aspose.PDF for Java. The Java example uses PdfFileEditor to target individual page numbers and apply equal top, bottom, left, and right margin values.
---
## Add margins to PDF pages

The Java sample adds 36-point margins to pages 1 and 3 of the source document.

### Steps

1. Create a `PdfFileEditor` instance.
2. Select the page numbers that should receive new margins.
3. Call `addMargins` with the input file, output file, page list, and margin values.
4. Save the updated PDF.

### Java example

```java
public static void addMarginsToPdfPages(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.addMargins(inputFile.toString(), outputFile.toString(), new int[] {1, 3}, 36, 36, 36, 36);
}
```
