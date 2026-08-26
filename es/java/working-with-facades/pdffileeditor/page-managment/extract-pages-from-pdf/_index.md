---
title: Extract Pages from PDF
linktitle: Extraer páginas de PDF
type: docs
weight: 30
url: /java/extract-pages-from-pdf/
description: Extract selected pages from a PDF in Java with the PdfFileEditor facade.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extract selected PDF pages into a new document with Java
Abstract: Learn how to extract pages from a PDF with Aspose.PDF for Java. The Java example uses PdfFileEditor to collect specific page numbers and write them into a separate output PDF.
---
## Extract pages from a PDF

El ejemplo de Java extrae las páginas 1, 4 y 3 en un nuevo documento PDF.

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
