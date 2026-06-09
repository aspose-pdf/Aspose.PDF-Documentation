---
title: 更改 PDF 文件的密码
type: docs
weight: 10
url: /zh/python-net/change-password/
description: 使用 Aspose.PDF for Python via .NET 更改受保护 PDF 文档的用户密码和所有者密码。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 更新 PDF 密码
Abstract: 了解如何使用 Aspose.PDF for Python via .NET 更改受保护 PDF 文件的用户密码和所有者密码。本示例演示了在保持现有加密和权限不变的情况下，安全地更新访问凭证的方法。
---

## 更改用户和所有者密码

在许多情况下，您可能需要在不更改现有安全设置的前提下更新受保护 PDF 的密码。这在轮换凭证、转移所有权或增强文档安全性时非常有用。

'change_password' 方法属于 [PdfFileSecurity](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/) class 让您：

- 更新用户密码（打开文档所需）
- 更新所有者密码（用于控制权限）
- 保留当前的加密和权限设置

1. 创建一个 'PdfFileSecurity' 对象。
1. 绑定输入 PDF。
1. 使用 'change_password()' 方法更改密码。
1. 保存更新后的 PDF。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Change User and Owner Password
def change_user_and_owner_password(infile, outfile):
    """Change user and owner passwords while keeping existing security settings."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Change passwords
    file_security.change_password(
        "owner_password", "new_user_password", "new_owner_password"
    )

    # Save updated PDF
    file_security.save(outfile)
```

## 更改密码并重置安全设置

在处理受保护的 PDF 文档时，单纯更改密码可能不足。您可能还需要调整权限，例如打印、复制或编辑权利。

了解如何在使用 Aspose.PDF for Python via .NET 重置 PDF 安全设置的同时更新用户密码和所有者密码。本示例展示了如何重新定义文档权限和加密强度以及新的访问凭证。

1. 创建一个 'PdfFileSecurity' 对象。
1. 绑定输入 PDF。
1. 创建一个‘DocumentPrivilege’对象并配置允许的操作。
1. 更改密码并重置安全设置。
1. 保存更新后的 PDF。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Change Password and Reset Security
def change_password_and_reset_security(infile, outfile):
    """Change passwords and reset document security settings."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define new privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Change passwords and reset security
    file_security.change_password(
        "owner_password",
        "new_user_password",
        "new_owner_password",
        privilege,
        pdf_facades.KeySize.X128,
    )

    # Save updated PDF
    file_security.save(outfile)
```

## 尝试更改密码而不抛出异常

在某些工作流中，特别是批处理或自动化系统中，避免可能中断执行的异常非常重要。与其抛出错误，您可能更倾向于使用一种报告成功或失败的安全操作。

的 \u0027try_change_password\u0027 方法 [PdfFileSecurity](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/) 类通过以下方式提供此功能：

1. 创建一个 'PdfFileSecurity' 对象。
1. 使用 \u0027bind_pdf()\u0027 方法加载 PDF 文档。
1. 尝试更改密码。
1. 检查结果。
1. 保存更新后的 PDF。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Try Change Password Without Exception
def try_change_password_without_exception(infile, outfile):
    """Attempt to change passwords without throwing an exception on failure."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Attempt to change passwords
    result = file_security.try_change_password(
        "owner_password", "new_user_password", "new_owner_password"
    )

    # Save only if operation succeeded
    if result:
        file_security.save(outfile)
    else:
        print("Password change failed. Check owner password or document security.")
```
