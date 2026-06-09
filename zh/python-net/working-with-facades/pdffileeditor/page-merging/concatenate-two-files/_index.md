---
title: 合并两个 PDF 文件
type: docs
weight: 60
url: /zh/python-net/concatenate-two-files/
description: 使用 Aspose.PDF for Python 将两个 PDF 文件合并为单个文档。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中将两个 PDF 文件合并为单个 PDF
Abstract: 了解如何使用 Aspose.PDF for Python 将两个 PDF 文件合并为单个文档。本示例演示了如何无缝合并两个 PDF，同时保留其原始内容和格式。
---

在合并报告、合同或表单时，合并两个 PDF 文件是一项常见任务。使用 Aspose.PDF for Python，您可以通过编程方式使用该类的 concatenate 方法将两个 PDF 合并为单个文档 the [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) 类。这确保了两个文件的所有页面都包含在输出的 PDF 中，同时保持原始的布局、内容和结构。

1. 创建一个 PdfFileEditor 对象。
1. 合并两个 PDF 文件。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_two_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.concatenate(files_to_merge[0], files_to_merge[1], output_file)
```
