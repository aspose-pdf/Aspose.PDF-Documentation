---
title: 在 PDF 文件中添加线对象
linktitle: 添加线
type: docs
weight: 40
url: /zh/python-net/add-line/
description: 本文解释如何使用 Aspose.PDF for Python via .NET 在 PDF 中创建线对象。
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 向 PDF 添加线对象
Abstract: 本文讨论如何使用 Aspose.PDF for Python via .NET 向 PDF 文档添加线对象。它解释了创建 `Document` 实例并向 PDF 添加 `Graph` 对象的过程。本文提供了创建和配置 `Line` 对象的详细步骤，包括指定其虚线模式和颜色。它包含代码片段，演示如何添加简单线、点划线以及如何在页面上绘制线以形成十字图案。每个部分均附有生成的 PDF 的可视化展示。本指南为希望使用 Aspose.PDF 通过图形元素增强 PDF 文档的开发者提供了实用资源。
---

## 添加线对象

Aspose.PDF for Python via .NET 支持向 PDF 文档添加图形对象（例如图形、线、矩形等）的功能。您还可以利用添加 [Line](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) 对象，在该对象中还可以指定虚线模式、颜色和其他格式设置。

请按照以下步骤操作：

1. 创建 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 实例。
1. 创建一个 Graph 对象
1. 将 [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) 对象添加到页面的段落集合中。
1. 创建并配置 Line
1. 将 [Line](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) 添加到 Graph 中
1. 保存我们的 PDF 文件。

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Create Graph instance
    graph = drawing.Graph(100, 400)

    # Add graph object to paragraphs collection of page instance
    page.paragraphs.add(graph)

    # Create Rectangle instance
    line = drawing.Line([100, 100, 200, 100])

    # Specify fill color for Graph object
    line.graph_info.dash_array = [0, 1, 0]
    line.graph_info.dash_phase = 1

    # Add rectangle object to shape collection of Graph object
    graph.shapes.append(line)

    # Save PDF file
    document.save(path_outfile)
```

![Add Line](add_line.png)

## 如何向 PDF 文档添加点划线

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Create Graph instance
    graph = drawing.Graph(100, 400)

    # Add graph object to paragraphs collection of page instance
    page.paragraphs.add(graph)

    # Create Rectangle instance
    line = drawing.Line([100, 100, 200, 100])

    # Set color for Line object
    line.graph_info.color = ap.Color.red

    # Specify fill color for Graph object
    line.graph_info.dash_array = [0, 1, 0]
    line.graph_info.dash_phase = 1

    # Add rectangle object to shape collection of Graph object
    graph.shapes.append(line)

    # Save PDF file
    document.save(path_outfile)
```

让我们查看结果：

![Dashed Line](dash_line.png)

## 跨页绘制线条

我们也可以使用线对象绘制一条从左下角到右上角以及从左上角到右下角的十字线。

请查看以下代码片段以实现此需求。

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Set page margin on all sides as 0
    page.page_info.margin.left = 0
    page.page_info.margin.right = 0
    page.page_info.margin.bottom = 0
    page.page_info.margin.top = 0

    # Create Graph object with Width and Height equal to page dimensions
    graph = drawing.Graph(page.page_info.width, page.page_info.height)

    # Create first line object starting from Lower-Left to Top-Right corner of page
    line = drawing.Line([page.rect.llx, 0, page.page_info.width, page.rect.ury])

    # Add line to shape collection of Graph object
    graph.shapes.append(line)

    # Draw line from Top-Left corner of page to Bottom-Right corner of page
    line2 = drawing.Line([0, page.rect.ury, page.page_info.width, page.rect.llx])

    # Add line to shape collection of Graph object
    graph.shapes.append(line2)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF file
    document.save(path_outfile)
```

![Drawing Line](draw_line.png)


