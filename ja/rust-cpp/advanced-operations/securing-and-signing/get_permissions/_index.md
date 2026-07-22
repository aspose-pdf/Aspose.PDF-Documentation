---
title: Rust を使用して権限を取得する
linktitle: 権限を取得する
type: docs
weight: 60
url: /ja/rust-cpp/get-permissions/
description: Aspose.PDF for Rust via C++ を使用して、パスワードで保護された PDF ドキュメントのアクセス権限を読み取り、表示します。
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## パスワードで保護された PDF ドキュメントの権限を取得する

このセクションでは、Rust でパスワードで保護された PDF ドキュメントのアクセス権限を読み取り、表示する方法を説明します。
PDF は所有者パスワードで開かれます。このパスワードはドキュメントのセキュリティ設定へのフルアクセスを許可します。その後、現在割り当てられている権限が取得され、コンソールに出力されます。

1. 保護された PDF ドキュメントを開く。
1. 呼び出す [get_permissions](https://reference.aspose.com/pdf/rust-cpp/security/get_permissions/) 許可された操作を定義する権限フラグを取得するために。
1. 取得した権限をコンソールに出力する。

```rs

    use asposepdf::{Document, Permissions};

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a password-protected PDF-document
        let pdf = Document::open_with_password("sample_with_permissions.pdf", "ownerpass")?;

        // Get current permissions of PDF-document
        let permissions: Permissions = pdf.get_permissions()?;

        // Print permissions
        println!("Permissions: {}", permissions);

        Ok(())
    }
```