---
title: 签名完整性检查
type: docs
weight: 70
url: /zh/python-net/signature-integrity-checks/
description: 了解如何使用 Python 中的 PdfFileSignature 检查 PDF 签名是否覆盖整个文档并验证已签署文档的完整性。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中验证 PDF 签名覆盖范围和完整性
Abstract: 本文解释了如何使用 Aspose.PDF for Python via .NET 检查已签署 PDF 文档中的数字签名完整性。它展示了如何验证签名是否覆盖整个文档以及如何验证已签署内容的完整性。
---

Aspose.PDF for Python via .NET 提供了 [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) 用于验证已签署 PDF 文档的外观层。文件签署后，你可以使用它检查签名是否适用于完整文档以及已签署内容是否仍然有效。

此示例演示了两种常见的完整性检查：

1. 检查签名是否覆盖整个文档。
1. 验证已签名 PDF 内容的完整性。

## 检查签名是否覆盖整个文档

使用 `covers_whole_document()` 当您需要确认签名适用于完整的 PDF，而不仅仅是其内容的一部分时。示例读取第一个可用的签名名称并检查其覆盖范围。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def check_signature_coverage(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        covers_document = pdf_signature.covers_whole_document(sign_name)
        print(f"Signature '{sign_name}' covers the whole document: {covers_document}")
    finally:
        pdf_signature.close()
```

## 验证文档完整性

使用 `verify_signed()` 以确认签名后文档内容未被更改。此方法有助于验证文档在所选签名下是否仍然有效。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def validate_document_integrity(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        is_valid = pdf_signature.verify_signed(sign_name)
        print(f"Document integrity for '{sign_name}' is valid: {is_valid}")
    finally:
        pdf_signature.close()
```

