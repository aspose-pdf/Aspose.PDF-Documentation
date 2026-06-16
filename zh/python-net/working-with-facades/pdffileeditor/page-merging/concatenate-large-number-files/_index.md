---
title: 合并大量 PDF 文件
type: docs
weight: 10
url: /zh/python-net/concatenate-large-number-files/
description: 使用 Aspose.PDF for Python 高效合并大量 PDF 文件。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中使用磁盘缓存合并大型 PDF 文件
Abstract: 了解如何使用 Aspose.PDF for Python 高效合并大量 PDF 文件。本示例演示如何启用磁盘缓存，以在不耗尽系统内存的情况下处理大型 PDF，确保多个文件的顺畅合并。
---

在处理大型 PDF 文件集合时，内存消耗可能成为合并过程的瓶颈。使用 Aspose.PDF for Python，您可以在 the [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) 类中高效合并多个 PDF。concatenate 方法将输入文件合并为单个 PDF，同时磁盘缓冲区防止高内存使用。这种方法非常适合处理大量文档、自动化报告生成或整合大型 PDF 档案。

1. 创建一个 PdfFileEditor 对象。
1. 合并多个 PDF 文件。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_large_number_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.use_disk_buffer = True  # Enable disk buffering for large files
    pdf_editor.concatenate(files_to_merge, output_file)
```
