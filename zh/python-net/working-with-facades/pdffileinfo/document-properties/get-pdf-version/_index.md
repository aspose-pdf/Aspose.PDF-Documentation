---
title: 获取 PDF 版本
type: docs
weight: 20
url: /zh/python-net/get-pdf-version/
description: 了解如何使用 Aspose.PDF for Python 以编程方式确定 PDF 文档的版本。本教程演示如何使用 PdfFileInfo 类检查文件的 PDF 版本。
lastmod: "2026-06-08"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Python 检索 PDF 版本
Abstract: PDF 文档具有指示其支持的功能和规范的版本号（例如 1.4、1.7、2.0）。了解 PDF 版本对于兼容性、功能支持和文档处理工作流非常重要。在本指南中，您将学习如何使用 Aspose.PDF for Python 中的 PdfFileInfo 类以编程方式检索 PDF 版本。
---

PDF 版本定义了文档中支持的功能和能力，包括表单字段、加密、批注和压缩。对于处理多个 PDF 的开发者来说，检查版本可以确保与处理这些文件的工具、库或工作流的兼容性。

使用 Aspose.PDF for Python，您可以轻松检查 PDF 版本，使用 [PdfFileInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) 类。

1. 加载 PDF 文档。
1. 检索其 PDF 版本。
1. 在控制台显示该版本。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_pdf_version(input_file_name):

    pdf_metadata = pdf_facades.PdfFileInfo(input_file_name)
    version = pdf_metadata.get_pdf_version()
    print(f"\nPDF Version: {version}")
```
