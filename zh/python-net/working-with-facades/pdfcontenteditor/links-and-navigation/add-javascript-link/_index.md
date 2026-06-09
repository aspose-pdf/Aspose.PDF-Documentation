---
title: 添加 JavaScript 链接
type: docs
weight: 30
url: /zh/python-net/add-javascript-link/
description: 此示例绑定一个输入 PDF，添加一个在点击时触发警报的 JavaScript 链接，并保存修改后的文档。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 PdfContentEditor 在 Python 中向 PDF 添加 JavaScript 链接
Abstract: 这个示例演示了如何使用 Aspose.PDF for Python via the Facades API 向 PDF 文档添加 JavaScript 链接。它展示了如何创建一个可点击区域，在点击时执行 JavaScript 代码，并保存更新后的 PDF。
---

PDF 中的 JavaScript 链接允许交互功能，例如显示警报、执行计算或动态修改文档内容。使用 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)，您可以在页面上定义一个可点击的矩形，并将其关联到自定义的 JavaScript 代码。

1. 创建一个 PdfContentEditor 实例。
1. 绑定输入的 PDF 文档。
1. 为可点击的 JavaScript 链接定义一个矩形。
1. 指定页码和链接颜色。
1. 分配 JavaScript 代码以在点击时执行。
1. 保存更新后的 PDF 文档。

```python
import aspose.pdf.facades as pdf_facades
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as apd
import aspose.pdf as ap

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_javascript_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add JavaScript link action
    content_editor.create_java_script_link(
        "app.alert('PdfContentEditor JavaScript link');",
        apd.Rectangle(160, 560, 260, 20),
        1,
        apd.Color.orange,
    )
    # Save updated document
    content_editor.save(outfile)
```
