---
title: 在 Python 中向 PDF 添加曲线形状
linktitle: 添加曲线
type: docs
weight: 30
url: /zh/python-net/add-curve/
description: 了解如何在 Python 中绘制并填充 PDF 文件中的曲线形状。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 在 PDF 文件中绘制曲线形状
Abstract: 本文展示了如何使用 Aspose.PDF for Python via .NET 向 PDF 文档添加曲线形状。内容包括创建带轮廓的曲线、填充曲线对象以及在 Graph 容器中渲染自定义曲线路径。
---

## 添加曲线对象

Aspose.PDF for Python via .NET 允许您添加 [曲线](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/curve/) 通过该方式将形状添加到 PDF 页面 [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) 类。

本文展示了如何创建带轮廓和填充的曲线。

请按照以下步骤：

1. 创建 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 实例。
1. 创建 [Graph 对象](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) 具有特定尺寸。
1. 设置 [边框](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) 针对 Graph 对象。
1. 添加 [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) 对象添加到页面的 paragraphs 集合。
1. 保存我们的 PDF 文件。

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_curve(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 200)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    curve1 = drawing.Curve([10, 10, 50, 60, 70, 10, 100, 120])
    curve1.graph_info.color = ap.Color.green_yellow
    graph.shapes.add(curve1)

    page.paragraphs.add(graph)
    document.save(outfile)
```

下图显示了使用我们的代码片段执行的结果：

![绘制曲线](drawing_curve.png)

## 创建填充曲线对象

本示例展示了如何添加一个填充颜色的 Curve 对象。

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing


def add_curve_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 200)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    curve1 = drawing.Curve([10, 10, 50, 60, 70, 10, 100, 120])
    curve1.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(curve1)

    page.paragraphs.add(graph)
    document.save(outfile)
```

添加填充曲线的结果:

![填充曲线](filled_curve.png)

## 相关图形主题

- [在 Python 中使用 PDF 图形](/pdf/zh/python-net/working-with-graphs/)
- [在 Python 中向 PDF 添加弧形](/pdf/zh/python-net/add-arc/)
- [在 Python 中向 PDF 添加直线形状](/pdf/zh/python-net/add-line/)
- [在 Python 中向 PDF 添加椭圆形状](/pdf/zh/python-net/add-ellipse/)