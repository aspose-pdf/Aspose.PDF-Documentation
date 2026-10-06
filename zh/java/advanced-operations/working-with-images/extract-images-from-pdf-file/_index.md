---
title: 使用 Java 从 PDF 文件中提取图像
linktitle: 提取图像
type: docs
weight: 30
url: /zh/java/extract-images-from-pdf-file/
description: 了解如何使用 Java 从 PDF 文件中提取嵌入的图像。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 使用 Java 从 PDF 文件中提取图像
Abstract: 本文展示了如何使用 Aspose.PDF for Java 从 PDF 文档中提取图像。它涵盖了从页面保存特定图像资源以及导出位于选定矩形区域内的图像。
---
Aspose.PDF for Java 支持直接图像资源提取和基于位置的过滤。

## 按索引提取嵌入的图像

当您需要从 PDF 页面保存特定图像资源时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 访问目标 [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/) 来自页面资源。
1. 将图像流保存到输出文件。

```java
public static void extractImage(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         OutputStream outputImage = Files.newOutputStream(outputFile)) {
        XImage image = document.getPages().get_Item(1).getResources().getImages().get_Item(1);
        image.save(outputImage);
    }
}
```

## 从特定页面区域提取图像

当仅需导出位于选定矩形内部的图像时，请使用此示例。

1. 定义目标 [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) 并打开源 PDF。
1. 使用 [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) 以检查页面上的图像位置。
1. 仅保存放置位置位于选定区域内的图像。

```java
public static void extractImageFromSpecificRegion(Path inputFile, Path outputFile) throws Exception {
    Rectangle rectangle = new Rectangle(0, 0, 590, 590, true);

    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);
        int index = 1;
        for (ImagePlacement imagePlacement : absorber.getImagePlacements()) {
            Point point1 = new Point(imagePlacement.getRectangle().getLLX(), imagePlacement.getRectangle().getLLY());
            Point point2 = new Point(imagePlacement.getRectangle().getURX(), imagePlacement.getRectangle().getURX());
            if (rectangle.contains(point1, true) && rectangle.contains(point2, true)) {
                Path indexedOutputFile = Path.of(outputFile.toString().replace("index", String.valueOf(index)));
                try (OutputStream outputImage = Files.newOutputStream(indexedOutputFile)) {
                    imagePlacement.getImage().save(outputImage);
                }
                index++;
            }
        }
    }
}
```
