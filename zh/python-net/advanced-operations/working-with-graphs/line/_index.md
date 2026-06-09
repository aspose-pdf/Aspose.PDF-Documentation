---
title: 在 Python 中向 PDF 添加线形状
linktitle: 添加线条
type: docs
weight: 40
url: /zh/python-net/add-line/
description: 学习如何在 Python 中的 PDF 文件中绘制线形状和样式化线条。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 在 PDF 文件中绘制线形状
Abstract: 本文展示了如何使用 Aspose.PDF for Python via .NET 向 PDF 文档添加线形状。它涵盖了创建基本线条、配置虚线样式以及在页面上绘制线条。
---

## 添加线对象

Aspose.PDF for Python via .NET 允许您添加 [线](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) 形状到 PDF 页面，使用 [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) 类。您可以控制线的颜色、虚线模式和位置。

请按照以下步骤：

1. 创建 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 实例。
1. 创建图形对象
1. 添加 [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) 对象添加到页面的 paragraphs 集合。
1. 创建并配置线条
1. 添加 [线](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) 到图形
1. 保存我们的 PDF 文件。

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing


def add_line(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(100, 400)
    page.paragraphs.add(graph)

    line = drawing.Line([100, 100, 200, 100])
    line.graph_info.dash_array = [0, 1, 0]
    line.graph_info.dash_phase = 1
    graph.shapes.add(line)

    document.save(outfile)
```

![添加线条](add_line.png)

## 如何在 PDF 文档中添加点划线

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_dotted_dashed_line(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(100, 400)
    page.paragraphs.add(graph)

    line = drawing.Line([100, 100, 200, 100])
    line.graph_info.color = ap.Color.red
    line.graph_info.dash_array = [0, 1, 0]
    line.graph_info.dash_phase = 1
    graph.shapes.add(line)

    document.save(outfile)
```

添加点划线后的结果：

![虚线](dash_line.png)

## 在页面上绘制线条

您也可以在页面上绘制线条以形成十字交叉。

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def draw_line_across_page(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    page.page_info.margin.left = 0
    page.page_info.margin.right = 0
    page.page_info.margin.bottom = 0
    page.page_info.margin.top = 0

    graph = drawing.Graph(page.page_info.width, page.page_info.height)
    line = drawing.Line([page.rect.llx, 0, page.page_info.width, page.rect.ury])
    graph.shapes.add(line)
    line2 = drawing.Line([0, page.rect.ury, page.page_info.width, page.rect.llx])
    graph.shapes.add(line2)
    page.paragraphs.add(graph)

    document.save(outfile)
```

![绘制线条](draw_line.png)

## 相关图形主题

- [在 Python 中使用 PDF 图形](/pdf/zh/python-net/working-with-graphs/)
- [在 Python 中向 PDF 添加曲线形状](/pdf/zh/python-net/add-curve/)
- [在 Python 中向 PDF 添加矩形形状](/pdf/zh/python-net/add-rectangle/)
- [使用 Python 检查 PDF 图形中的形状边界](/pdf/zh/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/)
