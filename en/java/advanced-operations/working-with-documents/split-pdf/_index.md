---
title: Split PDF Files in Java
linktitle: Split PDF files
type: docs
weight: 60
url: /java/split-pdf-document/
description: Learn how to split PDF pages into separate PDF files in Java.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Split PDF documents by pages, ranges, groups, and filename patterns using Java
Abstract: This article explains how to split PDF documents using Aspose.PDF for Java. It covers splitting into single pages, two or three parts, odd and even pages, fixed-size chunks, custom ranges, first or last page plus the rest, custom page groups, and stable filename generation.
---
Aspose.PDF for Java supports several splitting patterns beyond one-page-per-file output.

## Split a PDF into single-page files

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

## Split by parts, ranges, or N pages

The example class also includes:

- `splitDocumentsIntoTwoParts`
- `splitDocumentsIntoThreeParts`
- `splitDocumentsEveryNPages`
- `splitDocumentsByPageRanges`

## Split first or last page from the rest

`splitDocumentsFirstPageAndRest` and `splitDocumentsLastPageAndRest` create separate files for a leading or trailing page while keeping the remaining pages together.

## Split odd and even pages or custom page groups

`splitDocumentsOddEvenPages` creates `Odd_Pages.pdf` and `Even_Pages.pdf`. `splitDocumentsCustomPageGroups` creates grouped output based on explicit page-number lists.

## Generate stable file names

`splitDocumentsWithStableFilenames` uses `String.format("Page_%03d.pdf", pageNumber)` so the output remains naturally sortable.
