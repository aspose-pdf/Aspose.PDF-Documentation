---
title: 使用 Java 将文本图章添加到 PDF
linktitle: PDF 文件中的文本图章
type: docs
weight: 20
url: /java/text-stamps-in-the-pdf-file/
description: 了解如何使用 Java 将文本图章添加到 PDF 文档。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 将文本图章添加到 PDF 文件
Abstract: 本文介绍如何使用 Aspose.PDF for Java 将文本图章添加到 PDF 文件。它包括创建背景文本图章、定位、旋转以及自定义字体、大小、样式和颜色。
---
当您需要向 PDF 页面添加可见标签或水印时，请使用文本图章。

## 添加文本印记

当页面应显示具有自定义样式的旋转文本图章时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建 [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstamp/) 并配置其位置和文本外观。
1. 将图章添加到目标页面并保存文档。

```java
public static void addTextStamp(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextStamp textStamp = new TextStamp("Sample Stamp");
        textStamp.setBackground(true);
        textStamp.setXIndent(100);
        textStamp.setYIndent(100);
        textStamp.setRotate(Rotation.on90);
        textStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        textStamp.getTextState().setFontSize(14.0f);
        textStamp.getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        textStamp.getTextState().setForegroundColor(Color.getDarkGreen());
        document.getPages().get_Item(1).addStamp(textStamp);
        document.save(outputFile.toString());
    }
}
```
