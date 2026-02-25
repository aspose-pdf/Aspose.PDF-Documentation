---
title: 设置权限、加密和解密 PDF
linktitle: 加密和解密 PDF 文件
type: docs
weight: 70
url: /zh/python-net/set-privileges-encrypt-and-decrypt-pdf-file/
description: 使用 Python 通过不同的加密类型和算法加密 PDF 文件。同时，使用所有者密码解密 PDF 文件。
lastmod: "2025-06-22"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 加密或解密 PDF 文件
Abstract: 本文档页面解释了如何使用 Aspose.PDF for Python 设置文档权限、应用加密以及解密 PDF 文件。它指导开发者配置用户和所有者密码，定义访问限制（如打印、复制或编辑）。代码示例展示了如何在 Python 应用中有效保护敏感内容并管理 PDF 安全，确保受控访问和数据机密性。
---

在处理敏感或业务关键内容时，管理文档安全至关重要。Aspose.PDF for Python via .NET 提供了强大的 API，用于以编程方式应用加密、通过权限控制访问，并解密受保护的 PDF 文件。

本文为 Python 开发者提供了实际示例，演示在 PDF 工作流中设置权限、应用和移除加密、更改密码以及检测保护状态的全过程。

Aspose.PDF for Python via .NET 为开发者提供了对 PDF 安全的完整控制：

**设置权限** - 使用权限进行细粒度的访问控制。
**加密文件** - 使用自定义密码应用 AES 或 RC4 加密。
**解密文件** - 使用所有者密码移除安全保护。
**更改密码** - 在不更改内容的情况下轮换或更新凭证。
**检查安全** - 检测加密状态或所需的密码类型。

## 在现有 PDF 文件上设置权限

您可以通过分配用户和所有者密码以及访问权限来限制或允许特定操作（例如打印、复制、填写表单）。

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Instantiate Document Privileges object
        # Apply restrictions on all privileges
        document_privilege = ap.facades.DocumentPrivilege.forbid_all
        # Only allow screen reading
        document_privilege.allow_screen_readers = True
        # Encrypt the file with User and Owner password
        # Need to set the password, so that once the user views the file with user password
        # Only screen reading option is enabled
        document.encrypt("user", "owner", document_privilege, ap.CryptoAlgorithm.AE_SX128, False)
        # Save PDF document
        document.save(path_outfile)
```

## 使用不同的加密类型和算法加密 PDF 文件

加密 PDF 可确保只有拥有有效凭证的用户才能打开或修改该文件。

>关键术语：

- 用户密码。打开文档所需。

- 所有者密码。更改权限或移除加密所需。

- 密钥大小。使用 AE_SX128 在现代工作流中实现最高安全性。

以下代码片段展示了如何加密 PDF 文件。

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Encrypt PDF
        document.encrypt("user", "owner", ap.Permissions.EXTRACT_CONTENT, ap.CryptoAlgorithm.AE_SX128)
        # Save PDF document
        document.save(path_outfile)
```

## 使用所有者密码解密 PDF 文件

移除密码保护并恢复完整访问：

1. 使用正确的密码加载加密的 PDF（'password' 为用户或所有者密码）。
1. 移除文档中的所有密码保护和加密设置。
1. 将现在已解除保护的 PDF 保存到指定的输出文件。

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document with password
    with ap.Document(path_infile, "password") as document:
        # Decrypt PDF
        document.decrypt()
        # Save PDF document
        document.save(path_outfile)
```

## 更改 PDF 文件的密码

在保持内容和结构不变的情况下，更新 PDF 文档的安全凭证（用户和所有者密码）。

1. 使用现有的所有者密码（'owner'）打开 PDF，该密码提供完全访问权限，包括更改安全设置的权限。
1. 将旧密码替换为新的用户密码（'newuser'）和新的所有者密码（'newowner'）。
1. 使用更新后的密码设置保存 PDF。

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document with password
    with ap.Document(path_infile, "owner") as document:
        # Change password
        document.change_passwords("owner", "newuser", "newowner")
        # Save PDF document
        document.save(path_outfile)
```

## 如何 - 确定源 PDF 是否受密码保护

### 从数组中确定正确的密码

在某些情况下，您可能需要从潜在候选密码列表中识别正确的密码以访问受保护的 PDF。下面的代码片段演示了如何使用 Aspose.PDF for Python via .NET 检查 PDF 文件是否受密码保护，然后通过遍历预定义密码列表尝试解锁。

该过程包括：

1. 使用 PdfFileInfo 检测 PDF 是否被加密。
1. 使用 ap.Document() 尝试使用每个密码打开 PDF。
1. 如果成功，打印页数。
1. 如果不成功，捕获异常并报告失败的密码。

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    with ap.facades.PdfFileInfo() as pdf_file_info:
        # Bind PDF document
        pdf_file_info.bind_pdf(path_infile)
        # Determine if the source PDF is encrypted
        print("File is password protected " + str(pdf_file_info.is_encrypted))

        passwords = ["test", "test1", "test2", "test3", "sample"]

        for password_index in range(len(passwords)):
            try:
                with ap.Document(path_infile, passwords[password_index]) as document:
                    if len(document.pages) > 0:
                        print("Number of Pages in document are = " + str(len(document.pages)))
                    password_index = password_index + 1
            except Exception as e:
                print("Password = " + passwords[password_index] + " is not correct")
                password_index = password_index + 1
```


