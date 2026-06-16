---
title: 使用权限管理
type: docs
weight: 100
url: /zh/python-net/usage-rights-management/
description: 了解如何使用 PdfFileSignature 在 Python 中检测并移除 PDF 文档的使用权限。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中移除 PDF 使用权限
Abstract: 本文解释了如何使用 Aspose.PDF for Python via .NET 检查并移除 PDF 文档的使用权限。它展示了如何检查 PDF 是否包含使用权限，以及在移除这些权限后如何保存文档的新版本。
---

Aspose.PDF for Python via .NET 提供了 [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) 用于处理已签名 PDF 及相关使用权限设置的外观层。在某些工作流中，您可能需要检查文档是否包含使用权限，并在保存文件的更新版本之前将其移除。

此示例演示了一项常见的使用权限管理任务：

1. 检查 PDF 是否包含使用权限。
1. 从文档中移除使用权限。
1. 保存更新后的 PDF 文件。

## 检查 PDF 是否包含使用权限

在删除使用权限之前，示例通过调用检查文档的当前状态 `contains_usage_rights()`. 这可让您在进行更改之前确认是否存在使用权。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def check_usage_rights(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        had_usage_rights = pdf_signature.contains_usage_rights()
        print(f"PDF contains usage rights: {had_usage_rights}")
    finally:
        pdf_signature.close()
```

## 从 PDF 中移除使用权限

使用 `remove_usage_rights()` 当文档不再需要保留其现有的使用权设置时。示例检查初始状态，移除权限，并将更新后的 PDF 保存到新文件中。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def remove_usage_rights(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        had_usage_rights = pdf_signature.contains_usage_rights()
        print(f"PDF contains usage rights before removal: {had_usage_rights}")
        pdf_signature.remove_usage_rights()
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```
