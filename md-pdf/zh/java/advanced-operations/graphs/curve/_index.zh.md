---
title: 添加曲线对象到PDF文件
linktitle: 添加曲线
type: docs
weight: 30
url: /java/add-curve/
description: 本文解释了如何使用Aspose.PDF for Java在您的PDF中创建一个曲线对象。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 添加曲线对象

一个图形[曲线](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Curve)是投影线的连接联合，每条线在普通双点处与另外三条线相交。

Aspose.PDF for Java展示了如何在您的图形中使用贝塞尔曲线。贝塞尔曲线在计算机图形学中被广泛用于建模平滑曲线。曲线完全包含在其控制点的凸包中，这些点可以图形化显示并用于直观地操控曲线。整个曲线包含在四个给定点（它们的凸包）构成的四边形中。

在本文中，我们将研究简单图形曲线和填充曲线，您可以在您的PDF文档中创建这些曲线。

按照以下步骤操作：

1. 创建 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 实例。

1. 创建具有特定尺寸的 [Drawing object](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/package-frame)。

1. 为 Drawing object 设置 [Border](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph#setBorder-com.aspose.pdf.BorderInfo-)。

1. 将 [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph) 对象添加到页面的段落集合中。

1. 保存您的 PDF 文件

```java
    public static void ExampleCurve() {
        // 创建 Document 实例
        Document pdfDocument = new Document();
        // 将页面添加到 PDF 文件的页面集合中
        Page page = pdfDocument.getPages().add();

        // 创建具有特定尺寸的 Drawing object
        Graph graph = new Graph(400, 200);
        // 为 Drawing object 设置边框
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Curve curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120});

        curve1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().add(curve1);

        // 将 Graph 对象添加到页面的段落集合中
        page.getParagraphs().add(graph);

        // 保存 PDF 文件
        pdfDocument.save(_dataDir + "DrawingCurve1_out.pdf");
    }
```


以下图片显示了使用我们的代码片段执行的结果：

![绘制曲线](drawing_curve.png)

## 创建填充曲线对象

此示例展示了如何添加一个用颜色填充的曲线对象。

```java
    public static void ExampleFilledCurve() {
        // 创建文档实例
        Document pdfDocument = new Document();
        // 将页面添加到PDF文件的页面集合中
        Page page = pdfDocument.getPages().add();

        // 创建具有特定尺寸的绘图对象
        Graph graph = new Graph(400, 200);
        // 设置绘图对象的边框
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Curve curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120});
        curve1.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().add(curve1);

        // 将图形对象添加到页面的段落集合中
        page.getParagraphs().add(graph);

        // 保存PDF文件
        pdfDocument.save(_dataDir + "DrawingCurve2_out.pdf");
    }
```


Look at the result of adding a filled Curve:

![填充曲线](filled_curve.png)