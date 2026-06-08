---
title: 使用 XMP 保存元数据
type: docs
weight: 30
url: /zh/python-net/save-metadata-with-xmp/
description: 使用 Aspose.PDF for Python via .NET 通过 XMP 保存 PDF 元数据
lastmod: "2026-06-08"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Python 通过 XMP 保存 PDF 元数据
Abstract: 本指南演示了如何使用 Aspose.PDF for Python via .NET 通过 XMP（可扩展元数据平台）保存 PDF 元数据。XMP 确保标准元数据和自定义元数据都以标准化的 XML 格式嵌入到 PDF 中，提高了在不同应用程序和工作流之间的兼容性。
---

PDF 元数据可以通过多种方式存储，而 XMP 是在 PDF 文件中嵌入元数据的现代化、标准化方法。使用 Aspose.PDF，您可以更新 Title、Subject、Keywords 和 Creator 等标准字段，然后以 XMP 格式保存它们，以确保更广的兼容性和面向未来的可靠性。推荐使用此方法而不是传统的元数据存储方式。

1. 加载 PDF 文件。
1. 设置标准元数据字段。
1. 以 XMP 格式保存元数据。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def save_info_with_xmp(infile, outfile):

    # Get PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)

    # Set PDF metadata
    pdf_info.subject = "Aspose PDF for Python via .NET"
    pdf_info.title = "Aspose PDF for Python via .NET"
    pdf_info.keywords = "Aspose, PDF, Python, .NET"
    pdf_info.creator = "Aspose Team"

    # Save updated metadata
    pdf_info.save_new_info_with_xmp(outfile)
```
