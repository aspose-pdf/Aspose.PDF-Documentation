---
title: Append Pages to PDF
linktitle: Append Pages to PDF
type: docs
weight: 10
url: /java/append-pages-to-pdf/
description: Append pages from one PDF to another in Java with the PdfFileEditor facade.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Append a page range from one PDF document to another with Java
Abstract: Learn how to append pages to a PDF with Aspose.PDF for Java. The Java example uses PdfFileEditor to append a selected page range from another document to the end of the current PDF.
---
## Append pages to a PDF

The Java sample appends page 1 from a second PDF to the end of the first document.

### Steps

1. Create a `PdfFileEditor` instance.
2. Bind the main input PDF by passing its path to `append`.
3. Provide the secondary source file list and the page range to append.
4. Save the merged result to the output file.

### Java example

```java
public static void appendPagesToPdf(Path inputFile, Path sampleFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.append(inputFile.toString(), new String[] {sampleFile.toString()}, 1, 1, outputFile.toString());
}
```
