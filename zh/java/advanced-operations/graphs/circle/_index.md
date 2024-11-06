---
title: 向PDF文件添加圆形对象
linktitle: 添加圆形
type: docs
weight: 20
url: zh/java/add-circle/
description: 本文解释了如何使用Aspose.PDF for Java在PDF中创建圆形对象。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 添加圆形对象

像条形图一样，圆形图可以用于显示多个独立类别的数据。然而，与条形图不同的是，圆形图只能在您拥有构成整体的所有类别的数据时使用。因此，让我们看看如何使用Aspose.PDF for Java添加[Circle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Circle)对象。

请按照以下步骤操作：

1. 创建[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)实例

1. 创建具有特定尺寸的[Drawing object](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/package-frame)

1. 为 Drawing 对象设置 [Border](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph#setBorder-com.aspose.pdf.BorderInfo-)

1. 将 [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph) 对象添加到页面的段落集合中

1. 保存我们的 PDF 文件

```java
public static void ExampleCircle() {
        // 创建 Document 实例
        Document pdfDocument = new Document();
        // 将页面添加到 PDF 文件的页面集合中
        Page page = pdfDocument.getPages().add();

        // 创建具有特定尺寸的 Drawing 对象
        Graph graph = new Graph(400, 200);
        // 为 Drawing 对象设置边框
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Circle circle = new Circle(100,100,40);

        circle.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().add(circle);

        // 将 Graph 对象添加到页面的段落集合中
        page.getParagraphs().add(graph);

        // 保存 PDF 文件
        pdfDocument.save(_dataDir + "DrawingCircle1_out.pdf");
    }
```


我们的绘制圆形将如下所示：

![绘制圆形](drawing_circle.png)

## 创建填充圆对象

此示例展示了如何添加一个填充颜色的圆形对象。

```java

    public static void ExampleFilledCircle() {
        // 创建文档实例
        Document pdfDocument = new Document();
        // 将页面添加到PDF文件的页面集合中
        Page page = pdfDocument.getPages().add();

        // 创建具有特定尺寸的绘图对象
        Graph graph = new Graph(400, 200);
        // 为绘图对象设置边框
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Circle circle = new Circle(100,100,40);
        circle.getGraphInfo().setColor(Color.getGreenYellow());       
        circle.getGraphInfo().setFillColor(Color.getGreenYellow());

        graph.getShapes().add(circle);

        // 将图形对象添加到页面的段落集合中
        page.getParagraphs().add(graph);

        // 保存PDF文件
        pdfDocument.save(_dataDir + "DrawingCircle2_out.pdf");
    }
```


让我们看看添加填充圆的结果：

![填充圆](filled_circle.png)