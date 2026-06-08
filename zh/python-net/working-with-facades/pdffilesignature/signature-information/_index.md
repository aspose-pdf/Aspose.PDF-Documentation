---
title: 签名信息
type: docs
weight: 60
url: /zh/python-net/signature-information/
description: 了解如何使用 Python 中的 PdfFileSignature 从已签名的 PDF 文件中读取签名名称、签署者详细信息、时间戳以及签名元数据。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中读取 PDF 文档的签名详细信息
Abstract: 本文说明了如何使用 Aspose.PDF for Python via .NET 检查已签名 PDF 文档中的签名元数据。它展示了如何列出签名名称、读取签署者详细信息、获取签署日期和时间，以及提取签名原因和位置。
---

Aspose.PDF for Python via .NET 提供了 [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) 用于检查 PDF 文档中数字签名的外观层。文档签署后，您可以使用它读取签名名称并检索元数据，如签署人姓名、联系信息、签署时间、原因和位置。

本示例演示了四个常见的签名信息任务：

1. 列出已签名 PDF 中的所有签名名称。
1. 读取所选签名的签署人详细信息。
1. 获取签署日期和时间。
1. 读取签名原因和位置。

## 获取签名名称

当 PDF 可能包含一个或多个签名且您想检查哪些签名条目可用时，请使用此方法。示例打开文档并打印返回的列表。 `get_sign_names()`.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_names(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        signature_names = list_signature_names(pdf_signature)
        print(f"Signature Names: {signature_names}")
    finally:
        pdf_signature.close()
```

## 获取签署者详细信息

一旦您知道签名名称，就可以检索特定签名者的元数据。本示例读取文档中第一个可用签名的签名者姓名和联系信息。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signer_details(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signer_name = pdf_signature.get_signer_name(sign_name)
        contact_info = pdf_signature.get_contact_info(sign_name)
        print(
            f"Signer Details for '{sign_name}': "
            f"signer_name={signer_name}, contact_info={contact_info}"
        )
    finally:
        pdf_signature.close()
```

## 获取签名日期和时间

使用 `get_date_time()` 用于确定特定签名何时被应用。这对于审计以及在文档工作流中显示签名历史非常有用。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_date_and_time(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_date = pdf_signature.get_date_time(sign_name)
        print(f"Signature Date and Time for '{sign_name}': {signature_date}")
    finally:
        pdf_signature.close()
```

## 获取签名原因和位置

数字签名还可以存储描述性元数据，例如签名原因和位置。本例检索所选签名的这两个值并将它们一起打印。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_reason_and_location(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_reason = pdf_signature.get_reason(sign_name)
        signature_location = pdf_signature.get_location(sign_name)
        print(
            f"Signature Reason and Location for '{sign_name}': "
            f"reason={signature_reason}, location={signature_location}"
        )
    finally:
        pdf_signature.close()
```

