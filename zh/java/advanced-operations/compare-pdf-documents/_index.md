---
title: 在 Java 中比较 PDF 文档
linktitle: 比较 PDF
type: docs
weight: 130
url: /java/compare-pdf-documents/
description: 了解如何使用 Aspose.PDF 并排和图形差异输出来比较 Java 中的 PDF 文档。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 通过 Java 中的视觉差异输出比较 PDF 页面和完整文档
Abstract: 本文介绍如何使用 Aspose.PDF for Java 比较 PDF 文档。了解如何通过并排输出比较特定页面或整个 PDF 文件、生成图形 PDF 差异报告以及导出页面级图像差异。
---
Aspose.PDF for Java 提供并排和图形比较 API，用于检测 PDF 文件之间的差异。

## 比较页面并导出差异图像

当您需要针对特定​​的一对 PDF 页面进行基于图像的差异输出时，请使用此示例。

1. 打开两个源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 对象。
1. 使用 [GraphicalPdfComparer](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/graphicalpdfcomparer/) 获取页面级 [ImagesDifference](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/imagesdifference/)。
1. 使用“GraphicalPdfComparer”获取页面级“ImagesDifference”。
1. 导出生成的差异图像并处理比较结果。

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

## 并排比较特定页面

当仅应比较选定的页面并将其保存为并排 PDF 结果时，请使用此示例。

1. 打开两个源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 对象。
1. 配置 [SideBySideComparisonOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/sidebysidecomparisonoptions/) 以获得所需的比较模式。
1. 比较所选页面并保存输出 PDF。

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

## 以图形方式比较完整的 PDF 文档

此示例生成一个图形 PDF 报告，突出显示整个文档的视觉差异。

1. 打开两个源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 对象。
1. 配置 [GraphicalPdfComparer](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/graphicalpdfcomparer/) 阈值、颜色和分辨率。
1. 比较完整文档并保存图形输出 PDF。

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

## 并排比较整个文档

当需要在并排 PDF 输出中逐页比较整个文档时，请使用此示例。

1. 打开两个源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 对象。
1. 配置 [SideBySideComparisonOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/sidebysidecomparisonoptions/) 以获得所需的比较行为。
1. 比较完整文档并将结果保存为 PDF。

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
