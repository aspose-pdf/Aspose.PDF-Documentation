---
title: Merge PDF Files in Java
linktitle: Merge PDF files
type: docs
weight: 50
url: /java/merge-pdf/
description: Learn how to merge multiple PDF files into a single document in Java using Aspose.PDF.
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Combine PDF pages using Java
Abstract: This article explains how to merge two PDF documents in Java using Aspose.PDF. The example opens two source documents, appends the pages of the second document to the first one, and saves the merged result as a new PDF file.
---

Merging PDF files is useful when you need to combine related documents into a single file for distribution, archiving, or processing.

## Live Example

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) is a free online application for testing PDF merging in a browser.

This topic shows how to merge multiple PDF files into a single document in Java:

1. Open both source documents with the [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) constructor.
1. Append the [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) collection from the second [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) to the first one with `document1.getPages().add(document2.getPages())`.
1. Save the merged [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) to the output path.

## Merge two PDF documents

The following Java example is based on `MergeDocumentExamples.java`.

```java
public static void mergeTwoDocuments(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        document1.getPages().add(document2.getPages());
        document1.save(outputFile.toString());
    }
}
```
