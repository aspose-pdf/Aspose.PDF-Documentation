---
title: Obtener permisos usando Rust
linktitle: Obtener permisos
type: docs
weight: 60
url: /es/rust-cpp/get-permissions/
description: Leer y mostrar los permisos de acceso de un documento PDF protegido con contraseña con Aspose.PDF for Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Obtener permisos de un documento PDF protegido con contraseña

Esta sección explica cómo leer y mostrar los permisos de acceso de un documento PDF protegido con contraseña en Rust.
El PDF se abre con la contraseña del propietario, lo que otorga acceso total a la configuración de seguridad del documento. Luego se recuperan los permisos asignados actualmente y se imprimen en la consola.

1. Abra el documento PDF protegido.
1. Llamar [get_permissions](https://reference.aspose.com/pdf/rust-cpp/security/get_permissions/) para obtener los indicadores de permiso que definen qué operaciones están permitidas.
1. Imprima los permisos recuperados en la consola.

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