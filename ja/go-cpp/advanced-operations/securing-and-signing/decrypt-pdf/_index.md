---
title: Go を使用して PDF を復号化する
linktitle: PDF ファイルを復号化する
type: docs
weight: 40
url: /ja/go-cpp/decrypt-pdf/
description: C++ を介した Aspose.PDF for Go で PDF ファイルを復号化する。
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## オーナーパスワードを使用して PDF ファイルを復号化する

C++ を介した Aspose.PDF for Go を使用して、パスワードで保護された PDF ドキュメントを開き、復号化し、保存できます。PDF ファイルはオーナーパスワードで開かれ、すべてのセキュリティ制限を解除するように復号化され、そして新しい無保護のドキュメントとして保存されます。

1. 呼び出す [OpenWithPassword](https://reference.aspose.com/pdf/go-cpp/security/openwithpassword/) 暗号化された PDF にアクセスするために、ファイル名と所有者パスワードを指定してください。
1. 呼び出す [Decrypt](https://reference.aspose.com/pdf/go-cpp/security/decrypt/) このメソッドは、文書からパスワード保護とすべての関連するセキュリティ制限を削除します。
1. 復号化された PDF を次の方法で保存します: [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/).

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