---
title: 在 Python 中保护 PDF 文件
linktitle: 加密和解密 PDF 文件
type: docs
weight: 70
url: /zh/python-net/protect-pdf-file/
description: 了解如何在 Python 中加密文件、解密受保护的 PDF 并更改密码。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中设置 PDF 权限并管理加密。
Abstract: 本页介绍了如何使用 Aspose.PDF for Python via .NET 设置文档权限、应用加密、解密 PDF 文件以及更改密码。它涵盖了配置用户密码和所有者密码、定义访问限制（例如打印、复制和编辑），以及在 Python 应用程序中管理 PDF 安全。
---

## 使用密码和权限加密 PDF

使用 Aspose.PDF for Python via .NET 对 PDF 文档进行基于密码的加密并限制权限。

1. 加载 PDF 文档。
1. 创建一个 `DocumentPrivilege` 权限对象。
1. 启用所需的权限。
1. 设置用户密码和所有者密码。
1. 选择加密算法。
1. 对文档应用加密。
1. 保存加密后的 PDF。

```python
import aspose.pdf as ap

def encrypt_password(infile, outfile):
    """
    Encrypt PDF with password and permissions.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        encrypt_password("sample.pdf", "sample_protected.pdf")

    Note:
        Uses AES 128-bit encryption. Allows screen readers, forbids all other operations.
        User password: "userpassword", Owner password: "ownerpassword".
    """
    document = ap.Document(infile)
    document_privilege = ap.facades.DocumentPrivilege.forbid_all
    document_privilege.allow_screen_readers = True

    document.encrypt(
        "userpassword",
        "ownerpassword",
        document_privilege,
        ap.CryptoAlgorithm.AESx128,
        False,
    )
    document.save(outfile)
```

## 使用完整权限加密 PDF

使用 Aspose.PDF for Python via .NET 对 PDF 文档进行加密，同时允许完整的访问权限。此示例使用 RC4 128 位加密，以兼容较旧的 PDF 查看器。

1. 加载 PDF 文档。
1. 定义用户密码和所有者密码。
1. 设置完整访问权限。
1. 选择加密算法。
1. 调用 `encrypt()` 带有密码、权限和算法。
1. 保存加密后的 PDF。

```python
import aspose.pdf as ap

def encrypt_pdf_file(infile, outfile):
    """
    Encrypt PDF with full permissions.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        encrypt_pdf_file("sample.pdf", "sample_protected.pdf")

    Note:
        Uses RC4 128-bit encryption with allow_all privileges.
    """
    document = ap.Document(infile)
    document.encrypt(
        "userpassword",
        "ownerpassword",
        ap.facades.DocumentPrivilege.allow_all,
        ap.CryptoAlgorithm.RC4x128,
        False,
    )
    document.save(outfile)
```

## 使用所有者密码解密 PDF 文件

要移除密码保护并恢复完全访问权限：

1. 使用正确的密码（用户或拥有者）加载加密的 PDF。
1. 从文档中移除所有密码保护和加密设置。
1. 将现在未受保护的 PDF 保存到指定的输出文件。

```python
import aspose.pdf as ap

def decrypt_pdf_file(infile, outfile):
    """
    Decrypt password-protected PDF.

    Args:
        infile (str): Input encrypted PDF filename
        outfile (str): Output decrypted PDF filename

    Returns:
        None

    Example:
        decrypt_pdf_file("sample_protected.pdf", "sample_unprotected.pdf")

    Note:
        Requires user password to open document.
    """
    document = ap.Document(infile, "userpassword")
    document.decrypt()
    document.save(outfile)
```

## 更改 PDF 文件的密码

在保留 PDF 文档内容和结构的同时，更新其安全凭证（用户密码和所有者密码）。

1. 使用现有的拥有者密码打开 PDF，该密码提供对安全设置的完全访问权限。
1. 将旧密码替换为新的用户密码和新的拥有者密码。
1. 使用更新的密码设置保存 PDF。

```python
import aspose.pdf as ap

def change_password(infile, outfile):
    """
    Change user and owner passwords.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        change_password("sample_protected.pdf", "sample_changepassword.pdf")

    Note:
        Changes from ownerpassword to newuser/newowner.
    """
    document = ap.Document(infile, "ownerpassword")
    document.change_passwords("ownerpassword", "newuser", "newowner")
    document.save(outfile)

```

## 从数组中确定正确的密码

在某些情况下，您可能需要从可能的候选密码列表中识别出正确的密码以访问受保护的 PDF。下面的代码片段检查 PDF 文件是否已加密，然后通过遍历预定义的密码列表尝试打开它。

该过程包括：

1. 使用 `PdfFileInfo` 检测 PDF 是否被加密。
1. 使用每个密码打开 PDF `ap.Document()`.
1. 如果成功，它会打印页数。
1. 如果不是，它会捕获异常并报告密码错误。

```python
import aspose.pdf as ap

def determine_correct_password_from_list(infile):
    """
    Test multiple passwords to find correct one.

    Args:
        infile (str): Input encrypted PDF filename

    Returns:
        None

    Example:
        determine_correct_password_from_list("sample_protected.pdf")

    Note:
        Tries passwords: test, test1, test2, test3, userpassword.
        Prints page count if password is correct.
    """
    info = ap.facades.PdfFileInfo(infile)
    print(f"File is password protected {info.is_encrypted}")

    passwords = "test", "test1", "test2", "test3", "userpassword"

    for password in passwords:
        try:
            document = ap.Document(infile, password)
            count = len(document.pages)
            if count > 0:
                print(f"Number of Page in document are = {count}")
        except RuntimeError as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
```
