---
title: 向 PDF 文件添加圆形对象
linktitle: 添加圆形
type: docs
weight: 20
url: /zh/python-net/add-circle/
description: 本文解释如何使用 Aspose.PDF for Python via .NET 向 PDF 中创建圆形对象。
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 向 PDF 添加圆形对象
Abstract: 本文提供了使用 Aspose.PDF for Python via .NET 在 PDF 文档中创建圆形对象的指南。它解释了添加轮廓圆和填充圆图形的过程，强调当数据表示整体时，圆形图可作为显示跨多个类别数据的有用工具。文章包括创建 `Document` 实例、设置具有特定尺寸的 `Drawing` 对象、应用边框以及将 `Graph` 对象添加到 PDF 页面中的分步说明。代码示例展示了绘制简单圆形和填充圆形，并提供了设置颜色和向圆形添加文本的详细说明。还展示了这些操作的可视化结果，展示了 Aspose.PDF 在使用动态图形元素增强 PDF 内容方面的能力。
---

## 添加圆形对象

类似于条形图，圆形图可用于显示多个独立类别的数据。然而，与条形图不同，圆形图只能在拥有构成整体的所有类别数据时使用。因此，让我们看看如何使用 Aspose.PDF for Python .NET 添加一个 [圆形](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/circle/) 对象。

此示例说明了如何使用 Aspose.PDF for Python via .NET 以编程方式在 PDF 文档中绘制圆形。通过利用绘图模块，开发人员可以创建外观和位置精准控制的复杂图形元素。这一功能对于需要在 PDF 中动态生成图形内容的应用程序至关重要，例如技术图表、图形或自定义插图。

按照以下步骤操作：

1. 创建 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 实例。
1. 创建具有特定尺寸的 [绘图对象](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/)。
1. 为绘图对象设置 [边框](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties)。
1. 将 [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) 对象添加到页面的段落集合中。
1. 保存我们的 PDF 文件。

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 200)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create a circle with the specified coordinates and radius
    circle = drawing.Circle(100, 100, 40)

    # Set the circle's color
    circle.graph_info = drawing.GraphInfo()
    circle.graph_info.color = ap.Color.green_yellow

    # Add the circle to the graph shapes
    graph.shapes.add(circle)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

我们绘制的圆形将如下所示：

![绘制圆形](drawing_circle.png)

## 创建填充圆形对象

此示例展示了如何添加一个填充颜色的 Circle 对象。

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 200)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create a filled circle
    circle = drawing.Circle(100, 100, 40)
    circle.graph_info = drawing.GraphInfo()
    circle.graph_info.color = ap.Color.green_yellow
    circle.graph_info.fill_color = ap.Color.green
    circle.text = ap.text.TextFragment("Circle")

    # Add the circle to the graph shapes
    graph.shapes.add(circle)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

让我们看看添加填充圆形后的结果：

![填充圆形](filled_circle.png)


