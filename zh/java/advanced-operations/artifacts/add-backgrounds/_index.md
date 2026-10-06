---
title: 在 Java 中添加 PDF 背景
linktitle: 添加背景
type: docs
weight: 20
url: /zh/java/add-backgrounds/
description: 了解如何在 Java 中使用 `BackgroundArtifact` 与 Aspose.PDF 为 PDF 页面添加背景图像或背景颜色。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何在 Java 中为 PDF 添加背景
Abstract: 本文介绍了如何在 Java 中使用 Aspose.PDF 添加或删除 PDF 页面背景。内容包括添加背景图像、调整图像不透明度、应用背景颜色以及从页面中删除背景伪像。
---
背景伪像允许您在主页面内容后面放置非内容的视觉元素，而不更改文档的逻辑文本。

## 向 PDF 添加背景图像

当页面需要将图像显示为背景伪像时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 以及图像输入流。
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

## 添加带有不透明度的背景图像

此示例将在页面内容后面放置一个半透明的背景图像。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 以及图像流。
1. 创建一个 [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/)，分配图像，并设置透明度。
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

在页面应使用纯色背景而不是图像时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建一个 [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) 并分配背景颜色。
1. 将该工件添加到页面并保存输出文件。

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

## 删除背景伪影

当需要从页面中删除现有的背景伪影时，请使用此方法。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 以相反顺序遍历页面工件集合。
1. 删除类型为 pagination 且子类型为 background 的工件，然后保存文档。

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
