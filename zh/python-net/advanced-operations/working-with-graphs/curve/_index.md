---
title: 将曲线对象添加到 PDF 文件
linktitle: 添加曲线
type: docs
weight: 30
url: /zh/python-net/add-curve/
description: 本文解释了如何使用 Aspose.PDF for Python via .NET 在 PDF 中创建曲线对象。
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 将曲线对象添加到 PDF
Abstract: 本文讨论了使用 Aspose.PDF for Python via .NET 在 PDF 文档中实现图形曲线。它介绍了图形曲线的概念，即射线的集合，并详细说明了以编程方式创建简单和填充的贝塞尔曲线的过程。文章提供了逐步说明和代码片段，用于在 PDF 中绘制曲线，重点展示了使用 Aspose.PDF 绘图模块对图形元素的操作。该过程包括创建 `Document` 实例，定义具有指定尺寸的 `Drawing` 对象，设置边框，以及将 `Graph` 对象添加到 PDF 页面。通过显示结果曲线的图像，直观展示了这些代码示例的视觉效果。文章进一步探讨了填充曲线对象的创建，演示了如何为曲线设置填充颜色，这对于在 PDF 中生成技术图表、图形或自定义插图等动态图形内容至关重要。
---

## 添加曲线对象

图形 [Curve](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/curve/) 是射线的连接集合，每条线在普通双点处与另外三条线相交。

在本文中，我们将研究可在 PDF 文档中创建的简易图形曲线和填充曲线。

此示例演示了如何使用 Aspose.PDF for Python via .NET 在 PDF 文档中以编程方式绘制贝塞尔曲线。通过利用绘图模块，开发者可以创建外观和位置精确控制的复杂图形元素。这一功能对于需要在 PDF 中动态生成图形内容的应用至关重要，例如技术图表、图形或自定义插图。

请按照以下步骤操作：

1. 创建 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 实例。
1. 创建具有特定尺寸的 [Drawing object](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) 。
1. 为 Drawing 对象设置 [border](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) 。
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

    # Create a curve and set its properties
    curve1 = drawing.Curve([10, 10, 50, 60, 70, 10, 100, 120])
    curve1.graph_info = drawing.GraphInfo()
    curve1.graph_info.color = ap.Color.green_yellow

    # Add the curve to the graph shapes
    graph.shapes.add(curve1)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

下图显示了使用我们的代码片段执行后的结果：

![Drawing Curve](drawing_curve.png)

## 创建填充曲线对象

此示例展示了如何添加填充颜色的 Curve 对象。

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

    # Create a curve and set fill color
    curve1 = drawing.Curve([10, 10, 50, 60, 70, 10, 100, 120])
    curve1.graph_info = drawing.GraphInfo()
    curve1.graph_info.fill_color = ap.Color.green_yellow

    # Add the curve to the graph shapes
    graph.shapes.add(curve1)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

查看添加填充曲线的结果：

![Filled Curve](filled_curve.png)

