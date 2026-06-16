---
title: 向 PDF 插入页面
type: docs
weight: 40
url: /zh/python-net/insert-pages-into-pdf/
description: 使用 Aspose.PDF for Python 将一个 PDF 的页面插入另一个 PDF。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中将另一个 PDF 的页面插入现有 PDF
Abstract: 了解如何使用 Aspose.PDF for Python 将一个 PDF 的页面插入另一个 PDF。本示例演示如何将次要 PDF 中选定的页面添加到原始文档的特定位置，从而创建一个页面放置精确的合并 PDF。
---

在合并文档、添加内容或重新组织报告时，向现有 PDF 插入页面是常见需求。使用 Aspose.PDF for Python，开发者可以通过编程在指定位置将一个 PDF 的页面插入另一个 PDF。

本文展示了如何使用 insert 方法的 [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) class。通过指定要插入的页码和目标位置，您可以在保持原始格式和结构的同时合并不同 PDF 的内容。

1. 创建一个 PdfFileEditor 对象。
1. 定义插入位置和页码。
1. 插入页面。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


# Insert Pages into PDF
def insert_pages_into_pdf(infile, sample_file, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()

    # Define the page number where new pages will be inserted (1-based index)
    insert_page_number = 2

    pdf_editor.insert(infile, insert_page_number, sample_file, [1, 2], outfile)
```
