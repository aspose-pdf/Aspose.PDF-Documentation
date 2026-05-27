---
title: Create PDF Portfolios in Java
linktitle: Portfolio
type: docs
weight: 20
url: /java/portfolio/
description: Learn how to create and manage PDF portfolios in Java using Aspose.PDF.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Build and edit PDF portfolios with embedded files in Java
Abstract: This article explains how to create and manage PDF portfolios using Aspose.PDF for Java. Learn how to enable a collection on a document, add multiple file types to the portfolio, and remove all collection items from an existing PDF portfolio.
---
A PDF portfolio can bundle multiple files inside a single PDF container while preserving each file in its original format.

## Create a PDF portfolio

The following example creates a new document, enables a collection, and adds several files as portfolio items:

```java
public static void createPdfPortfolio(Path[] inputFiles, Path outputFile) {
    try (Document document = new Document()) {
        document.setCollection(new Collection());

        FileSpecification excel = new FileSpecification(inputFiles[0].toString());
        FileSpecification word = new FileSpecification(inputFiles[1].toString());
        FileSpecification image = new FileSpecification(inputFiles[2].toString());

        excel.setDescription("Excel File");
        word.setDescription("Word File");
        image.setDescription("Image File");

        document.getCollection().add(excel);
        document.getCollection().add(word);
        document.getCollection().add(image);

        document.save(outputFile.toString());
    }
}
```

## Remove files from a PDF portfolio

To clear the collection items from an existing portfolio, use `Collection.delete()`:

```java
public static void removeFilesFromPdfPortfolio(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getCollection().delete();
        document.save(outputFile.toString());
    }
}
```
