---
title: Go を使用してパスワード保護された PDF を開く
linktitle: パスワード保護された PDF を開く
type: docs
weight: 70
url: /ja/go-cpp/open-password-protected-pdf/
description: C++ を介して Aspose.PDF for Go でパスワード保護された PDF ファイルを開く。
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## パスワード保護された PDF ドキュメントを開く

このコードスニペットは、C++ を介して Aspose.PDF for Go を使用してパスワード保護された PDF ドキュメントを開く方法を説明します。ドキュメントはオーナーパスワードで開かれ、完全なアクセス権が提供され、メタデータの読み取り、権限の確認、ファイルの復号、またはコンテンツの変更といったさらなる操作が可能になります。

1. 保護された PDF ドキュメントを開く。
1. ファイル名と所有者パスワードを指定して [OpenWithPassword](https://reference.aspose.com/pdf/go-cpp/security/openwithpassword/) を呼び出し、暗号化された PDF にアクセスしてください。
1. 処理が完了したら、'defer pdf.Close()' を使用して、割り当てられたすべてのリソースを解放します。
1. ドキュメントを開いた後、PDF の復号化、権限の変更、情報の抽出などの追加タスクを実行できます。

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
