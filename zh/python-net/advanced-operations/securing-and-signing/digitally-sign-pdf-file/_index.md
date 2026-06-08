---
title: 在 Python 中添加数字签名或对 PDF 进行数字签名
linktitle: 对 PDF 进行数字签名
type: docs
weight: 10
url: /zh/python-net/digitally-sign-pdf-file/
description: 了解如何在 Python 中对 PDF 文档进行数字签名、添加时间戳以及验证签名。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 对 PDF 文件进行数字签名
Abstract: 本指南说明了如何使用 Aspose.PDF for Python via .NET 对 PDF 文档进行数字签名。它详细介绍了应用标准和高级数字签名的过程，使用证书（PFX 和 PKCS#12），以及自定义签名外观和行为。文档包含代码示例，演示如何对现有 PDF 进行签名、添加时间戳以及验证签名有效性。这使开发人员能够在其 Python 应用程序中确保文档的真实性、完整性，并符合数字签名标准。
---

## 使用数字签名签署 PDF

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_document(infile: str, outfile: str, pfxfile: str) -> None:
    """Sign a PDF document with a PKCS#7 certificate."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7(pfxfile, "12345")
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            signature.save(outfile)
```

一个 **PKCS#7 分离签名** 为文档添加数字签名，而不将内容嵌入签名块中。

当您需要对 PDF 文件使用基于证书的签名、验证签名有效性或向已签名文档添加可信时间戳时，请使用这些示例。

下面的示例使用 PKCS#7 分离数字签名对 PDF 文档进行签署，将签名应用于首页的指定矩形区域。

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_document_PKCS7_detached(
    infile: str,
    outfile: str,
    pfxfile: str,
    password: str,
) -> None:
    """Sign a PDF document with a detached PKCS#7 certificate."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7Detached(
                pfxfile,
                password,
                ap.DigestHashAlgorithm.SHA256,
            )
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            signature.save(outfile)
```

**验证 PDF 文档中的所有数字签名**

1. 创建一个 PdfFileSignature 实例，使您能够在 PDF 中处理签名。
1. 获取签名名称列表 `get_signature_names(True)`.
1. 检查列表中的第一个签名 `verify_signature` 以符合指定的证书。

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify(infile: str) -> None:
    """Verify all digital signatures in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            for signature_name in signature.get_signature_names(True):
                if not signature.verify_signature(signature_name):
                    raise Exception("Not verified")
```

**使用公钥证书文件验证签名**

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify_with_public_key_certificate1(certificate: str, infile: str) -> None:
    """Verify a signature with a public key certificate file."""
    with ap.facades.PdfFileSignature(infile) as file_sign:
        signature_names = file_sign.get_signature_names(True)
        with open(certificate, "rb") as file_stream:
            certificate_bytes = file_stream.read()
        print(file_sign.verify_signature(signature_names[0], certificate_bytes))
```

**使用从文件中提取的证书验证签名**

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify_with_public_key_certificate_from_signature(infile: str) -> None:
    """Verify a signature with the certificate extracted from the file."""
    with ap.facades.PdfFileSignature(infile) as file_sign:
        signature_names = file_sign.get_signature_names(True)
        certificate = []
        if file_sign.try_extract_certificate(signature_names[0], certificate):
            print(file_sign.verify_signature(signature_names[0], certificate[0]))
        else:
            print(False)
```

**验证已启用证书链验证的签名**

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify_signature_with_certificate_check(infile: str) -> None:
    """Verify signatures with certificate-chain validation enabled."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            for signature_name in signature.get_signature_names(True):
                options = ap.security.ValidationOptions()
                options.validation_mode = ap.security.ValidationMode.STRICT
                options.validation_method = ap.security.ValidationMethod.AUTO
                options.check_certificate_chain = True
                options.request_timeout = 20000
                validation_result = []
                verified = signature.verify_signature(
                    signature_name,
                    options,
                    validation_result,
                )
                print(f"Certificate validation result: {validation_result[0].status}")
                print(f"Is verified: {verified}")
```

## 为数字签名添加时间戳

### 如何为 PDF 添加带时间戳的数字签名

Aspose.PDF for Python 支持使用时间戳服务器或 Web 服务对 PDF 进行数字签名。

为了完成此要求， [时间戳设置](https://reference.aspose.com/pdf/python-net/aspose.pdf/timestampsettings/) 类已添加到 Aspose.PDF 命名空间。请查看以下获取时间戳并将其添加到 PDF 文档的代码片段：

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_with_time_stamp_server(
    infile: str,
    outfile: str,
    pfxfile: str,
    password: str,
) -> None:
    """Sign a PDF document and apply a timestamp from an external server."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7(pfxfile, password)
            pkcs.timestamp_settings = ap.TimestampSettings(
                "https://freetsa.org/tsr",
                "",
                ap.DigestHashAlgorithm.SHA256,
            )
            rect = drawing.Rectangle(100, 100, 200, 100)
            signature.sign(
                1, "Signature Reason", "Contact", "Location", True, rect, pkcs
            )
            signature.save(outfile)
```

## 使用 ECDSA 对 PDF 文档进行签名

使用 ECDSA（椭圆曲线数字签名算法）对 PDF 文档进行签名涉及利用椭圆曲线密码学生成数字签名。

上面的代码片段演示了如何使用 Aspose.PDF for Python 对 PDF 文档应用 PKCS#7 分离数字签名。通过加载文档、配置签名外观和安全设置并保存结果，此示例展示了一个完整且可靠的 PDF 文件数字签署工作流。

此方法通过在首页嵌入安全且可验证的签名，确保文档的真实性和完整性。使用 SHA-256 作为摘要算法符合现代密码学标准，而能够控制签名位置则为可见的批准标记提供了灵活性。

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_ecdsa(infile: str, outfile: str, pfxfile: str, password: str) -> None:
    """Sign a PDF document with an ECDSA signature."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7Detached(
                pfxfile,
                password,
                ap.DigestHashAlgorithm.SHA256,
            )
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            signature.save(outfile)
```

**在 PDF 文档中验证 ECDSA 签名**

```python
def verify_ecdsa(infile: str) -> None:
    """Verify ECDSA signatures in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            if not signature.contains_signature():
                raise Exception("Not contains signature")

            for signature_name in signature.get_signature_names(True):
                if not signature.verify_signature(signature_name):
                    raise Exception("Not verified")
```

## 相关安全主题

- [在 Python 中对 PDF 文件进行安全保护和签名](/pdf/zh/python-net/securing-and-signing/)
- [在 Python 中提取图像和签名信息](/pdf/zh/python-net/extract-image-and-signature-information/)
- [在 Python 中使用智能卡签署 PDF 文档](/pdf/zh/python-net/sign-pdf-document-from-smart-card/)
- [在 Python 中加密和解密 PDF 文件](/pdf/zh/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)