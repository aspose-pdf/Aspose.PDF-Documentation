---
title: Ajouter du texte à un PDF avec Rust
linktitle: Ajouter du texte à un PDF
type: docs
weight: 10
url: /fr/rust-cpp/add-text-to-pdf-file/
description: Apprenez comment ajouter du texte à un document PDF en Rust en utilisant Aspose.PDF pour l'amélioration du contenu et l'édition de documents.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
AlternativeHeadline: Ajouter du texte dans un PDF en utilisant Aspose.PDF pour Rust
Abstract: La section Add Text to PDF File de la documentation Aspose.PDF for C++ and Rust fournit des instructions étape par étape pour insérer du texte dans des documents PDF de manière programmatique. Elle couvre diverses méthodes d’ajout de texte, y compris le positionnement, la personnalisation des polices, les ajustements de couleur et les options d’alignement du texte. Le guide montre comment ajouter du texte à des pages et des emplacements spécifiques dans un PDF, assurant une mise en page précise du contenu. Avec des exemples de code détaillés et des explications, les développeurs peuvent facilement intégrer les fonctionnalités d’insertion de texte dans leurs applications pour une meilleure gestion des documents PDF.
SoftwareApplication: rust-cpp
---

Pour ajouter du texte à un fichier PDF existant :

1. Ouvrir un fichier PDF.
1. Ajouter le texte au document PDF avec [page_add_text](https://reference.aspose.com/pdf/rust-cpp/organize/page_add_text/) fonction.
1. Enregistre les modifications dans le même fichier.

## Ajout de texte

Le fragment de code suivant vous montre comment ajouter du texte dans un fichier PDF existant.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document from file
        let pdf = Document::open("sample.pdf")?;

        // Add text on page
        pdf.page_add_text(1, "added text")?;

        // Save the previously opened PDF-document
        pdf.save()?;

        Ok(())
    }
```
