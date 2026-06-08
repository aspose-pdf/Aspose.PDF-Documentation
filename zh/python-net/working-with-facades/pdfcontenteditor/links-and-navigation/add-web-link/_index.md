---
title: 添加网页链接
type: docs
weight: 60
url: /zh/python-net/add-web-link/
description: 此示例绑定一个输入 PDF，在第 1 页添加一个指向 Aspose 的 Python PDF 产品页面的蓝色网页链接注释，并保存修改后的文档。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中使用 PdfContentEditor 向 PDF 添加网页链接
Abstract: 此示例演示如何使用 Aspose.PDF for Python via the Facades API 向 PDF 文档添加网页链接。它展示了如何在页面上创建可点击区域，以在网页浏览器中打开指定的 URL 并保存更新后的文档。
---

PDF 中的网页链接允许用户直接导航到在线资源、网站或文档。使用 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)，您可以在 PDF 页面上定义一个矩形区域，该区域在点击时会在默认网页浏览器中打开 URL。

1. 创建一个 PdfContentEditor 实例。
1. 绑定输入的 PDF 文档。
1. 为可点击的网页链接定义一个矩形。
1. 指定 URL、页码和链接颜色。
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


def add_web_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add a web link annotation to page 1
    content_editor.create_web_link(
        apd.Rectangle(100, 650, 200, 20),
        "https://products.aspose.com/pdf/python-net/",
        1,
        apd.Color.blue,
    )
    # Save updated document
    content_editor.save(outfile)
```
