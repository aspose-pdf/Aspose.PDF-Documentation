---
title: 使用 Java 向 PDF 添加图像
linktitle: 添加图像
type: docs
weight: 10
url: /zh/java/add-image-to-existing-pdf-file/
description: 了解如何在 Java 中向现有 PDF 文件添加图像。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 使用 Java 向现有 PDF 文件添加图像
Abstract: 本文介绍了如何使用 Aspose.PDF for Java 向 PDF 文档添加图像。内容涵盖在固定坐标放置图像、通过低层页面操作符添加图像、为可访问性设置替代文本，以及使用 Flate 压缩嵌入图像数据。
---
Aspose.PDF for Java 同时支持高级图像放置和基于低层操作符的绘制。

## 使用页面坐标添加图像

当您需要在 PDF 页面上将图像放置在固定位置时，请使用此示例。

1. 创建一个新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加一个页面。
1. 调用 `page.addImage()` 带有源图像路径和目标矩形。
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

## 使用页面操作符添加图像

当您需要通过页面操作符对图像位置和缩放进行底层控制时，请使用此示例。

1. 创建一个新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并打开源图像流。
1. 将图像添加到页面资源并计算目标矩形。
1. 写入所需的图形操作符并保存文档。

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

当图像应包含供屏幕阅读器使用的可访问性元数据时，请使用此示例。

1. 创建一个新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并将图像添加到页面。
1. 获取已插入的 [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/) 来自页面资源。
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

## 使用 Flate 压缩添加图像

当您想使用 Flate 压缩嵌入图像数据时，请使用此示例。

1. 创建一个新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并打开图像流。
1. 将图像添加到页面资源中，使用 `ImageFilterType.Flate`.
1. 通过页面操作绘制图像并保存结果。

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
