---
title:  使用 Rust 加密 PDF
linktitle: 加密 PDF 文件
type: docs
weight: 10
url: /zh/rust-cpp/encrypt-pdf/
description: 使用 Aspose.PDF for Rust via C++ 加密 PDF 文件。
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 使用用户或所有者密码加密 PDF 文件

要轻松且安全地加密文档，您可以使用 Aspose.PDF for Rust via C++。

- 如果设置了 **user_password**，它是打开 PDF 所需提供的密码。Acrobat/Reader 将提示用户输入用户密码。如果密码不正确，文档将无法打开。
- 如果设置了 **owner_password**，它会控制权限，例如打印、编辑、提取、评论等。Acrobat/Reader 将根据权限设置阻止这些操作。如果您想设置/更改权限，Acrobat 将需要此密码。

该 PDF 同时使用用户密码和所有者密码进行保护，拥有特定的访问权限，并采用符合 PDF 2.0 标准的 AES-128 加密。加密后，文档会保存到磁盘，以确保受控访问和对 PDF 文件的安全处理。

1. 创建一个新的 PDF 文档。
1. 使用以下方式加密 PDF 文档 [加密](https://reference.aspose.com/pdf/rust-cpp/security/encrypt/) 方法。
1. 指定用户密码以限制打开文档。
1. 指定所有者密码以控制权限。
1. 使用权限位标志定义允许的操作。
1. 选择 AES-128 作为加密算法。
1. 启用 PDF 2.0 加密以符合现代安全合规性。
1. 使用以下方式保存加密的 PDF。 [保存为](https://reference.aspose.com/pdf/rust-cpp/core/save_as/). 

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