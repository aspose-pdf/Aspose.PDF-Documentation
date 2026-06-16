---
title: 清除 PDF 元数据
type: docs
weight: 10
url: /zh/python-net/clear-pdf-metadata/
description: 使用 Aspose.PDF for Python via .NET 删除 PDF 文档中的所有元数据。
lastmod: "2026-06-08"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Python 清除 PDF 元数据
Abstract: 本指南解释了如何使用 Aspose.PDF for Python via .NET 删除 PDF 文档中的所有元数据。您将学习清除标准和自定义元数据字段并保存已净化的 PDF。这对于隐私、安全或为公开发布准备 PDF 非常有用。
---

PDF 通常包含元数据，如标题、作者、关键字、创建日期和自定义字段。在某些情况下，您可能想要删除 PDF 的所有元数据，例如在分发或存档之前。Aspose.PDF 提供了 clear_info() 方法，可轻松删除所有元数据。清除后，您可以使用 save() 方法保存 PDF。

1. 加载 PDF 文件。
1. 清除所有元数据。
1. 保存已清理的 PDF。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def clear_pdf_metadata(infile, outfile):

    # Get PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)

    # Clear PDF metadata
    pdf_info.clear_info()

    # Save updated metadata
    pdf_info.save(outfile)
```
