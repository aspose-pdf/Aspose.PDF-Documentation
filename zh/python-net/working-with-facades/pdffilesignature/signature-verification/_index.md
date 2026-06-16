---
title: 签名验证
type: docs
weight: 90
url: /zh/python-net/signature-verification/
description: 了解如何使用 Python 中的 PdfFileSignature 验证数字签名并检查 PDF 是否包含签名。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中验证 PDF 签名
Abstract: 本文解释了如何使用 Aspose.PDF for Python via .NET 验证 PDF 文档中的数字签名。它展示了如何验证现有签名以及如何检查 PDF 是否包含任何签名。
---

Aspose.PDF for Python via .NET 提供了 [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) 用于验证已签名 PDF 文档的外观层。PDF 签名后，您可以使用它确认签名有效并检测文档是否包含任何签名条目。

本示例演示了两项常见的验证任务：

1. 验证已有的 PDF 签名是否有效。
1. 检查 PDF 是否包含任何签名。

## 验证 PDF 签名

使用 `verify_signature()` 当您需要在文档中验证特定签名时。该示例解析第一个可用的签名名称，并验证该签名是否有效。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def verify_pdf_signature(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        is_valid = pdf_signature.verify_signature(sign_name)
        print(f"Signature '{sign_name}' is valid: {is_valid}")
    finally:
        pdf_signature.close()
```

## 检查 PDF 是否包含签名

使用 `contains_signature()` 当您只需要了解 PDF 是否包含任何签名时。这在进行更详细的验证或提取逻辑之前，作为快速检查非常有用。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def check_if_pdf_contains_signatures(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        contains_signatures = pdf_signature.contains_signature()
        print(f"PDF contains signatures: {contains_signatures}")
    finally:
        pdf_signature.close()
```
