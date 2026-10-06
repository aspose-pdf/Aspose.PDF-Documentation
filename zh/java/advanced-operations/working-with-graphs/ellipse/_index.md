---
title: 在 Java 中向 PDF 添加椭圆形状
linktitle: 添加椭圆
type: docs
weight: 60
url: /zh/java/add-ellipse/
description: 了解如何在 Java 中的 PDF 文件中绘制、填充和标记椭圆形状。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 在 PDF 文件中绘制椭圆形状
Abstract: 本文展示了如何使用 Aspose.PDF for Java 向 PDF 文档添加椭圆形状。内容包括带轮廓的椭圆、填充的椭圆，以及在椭圆形状内放置文本片段。
---
## 添加椭圆轮廓

1. 创建新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 将一个 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 添加到文档。
1. 创建一个 [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 容器并将其添加到页面。
1. 创建 [Ellipse](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) 形状并配置其几何。
1. 添加 [Ellipse](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) 到 [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 容器。
1. 设置示例所需的形状属性，包括 [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/) 和 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/)。
1. 保存输出 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

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

完整示例向同一图形添加了两个不同的轮廓椭圆。

## 添加填充椭圆

`createEllipseFilled` 用...填充两个省略号 `Color.getGreenYellow()` 和 `Color.getDarkRed()`。

## 在椭圆内部添加文本

1. 创建新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 将一个 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 添加到文档。
1. 创建一个 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) 并设置所需的文本格式选项。
1. 创建一个 [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 容器并将其添加到页面。
1. 创建 [Ellipse](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) 形状并配置其几何。
1. 添加 [Ellipse](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) 到 [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 容器。
1. 保存输出 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

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
