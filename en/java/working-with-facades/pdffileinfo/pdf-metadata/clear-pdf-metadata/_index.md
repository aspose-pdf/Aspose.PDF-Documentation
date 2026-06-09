---
title: Clear PDF Metadata
type: docs
weight: 10
url: /java/clear-pdf-metadata/
description: Learn how to clear PDF metadata in Java with the PdfFileInfo facade.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Clearing PDF Metadata Using Aspose.PDF for Java
Abstract: Learn how to clear PDF metadata with Aspose.PDF for Java. The Java example uses PdfFileInfo to remove stored document information with `clearInfo()` and then saves the cleaned PDF to a new file.
---
## Clear PDF metadata

Use this workflow when you need to remove stored document information before sharing or archiving a PDF.

### Steps

1. Create a `PdfFileInfo` object for the input PDF.
2. Call `clearInfo()` to remove document metadata.
3. Save the result to a new file with `save()`.
4. Close the `PdfFileInfo` instance.

### Java example

```java
public static void clearPdfMetadata(Path inputFile, Path outputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    pdfInfo.clearInfo();
    pdfInfo.save(outputFile.toString());
    pdfInfo.close();
}
```
