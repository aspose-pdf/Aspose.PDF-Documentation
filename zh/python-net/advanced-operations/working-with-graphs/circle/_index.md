---
title: 在 Python 中向 PDF 添加圆形形状
linktitle: 添加圆形
type: docs
weight: 20
url: /zh/python-net/add-circle/
description: 了解如何在 Python 中绘制和填充 PDF 文件中的圆形形状。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 在 PDF 文件中绘制圆形形状
Abstract: 本文展示了如何使用 Aspose.PDF for Python via .NET 向 PDF 文档添加圆形形状。内容包括创建轮廓圆、用颜色填充圆以及在圆对象内部放置文本。
---

## 添加圆形对象

Aspose.PDF for Python via .NET 允许您添加 [圆形](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/circle/) 通过该方式将形状添加到 PDF 页面 [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) 类。使用圆形用于图表、批注和简单的可视元素。

请按照以下步骤：

1. 创建 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 实例。
1. 创建 [Graph 对象](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) 具有特定尺寸。
1. 设置 [边框](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) 针对 Graph 对象。
1. 添加 [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) 对象添加到页面的 paragraphs 集合。
1. 保存我们的 PDF 文件。

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_circle(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 200)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    circle = drawing.Circle(100, 100, 40)
    circle.graph_info.color = ap.Color.green_yellow
    graph.shapes.add(circle)

    page.paragraphs.add(graph)
    document.save(outfile)
```

我们绘制的圆将会是这样的：

![绘制圆形](drawing_circle.png)

## 创建填充圆对象

此示例演示了如何添加圆形并填充颜色。

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_circle_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 200)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    circle = drawing.Circle(100, 100, 40)
    circle.graph_info.color = ap.Color.green_yellow
    circle.graph_info.fill_color = ap.Color.green
    circle.text = ap.text.TextFragment("Circle")
    graph.shapes.add(circle)

    page.paragraphs.add(graph)
    document.save(outfile)
```

添加填充圆的结果：

![已填充圆形](filled_circle.png)

## 相关图形主题

- [在 Python 中使用 PDF 图形](/pdf/zh/python-net/working-with-graphs/)
- [在 Python 中向 PDF 添加弧形](/pdf/zh/python-net/add-arc/)
- [在 Python 中向 PDF 添加椭圆形状](/pdf/zh/python-net/add-ellipse/)
- [在 Python 中向 PDF 添加矩形形状](/pdf/zh/python-net/add-rectangle/)