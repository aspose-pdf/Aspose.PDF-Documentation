---
title: Get PDF Version
linktitle: Get PDF Version
type: docs
weight: 20
url: /java/get-pdf-version/
description: Learn how to retrieve the version of a PDF document in Java with the PdfFileInfo facade.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Retrieve PDF Version Using Aspose.PDF for Java
Abstract: Learn how to retrieve the PDF version with Aspose.PDF for Java. The Java example creates a PdfFileInfo object, reads the version string with `getPdfVersion()`, prints the result, and closes the file information object.
---
## Get PDF version

Use this workflow when you need to check file compatibility or route a document through version-specific processing logic.

### Steps

1. Create a `PdfFileInfo` object for the PDF file.
2. Call `getPdfVersion()` to retrieve the reported version.
3. Use or print the version value.
4. Close the `PdfFileInfo` instance.

### Java example

```java
public static void getPdfVersion(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println();
    System.out.println("PDF Version: " + pdfInfo.getPdfVersion());
    pdfInfo.close();
}
```
