---
title: 使用 Rust 解密 PDF
linktitle: 解密 PDF 文件
type: docs
weight: 40
url: /zh/rust-cpp/decrypt-pdf/
description: 使用 Aspose.PDF for Rust via C++ 解密 PDF 文件。
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 使用所有者密码解密 PDF 文件

您可以使用 Aspose.PDF for Rust via C++ 打开、解密并保存受密码保护的 PDF 文档。
使用所有者密码打开 PDF，解密以移除所有安全限制，然后将其另存为新的未受保护的 PDF。

1. 使用 [open_with_password](https://reference.aspose.com/pdf/rust-cpp/security/open_with_password/) 通过提供文件路径和所有者密码来加载受密码保护的 PDF。
1. 调用 [decrypt](https://reference.aspose.com/pdf/rust-cpp/security/decrypt/) 方法以移除文档的密码保护和所有相关的安全限制。
1. 使用以下方式保存已解密的 PDF [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/).

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