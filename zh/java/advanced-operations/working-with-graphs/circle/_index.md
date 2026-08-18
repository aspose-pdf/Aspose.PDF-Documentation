---
title: 使用 Java 将圆形添加到 PDF
linktitle: 添加圈子
type: docs
weight: 20
url: /java/add-circle/
description: 了解如何使用 Java 在 PDF 文件中绘制和填充圆形形状。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 在 PDF 文件中绘制圆形
Abstract: 本文介绍如何使用 Aspose.PDF for Java 将圆形添加到 PDF 文档。它涵盖了绘制圆形轮廓、用颜色填充圆形以及将文本放置在圆形形状内。
---
## 添加圆形轮廓

1. 创建一个新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 将[页面](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 添加到文档中。
1. 创建一个 [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 容器并将其添加到页面中。
1. 创建[圆形](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) 形状并配置其几何形状。
1. 将[圆](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) 添加到[图](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 容器中。
1. 设置示例所需的形状属性，包括[颜色](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/)。
1. 保存输出 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

```java
public static void addCircle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 200.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Circle circle = new Circle(100, 100, 40);
        circle.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().addItem(circle);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```

## 添加带有文本的实心圆

1. 创建一个新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 将[页面](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 添加到文档中。
1. 创建一个 [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 容器并将其添加到页面中。
1. 创建[圆形](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) 形状并配置其几何形状。
1. 将[圆](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) 添加到[图](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 容器中。
1. 设置示例所需的形状属性，包括[Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/)和[TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/)。
1. 保存输出 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

```java
public static void addCircleFilled(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 200.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Circle circle = new Circle(100, 100, 40);
        circle.getGraphInfo().setColor(Color.getGreenYellow());
        circle.getGraphInfo().setFillColor(Color.getGreen());
        circle.setText(new TextFragment("Circle"));
        graph.getShapes().addItem(circle);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```
