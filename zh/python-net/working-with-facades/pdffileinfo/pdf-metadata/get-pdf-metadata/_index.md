---
title: 获取 PDF 元数据
type: docs
weight: 20
url: /zh/python-net/get-pdf-metadata/
description: 使用 Aspose.PDF for Python 提取并显示 PDF 文档的元数据。
lastmod: "2026-06-08"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Python 检索 PDF 元数据。
Abstract: 本指南演示了如何使用 Aspose.PDF for Python 提取并显示 PDF 文档的元数据。您将学习如何访问标准 PDF 属性，如标题、作者、关键字、创建/修改日期，以及自定义元数据字段。此外，指南还涵盖了对 PDF 的有效性、加密和组合文档状态的检查。
---

PDF 文档通常包含描述文档内容、作者信息和权限的有价值元数据。Aspose.PDF 提供了便捷的 API 来检索标准和自定义的元数据属性。此代码片段演示了如何使用 [PdfFileInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) 类以编程方式检查 PDF 文件，包括 Python 中的逐步示例。

1. 加载 PDF 文件。
1. 检索标准元数据。
1. 检查 PDF 状态和安全性。
1. 检索自定义元数据。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_pdf_metadata(infile):

    # Get and display PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)
    print(f"Subject: {pdf_info.subject}")
    print(f"Title: {pdf_info.title}")
    print(f"Keywords: {pdf_info.keywords}")
    print(f"Creator: {pdf_info.creator}")
    print(f"Creation Date: {pdf_info.creation_date}")
    print(f"Modification Date: {pdf_info.mod_date}")

    # Check PDF status
    print(f"Is Valid PDF: {pdf_info.is_pdf_file}")
    print(f"Is Encrypted: {pdf_info.is_encrypted}")
    print(f"Has Open Password: {pdf_info.has_open_password}")
    print(f"Has Edit Password: {pdf_info.has_edit_password}")
    print(f"Is Portfolio: {pdf_info.has_collection}")

    # Retrieve and display a specific custom attribute
    reviewer = pdf_info.get_meta_info("Reviewer")
    print(f"Reviewer: {reviewer if reviewer else 'No Reviewer metadata found.'}")
```
