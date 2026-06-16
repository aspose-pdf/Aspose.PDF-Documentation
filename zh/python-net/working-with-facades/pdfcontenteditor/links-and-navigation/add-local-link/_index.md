---
title: 添加本地链接
type: docs
weight: 40
url: /zh/python-net/add-local-link/
description: 此示例绑定一个输入 PDF，在第 1 页添加一个红色本地链接，指向第 1 页，并保存修改后的文档。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 PdfContentEditor 在 Python 中为 PDF 添加本地链接
Abstract: 本示例演示了如何使用 Aspose.PDF for Python via the Facades API 向 PDF 文档添加本地链接。它展示了如何创建一个可点击区域，以在同一 PDF 的其他页面之间导航并保存更新后的文档。
---

本地链接在 PDF 中允许在同一文档的页面之间快速导航。使用 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)，您可以定义一个可点击的矩形，将一个页面链接到另一个页面，从而提升文档的可用性和导航性。

1. 创建一个 PdfContentEditor 实例。
1. 绑定输入的 PDF 文档。
1. 为可点击的本地链接定义一个矩形。
1. 指定源页面和目标页面。
1. 设置链接颜色。
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


def add_local_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add a local link on page 1 to destination page 1
    content_editor.create_local_link(
        apd.Rectangle(120, 620, 220, 20),
        1,
        1,
        apd.Color.red,
    )
    # Save updated document
    content_editor.save(outfile)
```
