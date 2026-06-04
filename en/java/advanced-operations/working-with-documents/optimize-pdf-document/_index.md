---
title: Optimize PDF Files in Java
linktitle: Optimize PDF
type: docs
weight: 30
url: /java/optimize-pdf/
description: Learn how to optimize, compress, and reduce PDF file size in Java using Aspose.PDF.
lastmod: "2026-06-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Compress PDF resources and reduce file size with Java
Abstract: This article explains how to optimize PDF files using Aspose.PDF for Java. It covers whole-document optimization, resource compression, image quality reduction, removing unused objects and streams, linking duplicate streams, unembedding fonts, flattening annotations and forms, grayscale conversion, and Flate image compression.
---
Aspose.PDF for Java exposes optimization features through `Document.optimize`, `optimizeResources`, and `OptimizationOptions`.

## Optimize a PDF and reduce resources

1. Open the source PDF document.
1. Optimize the PDF document.
1. Save the updated PDF document.

```java
public static void optimizePdf(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        document.optimize();
        document.save(outputFile.toString());
    }
}
```

`reduceSizePdf` uses `document.optimizeResources()` for a simpler resource-reduction pass.

## Compress images and remove unused data

1. Open the source PDF document.
1. Configure optimization options and optimize the document resources.
1. Set the properties required by the example.
1. Save the updated PDF document.

```java
public static void shrinkingOrCompressingAllImages(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.getImageCompressionOptions().setCompressImages(true);
        optimizeOptions.getImageCompressionOptions().setImageQuality(50);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
}
```
