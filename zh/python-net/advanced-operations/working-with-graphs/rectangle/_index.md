---
title: 在 Python 中向 PDF 添加矩形形状
linktitle: 添加矩形
type: docs
weight: 50
url: /zh/python-net/add-rectangle/
description: 学习如何在 Python 中绘制和填充 PDF 文件中的矩形形状。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 在 PDF 文件中绘制矩形形状
Abstract: 本文展示了如何使用 Aspose.PDF for Python via .NET 向 PDF 文档添加矩形形状。它涵盖了带轮廓的矩形、实色和渐变填充、Alpha 透明度以及 Z-order 控制。
---

## 添加 Rectangle 对象

Aspose.PDF for Python via .NET 允许您添加 [矩形](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) 通过该方式将形状添加到 PDF 页面 [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) 类。您可以绘制带轮廓的矩形并应用实色、渐变或透明填充。

请按照以下步骤：

1. 创建一个新的 PDF [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 添加 [页面](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 到 PDF 文件的 pages 集合。
1. 添加 [文本片段](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/) 到页面实例的段落集合。
1. 创建 [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) 实例。
1. 设置边框 [Graph 对象](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/).
1. 添加 [矩形](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) 对象到 Graph 对象的形状集合。
1. 将图形对象添加到页面实例的段落集合中。
1. 添加 [文本片段](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/) 到页面实例的段落集合。
1. 并保存您的 PDF 文件

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_rectangle(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    text_fragment = ap.text.TextFragment("Rectangle")
    page.paragraphs.add(text_fragment)

    graph = drawing.Graph(400, 300)
    page.paragraphs.add(graph)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)

    rect = drawing.Rectangle(20, 20, 350, 250)
    graph.shapes.add(rect)
    page.paragraphs.add(text_fragment)

    document.save(outfile)
```

![创建矩形](create_rectangle.png)

## 创建填充矩形对象

Aspose.PDF for Python via .NET 还提供了用特定颜色填充矩形对象的功能。

以下代码片段展示了如何添加 a。 [矩形](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) 被颜色填充的对象。

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def create_rectangle_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(100, 400)
    page.paragraphs.add(graph)

    rect = drawing.Rectangle(100, 100, 200, 120)
    rect.graph_info.fill_color = ap.Color.red
    graph.shapes.add(rect)

    document.save(outfile)
```

填充纯色的矩形的结果：

![已填充的矩形](fill_rectangle.png)

## 添加带渐变填充的绘图

Aspose.PDF for Python via .NET 支持向 PDF 文档添加图形对象的功能，有时需要用渐变颜色填充图形对象。

以下代码片段展示了如何添加 a。 [矩形](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) 填充了渐变颜色的对象。

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_drawing_with_gradient_fill(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    page.paragraphs.add(graph)

    rect = drawing.Rectangle(0, 0, 300, 300)
    gradient_color = ap.Color()
    gradient_settings = drawing.GradientAxialShading(ap.Color.red, ap.Color.blue)
    gradient_settings.start = ap.Point(0, 0)
    gradient_settings.end = ap.Point(350, 350)
    gradient_color.pattern_color_space = gradient_settings
    rect.graph_info.fill_color = gradient_color
    graph.shapes.add(rect)

    document.save(outfile)
```

![渐变矩形](gradient.png)

## 创建带 Alpha 颜色通道的矩形

Aspose.PDF for Python via .NET 也支持通过 Alpha 颜色通道实现透明度。

以下代码片段展示了如何添加 a。 [矩形](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) 带有 Alpha 值的对象。

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def create_rectangle_with_alpha_color_channel(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(100, 400)
    page.paragraphs.add(graph)

    rect = drawing.Rectangle(100, 100, 200, 120)
    rect.graph_info.fill_color = ap.Color.from_argb(128, 244, 180, 0)
    graph.shapes.add(rect)

    rect1 = drawing.Rectangle(200, 150, 200, 100)
    rect1.graph_info.fill_color = ap.Color.from_argb(160, 120, 0, 120)
    graph.shapes.add(rect1)

    document.save(outfile)
```

![矩形 Alpha 通道颜色](rectangle_color.png)

## 控制形状的 Z-Order

Aspose.PDF for .NET 支持向 PDF 文档添加图形对象（例如图形、线条、矩形等）的功能。向 PDF 文件中添加同一对象的多个实例时，我们可以通过指定 Z-Order 来控制它们的渲染。Z-Order 还用于需要将对象相互叠加渲染的情况。

以下代码片段展示了渲染的步骤 [矩形](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) 相互叠加的对象。

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing


def _add_rectangle_to_page(
    page: ap.Page,
    x: float,
    y: float,
    width: float,
    height: float,
    color: ap.Color,
    zindex: int,
):
    graph = drawing.Graph(width, height)
    graph.is_change_position = False
    graph.left = x
    graph.top = y
    rect = drawing.Rectangle(0, 0, width, height)
    rect.graph_info.fill_color = color
    rect.graph_info.color = color
    graph.shapes.add(rect)
    graph.z_index = zindex
    page.paragraphs.add(graph)


def control_z_order_of_rectangle(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(375, 300)
    page.page_info.margin.left = 0
    page.page_info.margin.top = 0

    _add_rectangle_to_page(page, 50, 40, 60, 40, ap.Color.red, 2)
    _add_rectangle_to_page(page, 20, 20, 30, 30, ap.Color.blue, 1)
    _add_rectangle_to_page(page, 40, 40, 60, 30, ap.Color.green, 0)

    document.save(outfile)
```

![控制 Z 顺序](control.png)

## 相关图形主题

- [在 Python 中使用 PDF 图形](/pdf/zh/python-net/working-with-graphs/)
- [使用 Python 检查 PDF 图形中的形状边界](/pdf/zh/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/)
- [在 Python 中向 PDF 添加直线形状](/pdf/zh/python-net/add-line/)
- [在 Python 中向 PDF 添加椭圆形状](/pdf/zh/python-net/add-ellipse/)