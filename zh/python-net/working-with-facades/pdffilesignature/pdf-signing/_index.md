---
title: 签署 PDF 文档
type: docs
weight: 10
url: /zh/python-net/pdf-signing/
description: 了解如何在 Python 中使用 PdfFileSignature 对 PDF 文档进行基于证书、具名和可见的数字签名。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中使用数字签名签署 PDF 文档
Abstract: 本文展示了如何使用 Aspose.PDF for Python via .NET 通过 PdfFileSignature 门面对 PDF 文档进行签名。它涵盖了证书配置、使用基本参数进行签名、使用 PKCS7 对象进行签名、分配签名名称以及应用可见签名外观。
---

Aspose.PDF for Python via .NET 提供了 [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) 用于对现有 PDF 文档应用数字签名的门面。使用证书文件，您可以以编程方式签署文档，将签名放置在页面上，分配签名元数据，并自定义签名的显示方式。

本文演示了几种常见的签名工作流：

1. 创建并绑定一个 `PdfFileSignature` 对象到输入的 PDF。
1. 配置签名证书。
1. 在目标页面上应用数字签名。
1. 可选地分配签名名称和可见外观。
1. 保存已签名的 PDF。

## 准备可重用的签名助手

在对 PDF 应用数字签名之前，设置一小组可重用的帮助函数是有益的。这些帮助函数会初始化签名处理器，定义可见签名区域，配置证书，并构建可重用的 PKCS#7 签名对象，从而使下面的签名示例保持自包含且更易于理解。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd


DEFAULT_CERTIFICATE_PASSWORD = "Aspose2021"
DEFAULT_SIGNATURE_NAME = "Signature1"


def create_pdf_file_signature(infile):
    pdf_signature = pdf_facades.PdfFileSignature()
    pdf_signature.bind_pdf(infile)
    return pdf_signature


def create_signature_rectangle():
    return apd.Rectangle(10, 10, 200, 60)


def configure_signature_certificate(
    pdf_signature, certificate_path, certificate_password=DEFAULT_CERTIFICATE_PASSWORD
):
    pdf_signature.set_certificate(certificate_path, certificate_password)


def create_pkcs7_signature(
    certificate_path, certificate_password=DEFAULT_CERTIFICATE_PASSWORD
):
    signature = ap.forms.PKCS7(certificate_path, certificate_password)
    signature.reason = "Document approval"
    signature.contact_info = "qa@example.com"
    signature.location = "New York, USA"
    signature.authority = "Aspose.PDF Example"
    return signature


def create_custom_signature_appearance():
    appearance = ap.forms.SignatureCustomAppearance()
    appearance.font_family_name = "Arial"
    appearance.font_size = 10
    appearance.show_contact_info = True
    appearance.show_location = True
    appearance.show_reason = True
    return appearance
```

## 使用基本证书参数签署 PDF

此方法将证书直接配置在 `PdfFileSignature` 对象。当您希望使用标准签名元数据的直接签名流程且不需要单独的签名对象管理时，这非常有用。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def sign_pdf_with_basic_parameters(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        configure_signature_certificate(pdf_signature, certificate_path)
        pdf_signature.sign(
            1,
            "Document approval",
            "qa@example.com",
            "New York, USA",
            False,
            create_signature_rectangle(),
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## 使用 PKCS7 对象签署 PDF

使用一个 `PKCS7` 对象当你需要先准备签名然后将其传入签名调用时使用。这种模式让你对签名设置有更多控制，并且是更高级工作流的良好基础。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def sign_pdf_with_certificate_object(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        signature = create_pkcs7_signature(certificate_path)
        pdf_signature.sign(1, False, create_signature_rectangle(), signature)
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## 使用具名签名对 PDF 进行签署

如果您的文档工作流依赖于预定义的签名字段名称，请将该名称传递给 `sign()`. 这使得随后在验证、处理或与批准工作流集成时更容易引用该签名。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def sign_pdf_with_named_signature(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        signature = create_pkcs7_signature(certificate_path)
        signature.reason = "Approved by signing workflow"
        pdf_signature.sign(
            1,
            DEFAULT_SIGNATURE_NAME,
            "Approved by signing workflow",
            "qa@example.com",
            "New York, USA",
            True,
            create_signature_rectangle(),
            signature,
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## 应用可见签名

您可以通过为其分配自定义外观，使签名在 PDF 页面上可见 `PKCS7` 对象。当输出文档需要向最终用户显示批准详情（例如原因、位置和联系信息）时，这非常有用。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def apply_visible_signature(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        signature = create_pkcs7_signature(certificate_path)
        signature.reason = "Visible approval signature"
        signature.custom_appearance = create_custom_signature_appearance()
        pdf_signature.sign(
            1,
            "Visible approval signature",
            "qa@example.com",
            "New York, USA",
            True,
            create_signature_rectangle(),
            signature,
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```
