---
title: Add Footer to PDF
type: docs
weight: 10
url: /java/add-footer/
description: Learn how to add text and image footers to PDF pages in Java with the PdfFileStamp facade.
lastmod: "2026-06-03"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add text and image footers to PDF in Java
Abstract: Learn how to add footer content to PDF documents with Aspose.PDF for Java using the PdfFileStamp facade. The Java examples cover plain text footers, image footers loaded from a stream, and text footers with explicit left, right, and bottom margins.
---
## Add footer to PDF

Use `PdfFileStamp` when you need repeated footer content on every page of a document.

### Steps

1. Create a `PdfFileStamp` instance and bind the source PDF.
2. Build the footer content as either `FormattedText` or an image stream.
3. Call the appropriate `addFooter` overload.
4. Save the updated file and close the facade object.

### Java examples

```java
public static void addTextFooter(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText("Sample Footer");
        pdfStamper.addFooter(text, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addImageFooter(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try (InputStream imageStream = Files.newInputStream(imageFile)) {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addFooter(imageStream, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addFooterWithMargins(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText("This footer has margins on all sides.");
        pdfStamper.addFooter(text, 20, 20, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```
