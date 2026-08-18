---
title: 使用 Java 将页面标记添加到 PDF
linktitle: 添加页戳
type: docs
weight: 30
url: /java/page-stamps-in-the-pdf-file/
description: 了解如何在 Java 中添加 PDF 页面图章作为叠加层或背景。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 将基于页面的图章添加到 PDF 文件
Abstract: 本文介绍如何使用 Aspose.PDF for Java 将页戳添加到 PDF 文档。该示例加载另一个 PDF 页面作为图章，将其配置为背景，并将其应用到目标页面。
---
Aspose.PDF for Java 可以应用另一个 PDF 中的页面作为图章或添加页码覆盖。

## 添加另一个 PDF 的页戳

当应将单独 PDF 中的页面用作背景图章时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 从外部 PDF 页面创建 [PdfPageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfpagestamp/)。
1. 配置图章并将其添加到目标页面，然后保存结果。

```java
public static void addPageStamp(Path inputFile, Path pageStampFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PdfPageStamp pageStamp = new PdfPageStamp(pageStampFile.toString(), 1);
        pageStamp.setBackground(true);
        document.getPages().get_Item(1).addStamp(pageStamp);
        document.save(outputFile.toString());
    }
}
```

## 添加标准页码印记

当目标页面应以自定义文本格式显示当前数字时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建并配置 [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/)。
1. 将图章添加到页面并保存文档。

```java
public static void addPageNumStamp(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageNumberStamp pageNumberStamp = new PageNumberStamp();
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setFormat("Page # of " + document.getPages().size());
        pageNumberStamp.setBottomMargin(10);
        pageNumberStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(1);
        pageNumberStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize(14.0f);
        pageNumberStamp.getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        pageNumberStamp.getTextState().setForegroundColor(Color.getBlueViolet());

        document.getPages().get_Item(1).addStamp(pageNumberStamp);
        document.save(outputFile.toString());
    }
}
```

## 添加罗马数字页码印记

当页码编号应从自定义值开始并使用大写罗马数字时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建 [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/) 并配置罗马数字编号。
1. 将图章添加到所有页面并保存 PDF。

```java
public static void addPageNumStampRoman(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageNumberStamp pageNumberStamp = new PageNumberStamp();
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setBottomMargin(10);
        pageNumberStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(42);
        pageNumberStamp.setNumberingStyle(NumberingStyle.NumeralsRomanUppercase);
        pageNumberStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize(14.0f);
        pageNumberStamp.getTextState().setFontStyle(FontStyles.Bold);
        pageNumberStamp.getTextState().setForegroundColor(Color.getBlueViolet());

        for (Page page : document.getPages()) {
            page.addStamp(pageNumberStamp);
        }
        document.save(outputFile.toString());
    }
}
```
