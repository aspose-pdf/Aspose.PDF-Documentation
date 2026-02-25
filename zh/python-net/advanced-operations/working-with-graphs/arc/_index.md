---
title: 向 PDF 文件添加弧对象
linktitle: 添加弧
type: docs
weight: 10
url: /zh/python-net/add-arc/
description: 本文说明如何使用 Aspose.PDF for Python via .NET 在 PDF 中创建弧对象。
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 向 PDF 添加弧对象
Abstract: 本文提供了使用 Aspose.PDF for Python via .NET 在 PDF 文档中添加和自定义弧对象的详细指南。它强调了该库能够合并弧形等图形元素的能力，这对于需要动态生成 PDF 内容的应用程序（如技术图表和自定义插图）至关重要。文章包含逐步指令和代码片段，演示如何创建 `Document` 实例、设置具有指定尺寸和边框属性的 `Drawing` 对象，以及向 PDF 页面添加 `Graph` 和 `Arc` 对象。此外，还涉及弧对象填充颜色的过程，展示如何为弧线和直线设置填充属性，并最终保存 PDF 文档。提供的示例为希望利用 Aspose.PDF 在 PDF 文件中进行精确图形操作的开发人员提供了实用指南。
---

## 添加弧对象

Aspose.PDF for Python via .NET 支持向 PDF 文档添加图形对象（例如图形、直线、矩形等）的功能。它还提供将弧对象填充为特定颜色的功能。

本示例演示如何使用 Aspose.PDF for Python via .NET 通过编程方式在 PDF 文档中绘制弧线。借助绘图模块，开发者可以创建复杂的图形元素，如弧线，并对其外观和位置进行精确控制。这一能力对于需要在 PDF 中动态生成图形内容的应用程序至关重要，例如技术图表、图形或自定义插图。

请按照以下步骤操作：

1. 创建 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 实例。
1. 创建 [Drawing object](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/)，具有特定尺寸。
1. 为 Drawing 对象设置 [边框](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties)。
1. 添加 [图形](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) 对象到页面的段落集合。
1. 保存我们的 PDF 文件。

以下代码片段展示了如何添加 [弧](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/arc/) 对象。

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 400)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create arcs and set their properties
    arc1 = drawing.Arc(100, 100, 95, 0, 90)
    arc1.graph_info = drawing.GraphInfo()
    arc1.graph_info.color = ap.Color.green_yellow
    graph.shapes.add(arc1)

    arc2 = drawing.Arc(100, 100, 90, 70, 180)
    arc2.graph_info = drawing.GraphInfo()
    arc2.graph_info.color = ap.Color.dark_blue
    graph.shapes.add(arc2)

    arc3 = drawing.Arc(100, 100, 85, 120, 210)
    arc3.graph_info = drawing.GraphInfo()
    arc3.graph_info.color = ap.Color.red
    graph.shapes.add(arc3)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

## 创建填充弧对象

下一个示例展示如何添加一个填充颜色且具有特定尺寸的弧对象。

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 400)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create an arc and set fill color
    arc = drawing.Arc(100, 100, 95, 0, 90)
    arc.graph_info = drawing.GraphInfo()
    arc.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(arc)

    # Create a line and set fill color
    line = drawing.Line([195, 100, 100, 100, 100, 195])
    line.graph_info = drawing.GraphInfo()
    line.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(line)

    # Add Graph object to the paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

让我们看看添加填充弧后的结果：

![已填充弧](filled_arc.png)

