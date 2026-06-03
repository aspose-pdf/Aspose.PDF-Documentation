---
title: Save Metadata with XMP
type: docs
weight: 30
url: /java/save-metadata-with-xmp/
description: Learn how to save PDF metadata with XMP in Java with the PdfFileInfo facade.
lastmod: "2026-06-03"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Saving PDF Metadata with XMP Using Aspose.PDF for Java
Abstract: Learn how to save PDF metadata with XMP using Aspose.PDF for Java. The Java example updates core metadata fields with PdfFileInfo and writes them back using `saveNewInfoWithXmp()` so the output document stores the information in XMP form.
---
## Save metadata with XMP

Use this workflow when you need the updated document information to be stored in XMP format.

### Steps

1. Create a `PdfFileInfo` object for the source PDF.
2. Set the metadata fields you want to update, such as subject, title, keywords, and creator.
3. Call `saveNewInfoWithXmp()` with the output file path.
4. Close the `PdfFileInfo` instance.

### Java example

```java
public static void saveInfoWithXmp(Path inputFile, Path outputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    pdfInfo.setSubject("Aspose PDF for Java");
    pdfInfo.setTitle("Aspose PDF for Java");
    pdfInfo.setKeywords("Aspose, PDF, Java");
    pdfInfo.setCreator("Aspose Team");
    pdfInfo.saveNewInfoWithXmp(outputFile.toString());
    pdfInfo.close();
}
```
