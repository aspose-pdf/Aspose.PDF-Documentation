---
title: 使用 Go 设置 PDF 文档的权限
linktitle: 设置权限
type: docs
weight: 80
url: /zh/go-cpp/set_permissions/
description: 通过 C++ 使用 Aspose.PDF for Go 为 PDF 文档设置权限。
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 为 PDF 文档设置访问权限

创建一个新的 PDF 文档，并使用用户密码和所有者密码进行保护，同时明确允许特定权限——如打印、修改内容和填写表单。随后将文档保存，并应用这些权限限制。

1. 创建一个新的 PDF 文档。
1. 调用 [SetPermissions](https://reference.aspose.com/pdf/go-cpp/security/setpermissions/) 以保护文档。
1. 指定用户密码以限制访问。
1. 指定所有者密码以控制安全设置。
1. 使用权限位标志定义允许的操作。
1. 使用保存已应用权限的 PDF [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/).

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

        // SetPermissions(userPassword, ownerPassword, permissions) sets permissions for PDF-document
        err = pdf.SetPermissions(
            "userpass",
            "ownerpass",
            asposepdf.PrintDocument|
                asposepdf.ModifyContent|
                asposepdf.FillForm,
        )
        if err != nil {
            log.Fatal(err)
        }
        // SaveAs(filename string) saves previously opened PDF-document with new filename
        err = pdf.SaveAs("sample_with_permissions.pdf")
        if err != nil {
            log.Fatal(err)
        }
    }
```