---
title: 使用 Java 替换现有 PDF 文件中的图像
linktitle: 替换图像
type: docs
weight: 70
url: /zh/java/replace-image-in-existing-pdf-file/
description: 了解如何在 Java 中替换现有 PDF 文件中的嵌入图像。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 使用 Java 替换现有 PDF 文件中的图像
Abstract: 本文展示了如何使用 Aspose.PDF for Java 替换 PDF 文档中的图像。它包括按资源索引替换图像以及使用 ImagePlacementAbsorber 替换找到的第一个匹配图像位置。
---
根据您需要定位图像的精确程度，可使用页面图像集合或基于位置的搜索。

## 通过资源索引替换图像

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 访问目标上的图像资源 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. 使用新图像文件替换目标图像资源。
1. 保存更新后的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void replaceImage(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        document.getPages().get_Item(1).getResources().getImages().replace(1, imageStream);
        document.save(outputFile.toString());
    }
}
```

## 使用 替换图像 `ImagePlacementAbsorber`

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 创建一个 [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) 并访问目标 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. 获取目标 [ImagePlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacement/) 并使用新的图像流替换它。
1. 保存更新后的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
