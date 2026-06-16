---
title: 尝试合并两个 PDF 文件
type: docs
weight: 90
url: /zh/python-net/try-concatenate-two-files/
description: 使用 Aspose.PDF for Python 合并两个 PDF 文件。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中安全合并两个 PDF 文件，无异常
Abstract: 了解如何使用 Aspose.PDF for Python 安全地合并两个 PDF 文件。try_concatenate 方法在不抛出异常的情况下合并文件，即使操作失败也能实现优雅的错误处理。
---

合并两个 PDF 文件有时可能因为文件损坏、不兼容的格式或其他问题而失败。使用 Aspose.PDF for Python，PdfFileEditor 类的 try_concatenate 方法允许您安全地尝试合并两个 PDF。如果操作失败，它会返回 False 而不是抛出异常，使您能够在自动化工作流或批处理过程中完全控制错误处理。

1. 创建一个 PdfFileEditor 对象。
1. 尝试合并两个 PDF 文件。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def try_concatenate_two_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    if not pdf_editor.try_concatenate(
        files_to_merge[0], files_to_merge[1], output_file
    ):
        print("Concatenation failed for the provided files.")
```
