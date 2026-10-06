---
title: 在 Java 中向 PDF 添加曲线形状
linktitle: 添加曲线
type: docs
weight: 30
url: /zh/java/add-curve/
description: 了解如何在 Java 中绘制并填充 PDF 文件中的曲线形状。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 在 PDF 文件中绘制曲线形状
Abstract: 本文展示了如何使用 Aspose.PDF for Java 向 PDF 文档添加曲线形状。它涵盖了从坐标数组创建曲线以及在 Graph 容器内应用描边颜色或填充颜色。
---
在 Aspose.PDF for Java 中，曲线是通过传递给的 float 坐标数组来定义的 `Curve`.

## 添加曲线轮廓

1. 创建新 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 添加 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 到文档。
1. 创建一个 [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 容器并将其添加到页面。
1. 创建 [Curve](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/curve/) 形状并配置其控制点。
1. 添加 [Curve](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/curve/) 到 [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 容器。
1. 设置示例所需的形状属性，包括 [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).
1. 保存输出的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
