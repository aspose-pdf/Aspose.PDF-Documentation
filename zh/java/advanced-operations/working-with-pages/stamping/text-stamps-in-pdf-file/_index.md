---
title: 在 Java 中向 PDF 添加文本水印
linktitle: PDF 文件中的文本水印
type: docs
weight: 20
url: /zh/java/text-stamps-in-the-pdf-file/
description: 了解如何在 Java 中向 PDF 文档添加文本水印。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 向 PDF 文件添加文本水印
Abstract: 本文说明了如何使用 Aspose.PDF for Java 向 PDF 文件添加文本水印。内容包括创建背景文本水印、设置位置、旋转以及自定义字体、大小、样式和颜色。
---
当需要在 PDF 页面添加可见标签或水印时，请使用文本水印。

## 添加文本印章

当页面需要显示带有自定义样式的旋转文本印章时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建一个 [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstamp/) 并配置其放置位置和文本外观。
1. 将印章添加到目标页面并保存文档。

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
