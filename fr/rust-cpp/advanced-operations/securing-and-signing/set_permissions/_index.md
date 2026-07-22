---
title: Définir les autorisations pour un document PDF en utilisant Rust
linktitle: Définir les autorisations
type: docs
weight: 80
url: /fr/rust-cpp/set_permissions/
description: Définir les autorisations pour un document PDF avec Aspose.PDF for Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Définir les autorisations d'accès pour un document PDF

Un nouveau document PDF est créé et protégé avec des mots de passe utilisateur et propriétaire, tandis que des actions spécifiques—comme l'impression, la modification du contenu et le remplissage des formulaires—sont explicitement autorisées. Le document est ensuite enregistré avec les restrictions d'autorisation définies appliquées.

1. Créer un nouveau document PDF.
1. Appeler [set_permissions](https://reference.aspose.com/pdf/rust-cpp/security/set_permissions/) pour protéger le document.
1. Spécifiez un mot de passe utilisateur pour restreindre l'accès.
1. Spécifiez un mot de passe propriétaire pour contrôler les paramètres de sécurité.
1. Définissez les opérations autorisées en utilisant un bitflag de permissions.
1. Enregistrez le PDF avec les autorisations appliquées en utilisant [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/).

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