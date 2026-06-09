---
title: Create PDF Files in Java
linktitle: Create PDF Document
type: docs
weight: 10
url: /java/create-pdf-document/
description: Learn how to create PDF files and build searchable PDFs in Java using Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Create PDF files and searchable PDF documents with Java
Abstract: This article shows how to create PDF documents using Aspose.PDF for Java. It covers creating a new PDF from scratch and converting an image-based document into a searchable PDF by supplying HOCR output from an external OCR engine.
---
Aspose.PDF for Java supports both simple document creation and OCR-assisted searchable PDF workflows.

## Create a new PDF document

1. Create a new PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Add a [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) to the document.
1. Create a [TextFragment](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/textfragment/) and add it to the page.
1. Save the output PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

```java
public static void createNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment("Hello World!"));
        document.save(outputFile.toString());
    }
}
```

## Create a searchable PDF

The `createSearchablePdf` example uses `Document.convert(...)` with a `CallBackGetHocr` implementation. The callback writes the source image to a temporary file, invokes Tesseract with the `hocr` option, reads the generated HOCR markup, and returns it to Aspose.PDF:

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create the `CallBackGetHocr` callback and convert the source document to searchable PDF content.
1. Save the updated PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

```java
public static void createSearchablePdf(Path inputFile, Path outputFile) {
    Path tempDir = outputFile.getParent().resolve("ocr-temp");
    CallBackGetHocr cbgh = new CallBackGetHocr() {
        @Override
        public String invoke(java.awt.image.BufferedImage img) {
            // save the image, run Tesseract with "hocr", and return the HOCR text
            return fileContents.toString();
        }
    };
    try (Document document = new Document(inputFile.toString())) {
        document.convert(cbgh);
        document.save(outputFile.toString());
    }
}
```
