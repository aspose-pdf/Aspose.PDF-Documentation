---
title: 使用 Java 将图像添加到 PDF
linktitle: 添加图片
type: docs
weight: 10
url: /java/add-image-to-existing-pdf-file/
description: 了解如何使用 Java 将图像添加到现有 PDF 文件。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: 使用 Java 将图像添加到现有 PDF 文件
Abstract: 本文介绍如何使用 Aspose.PDF for Java 将图像添加到 PDF 文档。它包括将图像放置在固定坐标、通过低级页面操作符添加图像、设置替代文本以实现可访问性，以及使用 Flate 压缩嵌入图像数据。
---
Aspose.PDF for Java 支持高级图像放置和低级基于操作员的绘图。

## 添加带有页面坐标的图像

当您需要将图像放置在 PDF 页面上的固定位置时，请使用此示例。

1. 创建新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加页面。
1. 使用源图像路径和目标矩形调用`page.addImage()`。
1. 保存生成的 PDF 文件。

```java
public static void addImage(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.addImage(imageFile.toString(), new Rectangle(20, 730, 120, 830, true));
        document.save(outputFile.toString());
    }
}
```

## 使用页面运算符添加图像

当您需要通过页面运算符对图像放置和缩放进行低级控制时，请使用此示例。

1. 创建一个新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并打开源图像流。
1. 将图像添加到页面资源中并计算目标矩形。
1. 编写所需的图形运算符并保​​存文档。

```java
public static void addImageUsingOperators(Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document();
         InputStream imageStream = Files.newInputStream(imageFile)) {
        Page page = document.getPages().add();
        page.setPageSize(842, 595);

        XImageCollection resourcesImages = page.getResources().getImages();
        String imageId = resourcesImages.add(imageStream);
        XImage xImage = resourcesImages.get_Item(resourcesImages.size());

        Rectangle rectangle = new Rectangle(
                0,
                0,
                page.getMediaBox().getWidth(),
                (page.getMediaBox().getWidth() * xImage.getHeight()) / xImage.getWidth(),
                true);

        page.getContents().add(new GSave());

        Matrix matrix = new Matrix(
                rectangle.getURX() - rectangle.getLLX(),
                0,
                0,
                rectangle.getURY() - rectangle.getLLY(),
                rectangle.getLLX(),
                rectangle.getLLX() + (page.getMediaBox().getHeight() - rectangle.getHeight()) / 2);
        page.getContents().add(new ConcatenateMatrix(matrix));
        page.getContents().add(new Do(imageId));
        page.getContents().add(new GRestore());

        document.save(outputFile.toString());
    }
}
```

## 添加图像并设置替代文本

当图像应包含屏幕阅读器的辅助功能元数据时，请使用此示例。

1. 创建一个新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并将图像添加到页面。
1. 从页面资源中获取插入的[XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/)。
1. 设置替代文本并保存 PDF。

```java
public static void addImageSetAlternativeTextForImage(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.setPageSize(842, 595);

        page.addImage(imageFile.toString(), new Rectangle(0, 0, 842, 595, true));

        XImage xImage = page.getResources().getImages().get_Item(1);
        boolean result = xImage.trySetAlternativeText("Alternative text for image", page);
        if (result) {
            System.out.println("Text has been added successfuly");
        }
        document.save(outputFile.toString());
    }
}
```

## 添加使用 Flate 压缩的图像

当您想要使用 Flate 压缩嵌入图像数据时，请使用此示例。

1. 创建一个新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并打开图像流。
1. 使用`ImageFilterType.Flate` 将图像添加到页面资源。
1. 通过页面算子绘制图像并保存结果。

```java
public static void addImageToPdfWithFlateCompression(Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document();
         InputStream imageStream = Files.newInputStream(imageFile)) {
        Page page = document.getPages().add();
        XImageCollection resourcesImages = page.getResources().getImages();
        String imageId = resourcesImages.add(imageStream, ImageFilterType.Flate);

        page.getContents().add(new GSave());

        Rectangle rectangle = new Rectangle(0, 0, 600, 600, true);
        Matrix matrix = new Matrix(
                rectangle.getURX() - rectangle.getLLX(),
                0,
                0,
                rectangle.getURY() - rectangle.getLLY(),
                rectangle.getLLX(),
                rectangle.getLLY());

        page.getContents().add(new ConcatenateMatrix(matrix));
        page.getContents().add(new Do(imageId));
        page.getContents().add(new GRestore());

        document.save(outputFile.toString());
    }
}
```
