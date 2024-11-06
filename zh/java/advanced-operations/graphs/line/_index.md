---
title: 将线对象添加到PDF文件
linktitle: 添加线条
type: docs
weight: 40
url: zh/java/add-line/
description: 本文解释了如何使用Aspose.PDF for Java在PDF中创建线对象。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 添加线对象

Aspose.PDF for Java支持向PDF文档添加图形对象（例如图形、线条、矩形等）的功能。您还可以添加[Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Line)对象，并可以为线条元素指定虚线模式、颜色和其他格式。

请按以下步骤操作：

1. 创建[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)实例。

1. 将[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page)添加到PDF文件的页面集合中。

1. 创建[Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph)实例。

1. 将Graph对象添加到页面实例的段落集合中。

1. 创建 [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) 实例。

1. 设置线宽。

1. 将 [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) 对象添加到 Graph 对象的形状集合中。

1. 保存您的 PDF 文件。

以下代码片段展示了如何添加一个填充颜色的 [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) 对象。

```java
 public static void ExampleLine() {
        // 创建 Document 实例
        Document pdfDocument = new Document();
        // 将页面添加到 PDF 文件的页面集合中
        Page page = pdfDocument.getPages().add();
        // 创建 Graph 实例
        Graph graph = new Graph(100, 400);

        // 将图形对象添加到页面实例的段落集合中
        page.getParagraphs().add(graph);

        // 创建 Rectangle 实例
        Line line = new Line(new float[] { 100, 100, 200, 100 });
        
        line.getGraphInfo().setLineWidth(5);
        
        // 将矩形对象添加到 Graph 对象的形状集合中
        graph.getShapes().add(line);

        // 保存 PDF 文件
        pdfDocument.save(_dataDir + "LineAdded.pdf");
    }
```


![Add Line](add_line.png)

## 如何在您的PDF文档中添加虚线

```java
public static void ExampleDashedLine() {
        // 创建Document实例
        Document pdfDocument = new Document();
        // 添加页面到PDF文件的页面集合中
        Page page = pdfDocument.getPages().add();

        // 创建具有特定尺寸的Drawing对象
        Graph canvas = new Graph(100, 400);
        // 将绘图对象添加到页面实例的段落集合中
        page.getParagraphs().add(canvas);

        // 创建Line对象
        Line line = new Line(new float[] { 100, 100, 200, 100 });

        // 设置Line对象的颜色
        line.getGraphInfo().setColor(Color.getRed());
        // 为线对象指定虚线数组
        line.getGraphInfo().setDashArray(new int[] { 0, 1, 0 });
        // 设置Line实例的虚线相位
        line.getGraphInfo().setDashPhase(1);
        // 将线添加到绘图对象的形状集合中
        canvas.getShapes().add(line);
        // 保存PDF文档
        pdfDocument.save(_dataDir + "DashLength_out.pdf");
    }
```


让我们检查结果：

![虚线](dash_line.png)

## 绘制贯穿页面的线

我们还可以使用线对象绘制从左下角到右上角以及从左上角到右下角的对角线。

请查看以下代码片段以实现此要求。

```java
    public static void ExampleLineAcrossPage() {
        // 创建文档实例
        Document pdfDocument = new Document();
        // 将页面添加到PDF文件的页面集合中
        Page page = pdfDocument.getPages().add();
        // 将页面的所有边距设置为0

        page.getPageInfo().getMargin().setLeft(0);
        page.getPageInfo().getMargin().setRight(0);
        page.getPageInfo().getMargin().setBottom(0);
        page.getPageInfo().getMargin().setTop(0);

        // 创建宽度和高度等于页面尺寸的图形对象
        Graph graph = new Graph((float) page.getPageInfo().getWidth(), (float) page.getPageInfo().getHeight());

        // 创建从页面的左下角到右上角的第一条线对象
        Line line = new Line(new float[] { (float) page.getRect().getLLX(), 0, (float) page.getPageInfo().getWidth(),
                (float) page.getRect().getURY() });

        // 将线添加到图形对象的形状集合中
        graph.getShapes().add(line);
        // 从页面的左上角绘制到右下角
        Line line2 = new Line(new float[] { 0, (float) page.getRect().getURY(), (float) page.getPageInfo().getWidth(),
                (float) page.getRect().getLLX() });

        // 将线添加到图形对象的形状集合中
        graph.getShapes().add(line2);
        // 将图形对象添加到页面的段落集合中
        page.getParagraphs().add(graph);

        // 保存PDF文件
        pdfDocument.save(_dataDir + "DrawingLine_out.pdf");
    }
```


![画线](draw_line.png)