---
title: 在 Java 中向 PDF 添加弧形
linktitle: 添加弧形
type: docs
weight: 10
url: /zh/java/add-arc/
description: 了解如何在 Java 中的 PDF 文件中绘制和填充弧形。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 在 PDF 文件中绘制弧形
Abstract: 本文展示了如何使用 Aspose.PDF for Java 向 PDF 文档添加弧形。内容包括绘制具有不同颜色的多个描边弧形，以及通过将弧形与闭合线相结合来创建填充的弧形段。
---
Aspose.PDF for Java 使用 `Graph` 以及形状对象，例如 `Arc` 和 `Line` 渲染矢量图形。

## 添加弧线轮廓

1. 创建新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 将一个 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 添加到文档。
1. 创建一个 [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 容器并将其添加到页面。
1. 创建 [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) 形状并配置其几何属性。
1. 添加 [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) 到 [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 容器。
1. 设置示例所需的形状属性，包括 [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/)。
1. 保存输出 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

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

完整示例向同一图形添加了三个具有不同半径、角度和颜色的弧。

## 添加一个已填充的弧段

1. 创建新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 将一个 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 添加到文档。
1. 创建一个 [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 容器并将其添加到页面。
1. 创建 [Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) 形状并配置其坐标。
1. 创建 [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) 形状并配置其几何属性。
1. 添加 [Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) 和 [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) 到 [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 容器。
1. 保存输出 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

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
