---
title: 调整 PDF 页面内容
type: docs
weight: 30
url: /zh/python-net/resize-pdf-page-contents/
description: 使用 Aspose.PDF for Python 调整特定 PDF 页面内容的大小。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中以编程方式调整 PDF 页面内容
Abstract: 了解如何使用 Aspose.PDF for Python 调整特定 PDF 页面内容的大小。本示例演示了如何在保持文档结构的同时调整页面内容的宽度和高度，从而更轻松地优化打印或查看的布局。
---

在为打印准备文档、将内容适配到特定布局或在文档中统一页面格式时，通常需要调整 PDF 页面内容的大小。使用 Aspose.PDF for Python，开发者可以以编程方式调整所选页面的内容大小，而无需手动编辑文档。

本文展示了如何使用 \u0027resize_contents\u0027 方法 [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) 用于修改 PDF 文件中特定页面的页面内容尺寸的类。通过指定目标宽度和高度，选定页面上的内容将相应地被重新调整大小。

1. 创建一个 PdfFileEditor 对象。
1. 调整页面内容大小。

参数：

- [1, 3] – 将要调整内容大小的页面编号列表。
- 400 – 页面内容的新宽度（单位：点）。
- 750 – 页面内容的新高度（单位：点）。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Resize PDF Page Contents
def resize_pdf_page_contents(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()

    if not pdf_editor.resize_contents(
        FileIO(infile), FileIO(outfile, "w"), [1, 3], 400, 750
    ):
        raise Exception("Failed to resize PDF page contents.")
```
