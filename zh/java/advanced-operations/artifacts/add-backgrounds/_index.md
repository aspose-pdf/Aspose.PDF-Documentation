---
title: 在 Java 中添加 PDF 背景
linktitle: 添加背景
type: docs
weight: 20
url: /java/add-backgrounds/
description: 了解如何使用 `BackgroundArtifact` 和 Aspose.PDF 在 Java 中向 PDF 页面添加背景图像或背景颜色。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用Java为PDF添加背景
Abstract: 本文介绍如何使用 Aspose.PDF 在 Java 中添加或删除 PDF 页面背景。它包括添加背景图像、调整图像不透明度、应用背景颜色以及从页面中删除背景伪影。
---
背景工件允许您将非内容视觉元素放置在主页内容后面，而无需更改逻辑文档文本。

## 添加背景图像到 PDF

当页面应将图像显示为背景工件时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 和图像输入流。
1. 创建一个 [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) 并分配图像流。
1. 将工件添加到目标页面并保存输出 PDF。

```java
public static void addBackgroundImageToPdf(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        BackgroundArtifact artifact = new BackgroundArtifact();
        artifact.setBackgroundImage(imageStream);
        document.getPages().get_Item(1).getArtifacts().add(artifact);
        document.save(outputFile.toString());
    }
}
```

## 添加不透明度的背景图像

此示例将半透明背景图像放置在页面内容后面。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 和图像流。
1. 创建一个 [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/)，指定图像并设置不透明度。
1. 将工件添加到页面并保存文档。

```java
public static void addBackgroundImageWithOpacityToPdf(Path inputFile, Path imageFile, Path outputFile)
        throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        BackgroundArtifact artifact = new BackgroundArtifact();
        artifact.setBackgroundImage(imageStream);
        artifact.setOpacity(0.5);
        document.getPages().get_Item(1).getArtifacts().add(artifact);
        document.save(outputFile.toString());
    }
}
```

## 为 PDF 添加背景颜色

当页面应使用纯色背景而不是图像时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建一个 [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) 并指定背景颜色。
1. 将工件添加到页面并保存输出文件。

```java
public static void addBackgroundColorToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        BackgroundArtifact artifact = new BackgroundArtifact();
        artifact.setBackgroundColor(Color.getDarkKhaki().toRgb());
        document.getPages().get_Item(1).getArtifacts().add(artifact);
        document.save(outputFile.toString());
    }
}
```

## 去除背景伪影

当应从页面中删除现有背景工件时，请使用此方法。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 以相反的顺序迭代页面工件集合。
1. 删除类型为分页且子类型为背景的工件，然后保存文档。

```java
public static void removeBackground(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Background) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```
