---
title: 将弧对象添加到PDF文件
linktitle: 添加弧
type: docs
weight: 10
url: zh/java/add-arc/
description: 本文解释了如何使用Aspose.PDF for Java在PDF中创建弧对象。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 添加弧对象

Aspose.PDF for Java支持向PDF文档添加图形对象（例如图形、线、矩形等）。它还提供用特定颜色填充弧对象的功能。

请按照以下步骤操作：

1. 创建[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)实例

1. 创建具有特定尺寸的[Drawing object](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/package-frame)

1. 为Drawing对象设置[Border](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph#setBorder-com.aspose.pdf.BorderInfo-)

1. 将[Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph)对象添加到页面的段落集合中

1. 保存我们的PDF文件

以下代码片段展示了如何添加[Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Arc)对象。

```java
    public static void ExampleArc() {
        // 创建文档实例
        Document pdfDocument = new Document();
        // 添加页面到 PDF 文件的页面集合
        Page page = pdfDocument.getPages().add();

        // 创建具有特定尺寸的绘图对象
        Graph graph = new Graph(400, 400);
        // 设置绘图对象的边框
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Arc arc1 = new Arc(100, 100, 95, 0, 90);
        arc1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().add(arc1);

        Arc arc2 = new Arc(100, 100, 90, 70, 180);
        arc2.getGraphInfo().setColor(Color.getDarkBlue());
        graph.getShapes().add(arc2);

        Arc arc3 = new Arc(100, 100, 85, 120, 210);
        arc3.getGraphInfo().setColor(Color.getRed());
        graph.getShapes().add(arc3);

        // 将图形对象添加到页面的段落集合中
        page.getParagraphs().add(graph);

        // 保存 PDF 文件
        pdfDocument.save(_dataDir + "DrawingArc_out.pdf");

    }
```


## 创建填充弧对象

下一个示例展示了如何添加一个用颜色和特定尺寸填充的弧对象。

```java
    public static void ExampleFilledArc() {
        // 创建 Document 实例
        Document pdfDocument = new Document();
        // 将页面添加到 PDF 文件的页面集合中
        Page page = pdfDocument.getPages().add();

        // 创建具有特定尺寸的 Drawing 对象
        Graph graph = new Graph(400, 400);
        // 为 Drawing 对象设置边框
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Arc arc = new Arc(100, 100, 95, 0, 90);
        arc.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().add(arc);

        Line line = new Line(new float[] { 195, 100, 100, 100, 100, 195 });
        line.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().add(line);

        // 将 Graph 对象添加到页面的段落集合中
        page.getParagraphs().add(graph);

        // 保存 PDF 文件
        pdfDocument.save(_dataDir + "DrawingArc_out.pdf");

    }
```


让我们看看添加填充弧的结果：

![填充弧](filled_arc.png)