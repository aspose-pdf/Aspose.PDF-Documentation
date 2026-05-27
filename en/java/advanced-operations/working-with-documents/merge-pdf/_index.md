---
title: Merge PDF Files in Java
linktitle: Merge PDF files
type: docs
weight: 50
url: /java/merge-pdf-documents/
description: Learn how to merge multiple PDF files into a single document in Java.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Combine full documents, selected ranges, and alternating pages with Java
Abstract: This article explains how to merge PDF documents using Aspose.PDF for Java. It covers combining two files, merging multiple documents, selecting page ranges, inserting one document into another at a specific position, alternating pages, and building merged output with section bookmarks.
---
Aspose.PDF for Java supports several merge strategies depending on how the output should be assembled.

## Merge two PDF documents

```java
public static void mergeTwoDocuments(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        document1.getPages().add(document2.getPages());
        document1.save(outputFile.toString());
    }
}
```

## Merge multiple documents or selected ranges

The example class also includes:

- `mergeMultipleDocuments` to append all pages from a list of input files.
- `mergeSelectedPageRanges` to combine only the requested pages from each source.
- `mergeInsertDocumentAtPosition` to insert one document after a chosen page number.

## Merge alternating pages

`mergeAlternatingPages` interleaves pages from two documents one by one until both sources are exhausted.

## Merge with section separators and bookmarks

`mergeWithSectionSeparatorsAndBookmarks` creates a separator page for each source document and adds `OutlineItemCollection` bookmarks so the merged output remains navigable.
