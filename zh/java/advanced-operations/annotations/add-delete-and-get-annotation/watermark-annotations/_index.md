---
title: 使用 Java 的水印注释
linktitle: 水印注释
type: docs
weight: 70
url: /zh/java/watermark-annotations/
description: 了解如何使用 Aspose.PDF for Java 在 PDF 文档中添加、检查和删除水印注释。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 在 PDF 文件中处理水印注释。
Abstract: 本文说明如何使用 Aspose.PDF for Java 在 PDF 文档中创建、检查和移除水印注释。它涵盖了添加带自定义文本状态和不透明度的文本水印注释、读取现有水印注释区域以及删除水印注释。
---
水印注释允许您在页面上放置可重复使用的覆盖内容，同时仍可通过注释集合进行管理。

## 添加水印注释

当您需要带自定义字体设置和不透明度的文本水印注释时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 创建一个 [WatermarkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/watermarkannotation/) 并将其添加到页面。
1. 配置 [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/)，水印文本和不透明度，然后保存文档。

```java
public static void watermarkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        WatermarkAnnotation watermarkAnnotation = new WatermarkAnnotation(
                page,
                new Rectangle(100, 100, 400, 200, true));

        page.getAnnotations().add(watermarkAnnotation);

        TextState textState = new TextState();
        textState.setForegroundColor(Color.getBlue());
        textState.setFontSize(25);
        textState.setFont(FontRepository.findFont("Arial"));

        watermarkAnnotation.setOpacity(0.5);
        watermarkAnnotation.setTextAndState(new String[]{"HELLO", "Line 1", "Line 2"}, textState);

        document.save(outputFile.toString());
    }
}
```

## 获取水印注释

此示例扫描注释集合并打印每个水印注释的矩形。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 遍历目标页面上的注释。
1. 按以下方式过滤注释 [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Watermark` 并打印它们的矩形。

```java
public static void watermarkGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation a : document.getPages().get_Item(1).getAnnotations()) {
            if (a.getAnnotationType() == AnnotationType.Watermark) {
                System.out.println(a.getRect());
            }
        }
    }
}
```

## 删除水印注释

当需要从文档中删除现有水印注释时，请使用此方法。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 收集指定类型的注释 [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Watermark`.
1. 删除已收集的注释并保存输出文件。

```java
public static void watermarkDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation a : document.getPages().get_Item(1).getAnnotations()) {
            if (a.getAnnotationType() == AnnotationType.Watermark) {
                toDelete.add(a);
            }
        }
        for (Annotation a : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(a);
        }
        document.save(outputFile.toString());
    }
}
```

## 相关注释主题

- [交互式批注](/pdf/zh/java/interactive-annotations/)
- [标记批注](/pdf/zh/java/markup-annotations/)
- [安全批注](/pdf/zh/java/security-annotations/)
- [形状批注](/pdf/zh/java/shape-annotations/)
- [文本注释](/pdf/zh/java/text-based-annotations/)
- [导入和导出注释](/pdf/zh/java/import-export-annotations/)
