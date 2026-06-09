---
title: 添加 PDF 文档链接
type: docs
weight: 50
url: /zh/python-net/add-pdf-document-link/
description: 本示例绑定一个输入 PDF，向另一个 PDF 的页面添加一个绿色链接，并保存修改后的文档。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 PdfContentEditor 在 Python 中添加 PDF 文档链接
Abstract: 本示例演示如何使用 Aspose.PDF for Python via the Facades API 向另一个 PDF 文档添加链接。它展示了如何创建一个可点击的区域，以打开不同的 PDF 并保存更新后的文档。
---

PDF 文档链接允许用户无缝地从一个 PDF 导航到另一个 PDF。使用 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), 您可以定义一个可点击的矩形，链接到另一个 PDF 文件中的页面，使您的文档具有交互性并相互连接。

1. 创建一个 PdfContentEditor 实例。
1. 绑定输入的 PDF 文档。
1. 为可点击链接定义一个矩形。
1. 指定链接的 PDF 文件、源页面和目标页面。
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


def add_pdf_document_link(infile, linked_pdf, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add link to another PDF document
    content_editor.create_pdf_document_link(
        apd.Rectangle(140, 590, 240, 20),
        linked_pdf,
        1,
        1,
        apd.Color.green,
    )
    # Save updated document
    content_editor.save(outfile)
```
