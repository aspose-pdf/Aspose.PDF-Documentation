---
title: 使用 Python 检查 PDF 图形中的形状边界
linktitle: 检查形状边界
type: docs
weight: 70
url: /zh/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/
description: 了解如何在 Python 中验证 PDF 图形集合中的形状边界。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 验证 PDF 文件中图形形状的边界
Abstract: 本文展示了如何使用 Aspose.PDF for Python via .NET 验证图形集合中的形状边界。它涵盖了配置 BoundsCheckMode、检测超出范围的形状以及安全处理边界异常。
---

## 检查图形中的形状边界

当您向 a 添加形状时 [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/)，您可以启用边界验证，以确保每个形状都适合图形区域。

使用 [BoundsCheckMode](https://reference.aspose.com/pdf/python-net/aspose.pdf/boundscheckmode/) 定义形状超出范围时的行为。在本例中， `THROW_EXCEPTION_IF_DOES_NOT_FIT` 用于引发异常。

请按照以下步骤：

1. 创建一个新的 PDF [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 添加一个 [页面](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. 创建一个 [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) 并将其添加到页面。
1. 创建一个 [矩形](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) 其超出图形边界。
1. 将边界检查模式设置为 `THROW_EXCEPTION_IF_DOES_NOT_FIT`.
1. 添加矩形并处理异常。
1. 保存文档。

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing


def check_shape_bounds(outfile: str):
    document = ap.Document()
    page = document.pages.add()

    graph = drawing.Graph(100, 100)
    graph.top = 10
    graph.left = 15
    graph.border = ap.BorderInfo(ap.BorderSide.BOX, 1, ap.Color.black)
    page.paragraphs.add(graph)

    rect = drawing.Rectangle(-1, 0, 50, 50)
    rect.graph_info.fill_color = ap.Color.tomato

    try:
        graph.shapes.update_bounds_check_mode(
            ap.BoundsCheckMode.THROW_EXCEPTION_IF_DOES_NOT_FIT
        )
        graph.shapes.add(rect)
    except Exception as e:
        print(e)

    document.save(outfile)
```

## 备注

- 使用 `THROW_EXCEPTION_IF_DOES_NOT_FIT` 当需要严格的布局验证时。
- 若要宽松的行为，请选择其他 `BoundsCheckMode` 基于您的布局需求的选项。

## 相关图形主题

- [在 Python 中使用 PDF 图形](/pdf/zh/python-net/working-with-graphs/)
- [在 Python 中向 PDF 添加矩形形状](/pdf/zh/python-net/add-rectangle/)
- [在 Python 中向 PDF 添加直线形状](/pdf/zh/python-net/add-line/)
- [在 Python 中向 PDF 添加椭圆形状](/pdf/zh/python-net/add-ellipse/)
