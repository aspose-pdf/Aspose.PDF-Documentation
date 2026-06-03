---
title: Get Page Offset
type: docs
weight: 20
url: /java/get-page-offset/
description: Learn how to inspect page X and Y offsets in Java with the PdfFileInfo facade.
lastmod: "2026-06-03"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Get PDF Page Offsets using Java
Abstract: Learn how to retrieve page offsets with Aspose.PDF for Java. The Java example uses PdfFileInfo to read the X and Y offsets of page 1 and converts the point values to inches for easier layout analysis.
---
## Get page offset

Use this workflow when you need to understand how page content is positioned relative to the PDF origin.

### Steps

1. Create a `PdfFileInfo` object for the input PDF.
2. Call `getPageXOffset` and `getPageYOffset` for the target page.
3. Convert the point values to inches by dividing by `72.0`.
4. Use or print the converted values.
5. Close the `PdfFileInfo` instance.

### Java example

```java
public static void getPageOffsets(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Page X Offset: " + (pdfInfo.getPageXOffset(1) / 72.0) + " inches");
    System.out.println("Page Y Offset: " + (pdfInfo.getPageYOffset(1) / 72.0) + " inches");
    pdfInfo.close();
}
```
