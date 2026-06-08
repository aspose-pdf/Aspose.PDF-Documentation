---
title: 添加线注释
type: docs
weight: 30
url: /zh/python-net/add-line-annotation/
description: 此示例绑定输入 PDF，绘制带方形线端点的红色线注释，并保存修改后的 PDF。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 PdfContentEditor 在 Python 中向 PDF 添加线注释
Abstract: 此示例演示如何使用 Aspose.PDF for Python via the Facades API 向 PDF 文档添加线注释。它说明了如何定义线的起点和终点、矩形边界、外观属性，并保存更新后的文档。
---

线注释对于强调文本、突出关系或吸引对 PDF 中特定区域的注意很有用。使用 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)，您可以通过指定起点和终点、边界矩形、颜色、边框样式和线端点，以编程方式创建线注释。

1. 创建 PdfContentEditor 对象。
1. 绑定输入 PDF。
1. 定义线注释属性。
1. 添加线注释。
1. 保存已更新的 Document。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_line_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    # Create LineAnnotation object
    rect = apd.Rectangle(100, 100, 200, 200)
    contents = "This is line annotation"
    content_editor.create_line(
        rect,
        contents,
        100,
        100,
        200,
        200,
        1,
        1,
        apd.Color.red,
        "Solid",
        [3, 2],
        ["Square"],
    )

    # Save output PDF file
    content_editor.save(outfile)
```
