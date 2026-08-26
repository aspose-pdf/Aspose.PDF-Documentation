---
title: Dividir PDF en páginas individuales
linktitle: Split PDF into Single Pages
type: docs
weight: 30
url: /java/split-pdf-into-single-pages/
description: Divida un PDF en archivos de salida de una sola página en Java con la fachada PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Export each page of a PDF to its own file with Java
Abstract: Learn how to split a PDF into single-page files with Aspose.PDF for Java. The Java example uses PdfFileEditor to write each page to an individual output PDF based on a filename pattern.
---
## Split PDF into single pages

Use this workflow when each source page must become its own PDF file.

### Steps

1. Create a `PdfFileEditor` instance.
2. Prepare an output file pattern that includes a page placeholder such as `%NUM%`.
3. Call `splitToPages` with the source file and output pattern.
4. Save the generated single-page files.

```java
public static void splitPdfIntoSinglePages(Path inputFile, Path outputFilePattern) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitToPages(inputFile.toString(), outputFilePattern.toString());
}
```
