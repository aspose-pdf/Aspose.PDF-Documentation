---
title: Split PDF to End
type: docs
weight: 40
url: /java/split-pdf-to-end/
description: Split a PDF from a chosen page to the end in Java with the PdfFileEditor facade.
lastmod: "2026-06-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extract pages from a starting point to the end of a PDF with Java
Abstract: Learn how to split a PDF to the end with Aspose.PDF for Java. The Java example uses PdfFileEditor to extract all pages starting from page 2 through the end of the source document.
---
## Split PDF to end

The Java sample extracts all pages starting from page 2.

### Steps

1. Create a `PdfFileEditor` instance.
2. Call `splitToEnd` with the source file, starting page number, and output file.
3. Save the resulting PDF document.

```java
public static void splitPdfToEnd(Path inputFile, Path outputFile) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitToEnd(inputFile.toString(), 2, outputFile.toString());
}
```
