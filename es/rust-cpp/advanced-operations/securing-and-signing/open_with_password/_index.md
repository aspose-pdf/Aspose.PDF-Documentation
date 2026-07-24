---
title: Abrir un PDF protegido con contraseña usando Rust
linktitle: Abrir un PDF protegido con contraseña
type: docs
weight: 70
url: /es/rust-cpp/open-password-protected-pdf/
description: Abrir un archivo PDF protegido con contraseña con Aspose.PDF for Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Abrir un documento PDF protegido con contraseña

Abrir un documento PDF protegido con contraseña con Aspose.PDF for Rust via C++. El documento se abre con la contraseña del propietario, que otorga acceso total y permite operaciones posteriores como leer metadatos, modificar contenido, cambiar permisos o eliminar el cifrado.

1. Abrir el documento PDF protegido con [open_with_password](https://reference.aspose.com/pdf/rust-cpp/security/open_with_password/) y proporcione la ruta del archivo junto con la contraseña del propietario para desbloquear el documento.
1. Trabaje con el documento abierto.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a password-protected PDF-document
        let _pdf = Document::open_with_password("sample_with_password.pdf", "ownerpass")?;

        // working...

        Ok(())
    }
```