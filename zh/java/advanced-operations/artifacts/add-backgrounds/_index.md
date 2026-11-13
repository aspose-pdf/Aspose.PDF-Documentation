---
title: 在 Java 中添加 PDF 背景
linktitle: 添加背景
type: docs
weight: 20
url: /zh/java/add-backgrounds/
description: 在 Java 中向 PDF 页面添加图像和纯色背景并调整图像不透明度。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中添加背景
Abstract: 在 Java 中向 PDF 页面添加图像和纯色背景并调整图像不透明度。
---
背景工件允许您在不更改逻辑文档文本的情况下，将非内容的视觉元素放置在主页面内容后面。

## 向 PDF 添加背景图像

当页面应将图像显示为背景工件时，请使用此示例。

1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 打开源 PDF，并打开图像流。
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

## 添加具有不透明度的背景图像

此示例将在页面内容后放置一个半透明的背景图像。

1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 打开源 PDF，并打开图像流。
1. 创建一个 [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/), 分配图像，并设置不透明度。
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

当页面应使用纯色背景而非图像时，请使用此示例。

1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 打开源 PDF.
1. 创建一个 [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) 并分配背景颜色。
1. 将构件添加到页面并保存输出文件。

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

## 相关主题

- [删除背景](/pdf/zh/java/remove-backgrounds/)
- [在 Java 中使用 PDF 工件](/pdf/zh/java/artifacts/)
