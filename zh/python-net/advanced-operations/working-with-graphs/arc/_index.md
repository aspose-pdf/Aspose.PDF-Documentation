---
title: 在 Python 中向 PDF 添加弧形
linktitle: 添加弧形
type: docs
weight: 10
url: /zh/python-net/add-arc/
description: 了解如何在 Python 中绘制和填充 PDF 文件中的弧形。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 在 PDF 文件中绘制弧形
Abstract: 本文展示了如何使用 Aspose.PDF for Python via .NET 向 PDF 文档添加弧形。它涵盖了创建描边弧形、绘制填充的弧段以及将它们添加到 Graph 容器中。
---

## 添加 Arc 对象

Aspose.PDF for Python via .NET 允许您添加 [弧](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/arc/) 形状到 PDF 页面，使用 [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) 类。您可以绘制带轮廓的弧形和填充的弧形段，用于图表和技术插图。

请按照以下步骤：

1. 创建 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 实例。
1. 创建 [Graph 对象](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) 具有特定尺寸。
1. 设置 [边框](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) 针对 Graph 对象。
1. 创建对应的弧对象。
1. 将此对象添加到图形对象的 Shapes 集合中。
1. 添加 [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) 对象添加到页面的 paragraphs 集合。
1. 保存我们的 PDF 文件。

以下代码片段展示了如何添加 a。 [弧](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/arc/) 对象。

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_arc(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    arc1 = drawing.Arc(100, 100, 95, 0, 90)
    arc1.graph_info.color = ap.Color.green_yellow
    graph.shapes.add(arc1)

    arc2 = drawing.Arc(100, 100, 90, 70, 180)
    arc2.graph_info.color = ap.Color.dark_blue
    graph.shapes.add(arc2)

    arc3 = drawing.Arc(100, 100, 85, 120, 210)
    arc3.graph_info.color = ap.Color.red
    graph.shapes.add(arc3)

    page.paragraphs.add(graph)
    document.save(outfile)
```

## 创建填充弧形对象

此示例演示如何添加带颜色填充的弧段。

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_arc_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    arc = drawing.Arc(100, 100, 95, 0, 90)

    arc.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(arc)

    line = drawing.Line([195, 100, 100, 100, 100, 195])
    line.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(line)

    page.paragraphs.add(graph)
    document.save(outfile)
```

添加填充弧形的结果：

![填充弧形](filled_arc.png)

## 相关图形主题

- [在 Python 中使用 PDF 图形](/pdf/zh/python-net/working-with-graphs/)
- [在 Python 中向 PDF 添加圆形](/pdf/zh/python-net/add-circle/)
- [在 Python 中向 PDF 添加曲线形状](/pdf/zh/python-net/add-curve/)
- [在 Python 中向 PDF 添加直线形状](/pdf/zh/python-net/add-line/)