---
title: 将 PDF 拆分为单页
type: docs
weight: 30
url: /zh/python-net/split-pdf-into-single-pages/
description: 使用 Aspose.PDF for Python 将 PDF 文档拆分为单页 PDF。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中将 PDF 拆分为单个页面
Abstract: 了解如何使用 Aspose.PDF for Python 将 PDF 文档拆分为单页 PDF。此方法会从原始 PDF 中提取每一页，并将其保存为单独的文件，以实现灵活的文档管理和处理。
---

将 PDF 拆分为单页对于页面级处理、打印或单独分发文档的各个部分非常有用。使用 Aspose.PDF for Python，'split_to_pages' 方法位于 [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) 类会为源文档中的每一页创建单独的 PDF 文件。此方法可实现页面的自动提取，用于存档、审阅或单独共享，同时保留原始布局和内容。

1. 创建一个 PdfFileEditor 对象。
1. 将 PDF 拆分为单独的页面。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Split PDF into Single Pages
def split_pdf_into_single_pages(input_pdf_path, output_pdf_path):
    pdf_file_editor = pdf_facades.PdfFileEditor()
    pdf_file_editor.split_to_pages(input_pdf_path, output_pdf_path)
```
