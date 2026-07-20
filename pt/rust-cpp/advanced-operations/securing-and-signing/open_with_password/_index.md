---
title: Abrir um PDF protegido por senha usando Rust
linktitle: Abrir um PDF protegido por senha
type: docs
weight: 70
url: /pt/rust-cpp/open-password-protected-pdf/
description: Abrir um arquivo PDF protegido por senha com Aspose.PDF for Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Abrir um documento PDF protegido por senha

Abrir um documento PDF protegido por senha com Aspose.PDF for Rust via C++. O documento é aberto com a senha do proprietário, que concede acesso total e permite operações adicionais, como ler metadados, modificar o conteúdo, alterar permissões ou remover a criptografia.

1. Abrir o documento PDF protegido com [open_with_password](https://reference.aspose.com/pdf/rust-cpp/security/open_with_password/) e forneça o caminho do arquivo junto com a senha do proprietário para desbloquear o documento.
1. Trabalhe com o documento aberto.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a password-protected PDF-document
        let _pdf = Document::open_with_password("sample_with_password.pdf", "ownerpass")?;

        // working...

        Ok(())
    }
```