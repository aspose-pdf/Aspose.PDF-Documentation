---
title: 为 PDF 页面添加页边距
type: docs
weight: 10
url: /zh/python-net/add-margins-to-pdf-pages/
description: 使用 Aspose.PDF for Python 为 PDF 的选定页面添加自定义页边距。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中为特定 PDF 页面添加自定义页边距
Abstract: 了解如何使用 Aspose.PDF for Python 为 PDF 的选定页面添加自定义页边距。本示例演示如何通过为各个页面指定顶部、底部、左侧和右侧页边距来扩展页面边界，使 PDF 更易打印或在视觉上保持一致。
---

为 PDF 页面添加页边距可以提升可读性、为打印做好准备或为注释预留空间。使用 Aspose.PDF for Python，开发人员可以在不修改内容布局的情况下，以编程方式为 PDF 的特定页面添加页边距。

在此代码片段中， [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) class 用于在输入文档的第 1 页和第 3 页添加 0.5 英寸的边距。边距以点为单位定义（1 英寸 = 72 点），并分别应用于每页的左、右、上、下。

1. 打开源 PDF 文档。
1. 创建一个 'PdfFileEditor' 实例。
1. 定义要修改的边距和页面。
1. 使用 'add_margins' 方法应用边距。
1. 将更新后的 PDF 保存到输出文件。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Add Margins to PDF Pages
def add_margins_to_pdf_pages(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    # Define the margins to be added (in points)
    left_margin = 36  # 0.5 inch
    right_margin = 36  # 0.5 inch
    top_margin = 36  # 0.5 inch
    bottom_margin = 36  # 0.5 inch

    pdf_editor.add_margins(
        infile, outfile, [1, 3], left_margin, right_margin, top_margin, bottom_margin
    )
```
