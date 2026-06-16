---
title: Split PDF from Beginning
linktitle: Split PDF from Beginning
type: docs
weight: 10
url: /java/split-pdf-from-beginning/
description: Split a PDF from the beginning in Java with the PdfFileEditor facade.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extract the first pages of a PDF into a new document with Java
Abstract: Learn how to split a PDF from the beginning with Aspose.PDF for Java. The Java example uses PdfFileEditor to take the first three pages of a document and save them as a separate PDF.
---
## Split PDF from beginning

The Java sample extracts the first three pages from the source document.

### Steps

1. Create a `PdfFileEditor` instance.
2. Call `splitFromFirst` with the source file, number of pages to keep, and output file.
3. Save the new PDF document.

```java
public static void splitPdfFromBeginning(Path inputFile, Path outputFile) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitFromFirst(inputFile.toString(), 3, outputFile.toString());
}
```
