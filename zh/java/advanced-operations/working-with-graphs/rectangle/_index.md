---
title: 在 Java 中将矩形添加到 PDF
linktitle: 添加矩形
type: docs
weight: 50
url: /java/add-rectangle/
description: 了解如何使用 Java 在 PDF 文件中绘制和填充矩形形状。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 在 PDF 文件中绘制矩形
Abstract: 本文介绍如何使用 Aspose.PDF for Java 向 PDF 文档添加矩形形状。它涵盖了轮廓矩形、实心填充、渐变填充、Alpha 透明度和重叠形状的 z 顺序控制。
---
## 添加矩形轮廓

1. 创建一个新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 将[页面](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 添加到文档中。
1. 创建一个 [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 容器并将其添加到页面中。
1. 创建 [矩形](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) 形状并配置其几何形状。
1. 将[矩形](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) 添加到[图形](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 容器中。
1. 保存输出 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

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

## 用纯色或渐变色填充矩形

矩形示例包括：

- `createRectangleFilled` 用于使用 `Color.getRed()` 进行实体填充
- `addDrawingWithGradientFill` 用于`GradientAxialShading` 填充

## 使用 Alpha 透明度

`createRectangleWithAlphaColorChannel` 使用`Color.fromArgb(...)` 应用半透明颜色，以便重叠的矩形保持可见。

## 控制矩形的 z 顺序

1. 创建一个新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 将[页面](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 添加到文档中。
1. 设置所需的[页面](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 大小。
1. 将配置的 [矩形](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) 形状添加到具有所需 z 顺序的目标页面。
1. 保存输出 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

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
