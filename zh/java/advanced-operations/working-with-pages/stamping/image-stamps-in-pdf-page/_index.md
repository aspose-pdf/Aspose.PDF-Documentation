---
title: 在 Java 中向 PDF 添加图像印章
linktitle: PDF 文件中的图像印章
type: docs
weight: 10
url: /zh/java/image-stamps-in-pdf-page/
description: 了解如何在 Java 中向 PDF 页面添加图像印章。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 向 PDF 页面添加图像印章和图像背景
Abstract: 本文说明了如何使用 Aspose.PDF for Java 向 PDF 文件添加图像印章。内容包括具有定位、旋转、不透明度和质量控制的图像印章，以及将图像用作浮动框的背景。
---
Aspose.PDF for Java 支持将图像印章用作覆盖层和基于图像的布局元素。

## 添加图像印章

当页面应显示具有自定义位置和不透明度的图像印章时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建一个 [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp/) 并配置其外观。
1. 将印章添加到页面并保存文档。

```java
public static void addImageStamp(Path inputFile, Path imageFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImageStamp imageStamp = new ImageStamp(imageFile.toString());
        imageStamp.setBackground(true);
        imageStamp.setXIndent(100);
        imageStamp.setYIndent(100);
        imageStamp.setHeight(300);
        imageStamp.setWidth(300);
        imageStamp.setRotate(Rotation.on270);
        imageStamp.setOpacity(0.5);

        document.getPages().get_Item(1).addStamp(imageStamp);
        document.save(outputFile.toString());
    }
}
```

## 添加具有质量控制的图像印章

当您需要调整图像印章的渲染质量时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建一个 [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp/) 并设置质量值。
1. 将印章添加到页面并保存结果。

```java
public static void addImageStampWithQualityControl(Path inputFile, Path imageFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImageStamp imageStamp = new ImageStamp(imageFile.toString());
        imageStamp.setQuality(10);
        document.getPages().get_Item(1).addStamp(imageStamp);
        document.save(outputFile.toString());
    }
}
```

## 使用图像作为浮动框的背景

当图像应作为样式化布局容器的背景时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并访问目标页面。
1. 创建一个带有文本和边框设置的 [FloatingBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/floatingbox/)。
1. 设置背景图像，将盒子添加到页面，并保存文档。

```java
public static void addImageAsBackgroundInFloatingBox(Path inputFile, Path imageFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        FloatingBox box = new FloatingBox(200.0f, 100.0f);
        box.setLeft(40);
        box.setTop(80);
        box.setHorizontalAlignment(HorizontalAlignment.Center);
        box.getParagraphs().add(new TextFragment("Text in Floating Box"));
        box.setBorder(new BorderInfo(BorderSide.All, Color.getRed()));

        Image image = new Image();
        image.setFile(imageFile.toString());
        box.setBackgroundImage(image);
        box.setBackgroundColor(Color.getYellow());
        page.getParagraphs().add(box);

        document.save(outputFile.toString());
    }
}
```
