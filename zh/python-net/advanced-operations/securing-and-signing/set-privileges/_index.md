---
title: 在 Python 中加密和解密 PDF 文件
linktitle: 加密和解密 PDF 文件
type: docs
weight: 70
url: /zh/python-net/set-privileges-encrypt-and-decrypt-pdf-file/
description: 了解如何在 Python 中设置 PDF 权限、加密文件、解密受保护的 PDF，以及更改密码。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中设置 PDF 权限并管理加密。
Abstract: 本文档页说明了如何使用 Aspose.PDF for Python 设置文档权限、应用加密以及解密 PDF 文件。它指导开发人员配置用户密码和所有者密码，定义访问限制（例如打印、复制或编辑）。代码示例展示了如何在 Python 应用程序中有效保护敏感内容并管理 PDF 安全，确保受控访问和数据机密性。
---

管理文档安全在处理敏感或业务关键内容时至关重要。Aspose.PDF for Python via .NET 提供了一个强大的 API，用于以编程方式应用加密、通过权限控制访问以及解密受保护的 PDF 文件。

本文向 Python 开发者展示如何在 PDF 工作流中通过实际示例设置权限、应用和移除加密、更改密码以及检测保护状态。

Aspose.PDF for Python via .NET 为开发者提供了对 PDF 安全性的完全控制：

**设置特权** - 使用权限进行细粒度访问控制。
**Encrypt File** - 使用自定义密码应用 AES 或 RC4 加密。
**解密文件** - 使用所有者密码移除安全保护。
**更改密码** - 在不更改内容的情况下轮换或更新凭据。
**检查安全性** - 检测加密状态或所需的密码类型。

当您需要使用密码保护 PDF 文档、限制打印或复制、旋转凭据，或检查文档是否已加密时，请使用此页面。

## 为现有 PDF 文件设置权限

您可以通过分配用户密码和所有者密码以及访问权限，限制或允许特定操作（例如，打印、复制、填写表单）。

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def set_privileges_on_existing_pdf_file(infile: str, outfile: str) -> None:
    """Set restricted privileges on an existing PDF document."""
    with ap.Document(infile) as document:
        document_privilege = ap.facades.DocumentPrivilege.forbid_all
        document_privilege.allow_screen_readers = True
        document.encrypt(
            "user",
            "owner",
            document_privilege,
            ap.CryptoAlgorithm.AESx128,
            False,
        )
        document.save(outfile)
```

## 使用不同的加密类型和算法加密 PDF 文件

对 PDF 加密可确保只有具有有效凭据的用户才能打开或修改文件。

>关键术语：

- 用户密码。打开文档时需要。

- 所有者密码。更改权限或移除加密时需要。

- 密钥大小。 在现代工作流中使用 AE_SX128 以获得最大安全性。

下面的代码片段向您展示如何加密 PDF 文件。

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def encrypt_pdf_file(infile: str, outfile: str) -> None:
    """Encrypt a PDF document with user and owner passwords."""
    with ap.Document(infile) as document:
        document.encrypt(
            "user",
            "owner",
            ap.Permissions.EXTRACT_CONTENT,
            ap.CryptoAlgorithm.AESx128,
        )
        document.save(outfile)
```

## 使用所有者密码解密 PDF 文件

要移除密码保护并恢复完全访问权限：

1. 使用正确的密码加载加密的 PDF（'password' 是用户密码或所有者密码）。
1. 删除文档中的所有密码保护和加密设置。
1. 将现在未受保护的 PDF 保存到指定的输出文件。

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def decrypt_pdf_file(infile: str, outfile: str) -> None:
    """Decrypt a password-protected PDF document."""
    with ap.Document(infile, "password") as document:
        document.decrypt()
        document.save(outfile)
```

## 使用公钥证书对 PDF 进行加密和解密

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def pub_sec_encryption(
    crypto_algorithm,
    pub_cert: str,
    in_pfx: str,
    outfile: str,
) -> None:
    """Demonstrate public-key encryption and decryption."""
    pfx_password = "12345"

    with ap.Document() as document:
        document.info.title = "TestTitle"
        document.info.author = "TestAuthor"
        page = document.pages.add()
        page.paragraphs.add(ap.text.TextFragment("Hello World!"))

        with open(pub_cert, "rb") as file_stream:
            byte_content = file_stream.read()

        document.encrypt(
            ap.Permissions.PRINT_DOCUMENT,
            crypto_algorithm,
            [byte_content],
        )
        document.save(outfile)

    with ap.Document(
        outfile,
        ap.security.CertificateEncryptionOptions(pub_cert, in_pfx, pfx_password),
    ) as document:
        print(document.info.title)
        print(document.info.author)

        text_absorber = ap.text.TextAbsorber()
        document.pages[1].accept(text_absorber)
        print(text_absorber.text)

        document.decrypt()
        document.save(path.join(path.dirname(outfile), "pubsec_decrypted_out.pdf"))
```

## 更改 PDF 文件的密码

更新 PDF 文档的安全凭证（用户密码和所有者密码），同时保持其内容和结构不变。

1. 使用现有的所有者密码（'owner'）打开 PDF，这提供了完全访问权限，包括更改安全设置的权限。
1. 用新的用户密码（'newuser'）和新的所有者密码（'newowner'）替换旧密码。
1. 使用更新的密码设置保存 PDF。

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def change_password(infile: str, outfile: str) -> None:
    """Change the passwords of a password-protected PDF document."""
    with ap.Document(infile, "owner") as document:
        document.change_passwords("owner", "newuser", "newowner")
        document.save(outfile)
```

## 如何 - 确定源 PDF 是否受密码保护

### 从数组中确定正确的密码

在某些场景中，您可能需要从潜在候选密码列表中识别正确的密码，以访问受保护的 PDF。下面的代码片段演示了如何检查 PDF 文件是否受密码保护，然后使用 Aspose.PDF for Python via .NET 通过遍历预定义的密码列表尝试解锁它。

该过程包括：

1. 使用 PdfFileInfo 检测 PDF 是否被加密。
1. 尝试使用 ap.Document() 用每个密码打开 PDF。
1. 如果成功，它会打印页数。
1. 如果不是，它会捕获异常并报告密码错误。

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def determine_correct_password_from_array(infile: str) -> None:
    """Try a list of passwords until the document opens successfully."""
    with ap.facades.PdfFileInfo() as pdf_file_info:
        pdf_file_info.bind_pdf(infile)
        print(f"File is password protected {pdf_file_info.is_encrypted}")

    passwords = ["test", "test1", "test2", "test3", "sample"]

    for password in passwords:
        try:
            with ap.Document(infile, password) as document:
                if len(document.pages) > 0:
                    print(f"Password = {password} is correct")
                    print(f"Number of pages in document = {len(document.pages)}")
                    break
        except Exception:
            print(f"Password = {password} is not correct")
```

## 相关安全主题

- [在 Python 中对 PDF 文件进行安全保护和签名](/pdf/zh/python-net/securing-and-signing/)
- [在 Python 中对 PDF 文件进行数字签名](/pdf/zh/python-net/digitally-sign-pdf-file/)
- [在 Python 中提取 PDF 的签名信息](/pdf/zh/python-net/extract-image-and-signature-information/)
- [在 Python 中使用智能卡签署 PDF 文档](/pdf/zh/python-net/sign-pdf-document-from-smart-card/)

