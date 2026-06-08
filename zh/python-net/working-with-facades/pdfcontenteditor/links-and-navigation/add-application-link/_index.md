---
title: 添加应用链接
type: docs
weight: 10
url: /zh/python-net/add-application-link/
description: 此示例绑定输入 PDF，在第一页添加应用启动链接，并保存修改后的文档。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 PdfContentEditor 在 Python 中为 PDF 添加应用启动链接
Abstract: 此示例演示如何使用 Aspose.PDF for Python via the Facades API 向 PDF 文档添加应用启动链接。它展示了如何创建一个可点击区域，在点击时打开指定的应用程序，并保存更新后的 PDF。
---

PDF 可以包含交互式元素，例如启动外部应用程序的链接。使用 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)，您可以在页面上定义一个矩形区域，点击后打开特定的可执行文件。

1. 创建一个 PdfContentEditor 实例。
1. 绑定输入的 PDF 文档。
1. 为可点击链接定义一个矩形区域。
1. 指定要启动的应用程序路径。
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


def add_application_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add application launch link
    content_editor.create_application_link(
        apd.Rectangle(180, 530, 260, 20),
        "notepad.exe",
        1,
        apd.Color.purple,
    )
    # Save updated document
    content_editor.save(outfile)
```
