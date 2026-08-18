---
title: 在 Java 中将曲线形状添加到 PDF
linktitle: 添加曲线
type: docs
weight: 30
url: /java/add-curve/
description: 了解如何使用 Java 在 PDF 文件中绘制和填充曲线形状。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 在 PDF 文件中绘制曲线形状
Abstract: 本文介绍如何使用 Aspose.PDF for Java 将曲线形状添加到 PDF 文档。它涵盖了从坐标数组创建曲线以及在图形容器内应用描边颜色或填充颜色。
---
Aspose.PDF for Java 中的曲线由传递给 `Curve` 的浮点坐标数组定义。

## 添加曲线轮廓

1. 创建一个新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 将[页面](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 添加到文档中。
1. 创建一个 [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 容器并将其添加到页面中。
1. 创建[曲线](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/curve/)形状并配置其控制点。
1. 将[曲线](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/curve/) 添加到[图形](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 容器中。
1. 设置示例所需的形状属性，包括[颜色](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/)。
1. 保存输出 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

```java
public static void addCurve(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 200.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Curve curve1 = new Curve(new float[]{10, 10, 50, 60, 70, 10, 100, 120});
        curve1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().addItem(curve1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```
