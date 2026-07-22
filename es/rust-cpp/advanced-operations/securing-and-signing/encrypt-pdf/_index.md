---
title:  Cifrar PDF usando Rust
linktitle: Cifrar archivo PDF
type: docs
weight: 10
url: /es/rust-cpp/encrypt-pdf/
description: Cifrar archivo PDF con Aspose.PDF for Rust a través de C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Cifrar archivo PDF usando contraseña de usuario o de propietario

Para cifrar documentos de forma fácil y segura, puedes usar Aspose.PDF for Rust a través de C++.

- El **user_password**, si está configurado, es lo que necesitas proporcionar para abrir un PDF. Acrobat/Reader solicitará al usuario que introduzca la contraseña de usuario. Si no es correcta, el documento no se abrirá.
- El **owner_password**, si se establece, controla los permisos, como imprimir, editar, extraer, comentar, etc. Acrobat/Reader impedirá estas cosas según la configuración de permisos. Acrobat requerirá esta contraseña si desea establecer/cambiar permisos.

El PDF está protegido con contraseñas de usuario y de propietario, permisos de acceso específicos y cifrado AES-128 conforme a los estándares PDF 2.0. Una vez cifrado, el documento se guarda en disco, garantizando acceso controlado y manejo seguro del archivo PDF.

1. Cree un nuevo documento PDF.
1. Cifre el documento PDF con [cifrar](https://reference.aspose.com/pdf/rust-cpp/security/encrypt/) método.
1. Especifique una contraseña de usuario para restringir la apertura del documento.
1. Especifique una contraseña de propietario para controlar los permisos.
1. Defina acciones permitidas usando una bandera de bits de permisos.
1. Elija AES-128 como el algoritmo de cifrado.
1. Habilite el cifrado PDF 2.0 para el cumplimiento de seguridad moderno.
1. Guarde el PDF encriptado usando [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/). 

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