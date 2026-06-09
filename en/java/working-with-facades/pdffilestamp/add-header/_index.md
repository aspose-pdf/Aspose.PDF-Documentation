---
title: Add Header to PDF
type: docs
weight: 20
url: /java/add-header/
description: Learn how to add text and image headers to PDF pages in Java with the PdfFileStamp facade.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add text and image headers to PDF in Java
Abstract: Learn how to add header content to PDF documents with Aspose.PDF for Java using the PdfFileStamp facade. The Java examples cover plain text headers, image headers loaded from a stream, and styled headers with explicit margin values.
---
## Add header to PDF

Use `PdfFileStamp` when you need repeated header content on each page.

### Steps

1. Create a `PdfFileStamp` instance and bind the source PDF.
2. Build the header content as `FormattedText` or load it from an image stream.
3. Call the appropriate `addHeader` overload.
4. Save the output and close the facade object.

### Java examples

```java
public static void addTextHeader(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText("Sample Header");
        pdfStamper.addHeader(text, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addImageHeader(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try (InputStream imageStream = Files.newInputStream(imageFile)) {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addHeader(imageStream, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addHeaderWithMargins(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText(
                "Sample Header",
                Color.BLUE,
                FontStyle.Helvetica,
                EncodingType.Winansi,
                true,
                12.0f);
        pdfStamper.addHeader(text, 20, 20, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```
