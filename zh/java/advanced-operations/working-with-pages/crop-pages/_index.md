---
title: 在 Java 中裁剪 PDF 页面
linktitle: 裁剪 PDF 页面
type: docs
weight: 70
url: /zh/java/crop-pages/
description: 了解如何在 Java 中裁剪 PDF 页面并调整裁剪框、修剪框、出血框和媒体框。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 裁剪页面并调整 PDF 文件中的页面框
Abstract: 本文解释了如何使用 Aspose.PDF for Java 裁剪 PDF 页面。它涵盖了将新裁剪矩形分配给裁剪框、修剪框、艺术框和出血框，以及基于检测到的图像内容自动裁剪页面。
---
Aspose.PDF for Java 允许您通过显式的框坐标或基于检测到的内容来裁剪页面。

## 通过设置页面框裁剪页面

当需要将相同的裁剪区域应用于主页面框时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建新的裁剪 [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/)。
1. 将矩形应用于与裁剪相关的页面框，并保存文档。

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

## 按检测到的内容裁剪页面

当裁剪区域应从页面上检测到的第一张图像中获取时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 使用 [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) 检测图像放置位置。
1. 如果找到图像，则将裁剪框设置为图像矩形，然后保存文档。

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
