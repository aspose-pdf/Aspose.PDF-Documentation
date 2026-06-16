---
title: Merge PDF Files in Java
linktitle: Merge PDF files
type: docs
weight: 50
url: /java/merge-pdf-documents/
description: Learn how to merge multiple PDF files into a single document in Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Combine full documents, selected ranges, and alternating pages with Java
Abstract: This article explains how to merge PDF documents using Aspose.PDF for Java. It covers combining two files, merging multiple documents, selecting page ranges, inserting one document into another at a specific position, alternating pages, and building merged output with section bookmarks.
---
Aspose.PDF for Java supports several merge strategies depending on how the output should be assembled.

## Merge two PDF documents

Use this approach when you need the simplest merge flow and want to append one complete document to another.

1. Open both source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) objects.
1. Add the [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) collection from the second document to the first document.
1. Save the updated PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

```java
public static void mergeTwoDocuments(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        document1.getPages().add(document2.getPages());
        document1.save(outputFile.toString());
    }
}
```

## Copy a selected page range between documents

This helper method keeps page-range merge logic in one place so other examples can reuse the same validated copy routine.

1. Open or receive the source and destination PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) objects.
1. Normalize the requested page range so it stays within the available [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) collection.
1. Add each page from the validated range to the destination document.

```java
private static void appendPageRange(Document sourceDocument, Document destinationDocument, int startPage, int endPage) {
    int totalPages = sourceDocument.getPages().size();
    if (totalPages == 0) {
        return;
    }

    int start = Math.max(1, startPage);
    int end = Math.min(endPage, totalPages);
    if (start > end) {
        return;
    }

    for (int pageNumber = start; pageNumber <= end; pageNumber++) {
        destinationDocument.getPages().add(sourceDocument.getPages().get_Item(pageNumber));
    }
}
```

## Merge multiple PDF documents into one file

Use this pattern when you need to combine a list of input files into a single output document in sequence.

1. Create an empty output PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Open each input file one at a time and copy its full [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) range into the output document.
1. Save the merged result after all source files have been processed.

```java
public static void mergeMultipleDocuments(List<Path> inputFiles, Path outputFile) {
    try (Document outputDocument = new Document()) {
        for (Path inputFile : inputFiles) {
            try (Document sourceDocument = new Document(inputFile.toString())) {
                appendPageRange(sourceDocument, outputDocument, 1, sourceDocument.getPages().size());
            }
        }
        outputDocument.save(outputFile.toString());
    }
}
```

## Merge selected page ranges from two documents

This example creates a custom output file by taking only specific page ranges from each source document.

1. Open both source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) objects and create a new output document.
1. Add only the required [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) ranges from each source document.
1. Save the assembled output document.

```java
public static void mergeSelectedPageRanges(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString());
         Document outputDocument = new Document()) {
        appendPageRange(document1, outputDocument, 1, 2);
        appendPageRange(document2, outputDocument, 2, 3);
        outputDocument.save(outputFile.toString());
    }
}
```

## Insert one PDF document into another at a specific position

Use this approach when one document should appear inside another instead of only before or after it.

1. Open the base and inserted PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) objects and create a new output document.
1. Copy the first part of the base document, then append the full inserted document, and finally append the remaining base [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) range.
1. Save the reordered result to a new file.

```java
public static void mergeInsertDocumentAtPosition(Path inputFile1, Path inputFile2, int insertAfterPage, Path outputFile) {
    try (Document baseDocument = new Document(inputFile1.toString());
         Document insertDocument = new Document(inputFile2.toString());
         Document outputDocument = new Document()) {
        int baseTotalPages = baseDocument.getPages().size();
        int insertIndex = Math.max(0, Math.min(insertAfterPage, baseTotalPages));

        appendPageRange(baseDocument, outputDocument, 1, insertIndex);
        appendPageRange(insertDocument, outputDocument, 1, insertDocument.getPages().size());
        appendPageRange(baseDocument, outputDocument, insertIndex + 1, baseTotalPages);

        outputDocument.save(outputFile.toString());
    }
}
```

## Merge two PDF documents by alternating pages

This example interleaves pages from two documents, which is useful when both inputs should contribute page-by-page to the final output.

1. Open both source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) objects and create a new output document.
1. Loop through the maximum available page count and add each available [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) from the first and second documents in turn.
1. Save the interleaved output document.

```java
public static void mergeAlternatingPages(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString());
         Document outputDocument = new Document()) {
        int document1Pages = document1.getPages().size();
        int document2Pages = document2.getPages().size();
        int maxPages = Math.max(document1Pages, document2Pages);

        for (int pageNumber = 1; pageNumber <= maxPages; pageNumber++) {
            if (pageNumber <= document1Pages) {
                outputDocument.getPages().add(document1.getPages().get_Item(pageNumber));
            }
            if (pageNumber <= document2Pages) {
                outputDocument.getPages().add(document2.getPages().get_Item(pageNumber));
            }
        }

        outputDocument.save(outputFile.toString());
    }
}
```

## Merge documents with separator pages and bookmarks

Use this pattern when the merged file should remain easy to navigate and clearly show where each source document starts.

1. Create an empty output PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) and open each source file in turn.
1. Add a separator [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) with a heading, then create an [OutlineItemCollection](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/outlineitemcollection/) bookmark for that section.
1. Append the source pages, optionally add a bookmark that points to the first content page, and save the final merged document.

```java
public static void mergeWithSectionSeparatorsAndBookmarks(List<Path> inputFiles, Path outputFile) {
    try (Document outputDocument = new Document()) {
        int sectionIndex = 1;
        for (Path inputFile : inputFiles) {
            try (Document sourceDocument = new Document(inputFile.toString())) {
                int sourcePageCount = sourceDocument.getPages().size();

                Page separatorPage = outputDocument.getPages().add();
                separatorPage.getParagraphs().add(new TextFragment(
                        "Section " + sectionIndex + ": " + inputFile.getFileName()));

                OutlineItemCollection sectionBookmark = new OutlineItemCollection(outputDocument.getOutlines());
                sectionBookmark.setTitle("Section " + sectionIndex);
                sectionBookmark.setAction(new GoToAction(separatorPage));
                outputDocument.getOutlines().add(sectionBookmark);

                int firstContentPageNumber = outputDocument.getPages().size() + 1;
                appendPageRange(sourceDocument, outputDocument, 1, sourcePageCount);

                if (sourcePageCount > 0 && firstContentPageNumber <= outputDocument.getPages().size()) {
                    OutlineItemCollection contentBookmark = new OutlineItemCollection(outputDocument.getOutlines());
                    contentBookmark.setTitle("Section " + sectionIndex + " Content");
                    contentBookmark.setAction(new GoToAction(outputDocument.getPages().get_Item(firstContentPageNumber)));
                    sectionBookmark.add(contentBookmark);
                }
            }
            sectionIndex++;
        }

        outputDocument.save(outputFile.toString());
    }
}
```
