---
title: 添加多边形批注
type: docs
weight: 40
url: /zh/python-net/add-polygon-annotation/
description: 此示例绑定输入 PDF，在首页绘制实心多边形，并将带有注释的修改后文档保存。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中使用 PdfContentEditor 为 PDF 添加多边形注释
Abstract: 此示例演示如何使用 Aspose.PDF for Python via the Facades API 向 PDF 文档添加多边形注释。它展示了如何定义多边形顶点、边框样式、注释边界、描述性文本，并保存更新后的文档。
---

多边形注释用于突出显示 PDF 中的不规则区域或形状，提供视觉强调或标记特定区域。使用 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), 您可以通过指定顶点坐标、边框样式、页码和注释矩形来创建多边形。

1. 创建 PdfContentEditor 对象。
1. 绑定输入 PDF。
1. 配置多边形属性。
1. 添加多边形注释。
1. 保存已更新的 Document。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_polygon_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    line_info = pdf_facades.LineInfo()
    line_info.border_style = 0  # 0 - Solid
    line_info.vertice_coordinate = [100, 200, 150, 260, 220, 220, 200, 160]
    content_editor.create_polygon(
        line_info,
        1,
        apd.Rectangle(90, 150, 150, 120),
        "This is polygon annotation",
    )

    # Save output PDF file
    content_editor.save(outfile)
```
