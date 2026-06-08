---
title: 在 Python 中使用智能卡签署 PDF 文档
linktitle: 使用智能卡进行 PDF 签名
type: docs
weight: 30
url: /zh/python-net/sign-pdf-document-from-smart-card/
description: 了解如何在 Python 中使用智能卡和外部证书签署 PDF 文档。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 从智能卡签署 PDF 文档
Abstract: 本指南解释了如何使用 Aspose.PDF for Python via .NET 通过智能卡对 PDF 文档进行数字签名。它演示了如何通过 Windows 证书存储访问存储在硬件设备（如 USB 令牌或智能卡）中的证书，并将其用于签署 PDF 文件。文档包含代码示例，展示如何定位相应的证书、配置签名属性以及将数字签名嵌入 PDF 中。这实现了符合数字签名标准的安全硬件支持签名，适用于高信任的企业和法律工作流。
---

Aspose.PDF 提供强大的功能，用于集成可视化和加密签名组件，确保数字签名 PDF 文档的真实性和专业呈现。

当您的签名过程依赖于存储在硬件支持设备（如智能卡、USB 令牌或受管理的证书存储）中的证书时，请使用此工作流。

## 使用签名字段进行智能卡签名

本示例演示如何使用 Aspose.PDF for Python 通过外部证书对 PDF 文档进行数字签名，并应用自定义签名外观图像：

1. 打开 PDF 文档。
1. 创建 PdfFileSignature 对象并将其绑定到文档。
1. 使用自定义方法检索本地数字证书 `get_local_certificate()`.
1. 基于所选证书设置 ExternalSignature。
1. 应用自定义签名外观图像（例如，公司徽标或手写签名）。
1. 在文档的首页进行数字签名，并附加指定的元数据（原因、联系方式、位置）。
1. 将已签名的文档保存到新的输出文件。

此方法非常适用于需要通过外部证书以编程方式进行签名的情况——例如硬件令牌、证书存储或受信任的提供者——并以个性化的视觉布局呈现。

以下是使用智能卡签署 PDF 文档的代码片段：

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_with_smart_card(infile: str, outfile: str, pngfile: str) -> None:
    """Sign a PDF document using a smart-card certificate."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature() as pdf_signature:
            pdf_signature.bind_pdf(document)
            external_signature = ap.forms.ExternalSignature(get_local_certificate())
            pdf_signature.signature_appearance = pngfile
            pdf_signature.sign(
                1,
                "Reason",
                "Contact",
                "Location",
                True,
                drawing.Rectangle(100, 100, 200, 200),
                external_signature,
            )
            pdf_signature.save(outfile)
```

## 验证数字签名

此代码片段演示了如何使用 Aspose.PDF for Python 验证 PDF 文档中的数字签名：

1. 打开 PDF 文件。
1. 创建一个 'PdfFileSignature object' 并将其绑定到文档。
1. 使用 'get_signature_names()' 检索所有签名字段名称的列表。
1. 通过 'verify_signature()' 遍历每个签名并验证其有效性。
1. 如果任何签名验证失败，则抛出异常。

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify_external_signature(infile: str) -> None:
    """Verify an external signature in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as pdf_signature:
            for signature_name in pdf_signature.get_signature_names(True):
                if not pdf_signature.verify_signature(signature_name):
                    raise Exception("Not verified")
```

## 使用外部证书签名

此代码片段演示了如何使用 Aspose.PDF for Python 并结合外部证书，在 PDF 文档中添加并签署数字签名字段：

1. 以二进制流打开 PDF 文件。
1. 创建 SignatureField 并将其放置在文档的第一页的指定位置。
1. 使用自定义方法检索本地数字证书 `get_local_certificate()`.
1. 设置 ExternalSignature，并提供权限、原因和联系信息等元数据。
1. 为签名字段分配唯一的字段名称 (partial_name = "sig1").
1. 在 PDF 的表单字段中添加签名字段。
1. 使用外部证书对字段进行签名。
1. 将已签名的文档保存到输出文件。

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def get_signature_info_using_signature_field(infile: str, outfile: str) -> None:
    """Create a signature field and sign it with an external certificate."""
    with open(infile, "rb+") as file_stream:
        document = ap.Document(file_stream)
        signature_field = ap.forms.SignatureField(
            document.pages[1],
            ap.Rectangle(100, 400, 10, 10, True),
        )
        selected_certificate = get_local_certificate()
        external_signature = ap.forms.ExternalSignature(selected_certificate)
        external_signature.authority = "Me"
        external_signature.reason = "Reason"
        external_signature.contact_info = "Contact"
        signature_field.partial_name = "sig1"
        document.form.add(signature_field, 1)
        signature_field.sign(external_signature)
        document.save(outfile)
```

## 相关安全主题

- [在 Python 中对 PDF 文件进行安全保护和签名](/pdf/zh/python-net/securing-and-signing/)
- [在 Python 中对 PDF 文件进行数字签名](/pdf/zh/python-net/digitally-sign-pdf-file/)
- [在 Python 中提取 PDF 的签名信息](/pdf/zh/python-net/extract-image-and-signature-information/)
- [在 Python 中加密和解密 PDF 文件](/pdf/zh/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)

