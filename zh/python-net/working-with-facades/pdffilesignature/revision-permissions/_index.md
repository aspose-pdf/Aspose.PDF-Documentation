---
title: 修订和权限
type: docs
weight: 40
url: /zh/python-net/revision-permissions/
description: 了解如何使用 Python 中的 PdfFileSignature 检查 PDF 文件中的签名修订、文档修订和认证权限。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中读取 PDF 签名修订和访问权限数据
Abstract: 本文阐述了如何使用 Aspose.PDF for Python via .NET 检查已签名或已认证 PDF 文件中的修订和权限信息。它展示了如何获取签名的修订号、统计文档的总修订次数，以及从认证的 PDF 中读取访问权限。
---

Aspose.PDF for Python via .NET 提供了 [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) 用于处理已签名和已认证 PDF 文档的外观层。除了添加签名外，您还可以检查签名元数据，以了解文档包含多少次修订以及认证后允许进行哪些更改。

此示例演示了三项常见的检查任务：

1. 获取现有签名的修订号。
1. 获取已签名文档中的修订总数。
1. 读取已认证 PDF 的访问权限。

## 获取签名的修订号

当 PDF 已经包含一个或多个签名且您需要识别与特定签名关联的修订时，请使用此方法。示例解析第一个可用的签名名称，然后调用 `get_revision()`.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_revision(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_revision = pdf_signature.get_revision(sign_name)
        print(f"Signature Revision for '{sign_name}': {signature_revision}")
    finally:
        pdf_signature.close()
```

## 获取文档修订的总数

使用 `get_total_revision()` 当您需要了解已签名的 PDF 中存储了多少修订时。这对于检查文档在原始签名应用后是否经过了多次更新非常有用。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_total_document_revisions(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        total_revisions = pdf_signature.get_total_revision()
        print(f"Total Document Revisions: {total_revisions}")
    finally:
        pdf_signature.close()
```

## 获取已认证 PDF 的访问权限

已认证的文档可以定义在认证后允许进行的更改。使用 `get_access_permissions()` 检查该权限级别并确定文档是否不允许任何更改、仅允许填写表单或其他受控修改。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_access_permissions(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        access_permissions = pdf_signature.get_access_permissions()
        print(f"Access Permissions: {access_permissions}")
    finally:
        pdf_signature.close()
```

