---
title: Compare PDF Documents in Java
linktitle: Compare PDF
type: docs
weight: 130
url: /java/compare-pdf-documents/
description: Learn how to compare PDF documents in Java using side-by-side and graphical difference output with Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Compare PDF pages and full documents with visual difference output in Java
Abstract: This article explains how to compare PDF documents using Aspose.PDF for Java. Learn how to compare specific pages or entire PDF files with side-by-side output, generate graphical PDF difference reports, and export page-level image differences.
---
Aspose.PDF for Java provides both side-by-side and graphical comparison APIs for detecting differences between PDF files.

## Compare two pages and export difference images

Use `GraphicalPdfComparer.getDifference` when you need image-based output for a specific page pair:

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) objects and run `GraphicalPdfComparer.getDifference` for the target [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) pair.

```java
public static void comparePdfWithGetDifferenceMethod(
        Path inputFile1, Path inputFile2, Path diffOutputFile, Path destinationOutputFile) throws Exception {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        GraphicalPdfComparer comparer = new GraphicalPdfComparer();
        ImagesDifference imagesDifference = comparer.getDifference(
                document1.getPages().get_Item(1),
                document2.getPages().get_Item(1));

        ImageIO.write(imagesDifference.differenceToImage(Color.getRed(), Color.getWhite()),
                "png", diffOutputFile.toFile());
        ImageIO.write(imagesDifference.getDestinationImage(), "png", destinationOutputFile.toFile());
        imagesDifference.dispose();
    }
}
```

This method creates a highlighted difference image and also saves the destination page image.

## Compare specific pages side by side

If you need a PDF report for selected pages, use `SideBySidePdfComparer.compare` with page objects:

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) objects and create the `SideBySideComparisonOptions` required by the example.
1. Compare the input [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) objects with `SideBySidePdfComparer.compare` and capture the result.
1. Set the comparison properties required by the example, including `ComparisonMode`.

```java
public static void comparingSpecificPages(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        SideBySideComparisonOptions options = new SideBySideComparisonOptions();
        options.setAdditionalChangeMarks(true);
        options.setComparisonMode(ComparisonMode.IgnoreSpaces);

        SideBySidePdfComparer.compare(
                document1.getPages().get_Item(1),
                document2.getPages().get_Item(1),
                outputFile.toString(),
                options);
    }
}
```

## Compare two documents graphically and save a PDF

The graphical comparer can generate a PDF output that highlights differences across the documents:

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) objects and create the `GraphicalPdfComparer`.
1. Set the comparison properties required by the example, including [Color](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/color/) and [Resolution](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.devices/resolution/).
1. Run `compareDocumentsToPdf` and save the graphical comparison output.

```java
public static void comparePdfWithCompareDocumentsToPdfMethod(
        Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        GraphicalPdfComparer pdfComparer = new GraphicalPdfComparer();
        pdfComparer.setThreshold(3.0);
        pdfComparer.setColor(Color.getBlue());
        pdfComparer.setResolution(new Resolution(300));
        pdfComparer.compareDocumentsToPdf(document1, document2, outputFile.toString());
    }
}
```

## Compare entire documents side by side

To compare all pages with side-by-side markup, pass complete `Document` objects:

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) objects and create the `SideBySideComparisonOptions` required by the example.
1. Compare the input PDF documents with `SideBySidePdfComparer.compare` and capture the result.
1. Set the comparison properties required by the example, including `ComparisonMode`.

```java
public static void comparingEntireDocuments(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        SideBySideComparisonOptions options = new SideBySideComparisonOptions();
        options.setAdditionalChangeMarks(true);
        options.setComparisonMode(ComparisonMode.IgnoreSpaces);

        SideBySidePdfComparer.compare(document1, document2, outputFile.toString(), options);
    }
}
```
