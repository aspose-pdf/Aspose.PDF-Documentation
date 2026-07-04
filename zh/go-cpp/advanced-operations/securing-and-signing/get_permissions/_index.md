---
title: 使用 Go 获取权限
linktitle: 获取权限
type: docs
weight: 60
url: /zh/go-cpp/get-permissions/
description: 使用 Aspose.PDF for Go via C++ 读取并显示受密码保护的 PDF 文档的访问权限。
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 获取受密码保护的 PDF 文档的权限

此示例演示了如何在 Go 中使用 Aspose.PDF for Go via C++ 检索、解释并显示受密码保护的 PDF 文档的访问权限。
使用所有者密码打开 PDF，读取其权限标志，并将每个启用的权限转换为人类可读的描述，然后打印到控制台。

1. 定义权限名称映射。
1. 将权限标志转换为可读文本。
1. 使用 [OpenWithPassword](https://reference.aspose.com/pdf/go-cpp/security/openwithpassword/) 使用所有者密码获取文档的安全信息。
1. 确保正确的资源清理。
1. 调用 [GetPermissions](https://reference.aspose.com/pdf/go-cpp/security/getpermissions/) 获取分配给 PDF 的当前权限位标志。
1. 显示权限。

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import (
        "fmt"
        "log"
        "strings"
    )

    var permissionNames = map[asposepdf.Permissions]string{
        asposepdf.PrintDocument:                  "Allow printing",
        asposepdf.ModifyContent:                  "Allow modifying content (except forms/annotations)",
        asposepdf.ExtractContent:                 "Allow copying/extracting text and graphics",
        asposepdf.ModifyTextAnnotations:          "Allow adding/modifying text annotations",
        asposepdf.FillForm:                       "Allow filling interactive forms",
        asposepdf.ExtractContentWithDisabilities: "Allow content extraction for accessibility",
        asposepdf.AssembleDocument:               "Allow inserting/rotating/deleting pages or changing structure",
        asposepdf.PrintingQuality:                "Allow high-quality / faithful printing",
    }

    func PermissionsToString(p asposepdf.Permissions) string {
        var result []string
        for flag, name := range permissionNames {
            if p&flag != 0 {
                result = append(result, name)
            }
        }
        if len(result) == 0 {
            return "None"
        }
        return strings.Join(result, ", ")
    }

    func main() {
        // OpenWithPassword(filename string, password string) opens a password-protected PDF-document
        pdf, err := asposepdf.OpenWithPassword("sample_with_permissions.pdf", "ownerpass")
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
        // GetPermissions() gets current permissions of PDF-document
        permissions, err := pdf.GetPermissions()
        if err != nil {
            log.Fatal(err)
        }
        // Print permissions
        fmt.Println("Permissions:", PermissionsToString(permissions))
    }
```