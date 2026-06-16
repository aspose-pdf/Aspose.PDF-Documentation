---
title: 为现有 PDF 文件设置权限
type: docs
weight: 40
url: /zh/python-net/set-privileges/
description: 设置和管理 PDF 文档权限，以控制用户的打印、复制和编辑等操作。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 管理 PDF 权限和访问控制
Abstract: 了解如何通过使用 Aspose.PDF for Python via .NET 设置文档权限来控制用户对 PDF 的操作。本指南涵盖了在有密码或无密码的情况下应用权限，以限制打印、复制或编辑等操作。
---

## 在无密码情况下设置 PDF 权限

了解如何在不指定用户或所有者密码的情况下，使用 Aspose.PDF for Python via .NET 为 PDF 应用文档权限。此代码片段演示了在保持文档可访问的同时，如何控制允许的操作。

1. 创建一个 'PdfFileSecurity' 对象。
1. 绑定输入 PDF。
1. 定义文档权限。
1. 调用 'set_privilege()' 方法而不传入密码。
1. 保存更新后的 PDF。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Set PDF Privileges Without Passwords
def set_pdf_privileges_without_passwords(infile, outfile):
    """Set PDF privileges without specifying user and owner passwords."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Apply privileges (owner password will be generated automatically)
    file_security.set_privilege(privilege)

    # Save updated PDF
    file_security.save(outfile)
```

## 使用用户和所有者密码设置 PDF 权限

为了完全保护 PDF 文档，通常需要同时具备访问控制（密码）和使用限制（权限）。通过将二者结合，您可以确保只有授权用户能够打开文档并执行特定操作。

使用带有密码参数的 set_privilege 方法，您可以：

- 使用用户密码保护文档
- 为完整控制定义所有者密码
- 配置允许的和受限的操作
- 强制执行文档级安全策略

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Set PDF Privileges with User and Owner Passwords
def set_pdf_privileges_with_passwords(infile, outfile):
    """Set PDF privileges using user and owner passwords."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True
    privilege.allow_copy = False

    # Apply privileges with passwords
    file_security.set_privilege("user_password", "owner_password", privilege)

    # Save updated PDF
    file_security.save(outfile)
```

## 尝试在不抛出异常的情况下设置 PDF 权限

此代码片段说明了如何控制访问并限制诸如复制的操作，同时允许诸如打印等其他操作。

1. 创建一个 'PdfFileSecurity' 对象。
1. 使用 \u0027bind_pdf()\u0027 方法加载源 PDF。
1. 定义文档权限。
1. 使用密码应用权限。
1. 保存更新后的 PDF。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Try Set PDF Privileges Without Exception
def try_set_pdf_privileges_without_exception(infile, outfile):
    """Attempt to set PDF privileges without throwing an exception on failure."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Attempt to apply privileges
    result = file_security.try_set_privilege(
        "user_password", "owner_password", privilege
    )

    # Save only if operation succeeded
    if result:
        file_security.save(outfile)
    else:
        print("Setting privileges failed. Check passwords or document state.")
```
