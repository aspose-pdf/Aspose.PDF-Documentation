---
title: 在 PDF 中添加分页符
type: docs
weight: 20
url: /zh/python-net/add-page-breaks-in-pdf/
description: 使用 Aspose.PDF for Python 向 PDF 文档插入分页符。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中以编程方式向 PDF 页面添加分页符
Abstract: 了解如何使用 Aspose.PDF for Python 向 PDF 文档插入分页符。此示例演示如何在指定的垂直位置拆分页面，使开发人员能够重新组织内容并动态创建额外的页面。
---

当您需要将长 PDF 页面拆分为多个页面或控制内容在文档中的分布时，分页符非常有用。使用 Aspose.PDF for Python，开发人员可以在特定位置插入分页符，无需手动编辑 PDF。

本文展示了如何使用 ‘add_page_break’ 方法的 [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) 类用于在选定页面的特定垂直坐标处插入分页符。该方法会创建一个新页面，并将断点以下的内容移动到该页面。

1. 创建一个 PdfFileEditor 对象。
1. 定义分页符的位置。
1. 插入分页符。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Add Page Breaks in PDF
def add_page_breaks_in_pdf(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.add_page_break(
        infile,
        outfile,
        [
            pdf_facades.PdfFileEditor.PageBreak(1, 400),
        ],
    )
```
