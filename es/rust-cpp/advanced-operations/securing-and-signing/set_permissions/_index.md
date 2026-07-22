---
title: Establecer permisos para un documento PDF usando Rust
linktitle: Establecer permisos
type: docs
weight: 80
url: /es/rust-cpp/set_permissions/
description: Establecer permisos para un documento PDF con Aspose.PDF para Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Establecer permisos de acceso para un documento PDF

Se crea un nuevo documento PDF y se protege con contraseñas de usuario y propietario, mientras que acciones específicas—como imprimir, modificar contenido y rellenar formularios—se permiten explícitamente. Luego, el documento se guarda aplicando las restricciones de permisos definidas.

1. Crear un nuevo documento PDF.
1. Llamar [set_permissions](https://reference.aspose.com/pdf/rust-cpp/security/set_permissions/) para proteger el documento.
1. Especifique una contraseña de usuario para restringir el acceso.
1. Especifique una contraseña de propietario para controlar la configuración de seguridad.
1. Defina operaciones permitidas usando una bandera de bits de permisos.
1. Guarda el PDF con los permisos aplicados usando [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/).

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