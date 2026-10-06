---
title: 在 Java 中向 PDF 添加线形状
linktitle: 添加线
type: docs
weight: 40
url: /zh/java/add-line/
description: 了解如何在 Java 中的 PDF 文件中绘制线形状和样式化线条。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 在 PDF 文件中绘制线形状
Abstract: 本文展示了如何使用 Aspose.PDF for Java 向 PDF 文档添加线形状。它涵盖了从坐标数组创建线条、应用虚线样式和颜色，以及在整个页面区域绘制线条。
---
## 添加虚线

1. 创建一个新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 添加一个 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 到文档。
1. 创建一个 [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 容器并将其添加到页面。
1. 创建 [Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) 形状并配置其坐标。
1. 添加 [Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) 到 [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 容器。
1. 保存输出的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addLine(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(100.0, 400.0);
        page.getParagraphs().add(graph);

        Line line = new Line(new float[]{100, 100, 200, 100});
        line.getGraphInfo().setDashArray(new int[]{0, 1, 0});
        line.getGraphInfo().setDashPhase(1);
        graph.getShapes().addItem(line);

        document.save(outputFile.toString());
    }
}
```

## 添加彩色点线或虚线

`addDottedDashedLine` 使用相同的坐标和虚线设置，但也应用 `Color.getRed()`.

## 在页面上绘制线条

1. 创建一个新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 添加一个 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 到文档。
1. 创建一个 [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 容器并将其添加到页面。
1. 创建 [Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) 形状并配置其坐标。
1. 添加 [Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) 到 [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 容器。
1. 保存输出的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void drawLineAcrossPage(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getPageInfo().getMargin().setLeft(0);
        page.getPageInfo().getMargin().setRight(0);
        page.getPageInfo().getMargin().setBottom(0);
        page.getPageInfo().getMargin().setTop(0);

        Graph graph = new Graph(page.getPageInfo().getWidth(), page.getPageInfo().getHeight());
        Line line = new Line(new float[]{
                (float) page.getRect().getLLX(),
                0,
                (float) page.getPageInfo().getWidth(),
                (float) page.getRect().getURY()
        });
        graph.getShapes().addItem(line);
        page.getParagraphs().add(graph);

        document.save(outputFile.toString());
    }
}
```
