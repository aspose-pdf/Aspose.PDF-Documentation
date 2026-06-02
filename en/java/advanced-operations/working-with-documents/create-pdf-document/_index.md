---
title: Create PDF Files in Java
linktitle: Create PDF Document
type: docs
weight: 10
url: /java/create-pdf-document/
description: Learn how to create PDF files and build searchable PDFs in Java using Aspose.PDF.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Create PDF files and searchable PDF documents with Java
Abstract: This article shows how to create PDF documents using Aspose.PDF for Java. It covers creating a new PDF from scratch and converting an image-based document into a searchable PDF by supplying HOCR output from an external OCR engine.
---
Aspose.PDF for Java supports both simple document creation and OCR-assisted searchable PDF workflows.

## Create a new PDF document

1. Initialize the PDF document and any resources required by this example.
2. Build and configure the Aspose.PDF objects needed to create a new PDF document.
3. Save the output document or generated file.

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

1. Initialize the PDF document and any resources required by this example.
2. Build and configure the Aspose.PDF objects needed to create a searchable PDF.
3. Save the output document or generated file.

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

This flow depends on an external OCR engine that can produce HOCR output. The example source is written around Tesseract.
