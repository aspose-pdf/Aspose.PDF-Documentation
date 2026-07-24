---
title:  Rust を使用して PDF を暗号化する
linktitle: PDF ファイルを暗号化する
type: docs
weight: 10
url: /ja/rust-cpp/encrypt-pdf/
description: Aspose.PDF for Rust via C++ を使用して PDF ファイルを暗号化する。
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## ユーザーまたは所有者パスワードを使用して PDF ファイルを暗号化する

ドキュメントを簡単かつ安全に暗号化するには、Aspose.PDF for Rust via C++ を使用できます。

- **user_password** が設定されている場合、PDF を開くために提供する必要があるものです。Acrobat/Reader はユーザーにユーザーパスワードの入力を求めます。正しくない場合、ドキュメントは開きません。
- **owner_password** が設定されている場合、印刷、編集、抽出、コメントなどの権限を制御します。Acrobat/Reader は権限設定に基づいてこれらの操作を許可しません。権限を設定または変更したい場合、Acrobat はこのパスワードを要求します。

PDF はユーザー パスワードとオーナーパスワードの両方、特定のアクセス権限、および PDF 2.0 標準に準拠した AES-128 暗号化で保護されています。暗号化されると、ドキュメントはディスクに保存され、アクセスが制御され、PDF ファイルの安全な取り扱いが保証されます。

1. 新しい PDF ドキュメントを作成します。
1. PDF ドキュメントを暗号化する [暗号化](https://reference.aspose.com/pdf/rust-cpp/security/encrypt/) 方法。
1. ドキュメントの開封を制限するためにユーザーパスワードを指定します。
1. 権限を制御するためにオーナーパスワードを指定します。
1. 許可されたアクションをパーミッションビットフラグで定義します。
1. 暗号化アルゴリズムとして AES-128 を選択します。
1. 最新のセキュリティ準拠のために PDF 2.0 暗号化を有効にします。
1. 暗号化された PDF を使用して保存します。 [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/). 

```rs

  use asposepdf::{CryptoAlgorithm, Document, Permissions};

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Create a new PDF-document
      let pdf = Document::new()?;

      // Encrypt PDF-document
      pdf.encrypt(
          "userpass",  // User password
          "ownerpass", // Owner password
          Permissions::PRINT_DOCUMENT | Permissions::MODIFY_CONTENT | Permissions::FILL_FORM, // Permissions bitflag
          CryptoAlgorithm::AESx128, // Encryption algorithm
          true,                     // Use PDF 2.0 encryption
      )?;

      // Save the encrypted PDF-document
      pdf.save_as("sample_with_password.pdf")?;

      Ok(())
  }
```