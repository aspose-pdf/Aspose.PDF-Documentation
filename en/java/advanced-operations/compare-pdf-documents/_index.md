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

## Compare pages and export difference images

Use this example when you need image-based difference output for a specific pair of PDF pages.

1. Open both source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) objects.
1. Use [GraphicalPdfComparer](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/comparison/graphicalpdfcomparer/) to get the page-level [ImagesDifference](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/comparison/imagesdifference/).
1. Export the generated difference images and dispose the comparison result.

```java
public static void comparePdfWithGetDifferenceMethod(
        Path inputFile1, Path inputFile2, Path diffOutputFile, Path destinationOutputFile) throws Exception {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        GraphicalPdfComparer comparer = new GraphicalPdfComparer();
        ImagesDifference imagesDifference = comparer.getDifference(document1.getPages().get_Item(1),
                document2.getPages().get_Item(1));

        ImageIO.write(imagesDifference.differenceToImage(Color.getRed(), Color.getWhite()),
                "png", diffOutputFile.toFile());
        ImageIO.write(imagesDifference.getDestinationImage(), "png", destinationOutputFile.toFile());
        imagesDifference.dispose();
    }
    System.out.println("Difference images saved to " + diffOutputFile + " and " + destinationOutputFile);
}
```

## Compare specific pages side by side

Use this example when only selected pages should be compared and saved as a side-by-side PDF result.

1. Open both source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) objects.
1. Configure [SideBySideComparisonOptions](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/comparison/sidebysidecomparisonoptions/) for the required comparison mode.
1. Compare the selected pages and save the output PDF.

```java
public static void comparingSpecificPages(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        SideBySideComparisonOptions options = new SideBySideComparisonOptions();
        options.setAdditionalChangeMarks(true);
        options.setComparisonMode(ComparisonMode.IgnoreSpaces);

        SideBySidePdfComparer.compare(document1.getPages().get_Item(1), document2.getPages().get_Item(1),
                outputFile.toString(), options);
    }
    System.out.println("Specific pages comparison saved to " + outputFile);
}
```

## Compare full PDF documents graphically

This example generates a graphical PDF report that highlights visual differences across the entire documents.

1. Open both source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) objects.
1. Configure the [GraphicalPdfComparer](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/comparison/graphicalpdfcomparer/) threshold, color, and resolution.
1. Compare the full documents and save the graphical output PDF.

```java
public static void comparePdfWithCompareDocumentsToPdfMethod(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        GraphicalPdfComparer pdfComparer = new GraphicalPdfComparer();
        pdfComparer.setThreshold(3.0);
        pdfComparer.setColor(Color.getBlue());
        pdfComparer.setResolution(new Resolution(300));
        pdfComparer.compareDocumentsToPdf(document1, document2, outputFile.toString());
    }
    System.out.println("Graphical comparison saved to " + outputFile);
}
```

## Compare entire documents side by side

Use this example when the whole documents should be compared page by page in a side-by-side PDF output.

1. Open both source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) objects.
1. Configure [SideBySideComparisonOptions](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/comparison/sidebysidecomparisonoptions/) for the desired comparison behavior.
1. Compare the full documents and save the result as a PDF.

```java
public static void comparingEntireDocuments(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        SideBySideComparisonOptions options = new SideBySideComparisonOptions();
        options.setAdditionalChangeMarks(true);
        options.setComparisonMode(ComparisonMode.IgnoreSpaces);

        SideBySidePdfComparer.compare(document1, document2, outputFile.toString(), options);
    }
    System.out.println("Entire document comparison saved to " + outputFile);
}
```
