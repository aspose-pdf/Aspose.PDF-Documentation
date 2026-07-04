---
title: Go を使用して権限を取得する
linktitle: 権限を取得する
type: docs
weight: 60
url: /ja/go-cpp/get-permissions/
description: C++ 経由で Aspose.PDF for Go を使用して、パスワードで保護された PDF ドキュメントのアクセス権限を読み取り、表示します。
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## パスワードで保護された PDF ドキュメントの権限を取得する

この例では、C++ 経由で Aspose.PDF for Go を使用して、Go でパスワードで保護された PDF ドキュメントからアクセス権限を取得し、解釈し、表示する方法を示します。
PDF は所有者パスワードで開かれ、権限フラグが読み取られ、許可されている各権限は人間が読める説明に変換され、コンソールに出力されます。

1. 権限名のマッピングを定義します。
1. 権限フラグを可読テキストに変換します。
1. 使用する [OpenWithPassword](https://reference.aspose.com/pdf/go-cpp/security/openwithpassword/) 所有者パスワードを使用して、文書のセキュリティ情報へのアクセスを取得します。
1. 適切なリソースのクリーンアップを確保します。
1. 呼び出す [GetPermissions](https://reference.aspose.com/pdf/go-cpp/security/getpermissions/) PDFに割り当てられた現在の権限ビットフラグを取得するために。
1. 権限を表示する。

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