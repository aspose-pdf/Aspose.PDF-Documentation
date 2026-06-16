---
title: 拆分 PDF 到末页
type: docs
weight: 40
url: /zh/python-net/split-pdf-to-end/
description: 使用 Aspose.PDF for Python 将 PDF 文档从指定页面拆分至最后一页。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中将 PDF 从特定页拆分至末页
Abstract: 了解如何使用 Aspose.PDF for Python 将 PDF 文档从指定页面拆分至最后一页。本示例演示了从指定页面开始提取所有页面，以创建新的 PDF 文件。
---

将 PDF 从特定页面拆分至末页在需要将文档后半部分作为单独文件时非常有用。使用 Aspose.PDF for Python，split_to_end 方法属于该 class [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) 该 class 允许您提取从任意页码开始直至文档最后一页的页面。这非常适合创建摘录、提取章节，或在无需手动编辑的情况下处理大型 PDF 的部分内容。

1. 创建一个 PdfFileEditor 对象。
1. 将 PDF 从特定页面拆分至文档末尾。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Split PDF to End
def split_pdf_to_end(input_pdf_path, output_pdf_path):
    pdf_file_editor = pdf_facades.PdfFileEditor()
    pdf_file_editor.split_to_end(input_pdf_path, 2, output_pdf_path)
```
