---
title: 签名提取
type: docs
weight: 50
url: /zh/python-net/signature-extraction/
description: 了解如何使用 Python 中的 PdfFileSignature 从已签名的 PDF 中提取签名图像和签署证书。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中从 PDF 提取签名图像和证书
Abstract: 本文说明了如何使用 Aspose.PDF for Python via .NET 从已签名的 PDF 文档中提取与签名相关的数据。它展示了如何读取第一个可用的签名，导出其图像，并将相关的证书流保存为输出文件。
---

Aspose.PDF for Python via .NET 提供了 [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) 用于检查和提取已签名 PDF 文档数据的外观接口。PDF 签名后，您可以使用它导出签名资源，例如可视签名图像和与签名关联的证书。

本示例演示了两项常见的提取任务：

1. 提取与签名关联的可视图像。
1. 从已签名的 PDF 中提取签名证书。

## 提取签名图像

当 PDF 包含可见签名且您想导出其图像数据时使用此方法。示例打开已签名的文档，获取第一个可用的签名名称，提取图像流，并将其写入文件。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def extract_signature_image(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_image = pdf_signature.extract_image(sign_name)
        write_stream_data(signature_image, outfile)
    finally:
        pdf_signature.close()
```

## 提取签名证书

使用 `extract_certificate()` 当您需要将证书数据附加到签名时。这对于检查、验证工作流或将签名者证书与 PDF 文档分开存储非常有用。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def extract_signature_certificate(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_certificate = pdf_signature.extract_certificate(sign_name)
        write_stream_data(signature_certificate, outfile)
    finally:
        pdf_signature.close()
```

