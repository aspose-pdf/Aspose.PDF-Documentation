---
title: 使用 Java 替换现有 PDF 文件中的图像
linktitle: 替换图像
type: docs
weight: 70
url: /java/replace-image-in-existing-pdf-file/
description: 了解如何使用 Java 替换现有 PDF 文件中的嵌入图像。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: 使用 Java 替换现有 PDF 文件中的图像
Abstract: 本文介绍如何使用 Aspose.PDF for Java 替换 PDF 文档中的图像。它涵盖了用资源索引替换图像以及替换使用 ImagePlacementAbsorber 找到的第一个匹配的图像位置。
---
根据您需要定位图像的精确程度，使用页面图像集合或基于位置的搜索。

## 通过资源索引替换图像

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 访问目标[页面](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)上的图片资源。
1. 将目标图像资源替换为新图像文件。
1. 保存更新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

```java
public static void replaceImage(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        document.getPages().get_Item(1).getResources().getImages().replace(1, imageStream);
        document.save(outputFile.toString());
    }
}
```

## 使用`ImagePlacementAbsorber`替换图像

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建一个 [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) 并访问目标 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 获取目标 [ImagePlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacement/) 并将其替换为新图像流。
1. 保存更新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

```java
public static void replaceImageWithAbsorber(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);

        if (absorber.getImagePlacements().size() > 0) {
            ImagePlacement imagePlacement = absorber.getImagePlacements().get_Item(1);
            try (InputStream imageStream = Files.newInputStream(imageFile)) {
                imagePlacement.replace(imageStream);
            }
        }

        document.save(outputFile.toString());
    }
}
```
