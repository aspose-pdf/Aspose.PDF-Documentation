---
title: 合并多个 PDF 文件
type: docs
weight: 20
url: /zh/python-net/concatenate-pdf-files/
description: 使用 Aspose.PDF for Python 将多个 PDF 文件合并为单个文档。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中将多个 PDF 文件合并为一个 PDF
Abstract: 了解如何使用 Aspose.PDF for Python 将多个 PDF 文件合并为单个文档。此示例演示如何使用 concatenate 方法无缝合并多个 PDF，同时保留其内容和格式。
---

合并 PDF 文件是文档管理、报告和自动化工作流中的常见任务。使用 Aspose.PDF for Python，开发人员可以轻松将多个 PDF 文件合并为单一的综合文档。该类的 concatenate 方法 [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) 确保所有输入文件的页面都保留在最终输出中，保持原始布局和内容。此方法对于创建综合报告、合并表单或高效归档多个文档非常有用。

1. 创建一个 PdfFileEditor 对象。
1. 合并多个 PDF 文件。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_pdf_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.concatenate(files_to_merge, output_file)
```
