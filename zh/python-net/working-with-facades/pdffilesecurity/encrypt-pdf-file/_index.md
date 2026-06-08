---
title: 加密 PDF 文件
type: docs
weight: 30
url: /zh/python-net/encrypt-pdf-file/
description: 加密 PDF 文档并配置权限，以控制用户对文件的操作。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 加密 PDF 并控制用户操作
Abstract: 了解如何使用 Aspose.PDF for Python via .NET 加密 PDF 并定义特定的用户权限。本指南展示了如何在保持文档安全的同时，允许或限制诸如打印和复制等操作。
---

## 使用用户密码和所有者密码加密 PDF

在共享敏感或受限制内容时，确保 PDF 文档的安全至关重要。加密允许您使用密码保护文档，并定义用户可以执行的操作。此代码片段展示了如何应用用户密码和所有者密码以及访问权限来保护 PDF 文件。

1. 创建一个 PdfFileSecurity 对象。
1. 绑定输入 PDF。
1. 定义文档权限。
1. 加密 PDF。
1. 保存已加密的 PDF。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Encrypt PDF with User and Owner Password
def encrypt_pdf_with_user_owner_password(infile, outfile):
    """Encrypt a PDF document using user and owner passwords."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define document privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Encrypt the PDF
    file_security.encrypt_file(
        "user_password", "owner_password", privilege, pdf_facades.KeySize.X128
    )

    # Save encrypted PDF
    file_security.save(outfile)
```

## 使用权限加密 PDF

下面的代码片段解释如何在允许打印和复制等选定操作的同时限制其他操作。

1. 初始化 [PdfFileSecurity](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/) 类。
1. 绑定输入 PDF。
1. 配置文档权限。
1. 调用 'encrypt_file()' 方法。
1. 保存已加密的 PDF。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Encrypt PDF with Permissions
def encrypt_pdf_with_permissions(infile, outfile):
    """Encrypt a PDF document and configure specific permissions."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Configure privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True
    privilege.allow_copy = True

    # Encrypt the PDF
    file_security.encrypt_file(
        "user_password", "owner_password", privilege, pdf_facades.KeySize.X128
    )

    # Save encrypted PDF
    file_security.save(outfile)
```

## 使用加密算法加密 PDF

PDF 加密不仅通过密码保护文档，还允许您选择加密算法和强度。选择适当的算法可为敏感文档提供更强的安全性。

1. 创建一个 PdfFileSecurity 对象。
1. 绑定输入 PDF。
1. 定义文档权限。
1. 使用算法加密 PDF。
1. 保存已加密的 PDF。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Encrypt PDF with Encryption Algorithm
def encrypt_pdf_with_encryption_algorithm(infile, outfile):
    """Encrypt a PDF document using a specific encryption algorithm."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Encrypt the PDF using AES algorithm
    file_security.encrypt_file(
        "user_password",
        "owner_password",
        privilege,
        pdf_facades.KeySize.X256,
        pdf_facades.Algorithm.AES,
    )

    # Save encrypted PDF
    file_security.save(outfile)
```
