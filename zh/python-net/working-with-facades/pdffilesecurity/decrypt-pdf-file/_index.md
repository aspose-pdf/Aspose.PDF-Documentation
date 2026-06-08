---
title: 解密 PDF 文件
type: docs
weight: 20
url: /zh/python-net/decrypt-pdf-file/
description: 本指南说明如何移除诸如打印、复制和编辑等限制，以获得对 PDF 文档的完全访问权限。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 移除 PDF 的密码保护
Abstract: 本文演示如何使用所有者密码解密 PDF 文件。它涵盖了移除限制打印、编辑或复制内容等操作的安全限制的过程。通过应用正确的所有者密码，用户可以解锁文档并重新获得对其功能的全部控制。
---

## 使用所有者密码解密 PDF

使用 Aspose.PDF for Python via .NET 的所有者密码解密受密码保护的 PDF 文档。此操作会移除加密并允许对文档进行无限制访问。

1. 创建一个 'PdfFileSecurity' 对象。
1. 使用 'bind_pdf()' 方法加载加密的 PDF。
1. 解密文档。
1. 保存已解密的 PDF。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Decrypt PDF with Owner Password
def decrypt_pdf_with_owner_password(infile, outfile):
    """Decrypt a PDF document using the owner password."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Decrypt the PDF
    file_security.decrypt_file("owner_password")

    # Save decrypted PDF
    file_security.save(outfile)
```

## 尝试解密 PDF 而不抛出异常

PDF 文档通常受到密码保护以限制访问和使用。要完全访问或修改此类文档，您可能需要移除加密。使用 Aspose.PDF for Python via .NET，利用所有者密码解密受保护的 PDF 文档，以移除加密和访问限制。

1. 创建一个 'PdfFileSecurity' 对象。
1. 绑定输入 PDF。
1. 解密 PDF。
1. 保存输出 PDF。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Try Decrypt PDF Without Exception
def try_decrypt_pdf_without_exception(infile, outfile):
    """Attempt to decrypt a PDF without throwing an exception on failure."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Attempt to decrypt the PDF
    result = file_security.try_decrypt_file("owner_password")

    # Save only if decryption was successful
    if result:
        file_security.save(outfile)
    else:
        print("Decryption failed. Check password or document security.")
```
