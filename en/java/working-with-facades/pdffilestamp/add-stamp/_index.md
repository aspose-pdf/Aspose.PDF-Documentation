---
title: Add Stamp to PDF
type: docs
weight: 40
url: /java/add-stamp/
description: Learn how to add an image stamp to PDF pages in Java with the PdfFileStamp facade.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add image stamps to PDF in Java
Abstract: Learn how to add stamp content to PDF documents with Aspose.PDF for Java using the PdfFileStamp facade. The current Java example set shows how to create a `Stamp`, bind it to an image file, add it to the document, and save the stamped PDF.
---
## Add stamp to PDF

Use this workflow when an image-based stamp should be applied to the PDF.

### Steps

1. Create a `PdfFileStamp` instance and bind the source PDF.
2. Create a `Stamp` object.
3. Bind the stamp to an image file with `bindImage`.
4. Add the stamp to the document with `addStamp`.
5. Save the output and close the facade object.

### Java example

```java
public static void addStampToPdf(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

The current `PdfFileStampExamples.java` class does not include a separate Java sample for text-only stamps, rotation, or opacity configuration.
