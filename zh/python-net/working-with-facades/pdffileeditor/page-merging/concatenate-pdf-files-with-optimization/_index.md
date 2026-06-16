---
title: 合并 PDF 文件并进行优化
type: docs
weight: 30
url: /zh/python-net/concatenate-pdf-files-with-optimization/
description: 使用 Aspose.PDF for Python 将多个 PDF 文件合并为单个优化的 PDF。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中合并 PDF 文件并生成优化的输出
Abstract: 了解如何使用 Aspose.PDF for Python 将多个 PDF 文件合并为单个优化的 PDF。本示例演示如何启用大小优化，以在保持内容和格式的同时减小输出文件的大小。
---

在合并多个 PDF 时，生成的文件可能会变得很大，尤其是其中包含图像或复杂内容时。使用 Aspose.PDF for Python，开发者可以在合并过程中启用优化，以在不降低质量的前提下降小文件尺寸。类中的 optimize_size 属性在 the [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) 类确保合并后的 PDF 紧凑高效，使其适合共享、存储或归档。

1. 创建一个 PdfFileEditor 对象并启用优化。
1. 合并 PDF 文件。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_pdf_files_with_optimization(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.optimize_size = True  # Enable optimization for smaller output file size
    pdf_editor.concatenate(files_to_merge, output_file)
```
