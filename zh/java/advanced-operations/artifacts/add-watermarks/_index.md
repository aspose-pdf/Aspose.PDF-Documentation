---
title: 用Java给PDF添加水印
linktitle: 添加水印
type: docs
weight: 30
url: /java/add-watermarks/
description: 了解如何使用 Aspose.PDF for Java 添加、提取和删除 PDF 文件中的水印工件。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何用Java给PDF添加水印
Abstract: 本文介绍如何使用 Aspose.PDF for Java 添加、检查和删除 PDF 文档中的水印伪影。它涵盖了创建具有对齐、旋转、不透明度和背景设置的文本水印、检查页面上的水印伪影以及删除它们。
---
水印工件使您可以在页面上放置持久的视觉标记，而无需将它们混合到主文档内容中。

## 从 PDF 中提取水印伪影

当您需要检查现有水印工件并读取其文本或位置时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 迭代目标页面的工件集合。
1. 过滤水印分页工件并打印其文本和矩形。

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

## 添加水印神器

当页面应显示具有自定义旋转、不透明度和背景位置的居中文本水印时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建一个 [WatermarkArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/watermarkartifact/) 并配置其文本状态和位置设置。
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

当应从页面中删除现有水印工件时，请使用此方法。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 以相反的顺序迭代页面工件集合。
1. 删除子类型为水印的分页工件，然后保存文档。

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
