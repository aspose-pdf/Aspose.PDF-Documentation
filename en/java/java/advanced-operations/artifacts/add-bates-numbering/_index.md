---
title: Add Bates Numbering to PDF in Java
linktitle: Adding Bates Numbering
type: docs
weight: 10
url: /java/add-bates-numbering/
description: Learn how to add and remove Bates numbering in PDF documents using Java with Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add Bates Numbering via Java
Abstract: This article explains how to create and remove Bates numbering artifacts in PDF documents using Aspose.PDF for Java. It covers configuring a `BatesNArtifact`, applying it through Bates numbering helpers or generic pagination helpers, and removing Bates numbering from a document.
---
Bates numbering artifacts are useful in legal, archival, and document-control workflows where each page needs a persistent page-level identifier.

## Add Bates numbering with the dedicated helper

Use this example when you want to apply Bates numbering through the dedicated page collection helper.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) and add any extra pages required by the sample.
1. Create the [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/) configuration.
1. Apply Bates numbering to the page collection and save the output file.

```java
public static void addBatesNArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = 0; i < 2; i++) {
            document.getPages().add();
        }

        BatesNArtifact batesArtifact = createBatesArtifact();
        PageCollectionExtensions.addBatesNumbering(document.getPages(), batesArtifact);
        document.save(outputFile.toString());
    }
}
```

## Add Bates numbering through pagination artifacts

This example applies Bates numbering by passing the Bates artifact through the generic pagination API.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) and add the required pages.
1. Create the [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/) and add it to a pagination artifact list.
1. Apply the pagination artifacts to the page collection and save the document.

```java
public static void addBatesNArtifactPagination(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = 0; i < 2; i++) {
            document.getPages().add();
        }

        BatesNArtifact batesArtifact = createBatesArtifact();
        List<PaginationArtifact> paginationArtifacts = new ArrayList<>();
        paginationArtifacts.add(batesArtifact);
        PageCollectionExtensions.addPagination(document.getPages(), paginationArtifacts);
        document.save(outputFile.toString());
    }
}
```

## Delete Bates numbering

Use this approach when existing Bates numbering artifacts should be removed from the document.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Call the page collection helper that deletes Bates numbering.
1. Save the cleaned output file.

```java
public static void deleteBatesNumbering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageCollectionExtensions.deleteBatesNumbering(document.getPages());
        document.save(outputFile.toString());
    }
}
```
