---
title: 在 Java 中向 PDF 添加圆形形状
linktitle: 添加圆形
type: docs
weight: 20
url: /zh/java/add-circle/
description: 了解如何在 Java 中绘制和填充 PDF 文件中的圆形形状。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 在 PDF 文件中绘制圆形形状
Abstract: 本文展示了如何使用 Aspose.PDF for Java 向 PDF 文档添加圆形形状。它涵盖了绘制圆形轮廓、用颜色填充圆形以及在圆形内放置文本。
---
## 添加圆形轮廓

1. 创建一个新的PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 添加一个 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 到文档。
1. 创建一个 [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 容器并将其添加到页面。
1. 创建 [Circle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) 形状并配置其几何属性。
1. 添加 [Circle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) 到 [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 容器。
1. 设置示例所需的形状属性，包括 [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).
1. 保存输出 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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

## 添加一个带文本的实心圆

1. 创建一个新的PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 添加一个 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 到文档。
1. 创建一个 [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 容器并将其添加到页面。
1. 创建 [Circle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) 形状并配置其几何属性。
1. 添加 [Circle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) 到 [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 容器。
1. 设置示例所需的形状属性，包括 [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/) 和 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
1. 保存输出 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
