---
title: Set PDF Metadata
type: docs
weight: 50
url: /java/set-pdf-metadata/
description: Learn how to update PDF metadata in Java with the PdfFileInfo facade.
lastmod: "2026-06-03"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Updating PDF Metadata Using Aspose.PDF for Java
Abstract: Learn how to update PDF metadata with Aspose.PDF for Java. The Java example uses PdfFileInfo to set standard metadata fields such as subject, title, keywords, and creator, adds a custom metadata entry, and saves the result to a new PDF.
---
## Set PDF metadata

Use this workflow when you need to normalize or enrich document information before saving the PDF.

### Steps

1. Create a `PdfFileInfo` object for the source PDF.
2. Set the standard metadata fields you want to update.
3. Add any custom metadata with `setMetaInfo`.
4. Save the updated document with `save()`.
5. Close the `PdfFileInfo` instance.

### Java example

```java
public static void setPdfMetadata(Path inputFile, Path outputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    pdfInfo.setSubject("Aspose PDF for Java");
    pdfInfo.setTitle("Aspose PDF for Java");
    pdfInfo.setKeywords("Aspose, PDF, Java");
    pdfInfo.setCreator("Aspose Team");
    pdfInfo.setMetaInfo("CustomKey", "CustomValue");
    pdfInfo.save(outputFile.toString());
    pdfInfo.close();
}
```
