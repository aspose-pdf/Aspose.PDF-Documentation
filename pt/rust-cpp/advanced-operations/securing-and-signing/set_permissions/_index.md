---
title: Definir permissões para um documento PDF usando Rust
linktitle: Definir permissões
type: docs
weight: 80
url: /pt/rust-cpp/set_permissions/
description: Definir permissões para um documento PDF com Aspose.PDF for Rust via C\u002B\u002B.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Definir permissões de acesso para um documento PDF

Um novo documento PDF é criado e protegido com senhas de usuário e proprietário, enquanto ações específicas\u2014como impressão, modificação de conteúdo e preenchimento de formulários\u2014são explicitamente permitidas. O documento é então salvo com as restrições de permissão definidas aplicadas.

1. Criar um novo documento PDF.
1. Chamar [set_permissions](https://reference.aspose.com/pdf/rust-cpp/security/set_permissions/) para proteger o documento.
1. Especifique uma senha de usuário para restringir o acesso.
1. Especifique uma senha de proprietário para controlar as configurações de segurança.
1. Defina as operações permitidas usando uma bandeira de bits de permissões.
1. Salvar o PDF com permissões aplicadas usando [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/).

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