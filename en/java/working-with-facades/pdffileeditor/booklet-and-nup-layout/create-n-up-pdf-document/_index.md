---
title: Create N-Up PDF Document
linktitle: Create N-Up PDF Document
type: docs
weight: 10
url: /java/create-n-up-pdf-document/
description: Create a 2x2 N-Up PDF layout in Java with the PdfFileEditor facade.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Generate an N-Up PDF layout from an existing document in Java
Abstract: Learn how to create an N-Up PDF document with Aspose.PDF for Java. The Java example uses PdfFileEditor to place four source pages on each output sheet and also shows a boolean-return variant for failure checking.
---
## Create an N-Up PDF document

The Java sample uses `PdfFileEditor.makeNUp` to build a 2x2 layout from an existing PDF.

### Steps

1. Create a `PdfFileEditor` instance.
2. Call `makeNUp` with the input file, output file, and the number of columns and rows.
3. Save the generated document.
4. If you want explicit success checking, call the boolean-return variant and handle a `false` result.

### Java example

```java
public static void createNupPdfDocument(Path inputFile, Path outputFile) {
    PdfFileEditor nupMaker = new PdfFileEditor();
    nupMaker.makeNUp(inputFile.toString(), outputFile.toString(), 2, 2);
}

public static void tryCreateNupPdfDocument(Path inputFile, Path outputFile) {
    PdfFileEditor nupMaker = new PdfFileEditor();
    if (!nupMaker.makeNUp(inputFile.toString(), outputFile.toString(), 2, 2)) {
        System.out.println("Failed to create N-Up PDF document.");
    }
}
```
