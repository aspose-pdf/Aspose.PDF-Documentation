---
title: Add Bates Numbering to PDF in Java
linktitle: Adding Bates Numbering
type: docs
weight: 10
url: /java/add-bates-numbering/
description: Learn how to add and remove Bates numbering in PDF documents using Java with Aspose.PDF.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add Bates Numbering via Java
Abstract: This article explains how to create and remove Bates numbering artifacts in PDF documents using Aspose.PDF for Java. It covers configuring a `BatesNArtifact`, applying it through Bates numbering helpers or generic pagination helpers, and removing Bates numbering from a document.
---
## Create a Bates numbering artifact

```java
public static BatesNArtifact createBatesArtifact() {
    BatesNArtifact artifact = new BatesNArtifact();
    artifact.setStartPage(1);
    artifact.setEndPage(0);
    artifact.setSubset(Subset.All);
    artifact.setNumberOfDigits(6);
    artifact.setStartNumber(1);
    artifact.setPrefix("");
    artifact.setSuffix("");
    artifact.setArtifactVerticalAlignment(VerticalAlignment.Bottom);
    artifact.setArtifactHorizontalAlignment(HorizontalAlignment.Right);
    artifact.setRightMargin(72);
    artifact.setLeftMargin(72);
    artifact.setTopMargin(36);
    artifact.setBottomMargin(36);
    return artifact;
}
```

## Add or remove Bates numbering

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

```java
public static void deleteBatesNumbering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageCollectionExtensions.deleteBatesNumbering(document.getPages());
        document.save(outputFile.toString());
    }
}
```
