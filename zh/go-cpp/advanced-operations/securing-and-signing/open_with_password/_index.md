---
title: 使用 Go 打开受密码保护的 PDF
linktitle: 打开受密码保护的 PDF
type: docs
weight: 70
url: /zh/go-cpp/open-password-protected-pdf/
description: 使用 Aspose.PDF for Go 通过 C++ 打开受密码保护的 PDF 文件。
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 打开受密码保护的 PDF 文档

此代码片段说明了如何使用 Aspose.PDF for Go 通过 C++ 打开受密码保护的 PDF 文档。该文档使用所有者密码打开，所有者密码提供完整访问权限，并允许进一步操作，例如读取元数据、检查权限、解密文件或修改内容。

1. 打开受保护的 PDF 文档。
1. 调用 [OpenWithPassword](https://reference.aspose.com/pdf/go-cpp/security/openwithpassword/) 并提供文件名以及所有者密码以解锁文档。
1. 使用 'defer pdf.Close()' 在处理完成后释放所有已分配的资源。
1. 打开文档后，您可以继续执行其他任务，例如解密 PDF、更改权限或提取信息。

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
        // working...
    }
```