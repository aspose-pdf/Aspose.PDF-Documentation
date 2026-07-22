---
title: Décrypter le PDF avec Rust
linktitle: Décrypter le fichier PDF
type: docs
weight: 40
url: /fr/rust-cpp/decrypt-pdf/
description: Décrypter le fichier PDF avec Aspose.PDF for Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Décrypter le fichier PDF en utilisant le mot de passe du propriétaire

Vous pouvez ouvrir, décrypter et enregistrer un document PDF protégé par mot de passe en utilisant Aspose.PDF for Rust via C++.
Le PDF est ouvert avec le mot de passe du propriétaire, décrypté pour supprimer toutes les restrictions de sécurité, puis enregistré comme un nouveau PDF non protégé.

1. Utiliser [open_with_password](https://reference.aspose.com/pdf/rust-cpp/security/open_with_password/) pour charger un PDF protégé par mot de passe en fournissant le chemin du fichier et le mot de passe du propriétaire.
1. Appelez le [decrypt](https://reference.aspose.com/pdf/rust-cpp/security/decrypt/) méthode pour supprimer la protection par mot de passe et toutes les restrictions de sécurité associées du document.
1. Enregistrer le PDF décrypté en utilisant [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/).

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a password-protected PDF-document
      let pdf = Document::open_with_password("sample_with_password.pdf", "ownerpass")?;

      // Decrypt PDF-document
      pdf.decrypt()?;

      // Save the previously opened PDF-document with new filename
      pdf.save_as("sample_decrypt.pdf")?;

      Ok(())
  }
```