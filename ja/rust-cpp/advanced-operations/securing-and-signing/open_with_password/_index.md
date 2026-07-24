---
title: Rust を使用してパスワード保護された PDF を開く
linktitle: パスワード保護された PDF を開く
type: docs
weight: 70
url: /ja/rust-cpp/open-password-protected-pdf/
description: C++ 経由で Aspose.PDF for Rust を使用してパスワード保護された PDF ファイルを開く。
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## パスワード保護された PDF ドキュメントを開く

C++ 経由で Aspose.PDF for Rust を使用してパスワード保護された PDF ドキュメントを開く。ドキュメントは所有者のパスワードで開かれ、フルアクセスが許可され、メタデータの読み取り、コンテンツの変更、権限の変更、暗号化の解除などの操作が可能です。

1. 保護された PDF ドキュメントを開く [open_with_password](https://reference.aspose.com/pdf/rust-cpp/security/open_with_password/) ファイルパスと所有者パスワードを提供して、ドキュメントのロックを解除します。
1. 開かれたドキュメントで作業します。

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a password-protected PDF-document
        let _pdf = Document::open_with_password("sample_with_password.pdf", "ownerpass")?;

        // working...

        Ok(())
    }
```