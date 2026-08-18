---
title: 在 Java 中更改 PDF 页面大小
linktitle: 更改页面大小
type: docs
weight: 40
url: /java/change-page-size/
description: 了解如何使用 Java 读取和更改 PDF 页面尺寸。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 读取和更新页面尺寸和框
Abstract: 本文演示如何使用 Aspose.PDF for Java 读取和修改 PDF 页面尺寸。它包括获取页面尺寸、测量应用旋转的页面尺寸以及将第一页更新为新尺寸，同时打印更改前后的盒子尺寸。
---
Aspose.PDF for Java 可以报告页面尺寸并更新它们。

## 更改页面大小

当您需要调整现有页面的大小并检查更改前后的页面框时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 获取目标 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 并打印其当前框值。
1. 设置新的页面大小并保存文档。

```java
public static void setPageSize(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        printBoxes("Before set", page);
        page.setPageSize(597.6, 842.4);
        printBoxes("After set", page);
        document.save(outputFile.toString());
    }
}
```

## 获取页面大小

当您需要读取页面的可见尺寸时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 获取启用旋转处理的页面矩形。
1. 输出页面的宽度和高度。

```java
public static void getPageSize(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Rectangle rectangle = document.getPages().get_Item(1).getPageRect(true);
        System.out.println(rectangle.getWidth() + " : " + rectangle.getHeight());
    }
}
```

## 获取应用旋转的页面大小

当您需要比较考虑旋转之前和之后的页面尺寸时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 旋转目标[页面](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 读取带有和不带有旋转处理的页面矩形并输出这两个值。

```java
public static void getPageSizeRotation(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        page.setRotate(Rotation.on90);
        Rectangle rectangle = page.getPageRect(false);
        System.out.println(rectangle.getWidth() + " : " + rectangle.getHeight());
        rectangle = page.getPageRect(true);
        System.out.println(rectangle.getWidth() + " : " + rectangle.getHeight());
    }
}
```
