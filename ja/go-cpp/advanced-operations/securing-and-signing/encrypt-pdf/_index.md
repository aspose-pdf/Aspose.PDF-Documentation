---
title:  Go を使用して PDF を暗号化する
linktitle: PDF ファイルを暗号化
type: docs
weight: 10
url: /ja/go-cpp/encrypt-pdf/
description: C++ を介して Aspose.PDF for Go で PDF ファイルを暗号化する。
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## ユーザーまたは所有者パスワードを使用して PDF ファイルを暗号化

ドキュメントを簡単かつ安全に暗号化するには、C++ を介して Aspose.PDF for Go を使用できます。

- **userPassword** が設定されている場合、PDF を開くために必要です。Acrobat/Reader はユーザーにユーザーパスワードの入力を求めます。正しくない場合、ドキュメントは開きません。
- **ownerPassword** が設定されている場合、印刷、編集、抽出、コメントなどの権限を制御します。Acrobat/Reader は権限設定に基づきこれらの操作を許可しません。権限を設定/変更したい場合、Acrobat はこのパスワードを要求します。

PDF はユーザー パスワードとオーナーパスワードで保護され、特定のアクセス権限が設定され、AES-128 アルゴリズムと PDF 2.0 互換のセキュリティで暗号化されています。暗号化されたドキュメントはその後ディスクに保存されます。

1. 新しい PDF ドキュメントを作成します。
1. PDF ドキュメントを暗号化します [encrypt](https://reference.aspose.com/pdf/go-cpp/security/encrypt/) 方法。
1. ドキュメントの開封を制限するためにユーザーパスワードを指定します。
1. 権限を管理するためにオーナーパスワードを指定します。
1. 許可されたアクションをパーミッションビットフラグで定義します。
1. 暗号化アルゴリズムとして AES-128 を選択します。
1. 最新のセキュリティ要件に対応するため、PDF 2.0 暗号化を有効にします。
1. 使用して保護されたドキュメントを保存します。 [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/)、新しいファイルに書き込んでいます。

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