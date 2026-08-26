---
title: Dividir PDF desde el principio
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
AlternativeHeadline: Extrae las primeras páginas de un PDF en un nuevo documento con Java
Abstract: Aprenda a dividir un PDF desde el principio con Aspose.PDF para Java. El ejemplo de Java utiliza PdfFileEditor para tomar las tres primeras páginas de un documento y guardarlas como un PDF independiente.
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
