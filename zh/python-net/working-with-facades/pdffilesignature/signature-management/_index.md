---
title: 签名管理
type: docs
weight: 80
url: /zh/python-net/signature-management/
description: 了解如何使用 Python 中的 PdfFileSignature 从 PDF 文档中删除数字签名，并可选地清理签名字段。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中删除 PDF 签名并清理签名字段
Abstract: 本文阐述了如何使用 Aspose.PDF for Python via .NET 管理 PDF 文档中现有的数字签名。它展示了如何从 PDF 中删除签名以及如何连同其关联的签名字段一起删除签名。
---

Aspose.PDF for Python via .NET 提供了 [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) 用于处理 PDF 文档中现有数字签名的外观层。除了读取和验证签名外，当工作流需要更新已签署的内容或清除签名字段时，您也可以删除签名。

此示例演示了两个常见的签名管理任务：

1. 从 PDF 文档中移除签名。
1. 移除签名并清理相关的签名字段。

## 从 PDF 中移除签名

使用 `remove_signature()` 当您想要从文档中删除选定的签名，同时保留底层签名字段结构时。示例打开已签名的 PDF，解析签名名称，将其移除，并保存更新后的输出文件。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def remove_signature_from_pdf(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        pdf_signature.remove_signature(sign_name)
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## 删除签名并清理字段

使用带有附加的 `True` 当您想要删除签名并清理相关签名字段时使用此标记。此功能在签名删除后不希望该字段保留在文档中时非常有用。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def remove_signature_with_field_cleanup(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        pdf_signature.remove_signature(sign_name, True)
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```
