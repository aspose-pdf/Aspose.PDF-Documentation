---
title: 从开头拆分 PDF
type: docs
weight: 10
url: /zh/python-net/split-pdf-from-beginning/
description: 使用 Aspose.PDF for Python 从开头拆分 PDF 文档。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中使用 Aspose.PDF 从起始位置拆分 PDF
Abstract: 了解如何使用 Aspose.PDF for Python 从开头拆分 PDF 文档。此示例演示从第1页开始提取特定页数，以创建新的 PDF 文档。
---

从开头拆分 PDF 在您需要将文档的前几页作为单独文件时非常有用。使用 Aspose.PDF for Python，类中的 split_from_first 方法 [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) 类允许您从第1页开始提取指定页数。此功能非常适合生成摘录、预览或更大 PDF 的较小部分，而无需手动编辑原始文件。

1. 创建一个 PdfFileEditor 对象。
1. 从第一页拆分 PDF。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Split PDF from Beginning
def split_pdf_from_beginning(input_pdf_path, output_pdf_path):
    pdf_file_editor = pdf_facades.PdfFileEditor()
    pdf_file_editor.split_from_first(input_pdf_path, 3, output_pdf_path)
```
