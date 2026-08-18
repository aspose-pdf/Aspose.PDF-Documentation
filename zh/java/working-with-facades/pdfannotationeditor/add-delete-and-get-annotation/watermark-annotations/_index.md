---
title: 使用 Java 的水印注释
linktitle: Watermark Annotations
type: docs
weight: 70
url: /java/pdfannotationeditor-class/watermark-annotations/
description: 了解如何使用 Java 在 PDF 文档中添加、检查和删除水印注释。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: 使用 Java 处理 PDF 文件中的水印注释
Abstract: 本文介绍如何使用 Java 创建、检查和删除 PDF 文档中的水印注释。它包括添加具有自定义文本状态和不透明度的文本水印注释、读取现有水印注释区域以及删除水印注释。
---
## 添加水印注释

1. 打开输入 PDF 并定义将放置水印注释的矩形。
2. 创建`WatermarkAnnotation`，将其添加到页面，并配置水印文本状态和不透明度。
3. 应用水印文本行并保存修改后的 PDF。

```java
public static void watermarkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        WatermarkAnnotation watermarkAnnotation = new WatermarkAnnotation(
                document.getPages().get_Item(1), new Rectangle(100, 0, 400, 100, true));

        document.getPages().get_Item(1).getAnnotations().add(watermarkAnnotation);

        TextState textState = new TextState();
        textState.setForegroundColor(Color.getBlue());
        textState.setFontSize(25);
        textState.setFont(FontRepository.findFont("Arial"));

        watermarkAnnotation.setOpacity(0.5);
        watermarkAnnotation.setTextAndState(new String[]{"HELLO", "Line 1", "Line 2"}, textState);

        document.save(outputFile.toString());
    }
}
```
