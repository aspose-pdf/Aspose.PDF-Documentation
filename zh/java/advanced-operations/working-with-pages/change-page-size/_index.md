---
title: 在 Java 中更改 PDF 页面尺寸
linktitle: 更改页面尺寸
type: docs
weight: 40
url: /zh/java/change-page-size/
description: 了解如何在 Java 中读取和更改 PDF 页面尺寸。
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 读取并更新页面尺寸和盒子
Abstract: 本文演示了如何使用 Aspose.PDF for Java 读取和修改 PDF 页面尺寸。内容包括获取页面大小、在应用旋转后测量页面大小，以及在打印更改前后的盒子尺寸的同时，将第一页更新为新的尺寸。
---
Aspose.PDF for Java 既可以报告页面尺寸，也可以更新它们。

## 更改页面尺寸

当您需要调整现有页面大小并在更改前后检查页面框时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 获取目标 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 并打印其当前的框值。
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

## 获取页面尺寸

当您需要读取页面的可见尺寸时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 获取页面矩形，并启用旋转处理。
1. 输出页面宽度和高度。

```java
public static void getPageSize(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Rectangle rectangle = document.getPages().get_Item(1).getPageRect(true);
        System.out.println(rectangle.getWidth() + " : " + rectangle.getHeight());
    }
}
```

## 获取已应用旋转的页面尺寸

当您需要比较在考虑旋转前后的页面尺寸时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 旋转目标 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. 读取页面矩形（包含旋转处理和不包含旋转处理），并输出两个值。

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
