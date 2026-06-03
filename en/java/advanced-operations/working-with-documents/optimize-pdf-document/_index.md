---
title: Optimize PDF Files in Java
linktitle: Optimize PDF
type: docs
weight: 30
url: /java/optimize-pdf/
description: Learn how to optimize, compress, and reduce PDF file size in Java using Aspose.PDF.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Compress PDF resources and reduce file size with Java
Abstract: This article explains how to optimize PDF files using Aspose.PDF for Java. It covers whole-document optimization, resource compression, image quality reduction, removing unused objects and streams, linking duplicate streams, unembedding fonts, flattening annotations and forms, grayscale conversion, and Flate image compression.
---
Aspose.PDF for Java exposes optimization features through `Document.optimize`, `optimizeResources`, and `OptimizationOptions`.

## Optimize a PDF and reduce resources

1. Open or create the PDF document used in this example.
2. Use the Aspose.PDF API calls shown in the snippet to optimize a PDF and reduce resources.
3. Save the document or inspect the result, depending on the scenario.

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

1. Open or create the PDF document used in this example.
2. Use the Aspose.PDF API calls shown in the snippet to compress images and remove unused data.
3. Save the document or inspect the result, depending on the scenario.

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


