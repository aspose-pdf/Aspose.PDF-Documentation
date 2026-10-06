---
title: 在 Java 中向 PDF 添加水印
linktitle: 添加水印
type: docs
weight: 30
url: /zh/java/add-watermarks/
description: 了解如何使用 Aspose.PDF for Java 在 PDF 文件中添加、提取和删除水印工件。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Java 向 PDF 添加水印
Abstract: 本文解释了如何使用 Aspose.PDF for Java 在 PDF 文档中添加、检查和移除水印工件。它涵盖了创建带有对齐、旋转、不透明度和背景设置的文本水印、检查页面上的水印工件以及删除它们。
---
水印工件允许您在页面上放置持久的视觉标记，而不会将其混入主文档内容。

## 从 PDF 中提取水印工件

当您需要检查现有水印工件并读取其文本或位置时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 遍历目标页面的伪影集合。
1. 过滤水印分页伪影并打印它们的文本和矩形。

```java
public static void extractWatermarkFromPdf(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Artifact artifact : document.getPages().get_Item(1).getArtifacts()) {
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                System.out.println(artifact.getText() + " " + artifact.getRectangle());
            }
        }
    }
}
```

## 添加水印工件

当页面需要显示居中文本水印，并具有自定义旋转、透明度和背景放置时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 创建一个 [WatermarkArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/watermarkartifact/) 并配置其文本状态和放置设置。
1. 将水印添加到页面并保存输出文件。

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

## 删除水印伪影

当需要从页面中移除现有的水印伪影时，请使用此方法。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 反向遍历页面伪影集合。
1. 删除子类型为水印的分页伪影，然后保存文档。

```java
public static void deleteWatermarkArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```
