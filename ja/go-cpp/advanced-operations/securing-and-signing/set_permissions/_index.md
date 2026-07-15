---
title: Go を使用して PDF ドキュメントの権限を設定する
linktitle: 権限を設定する
type: docs
weight: 80
url: /ja/go-cpp/set_permissions/
description: C++ を介して Aspose.PDF for Go を使用して PDF ドキュメントの権限を設定する。
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF ドキュメントのアクセス権限を設定する

新しい PDF ドキュメントが作成され、ユーザー パスワードと所有者パスワードで保護されます。その際、印刷、コンテンツの変更、フォームへの入力など、特定の権限が明示的に許可されます。その後、これらの権限制限が適用された状態でドキュメントが保存されます。

1. 新しい PDF ドキュメントを作成する。
1. [SetPermissions](https://reference.aspose.com/pdf/go-cpp/security/setpermissions/)を呼び出してドキュメントを保護します。
1. アクセスを制限するためにユーザーパスワードを指定します。
1. セキュリティ設定を制御するためにオーナーパスワードを指定します。
1. 許可ビットフラグを使用して許可された操作を定義します。
1. 権限を適用したPDFを保存するには、[SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/)を使用します。

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