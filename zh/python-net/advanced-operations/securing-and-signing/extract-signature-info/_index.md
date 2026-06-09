---
title: 在 Python 中从 PDF 提取签名信息
linktitle: 从签名中提取详细信息
type: docs
weight: 20
url: /zh/python-net/extract-image-and-signature-information/
description: 学习如何在 Python 中从 PDF 文件中提取签名图像、证书和数字签名详细信息。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中从 PDF 中提取签名图像和证书详细信息。
Abstract: 本文介绍了如何使用 Aspose.PDF for Python 从 PDF 文档中提取图像和数字签名信息。了解如何检索签名图像、提取证书数据、检查签名算法以及检测已签名 PDF 文件中的受损签名。
---

## 从签名字段提取图像

Aspose.PDF for Python via .NET 让您检索嵌入在 a 中的可视图像 [签名字段](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/). 当您需要显示或归档签名外观而无需渲染完整 PDF 时，这很有用。

下面的示例遍历所有表单字段，查找每一个 `SignatureField`, 并将其图像保存为 JPEG 文件：

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def extract_images_from_signature_field(infile: str, outfile: str) -> None:
    """Extract the image stored in a signature field."""
    with ap.Document(infile) as document:
        for field in document.form:
            if not isinstance(field, ap.forms.SignatureField):
                continue

            image_stream = field.extract_image()
            if image_stream is None:
                continue

            image = drawing.Bitmap.from_stream(image_stream)
            image.save(outfile, drawing.imaging.ImageFormat.jpeg)
```

## 读取签名算法详情

使用 `PdfFileSignature.get_signatures_info()` 读取文档中每个签名的加密元数据——包括摘要算法、算法类型、加密标准和签名名称：

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def get_signatures_info(infile: str) -> None:
    """Print information about all signatures in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            for signature_info in signature.get_signatures_info():
                print(signature_info.DIGEST_HASH_ALGORITHM)
                print(signature_info.ALGORITHM_TYPE)
                print(signature_info.CRYPTOGRAPHIC_STANDARD)
                print(signature_info.signature_name)
```

## 从签名字段中提取数字证书

使用 [提取证书](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/#methods) 方法在 a `SignatureField` 检索嵌入的证书为字节流并将其保存到磁盘以进行外部验证：

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def extract_certificate(infile: str, outfile: str) -> None:
    """Extract a certificate from a signature field and save it to disk."""
    with ap.Document(infile, password="owner") as document:
        for field in document.form:
            if not isinstance(field, ap.forms.SignatureField):
                continue

            certificate_stream = field.extract_certificate()
            if certificate_stream is None:
                continue

            with certificate_stream:
                bytes_data = bytearray(certificate_stream.length)
                certificate_stream.read(bytes_data, 0, len(bytes_data))
                with open(outfile, "wb") as file_stream:
                    file_stream.write(bytes_data)
                return
```

## 使用 PdfFileSignature 外观提取证书

`PdfFileSignature.try_extract_certificate()` 提供了一种通过签名名称检索证书的替代方法。以下示例遍历所有签名名称，并尝试对每个进行提取：

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def extract_certificate_try_extract_certificate_method(infile: str) -> None:
    """Extract certificates with the try_extract_certificate facade method."""
    with ap.Document(infile, password="owner") as document:
        with ap.facades.PdfFileSignature(document) as signature:
            for signature_name in signature.get_signature_names(True):
                certificate = []
                if signature.try_extract_certificate(signature_name, certificate):
                    print("The certificate extraction succeeded")
```

## 验证外部数字签名

要确认文档在签名后未被修改，请使用以下方式验证每个外部签名 `PdfFileSignature.verify_signature()`. 下面的示例会在任何验证失败的签名时抛出异常：

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

## 检测受损的签名

`SignaturesCompromiseDetector` 检查文档中的任何数字签名是否因后续更改而失效。 在法律、金融或合规工作流中使用此功能，以确保文档完整性得到保证。

下面的示例检查受损的签名，并报告它们的名称以及文档的整体签名覆盖率：

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def check(infile: str) -> None:
    """Check whether a PDF contains compromised signatures."""
    with ap.Document(infile) as document:
        detector = ap.SignaturesCompromiseDetector(document)
        result = []

        if detector.check(result):
            print("No signature compromise detected")
            return

        if result[0].has_compromised_signatures:
            print(
                f"Count of compromised signatures: {len(result[0].COMPROMISED_SIGNATURES)}"
            )
            for signature_name in result[0].COMPROMISED_SIGNATURES:
                print(f"Signature name: {signature_name.FULL_NAME}")

        print(result[0].signatures_coverage)
```

## 相关安全主题

- [在 Python 中对 PDF 文件进行安全保护和签名](/pdf/zh/python-net/securing-and-signing/)
- [在 Python 中对 PDF 文件进行数字签名](/pdf/zh/python-net/digitally-sign-pdf-file/)
- [在 Python 中使用智能卡签署 PDF 文档](/pdf/zh/python-net/sign-pdf-document-from-smart-card/)
- [在 Python 中加密和解密 PDF 文件](/pdf/zh/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)
