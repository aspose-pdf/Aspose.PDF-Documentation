---
title: 使用 Python 检查 Shapes 集合中的形状边界
type: docs
weight: 70
url: /zh/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/
description: 了解如何在将形状插入 Shapes 集合时检查其边界，以确保它适合其父容器。
lastmod: "2025-05-14"
draft: false
TechArticle: true
AlternativeHeadline: 检查 Shapes 中形状边界的指南
Abstract: 本文提供了在 Shapes 集合中使用边界检查功能的全面指南，特别是使用 Python 处理 PDF 文档时。该功能有助于确保图形元素（如形状）能够正确地适配其父容器。它可以配置为在组件超出容器边界时抛出异常，从而实现稳健的错误处理。指南演示了创建新 PDF 文档、添加页面以及在图形对象中建立图形元素（矩形形状）的过程。提供了实例化 `Document`、添加 `Page` 和创建 `Graph` 对象的详细说明。文中描述了设置 `Rectangle` 形状并将 `BoundsCheckMode` 配置为 `THROW_EXCEPTION_IF_DOES_NOT_FIT`，确保如果形状未能适配图形的指定尺寸时会抛出异常。整个过程通过使用 Aspose.PDF 库的 Python 代码示例进行说明，突出这些功能的实际实现。
---

本文提供了关于在 Shapes 集合中使用边界检查功能的详细指南。该功能确保元素适配其父容器，并且可以配置为在组件不适配时抛出异常。

1. 创建一个新的 PDF [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. 添加页面
1. 创建一个 [图形](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/)
1. 创建矩形形状
1. 边界检查模式
1. 将 [矩形](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) 添加到图形

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Create a Graph object with specified dimensions
    graph = ap.drawing.Graph(100, 100)
    graph.top = 10
    graph.left = 15
    graph.border = ap.BorderInfo(ap.BorderSide.BOX, 1, ap.Color.black)
    page.paragraphs.add(graph)

    # Create a shape object(for example, Rectangle) with specified dimensions
    rect = drawing.Rectangle(-1, 0, 50, 50)
    rect.graph_info.fill_color = ap.Color.tomato

    # Set the BoundsCheck mode to THROW_EXCEPTION_IF_DOES_NOT_FIT
    graph.shapes.update_bounds_check_mode(ap.BoundsCheckMode.THROW_EXCEPTION_IF_DOES_NOT_FIT)

    # Add the rectangle to the graph
    graph.shapes.add(rect)
```            
