---
title: 用 Java 裁剪 PDF 页面
linktitle: 裁剪 PDF 页面
type: docs
weight: 70
url: /java/crop-pages/
description: 了解如何在 Java 中裁剪 PDF 页面以及调整裁剪、修剪、出血和媒体框。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 裁剪 PDF 文件中的页面并调整页面框
Abstract: 本文介绍如何使用 Aspose.PDF for Java 裁剪 PDF 页面。它包括将新的裁剪矩形分配给裁剪、修剪、艺术和出血框，以及根据检测到的图像内容自动裁剪页面。
---
Aspose.PDF for Java 允许您通过显式框坐标或基于检测到的内容来裁剪页面。

## 通过设置页面框裁剪页面

当您需要将相同的裁剪区域应用到主页框时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建新裁剪[矩形](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/)。
1. 将矩形应用到与裁剪相关的页面框并保存文档。

```java
public static void cropPage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Rectangle newBox = new Rectangle(200, 220, 2170, 1520, true);
        document.getPages().get_Item(1).setCropBox(newBox);
        document.getPages().get_Item(1).setTrimBox(newBox);
        document.getPages().get_Item(1).setArtBox(newBox);
        document.getPages().get_Item(1).setBleedBox(newBox);
        document.save(outputFile.toString());
    }
}
```

## 根据检测到的内容裁剪页面

当裁剪区域应源自页面上第一个检测到的图像时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 使用 [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) 检测图像位置。
1. 如果找到图像矩形，则将裁剪框设置为图像矩形，然后保存文档。

```java
public static void cropPageByContent(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);
        if (absorber.getImagePlacements().size() > 0) {
            document.getPages().get_Item(1).setCropBox(absorber.getImagePlacements().get_Item(1).getRectangle());
        } else {
            System.out.println("No images found on the first page");
        }
        document.save(outputFile.toString());
    }
}
```
