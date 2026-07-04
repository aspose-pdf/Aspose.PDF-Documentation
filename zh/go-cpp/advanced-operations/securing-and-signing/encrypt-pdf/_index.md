---
title:  使用 Go 加密 PDF
linktitle: 加密 PDF 文件
type: docs
weight: 10
url: /zh/go-cpp/encrypt-pdf/
description: 使用 Aspose.PDF for Go via C++ 加密 PDF 文件。
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 使用用户或所有者密码加密 PDF 文件

要轻松且安全地加密文档，您可以使用 Aspose.PDF for Go via C++。

- **userPassword**，如果已设置，是打开 PDF 所需提供的密码。Acrobat/Reader 将提示用户输入用户密码。如果密码不正确，文档将无法打开。
- 如果设置了 **ownerPassword**，它会控制权限，例如打印、编辑、提取、评论等。Acrobat/Reader 将根据权限设置阻止这些操作。如果您想设置/更改权限，Acrobat 将要求此密码。

该 PDF 受用户密码和所有者密码保护，配置了特定的访问权限，并使用 AES-128 算法以及 PDF 2.0–兼容的安全性进行加密。加密后的文档随后被保存到磁盘。

1. 创建一个新的 PDF 文档。
1. 使用以下方式加密 PDF 文档 [encrypt](https://reference.aspose.com/pdf/go-cpp/security/encrypt/) 方法。
1. 指定用户密码以限制打开文档。
1. 指定所有者密码以控制权限。
1. 使用权限位标志定义允许的操作。
1. 选择 AES-128 作为加密算法。
1. 启用 PDF 2.0 加密以符合现代安全合规性。
1. 使用 以下方式保存已加密的文档。 [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/), 将其写入新文件。

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
        // New creates a new PDF-document
        pdf, err := asposepdf.New()
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
        // Encrypt(userPassword, ownerPassword, permissions, cryptoAlgorithm, usePdf20) encrypts PDF-document
        err = pdf.Encrypt(
            "userpass",
            "ownerpass",
            asposepdf.PrintDocument|asposepdf.ModifyContent|asposepdf.FillForm,
            asposepdf.AESx128,
            true,
        )
        if err != nil {
            log.Fatal(err)
        }
        // SaveAs(filename string) saves previously opened PDF-document with new filename
        err = pdf.SaveAs("sample_with_password.pdf")
        if err != nil {
            log.Fatal(err)
        }
    }
```