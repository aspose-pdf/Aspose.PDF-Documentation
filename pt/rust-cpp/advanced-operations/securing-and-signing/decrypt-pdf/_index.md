---
title: Descriptografar PDF usando Rust
linktitle: Descriptografar arquivo PDF
type: docs
weight: 40
url: /pt/rust-cpp/decrypt-pdf/
description: Descriptografar arquivo PDF com Aspose.PDF for Rust via C\u002B\u002B.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Descriptografar arquivo PDF usando senha do proprietário

Você pode abrir, descriptografar e salvar um documento PDF protegido por senha usando Aspose.PDF for Rust via C\u002B\u002B.
O PDF é aberto com a senha do proprietário, descriptografado para remover todas as restrições de segurança e, em seguida, salvo como um novo PDF sem proteção.

1. Use [open_with_password](https://reference.aspose.com/pdf/rust-cpp/security/open_with_password/) para carregar um PDF protegido por senha fornecendo o caminho do arquivo e a senha do proprietário.
1. Chame o [decrypt](https://reference.aspose.com/pdf/rust-cpp/security/decrypt/) método para remover a proteção por senha e todas as restrições de segurança associadas ao documento.
1. Salvar o PDF descriptografado usando [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/).

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