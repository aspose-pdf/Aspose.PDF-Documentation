---
title: 添加折线注释
type: docs
weight: 50
url: /zh/python-net/add-polyline-annotation/
description: 示例绑定一个输入 PDF，在第一页创建一个实心折线，并将带注释的修改后文档保存。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 PdfContentEditor 在 Python 中向 PDF 添加折线注释
Abstract: 本示例演示如何使用 Aspose.PDF for Python via the Facades API 向 PDF 文档添加折线注释。它展示了如何定义顶点序列、边框样式、注释矩形、文本，并保存更新后的文档。
---

折线注释允许您在 PDF 中突出显示一系列相连的线段。使用 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)，您可以通过指定顶点坐标、边框样式、页码和注释边界来绘制折线。这对在图表和文档中直观地表示路径、趋势或连接非常有用。

1. 创建 PdfContentEditor 对象。
1. 绑定输入 PDF。
1. 配置 Polyline 属性。
1. 添加 Polyline 注释。
1. 保存已更新的 Document。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_polyline_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    line_info = pdf_facades.LineInfo()
    line_info.border_style = 0  # 0 - Solid
    line_info.vertice_coordinate = [120, 420, 180, 460, 230, 430, 290, 470]
    content_editor.create_poly_line(
        line_info,
        1,
        apd.Rectangle(110, 410, 200, 90),
        "This is polyline annotation",
    )

    # Save output PDF file
    content_editor.save(outfile)
```
