---
title: Descifrar PDF usando Rust
linktitle: Descifrar archivo PDF
type: docs
weight: 40
url: /es/rust-cpp/decrypt-pdf/
description: Descifrar archivo PDF con Aspose.PDF for Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Descifrar archivo PDF usando la contraseña del propietario

Puedes abrir, descifrar y guardar un documento PDF protegido con contraseña usando Aspose.PDF for Rust via C++.
El PDF se abre con la contraseña del propietario, se descifra para eliminar todas las restricciones de seguridad y luego se guarda como un nuevo PDF sin protección.

1. Usar [open_with_password](https://reference.aspose.com/pdf/rust-cpp/security/open_with_password/) para cargar un PDF protegido con contraseña proporcionando la ruta del archivo y la contraseña del propietario.
1. Llame al [decrypt](https://reference.aspose.com/pdf/rust-cpp/security/decrypt/) método para eliminar la protección con contraseña y todas las restricciones de seguridad asociadas del documento.
1. Guardar el PDF descifrado usando [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/).

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