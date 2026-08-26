---
title: Concatenate Two PDF Files
linktitle: Concatenate Two PDF Files
type: docs
weight: 60
url: /java/concatenate-two-files/
description: Merge two PDF files into one document in Java with the PdfFileEditor facade.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Concatenate two PDF files into a single output document with Java
Abstract: Learn how to concatenate two PDF files with Aspose.PDF for Java. The Java example uses PdfFileEditor and the array-based `concatenate` overload to combine two source documents into one output PDF.
---
## Concatenar dos archivos PDF

Este artículo se asigna directamente al ejemplo `mergePdfDocuments` en `PdfFileEditorExamples.java`.

### Steps

1. Cree una instancia `PdfFileEditor`.
2. Pass the two input file paths as a string array.
3. Call `concatenate` with the array and output file path.
4. Save the merged PDF.

```java
public static void mergePdfDocuments(Path firstInputFile, Path secondInputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.concatenate(new String[] {firstInputFile.toString(), secondInputFile.toString()}, outputFile.toString());
}
```
