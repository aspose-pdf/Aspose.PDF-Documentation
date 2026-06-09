---
title: List Stamps
type: docs
weight: 20
url: /java/list-stamps/
description: Learn how to list rubber stamps on a page in Java using the PdfContentEditor facade in Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: List PDF rubber stamps in Java
Abstract: This article shows how to bind a PDF, retrieve the stamps on a page, and inspect the resulting collection using the PdfContentEditor facade in Aspose.PDF for Java.
---
## List stamps on a page

1. Bind the source PDF to the `PdfContentEditor` facade.
2. Call `getStamps(pageNumber)` to retrieve the stamps on the target page.
3. Inspect the resulting `StampInfo[]` collection.

```java
public static void listStamps(Path inputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        StampInfo[] stamps = editor.getStamps(1);
        System.out.println("Stamps on page 1: " + stamps.length);
    } finally {
        editor.close();
    }
}
```
