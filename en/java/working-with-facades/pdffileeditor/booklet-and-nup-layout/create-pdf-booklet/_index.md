---
title: Create PDF Booklet
type: docs
weight: 20
url: /java/create-pdf-booklet/
description: Create a booklet-ready PDF from an existing document in Java with the PdfFileEditor facade.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Generate booklet output from a PDF document in Java
Abstract: Learn how to create a PDF booklet with Aspose.PDF for Java. The Java example uses PdfFileEditor to reorder pages for booklet printing and also includes a boolean-return variant for simple success checking.
---
## Create a PDF booklet

Use `PdfFileEditor.makeBooklet` to rearrange the pages of an existing PDF into booklet order.

### Steps

1. Create a `PdfFileEditor` instance.
2. Call `makeBooklet` with the source PDF and output file.
3. Save the booklet document.
4. If you want to check the return status, use the boolean-return variant and handle a failed result.

### Java example

```java
public static void createPdfBooklet(Path inputFile, Path outputFile) {
    PdfFileEditor bookletMaker = new PdfFileEditor();
    bookletMaker.makeBooklet(inputFile.toString(), outputFile.toString());
}

public static void tryCreatePdfBooklet(Path inputFile, Path outputFile) {
    PdfFileEditor bookletMaker = new PdfFileEditor();
    if (!bookletMaker.makeBooklet(inputFile.toString(), outputFile.toString())) {
        System.out.println("Failed to create booklet.");
    }
}
```
