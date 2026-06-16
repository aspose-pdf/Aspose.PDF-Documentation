---
title: Create PDF Portfolios in Java
linktitle: Portfolio
type: docs
weight: 20
url: /java/portfolio/
description: Learn how to create and manage PDF portfolios in Java using Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Build and edit PDF portfolios with embedded files in Java
Abstract: This article explains how to create and manage PDF portfolios using Aspose.PDF for Java. Learn how to enable a collection on a document, add multiple file types to the portfolio, and remove all collection items from an existing PDF portfolio.
---
A PDF portfolio can bundle multiple files inside a single PDF container while preserving each file in its original format.

## Create a PDF portfolio

Use this example when you need to package several files into a PDF portfolio collection.

1. Create a new PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) and enable its [Collection](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/collection/).
1. Create [FileSpecification](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/filespecification/) objects for each input file and set their descriptions.
1. Add the files to the portfolio collection and save the output document.

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

Use this example when an existing PDF portfolio collection should be cleared.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Delete the document collection entries.
1. Save the cleaned output document.

```java
public static void removeFilesFromPdfPortfolio(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getCollection().delete();
        document.save(outputFile.toString());
    }
}
```
