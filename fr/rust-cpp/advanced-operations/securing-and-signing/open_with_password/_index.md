---
title: Ouvrir un PDF protégé par mot de passe avec Rust
linktitle: Ouvrir un PDF protégé par mot de passe
type: docs
weight: 70
url: /fr/rust-cpp/open-password-protected-pdf/
description: Ouvrir un fichier PDF protégé par mot de passe avec Aspose.PDF for Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ouvrir un document PDF protégé par mot de passe

Ouvrir un document PDF protégé par mot de passe avec Aspose.PDF for Rust via C++. Le document est ouvert avec le mot de passe du propriétaire, qui accorde un accès complet et permet d'autres opérations telles que la lecture des métadonnées, la modification du contenu, la modification des autorisations ou la suppression du chiffrement.

1. Ouvrir le document PDF protégé avec [open_with_password](https://reference.aspose.com/pdf/rust-cpp/security/open_with_password/) et fournissez le chemin du fichier ainsi que le mot de passe propriétaire pour déverrouiller le document.
1. Travaillez avec le document ouvert.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a password-protected PDF-document
        let _pdf = Document::open_with_password("sample_with_password.pdf", "ownerpass")?;

        // working...

        Ok(())
    }
```