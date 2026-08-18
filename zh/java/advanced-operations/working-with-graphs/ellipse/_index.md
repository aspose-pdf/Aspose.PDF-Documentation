---
title: 在 Java 中将椭圆形状添加到 PDF
linktitle: 添加椭圆
type: docs
weight: 60
url: /java/add-ellipse/
description: 了解如何使用 Java 在 PDF 文件中绘制、填充和标记椭圆形状。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 在 PDF 文件中绘制椭圆形状
Abstract: 本文介绍如何使用 Aspose.PDF for Java 将椭圆形状添加到 PDF 文档。它涵盖了轮廓椭圆、填充椭圆以及将文本片段放置在椭圆形状内。
---
## 添加椭圆轮廓

1. 创建一个新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 将[页面](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 添加到文档中。
1. 创建一个 [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 容器并将其添加到页面中。
1. 创建 [椭圆](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) 形状并配置其几何形状。
1. 将[椭圆](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) 添加到[图形](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 容器中。
1. 设置示例所需的形状属性，包括[Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/)和[TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/)。
1. 保存输出 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

```java
public static void addEllipse(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 400.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Ellipse ellipse1 = new Ellipse(150, 100, 120, 60);
        ellipse1.getGraphInfo().setColor(Color.getGreenYellow());
        ellipse1.setText(new TextFragment("Ellipse"));
        graph.getShapes().addItem(ellipse1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```

完整的示例将两个不同的轮廓椭圆添加到同一个图形中。

## 添加实心椭圆

`createEllipseFilled` 用`Color.getGreenYellow()` 和`Color.getDarkRed()` 填充两个椭圆。

## 在省略号内添加文本

1. 创建一个新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 将[页面](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 添加到文档中。
1. 创建一个 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) 并设置所需的文本格式选项。
1. 创建一个 [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 容器并将其添加到页面中。
1. 创建 [椭圆](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) 形状并配置其几何形状。
1. 将[椭圆](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) 添加到[图形](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 容器中。
1. 保存输出 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

```java
public static void addTextInsideEllipse(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 400.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        TextFragment textFragment = new TextFragment("Ellipse");
        textFragment.getTextState().setFont(FontRepository.findFont("Helvetica"));
        textFragment.getTextState().setFontSize(24);

        Ellipse ellipse1 = new Ellipse(100, 100, 120, 180);
        ellipse1.getGraphInfo().setFillColor(Color.getGreenYellow());
        ellipse1.setText(textFragment);
        graph.getShapes().addItem(ellipse1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```
