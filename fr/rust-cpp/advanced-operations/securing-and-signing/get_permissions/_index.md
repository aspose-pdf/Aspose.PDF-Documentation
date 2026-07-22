---
title: Obtenir les autorisations avec Rust
linktitle: Obtenir les autorisations
type: docs
weight: 60
url: /fr/rust-cpp/get-permissions/
description: Lire et afficher les autorisations d’accès d’un document PDF protégé par mot de passe avec Aspose.PDF pour Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Obtenir les autorisations d’un document PDF protégé par mot de passe

Cette section explique comment lire et afficher les autorisations d’accès d’un document PDF protégé par mot de passe en Rust.
Le PDF est ouvert avec le mot de passe propriétaire, qui accorde un accès complet aux paramètres de sécurité du document. Les autorisations actuellement assignées sont ensuite récupérées et affichées dans la console.

1. Ouvrez le document PDF protégé.
1. Appelez [get_permissions](https://reference.aspose.com/pdf/rust-cpp/security/get_permissions/) pour obtenir les indicateurs d’autorisation qui définissent quelles opérations sont autorisées.
1. Affichez les autorisations récupérées dans la console.

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