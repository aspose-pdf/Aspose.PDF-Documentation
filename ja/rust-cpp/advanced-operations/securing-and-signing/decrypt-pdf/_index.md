---
title: Rust を使用して PDF を復号化する
linktitle: PDF ファイルを復号化する
type: docs
weight: 40
url: /ja/rust-cpp/decrypt-pdf/
description: C++ 経由で Rust 用 Aspose.PDF を使用して PDF ファイルを復号化する。
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## オーナーパスワードを使用して PDF ファイルを復号化する

C++ 経由で Rust 用 Aspose.PDF を使用して、パスワードで保護された PDF ドキュメントを開き、復号化し、保存できます。
PDF はオーナーパスワードで開かれ、すべてのセキュリティ制限が解除されるように復号化され、その後、新しい保護されていない PDF として保存されます。

1. 使用 [open_with_password](https://reference.aspose.com/pdf/rust-cpp/security/open_with_password/) ファイルパスと所有者パスワードを指定して、パスワードで保護された PDF をロードします。
1. 呼び出す [decrypt](https://reference.aspose.com/pdf/rust-cpp/security/decrypt/) メソッドは、文書からパスワード保護とそれに関連するすべてのセキュリティ制限を解除します。
1. 復号化されたPDFを使用して保存する [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/).

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a password-protected PDF-document
      let pdf = Document::open_with_password("sample_with_password.pdf", "ownerpass")?;

      // Decrypt PDF-document
      pdf.decrypt()?;

      // Save the previously opened PDF-document with new filename
      pdf.save_as("sample_decrypt.pdf")?;

      Ok(())
  }
```