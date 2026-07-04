---
title: 使用 Go 解密 PDF
linktitle: 解密 PDF 文件
type: docs
weight: 40
url: /zh/go-cpp/decrypt-pdf/
description: 使用 Aspose.PDF for Go via C++ 解密 PDF 文件。
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 使用所有者密码解密 PDF 文件

您可以使用 Aspose.PDF for Go via C++ 打开、解密并保存受密码保护的 PDF 文档。PDF 文件使用所有者密码打开，解密以移除所有安全限制，然后保存为新的未受保护文档。

1. 调用 [OpenWithPassword](https://reference.aspose.com/pdf/go-cpp/security/openwithpassword/) 并提供文件名以及所有者密码以访问加密的 PDF。
1. 调用 [Decrypt](https://reference.aspose.com/pdf/go-cpp/security/decrypt/) 方法，以移除文档的密码保护和所有相关的安全限制。
1. 使用以下方式保存已解密的 PDF [保存为](https://reference.aspose.com/pdf/go-cpp/core/saveas/).

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
        // OpenWithPassword(filename string, password string) opens a password-protected PDF-document
        pdf, err := asposepdf.OpenWithPassword("sample_with_password.pdf", "ownerpass")
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
        // Decrypt() decrypts PDF-document
        err = pdf.Decrypt()
        if err != nil {
            log.Fatal(err)
        }
        // SaveAs(filename string) saves previously opened PDF-document with new filename
        err = pdf.SaveAs("sample_without_password.pdf")
        if err != nil {
            log.Fatal(err)
        }
    }
```