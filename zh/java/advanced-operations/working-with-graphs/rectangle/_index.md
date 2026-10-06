---
title: 在 Java 中向 PDF 添加矩形形状
linktitle: 添加矩形
type: docs
weight: 50
url: /zh/java/add-rectangle/
description: 了解如何在 Java 中的 PDF 文件中绘制和填充矩形形状。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 在 PDF 文件中绘制矩形形状
Abstract: 本文演示如何使用 Aspose.PDF for Java 向 PDF 文档添加矩形形状。内容包括带轮廓的矩形、实心填充、渐变填充、Alpha 透明度以及重叠形状的 Z 顺序控制。
---
## 添加矩形轮廓

1. 创建一个新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 添加一个 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 到文档。
1. 创建一个 [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 容器并将其添加到页面。
1. 创建 [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) 形状并配置其几何。
1. 添加 [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) 到 [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 容器。
1. 保存输出 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addRectangle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 300.0);
        page.getParagraphs().add(graph);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getRed()));

        Rectangle rectangle = new Rectangle(20, 20, 350, 250);
        graph.getShapes().addItem(rectangle);

        document.save(outputFile.toString());
    }
}
```

## 使用实心或渐变颜色填充矩形

矩形示例包括:

- `createRectangleFilled` 用于实心填充 `Color.getRed()`
- `addDrawingWithGradientFill` 对于一个 `GradientAxialShading` 填充

## 使用 alpha 透明度

`createRectangleWithAlphaColorChannel` 应用半透明颜色 `Color.fromArgb(...)` 因此，重叠的矩形保持可见。

## 控制矩形的 z-order

1. 创建一个新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 添加一个 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 到文档。
1. 设置所需的 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 大小。
1. 添加已配置的 [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) 形状到目标页面，并使用所需的 z-order。
1. 保存输出 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void controlZOrderOfRectangle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.setPageSize(375, 300);
        page.getPageInfo().getMargin().setLeft(0);
        page.getPageInfo().getMargin().setTop(0);

        addRectangleToPage(page, 50, 40, 60, 40, Color.getRed(), 2);
        addRectangleToPage(page, 20, 20, 30, 30, Color.getBlue(), 1);
        addRectangleToPage(page, 40, 40, 60, 30, Color.getGreen(), 0);

        document.save(outputFile.toString());
    }
}
```
