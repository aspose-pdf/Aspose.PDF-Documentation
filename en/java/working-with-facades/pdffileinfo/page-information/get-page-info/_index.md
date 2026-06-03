---
title: Get Page Information
type: docs
weight: 10
url: /java/get-page-info/
description: Learn how to inspect page width, height, and rotation in Java with the PdfFileInfo facade.
lastmod: "2026-06-03"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Get PDF Page Information Using Aspose.PDF for Java
Abstract: Learn how to retrieve page information with Aspose.PDF for Java. The Java example uses PdfFileInfo to read the width, height, and rotation of page 1 so you can inspect its layout before further processing.
---
## Get page information

This example reads the main geometric properties of page 1.

### Steps

1. Create a `PdfFileInfo` object for the source PDF.
2. Call `getPageWidth`, `getPageHeight`, and `getPageRotation` for the page you want to inspect.
3. Use or print the returned values.
4. Close the `PdfFileInfo` instance.

### Java example

```java
public static void getPageInformation(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Page Width: " + pdfInfo.getPageWidth(1));
    System.out.println("Page Height: " + pdfInfo.getPageHeight(1));
    System.out.println("Page Rotation: " + pdfInfo.getPageRotation(1));
    pdfInfo.close();
}
```
