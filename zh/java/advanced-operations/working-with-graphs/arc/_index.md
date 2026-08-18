---
title: 用 Java 将弧形添加到 PDF
linktitle: 添加圆弧
type: docs
weight: 10
url: /java/add-arc/
description: 了解如何使用 Java 在 PDF 文件中绘制和填充圆弧形状。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 在 PDF 文件中绘制圆弧形状
Abstract: 本文介绍如何使用 Aspose.PDF for Java 将弧形添加到 PDF 文档。它涵盖了用不同颜色绘制多个轮廓弧以及通过将弧与闭合线组合来创建填充弧段。
---
Aspose.PDF for Java 使用`Graph` 以及`Arc` 和`Line` 等形状对象来渲染矢量图形。

## 添加圆弧轮廓

1. 创建一个新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 将[页面](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 添加到文档中。
1. 创建一个 [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 容器并将其添加到页面中。
1. 创建 [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) 形状并配置其几何形状。
1. 将 [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) 添加到 [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 容器中。
1. 设置示例所需的形状属性，包括[颜色](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/)。
1. 保存输出 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

```java
public static void addArc(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 400.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Arc arc1 = new Arc(100, 100, 95, 0, 90);
        arc1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().addItem(arc1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```

完整的示例将具有不同半径、角度和颜色的三个圆弧添加到同一个图形中。

## 添加填充圆弧段

1. 创建一个新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 将[页面](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 添加到文档中。
1. 创建一个 [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 容器并将其添加到页面中。
1. 创建[直线](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/)形状并配置其坐标。
1. 创建 [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) 形状并配置其几何形状。
1. 将[直线](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) 和[弧](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) 添加到[图形](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 容器中。
1. 保存输出 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

```java
public static void addArcFilled(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 400.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Arc arc = new Arc(100, 100, 95, 0, 90);
        arc.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().addItem(arc);

        Line line = new Line(new float[]{195, 100, 100, 100, 100, 195});
        line.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().addItem(line);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```
