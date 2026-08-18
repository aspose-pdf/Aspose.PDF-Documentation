---
title: Add Page Breaks in PDF
linktitle: Add Page Breaks in PDF
type: docs
weight: 20
url: /java/add-page-breaks-in-pdf/
description: Insert page breaks into a PDF in Java with the PdfFileEditor facade.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Insert page breaks at fixed positions in a PDF document with Java
Abstract: Learn how to add page breaks with Aspose.PDF for Java. The Java example uses PdfFileEditor.PageBreak to split a page at a specific vertical position and save the result as a new PDF.
---
## Add page breaks in a PDF

Use this workflow when a page needs to be split into multiple pages at a known Y position.

### Steps

1. Create a `PdfFileEditor` instance.
2. Build one or more `PdfFileEditor.PageBreak` entries with the page number and break position.
3. Pass the page break array to `addPageBreak`.
4. Save the updated PDF document.

### Java example

```java
public static void addPageBreaksInPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.addPageBreak(inputFile.toString(), outputFile.toString(), new PdfFileEditor.PageBreak[] {
            new PdfFileEditor.PageBreak(1, 400)
    });
}
```
