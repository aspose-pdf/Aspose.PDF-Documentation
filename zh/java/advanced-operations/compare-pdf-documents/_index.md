---
title: 在 Java 中比较 PDF 文档
linktitle: 比较 PDF
type: docs
weight: 130
url: /zh/java/compare-pdf-documents/
description: 了解如何在 Java 中使用 Aspose.PDF 通过并排和图形差异输出比较 PDF 文档。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中通过可视差异输出比较 PDF 页面和完整文档
Abstract: 本文介绍了如何使用 Aspose.PDF for Java 对 PDF 文档进行比较。了解如何比较特定页面或整个 PDF 文件并生成并排输出，生成图形化 PDF 差异报告，并导出页面级别的图像差异。
---
Aspose.PDF for Java 提供了并排和图形化比较 API，用于检测 PDF 文件之间的差异。

## 比较页面并导出差异图像

当您需要针对特定 PDF 页面对生成基于图像的差异输出时，请使用此示例。

1. 打开两个源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 对象。
1. 使用 [GraphicalPdfComparer](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/graphicalpdfcomparer/) 获取页面级别的 [ImagesDifference](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/imagesdifference/)。
1. 使用 'GraphicalPdfComparer' 来获取页面级别的 'ImagesDifference'。
1. 导出生成的差异图像并释放比较结果。

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

当仅需比较选定页面并将其保存为并排 PDF 结果时，请使用此示例。

1. 打开两个源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 对象。
1. 配置 [SideBySideComparisonOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/sidebysidecomparisonoptions/) 用于所需的比较模式。
1. 比较选定的页面并保存输出 PDF。

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

此示例生成一个图形化的 PDF 报告，突出显示整个文档中的视觉差异。

1. 打开两个源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 对象。
1. 配置 [GraphicalPdfComparer](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/graphicalpdfcomparer/) 阈值、颜色和分辨率。
1. 比较完整的文档并保存图形化输出 PDF。

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

当需要将整个文档逐页进行对比并生成并排的 PDF 输出时，请使用此示例。

1. 打开两个源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 对象。
1. 配置 [SideBySideComparisonOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/sidebysidecomparisonoptions/) 以实现所需的比较行为。
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
