---
title: Расшифровать PDF с использованием Rust
linktitle: Расшифровать PDF‑файл
type: docs
weight: 40
url: /ru/rust-cpp/decrypt-pdf/
description: Расшифровать PDF‑файл с помощью Aspose.PDF for Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Расшифровать PDF‑файл, используя пароль владельца

Вы можете открыть, расшифровать и сохранить защищённый паролем PDF‑документ, используя Aspose.PDF for Rust via C++.
PDF открывается с паролем владельца, расшифровывается для снятия всех ограничений безопасности, а затем сохраняется как новый, незащищённый PDF.

1. Используйте [open_with_password](https://reference.aspose.com/pdf/rust-cpp/security/open_with_password/) для загрузки PDF, защищённого паролем, указав путь к файлу и пароль владельца.
1. Вызовите [decrypt](https://reference.aspose.com/pdf/rust-cpp/security/decrypt/) метод для снятия защиты паролем и всех связанных ограничений безопасности с документа.
1. Сохраните расшифрованный PDF с помощью [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/).

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
