---
title: Split PDF Files in Java
linktitle: Split PDF files
type: docs
weight: 60
url: /java/split-pdf/
description: Learn how to split a PDF into single-page PDF files in Java using Aspose.PDF.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Splitting PDF pages using Java
Abstract: This article shows how to split a PDF document into separate single-page PDF files in Java using Aspose.PDF. The example opens the source document, iterates through its pages, creates a new document for each page, and saves each page as an individual PDF file.
---
Splitting a PDF into separate files is useful when you need to export each page for review, storage, or downstream processing.

## Live Example

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) is a free online application for testing PDF splitting in a browser.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

This example uses the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) class to open a PDF file and iterate through its pages. For each [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/), it creates a new document, adds the page to it, and saves the result as a separate PDF file.

To split a PDF into individual page files in Java:

1. Open the source PDF with the `Document` constructor.
1. Iterate through the pages returned by `document.getPages()`.
1. Create a new empty `Document` for each page.
1. Add the current page to the new document.
1. Save the new document with a unique file name.
1. Close both documents when processing is complete.

## Split PDF into single-page files

The following Java example is based on `SplitDocumentExamples.java` and saves pages as `Page_1.pdf`, `Page_2.pdf`, and so on.

```java
public static void splitDocument(Path inputFile, Path outputDir) {
    Document document = new Document(inputFile.toString());
    try {
        int pageCount = 1;
        for (Page page : document.getPages()) {
            Document newDocument = new Document();
            try {
                newDocument.getPages().add(page);
                newDocument.save(outputDir.resolve("Page_" + pageCount + ".pdf").toString());
            } finally {
                newDocument.close();
            }
            pageCount++;
        }
    } finally {
        document.close();
    }
}
```
