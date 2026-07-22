---
title: Rust を使用して PDF ドキュメントの権限を設定する
linktitle: 権限を設定する
type: docs
weight: 80
url: /ja/rust-cpp/set_permissions/
description: C++ 経由で Rust 用 Aspose.PDF を使用して PDF ドキュメントの権限を設定する。
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF ドキュメントのアクセス権限を設定する

新しい PDF ドキュメントを作成し、ユーザー パスワードとオーナー パスワードで保護します。また、印刷、コンテンツの変更、フォームへの入力など、特定の操作を明示的に許可します。その後、定義された権限制限を適用した状態でドキュメントを保存します。

1. 新しい PDF ドキュメントを作成する。
1. 呼び出す [set_permissions](https://reference.aspose.com/pdf/rust-cpp/security/set_permissions/) 文書を保護するために。
1. アクセスを制限するためにユーザーパスワードを指定します。
1. セキュリティ設定を管理するために所有者パスワードを指定します。
1. 許可された操作をパーミッションビットフラグで定義します。
1. 権限を適用したPDFを保存するには [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/).

```rs

    use asposepdf::{Document, Permissions};

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Create a new PDF-document
        let pdf = Document::new()?;

        // Set permissions for PDF-document.
        pdf.set_permissions(
            "userpass",  // User password
            "ownerpass", // Owner password
            Permissions::PRINT_DOCUMENT | Permissions::MODIFY_CONTENT | Permissions::FILL_FORM, // Permissions bitflag
        )?;

        // Save the PDF-document with the updated permissions
        pdf.save_as("sample_with_permissions.pdf")?;

        Ok(())
    }
```