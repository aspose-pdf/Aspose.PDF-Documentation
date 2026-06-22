---
title: Optimize PDF Files in Java
linktitle: Optimize PDF
type: docs
weight: 30
url: /java/optimize-pdf/
description: Learn how to optimize, compress, and reduce PDF file size in Java using Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Compress PDF resources and reduce file size with Java
Abstract: This article explains how to optimize PDF files using Aspose.PDF for Java. It covers whole-document optimization, resource compression, image quality reduction, removing unused objects and streams, linking duplicate streams, unembedding fonts, flattening annotations and forms, grayscale conversion, and Flate image compression.
---
Aspose.PDF for Java exposes optimization features through `Document.optimize`, `optimizeResources`, and `OptimizationOptions`.

## Optimize a PDF with general document optimization

Use this example when you want Aspose.PDF to apply the built-in whole-document optimization routine.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Call `optimize()` on the document.
1. Save the optimized file and compare the original and output sizes.

```java
public static void optimizePdf(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        document.optimize();
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## Reduce PDF size by optimizing resources

This example focuses on resource-level optimization without manually configuring individual options.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Run `optimizeResources()` to optimize internal resources.
1. Save the result and print the input and output file sizes.

```java
public static void reduceSizePdf(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        document.optimizeResources();
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## Compress all images in a PDF

Use this approach when image-heavy documents need a smaller file size and some image quality reduction is acceptable.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Create [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.optimization/optimizationoptions/) and enable image compression with the required quality level.
1. Optimize the document resources with those settings.
1. Save the optimized file and compare file sizes.

```java
public static void shrinkingOrCompressingAllImages(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.getImageCompressionOptions().setCompressImages(true);
        optimizeOptions.getImageCompressionOptions().setImageQuality(50);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## Remove unused objects from a PDF

This example removes unused objects that may remain in the document structure after edits or merges.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Create [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) and enable removal of unused objects.
1. Optimize the resources and save the updated file.
1. Print the original and reduced file sizes.

```java
public static void removingUnusedObjects(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setRemoveUnusedObjects(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## Remove unused streams from a PDF

Use this approach when you want to discard stream data that is no longer referenced by the document.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Configure [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) to remove unused streams.
1. Optimize the resources, save the output document, and compare file sizes.

```java
public static void removingUnusedStreams(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setRemoveUnusedStreams(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## Link duplicate streams in a PDF

This example deduplicates repeated streams so identical content can be stored only once.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Create [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) and enable duplicate stream linking.
1. Optimize the resources, save the output document, and print the file sizes.

```java
public static void linkingDuplicateStreams(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setLinkDuplicateStreams(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## Unembed fonts from a PDF

Use this option when reducing file size is more important than keeping embedded font data in the output.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Configure [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) to unembed fonts.
1. Optimize the resources, save the document, and compare file sizes.

```java
public static void unembedFonts(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setUnembedFonts(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## Flatten annotations in a PDF

This example converts annotations into static page content so they no longer remain interactive objects.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterate through each [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) and its [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) collection.
1. Flatten every annotation and save the updated document.

```java
public static void flattenAnnotations(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            for (Annotation annotation : page.getAnnotations()) {
                annotation.flatten();
            }
        }
        document.save(outputFile.toString());
    }
}
```

## Flatten PDF form fields

Use this approach when fillable form fields should become fixed content before distribution or archiving.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Check whether the document contains form widgets.
1. Flatten each [Field](https://reference.aspose.com/pdf/java/com.aspose.pdf/field/) represented by a [WidgetAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/widgetannotation/).
1. Save the output file and print the file sizes.

```java
public static void flattenForms(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getForm() != null && document.getForm().size() > 0) {
            for (WidgetAnnotation annotation : document.getForm()) {
                if (annotation instanceof Field field) {
                    field.flatten();
                }
            }
        }
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## Convert a PDF to grayscale

This example changes each page to grayscale, which can help reduce color complexity and standardize output for archival or printing workflows.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterate through each [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) in the document.
1. Call `makeGrayscale()` on every page and save the output file.

```java
public static void convertPdfFromRgbColorspaceToGrayscale(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            page.makeGrayscale();
        }
        document.save(outputFile.toString());
    }
}
```

## Use FlateDecode image compression

Use this pattern when you want to apply Flate-based compression to images during PDF resource optimization.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Create [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) and set the image encoding to [ImageEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageencoding/).`Flate`.
1. Optimize the document resources and save the output file.

```java
public static void usingFlatedecodeCompression(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizationOptions = new OptimizationOptions();
        optimizationOptions.getImageCompressionOptions().setEncoding(ImageEncoding.Flate);
        document.optimizeResources(optimizationOptions);
        document.save(outputFile.toString());
    }
}
```

## Print original and optimized file sizes

This helper method reports the size difference between the source file and the optimized output file.

1. Read the size of the input file.
1. Read the size of the output file.
1. Print both values in a single status message.

```java
private static void printFileSizes(Path inputFile, Path outputFile) throws Exception {
    System.out.println("Original file size: " + Files.size(inputFile)
            + ". Reduced file size: " + Files.size(outputFile));
}
```
