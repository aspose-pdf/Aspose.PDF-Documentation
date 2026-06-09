---
title: 添加曲线注释
type: docs
weight: 20
url: /zh/python-net/add-curve-annotation/
description: 此示例绑定一个输入 PDF，在首页绘制虚线曲线，并保存修改后的文档。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 PdfContentEditor 在 Python 中向 PDF 添加曲线注释
Abstract: 此示例演示如何使用 Aspose.PDF for Python via the Facades API 向 PDF 文档添加曲线注释。它展示了如何定义曲线顶点、边框样式、注释边界、文本内容，并保存更新后的文档。
---

曲线注释用于在 PDF 中突出显示不规则路径或形状，提供视觉强调或标记重要区域。使用 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), 您可以通过指定顶点序列、边框样式、可见性、注释矩形以及描述性文本来绘制曲线。

1. 创建 PdfContentEditor 对象。
1. 绑定 onput PDF。
1. 配置 Curve 属性。
1. 绘制 Curve 注释。
1. 保存已更新的 Document。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_curve_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    line_info = pdf_facades.LineInfo()
    line_info.border_style = 1  # 1 - Dashed
    line_info.vertice_coordinate = [120, 520, 160, 560, 220, 540, 280, 580]
    line_info.visibility = True
    content_editor.draw_curve(
        line_info,
        1,
        apd.Rectangle(110, 510, 220, 100),
        "This is curve annotation",
    )

    # Save output PDF file
    content_editor.save(outfile)
```
