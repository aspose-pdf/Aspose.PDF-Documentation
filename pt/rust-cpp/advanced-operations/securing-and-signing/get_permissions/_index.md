---
title: Obter permissões usando Rust
linktitle: Obter permissões
type: docs
weight: 60
url: /pt/rust-cpp/get-permissions/
description: Leia e exiba as permissões de acesso de um documento PDF protegido por senha com Aspose.PDF for Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Obter permissões de um documento PDF protegido por senha

Esta seção explica como ler e exibir as permissões de acesso de um documento PDF protegido por senha em Rust.
O PDF é aberto com a senha do proprietário, que concede acesso total às configurações de segurança do documento. As permissões atualmente atribuídas são então recuperadas e impressas no console.

1. Abra o documento PDF protegido.
1. Chame [get_permissions](https://reference.aspose.com/pdf/rust-cpp/security/get_permissions/) para obter os sinalizadores de permissão que definem quais operações são permitidas.
1. Imprima as permissões recuperadas no console.

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