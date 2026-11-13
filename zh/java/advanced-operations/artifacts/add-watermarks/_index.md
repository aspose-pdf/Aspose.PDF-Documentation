---
title: 在 Java 中向 PDF 添加水印
linktitle: 添加水印
type: docs
weight: 30
url: /zh/java/add-watermarks/
description: 在 Java 中向 PDF 页面添加样式化文本水印工件。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中添加水印
Abstract: 在 Java 中向 PDF 页面添加样式化文本水印工件。
---
水印工件允许您在页面上放置持久的视觉标记，而不会将其混入主文档内容。

## 添加水印工件

当页面需要显示居中文本水印，并使用自定义旋转、透明度和背景放置时，请使用此示例。

1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 打开源 PDF.
1. 创建一个 [WatermarkArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/watermarkartifact/) 并配置其文本状态和放置设置。
1. 在页面上添加水印并保存输出文件。

```java
public static void addWatermarkArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextState textState = new TextState();
        textState.setFontSize(72);
        textState.setForegroundColor(Color.getBlueViolet());
        textState.setFontStyle(FontStyles.Bold);
        textState.setFont(FontRepository.findFont("Arial"));

        WatermarkArtifact watermark = new WatermarkArtifact();
        watermark.setTextAndState("WATERMARK", textState);
        watermark.setArtifactHorizontalAlignment(HorizontalAlignment.Center);
        watermark.setArtifactVerticalAlignment(VerticalAlignment.Center);
        watermark.setRotation(60);
        watermark.setOpacity(0.2);
        watermark.setBackground(true);

        document.getPages().get_Item(1).getArtifacts().add(watermark);
        document.save(outputFile.toString());
    }
}
```

## 相关主题

- [提取水印详细信息](/pdf/zh/java/extract-watermarks/)
- [删除水印](/pdf/zh/java/remove-watermarks/)
- [在 Java 中使用 PDF 工件](/pdf/zh/java/artifacts/)
