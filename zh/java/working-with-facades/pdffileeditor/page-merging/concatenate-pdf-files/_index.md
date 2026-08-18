---
title: Concatenate Multiple PDF Files
linktitle: Concatenate Multiple PDF Files
type: docs
weight: 20
url: /java/concatenate-pdf-files/
description: Merge PDF files in Java with the array-based PdfFileEditor concatenate workflow.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Merge multiple PDF files into one document with Java
Abstract: Learn how to concatenate PDF files with Aspose.PDF for Java. The repository sample uses the array-based `concatenate` overload with two inputs, and the same workflow can be extended to longer file lists because the method accepts a string array of source paths.
---
## Concatenate PDF files

The Java sample merges two files by passing them to the array-based `concatenate` overload.

### Steps

1. Create a `PdfFileEditor` instance.
2. Build a string array with the input PDF paths.
3. Call `concatenate` with the input array and output file path.
4. Save the merged document.

```java
public static void mergePdfDocuments(Path firstInputFile, Path secondInputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.concatenate(new String[] {firstInputFile.toString(), secondInputFile.toString()}, outputFile.toString());
}
```

To merge more than two files, extend the string array passed to `concatenate`.
