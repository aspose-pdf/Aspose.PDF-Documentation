---
title:  Criptografar PDF usando Rust
linktitle: Criptografar arquivo PDF
type: docs
weight: 10
url: /pt/rust-cpp/encrypt-pdf/
description: Criptografar arquivo PDF com Aspose.PDF for Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Criptografar arquivo PDF usando senha de usuário ou senha do proprietário

Para criptografar documentos de forma fácil e segura, você pode usar Aspose.PDF for Rust via C++.

- O **user_password**, se definido, é o que você precisa fornecer para abrir um PDF. O Acrobat/Reader solicitará que o usuário insira a senha de usuário. Se não estiver correta, o documento não será aberto.
- A **owner_password**, se definida, controla as permissões, como impressão, edição, extração, comentários, etc. Acrobat/Reader impedirá essas ações com base nas configurações de permissão. Acrobat exigirá esta senha se você quiser definir/alterar permissões.

O PDF está protegido com senhas de usuário e de proprietário, permissões de acesso específicas e criptografia AES-128 em conformidade com os padrões PDF 2.0. Uma vez criptografado, o documento é salvo em disco, garantindo acesso controlado e manuseio seguro do arquivo PDF.

1. Crie um novo documento PDF.
1. Criptografe o documento PDF com [criptografar](https://reference.aspose.com/pdf/rust-cpp/security/encrypt/) método.
1. Especifique uma senha de usuário para restringir a abertura do documento.
1. Especifique uma senha de proprietário para controlar as permissões.
1. Defina as ações permitidas usando um bitflag de permissões.
1. Escolha AES-128 como o algoritmo de criptografia.
1. Habilite a criptografia PDF 2.0 para conformidade de segurança moderna.
1. Salve o PDF criptografado usando [salvar_como](https://reference.aspose.com/pdf/rust-cpp/core/save_as/). 

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