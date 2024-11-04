---
title: 将矩形对象添加到PDF文件
linktitle: 添加矩形
type: docs
weight: 50
url: /java/add-rectangle/
description: 本文解释了如何使用Aspose.PDF for Java在PDF中创建矩形对象。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 添加矩形对象

Aspose.PDF for Java支持在PDF文档中添加图形对象（例如图形、线条、矩形等）。您还可以利用[Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Rectangle)对象的功能，填充某种颜色的矩形对象，控制Z轴顺序，添加渐变色填充等。

首先，让我们看看创建矩形对象的可能性。

请按照以下步骤操作：

1. 创建一个新的PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)

1. 将[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page)添加到PDF文件的页面集合中


1. 将[文本片段](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment)添加到页面实例的段落集合中

1. 创建[图形](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph)实例

1. 设置[绘图对象](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/package-frame)的边框

1. 创建矩形实例

1. 将[矩形](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Rectangle)对象添加到图形对象的形状集合中

1. 将图形对象添加到页面实例的段落集合中

1. 将[文本片段](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment)添加到页面实例的段落集合中

1. 并保存您的PDF文件

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.BorderInfo;
import com.aspose.pdf.BorderSide;
import com.aspose.pdf.Color;
import com.aspose.pdf.Document;
import com.aspose.pdf.Page;
import com.aspose.pdf.Point;
import com.aspose.pdf.TextFragment;
import com.aspose.pdf.drawing.*;

public class WorkingWithGraphs {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    public static void ExampleRectangle() {

        // 创建一个新的PDF文档
        Document pdfDocument = new Document();

        // 将页面添加到PDF文件的页面集合中
        Page page = pdfDocument.getPages().add();

        // 将文本片段添加到页面实例的段落集合中
        page.getParagraphs().add(new TextFragment("图形对象之前的文本"));

        // 创建图形实例
        Graph graph = new Graph(400, 200);

        // 设置绘图对象的边框
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getRed());
        graph.setBorder(borderInfo);

        // 创建矩形实例
        Rectangle rect = new Rectangle(10, 10, 380, 180);

        // 将矩形对象添加到图形对象的形状集合中
        graph.getShapes().add(rect);

        // 将图形对象添加到页面实例的段落集合中
        page.getParagraphs().add(graph);

        // 将文本片段添加到页面实例的段落集合中
        page.getParagraphs().add(new TextFragment("图形对象之后的文本"));

        // 保存PDF文件
        pdfDocument.save(_dataDir + "CreateRectangle_out.pdf");
    }
```


![Create Rectangle](create_rectangle.png)

## 创建填充矩形对象

Aspose.PDF for Java 还提供了用某种颜色填充矩形对象的功能。

以下代码片段展示了如何添加一个用颜色填充的[Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle)对象。

```java
   public static void ExampleRectangleFilledSolidColor() {

        Document pdfDocument = new Document();

        // 将页面添加到 PDF 文件的页面集合中
        Page page = pdfDocument.getPages().add();
        // 创建 Graph 实例
        Graph graph = new Graph(100, 400);

        // 将图形对象添加到页面实例的段落集合中
        page.getParagraphs().add(graph);

        // 创建 Rectangle 实例
        Rectangle rect = new Rectangle(100, 100, 200, 120);

        // 为 Graph 对象指定填充颜色
        rect.getGraphInfo().setFillColor(Color.getRed());

        // 将矩形对象添加到 Graph 对象的形状集合中
        graph.getShapes().add(rect);

        // 保存 PDF 文件
        pdfDocument.save(_dataDir + "CreateFilledRectangle_out.pdf");
    }
```


看一下填充实色的矩形结果：

![填充矩形](fill_rectangle.png)

## 添加渐变填充的绘图

Aspose.PDF for Java 支持向 PDF 文档添加图形对象的功能，有时需要用渐变色填充图形对象。要用渐变色填充图形对象，我们需要使用 gradientAxialShading 对象设置 setPatterColorSpace，如下所示。

以下代码片段展示了如何添加填充渐变色的 [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) 对象。

```java
   public static void ExampleRectangleFilledGradient() {

        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();

        Graph graph = new Graph(300, 300);
        page.getParagraphs().add(graph);
        Rectangle rect = new Rectangle(0, 0, 300, 300);
        graph.getShapes().add(rect);

        // 指定图形对象的渐变填充颜色并填充
        Color gradientFill = new com.aspose.pdf.Color();
        rect.getGraphInfo().setFillColor(gradientFill);

        GradientAxialShading gradientAxialShading = new GradientAxialShading(Color.getRed(), Color.getBlue());

        gradientAxialShading.setStart(new Point(0, 0));
        gradientAxialShading.setEnd(new Point(300, 300));
        gradientFill.setPatternColorSpace(gradientAxialShading);

        // 保存 PDF 文件
        pdfDocument.save(_dataDir + "AddDrawingWithGradientFill_out.pdf");
    }
```


![Gradient Rectangle](gradient.png)

## 用 Alpha 颜色通道创建矩形

Aspose.PDF for Java 支持用特定颜色填充矩形对象。矩形对象也可以有 Alpha 颜色通道，以提供透明的外观。以下代码片段展示了如何添加具有 Alpha 颜色通道的 [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) 对象。

图像的像素可以存储关于其不透明度的信息以及颜色值。这允许创建具有透明或半透明区域的图像。

与其使颜色透明，每个像素存储关于其不透明程度的信息。这种不透明数据称为 alpha 通道，通常存储在像素的颜色通道之后。

在我们的代码片段中，我们使用了 [com.aspose.pdf.Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/Color) 的 [fromArgb](https://reference.aspose.com/pdf/java/com.aspose.pdf/Color#fromArgb-int-int-int-) 方法。
 我们需要指定值，其中前3个是颜色分量，范围为0到255，最后一个是透明度级别（alpha通道），由0到1之间的小数指定。

```java
    public static void ExampleRectangleAlphaChannelColor() {
        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();

        // 创建Graph实例
        Graph graph = new Graph(100, 400);

        // 创建具有特定尺寸的矩形对象
        Rectangle rect1 = new Rectangle(100, 100, 200, 100);
        Color color1 = Color.fromArgb(128, 224, 0, 224);
        rect1.getGraphInfo().setFillColor(color1);
        // 将矩形对象添加到Graph实例的形状集合中
        graph.getShapes().add(rect1);

        // 创建第二个矩形对象
        Rectangle rect2 = new Rectangle(200, 150, 200, 100);
        Color color2 = Color.fromArgb(64, 0, 224, 224);
        rect2.getGraphInfo().setFillColor(color2);
        graph.getShapes().add(rect2);

        // 将Graph实例添加到页面对象的段落集合中
        page.getParagraphs().add(graph);

        // 保存PDF文件
        pdfDocument.save(_dataDir + "CreateRectangleWithAlphaColor_out.pdf");
    }
```

![Rectangle Alpha Channel Color](rectangle_color.png)

## 控制矩形的 Z-Order

Aspose.PDF for Java 支持在 PDF 文档中添加图形对象（例如图形、线条、矩形等）的功能。当在 PDF 文件中添加多个相同对象的实例时，我们可以通过指定 Z-Order 来控制它们的渲染。当我们需要将对象渲染在彼此之上时，也会使用 Z-Order。

以下代码片段展示了在彼此之上渲染 [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) 对象的步骤。

```java
   public static void Controlling_Z_Order() {

        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();

        // 创建一个新的矩形，颜色为红色，Z-Order 为 0，具有特定尺寸
        AddRectangle(page, 50, 40, 60, 40, Color.getRed(), 2);
        // 创建一个新的矩形，颜色为蓝色，Z-Order 为 0，具有特定尺寸
        AddRectangle(page, 20, 20, 30, 30, Color.getBlue(), 1);
        // 创建一个新的矩形，颜色为绿色，Z-Order 为 0，具有特定尺寸
        AddRectangle(page, 40, 40, 60, 30, Color.getGreen(), 0);

        // 保存生成的 PDF 文件
        pdfDocument.save(_dataDir + "ControlRectangleZOrder_out.pdf");

    }
```


![控制 Z 顺序](control.png)