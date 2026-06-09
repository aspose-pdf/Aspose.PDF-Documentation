---
title: Split PDF Files in Java
linktitle: Split PDF files
type: docs
weight: 60
url: /java/split-pdf-document/
description: Learn how to split PDF pages into separate PDF files in Java.
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Split PDF documents by pages, ranges, groups, and filename patterns using Java
Abstract: This article explains how to split PDF documents using Aspose.PDF for Java. It covers splitting into single pages, two or three parts, odd and even pages, fixed-size chunks, custom ranges, first or last page plus the rest, custom page groups, and stable filename generation.
---
Aspose.PDF for Java supports several splitting patterns beyond one-page-per-file output.

## Split a PDF into single-page files

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create a new PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) for each [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) you want to export.
1. Add the selected [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) to the new document.
1. Save each output PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

```java
public static void splitDocuments(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        for (int pageNumber = 1; pageNumber <= document.getPages().size(); pageNumber++) {
            try (Document newDocument = new Document()) {
                newDocument.getPages().add(document.getPages().get_Item(pageNumber));
                newDocument.save(outputDir.resolve("Page_" + pageNumber + ".pdf").toString());
            }
        }
    }
}
```
