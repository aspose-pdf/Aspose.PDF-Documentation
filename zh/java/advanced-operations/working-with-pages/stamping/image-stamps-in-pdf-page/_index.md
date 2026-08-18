---
title: 使用 Java 将图像标记添加到 PDF
linktitle: PDF 文件中的图像图章
type: docs
weight: 10
url: /java/image-stamps-in-pdf-page/
description: 了解如何使用 Java 将图像图章添加到 PDF 页面。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 将图像图章和图像背景添加到 PDF 页面
Abstract: 本文介绍如何使用 Aspose.PDF for Java 将图像图章添加到 PDF 文件。它涵盖了具有定位、旋转、不透明度和质量控制的图像印章，并使用图像作为浮动框的背景。
---
Aspose.PDF for Java 支持图像图章作为叠加层和图像支持的布局元素。

## 添加图像印记

当页面应显示具有自定义位置和不透明度的图像图章时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建一个 [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp/) 并配置其外观。
1. 将图章添加到页面并保存文档。

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

## 添加具有质量控制的图像印记

当您需要调整图像戳记的渲染质量时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建 [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp/) 并设置质量值。
1. 将图章添加到页面并保存结果。

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

## 使用图像作为浮动框背景

当图像应用作样式布局容器的背景时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并访问目标页面。
1. 创建一个带有文本和边框设置的 [FloatingBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/floatingbox/)。
1. 设置背景图像，将框添加到页面，然后保存文档。

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
