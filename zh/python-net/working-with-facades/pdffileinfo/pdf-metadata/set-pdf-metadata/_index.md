---
title: 设置 PDF 元数据
type: docs
weight: 50
url: /zh/python-net/set-pdf-metadata/
description: 使用 Aspose.PDF for Python via .NET 修改并保存 PDF 文档中的元数据。
lastmod: "2026-06-08"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Python 更新 PDF 元数据
Abstract: 本指南说明了如何使用 Aspose.PDF for Python via .NET 修改并保存 PDF 文档中的元数据。它演示了如何更新标准 PDF 属性，如标题、主题、关键字和创建者，以及自定义元数据字段。完成后，您将能够以编程方式更新 PDF 元数据并保存更改。
---

PDF 文档可以包含标准元数据（Title、Subject、Keywords、Creator、Author）和以 XMP 属性存储的自定义元数据。Aspose.PDF 提供了一个简洁的 API 用于在 Python 中修改这些属性。本指南涵盖了如何更新这些字段并使用 the [PdfFileInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) 类。

1. 加载 PDF 文件。
1. 更新标准元数据。
1. 添加或更新自定义元数据。
1. 保存更新后的元数据。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_pdf_metadata(infile, outfile):

    # Get PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)

    # Set PDF metadata
    pdf_info.subject = "Aspose PDF for Python via .NET"
    pdf_info.title = "Aspose PDF for Python via .NET"
    pdf_info.keywords = "Aspose, PDF, Python, .NET"
    pdf_info.creator = "Aspose Team"

    pdf_info.set_meta_info("CustomKey", "CustomValue")

    # pdf_info.save_new_info(outfile)
    # Is obsolete, use save() method instead

    # Save updated metadata
    pdf_info.save(outfile)
```
