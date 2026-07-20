---
title: Supprimer des pages PDF avec Rust via C++
linktitle: Supprimer des pages PDF
type: docs
weight: 30
url: /fr/rust-cpp/delete-pages/
description: Vous pouvez supprimer des pages de votre fichier PDF en utilisant Aspose.PDF for Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Supprimer des pages PDF avec Aspose.PDF for Rust
Abstract: Aspose.PDF for Rust via C++ offre une fonctionnalité efficace pour supprimer des pages des documents PDF, permettant aux développeurs de retirer facilement les pages indésirables ou inutiles. La bibliothèque permet la suppression d'une ou de plusieurs pages en spécifiant les numéros de page ou les plages, assurant des modifications précises du document. Cette fonctionnalité aide à rationaliser les fichiers PDF en éliminant le contenu redondant et en optimisant la structure du document. La documentation fournit des instructions étape par étape ainsi que des exemples de code pour aider les développeurs à mettre en œuvre la fonctionnalité de suppression de pages efficacement dans leurs applications.
SoftwareApplication: rust-cpp
---

Vous pouvez supprimer des pages d'un fichier PDF en utilisant **Aspose.PDF for Rust via C++**. Le fragment de code suivant montre comment manipuler un document PDF en supprimant une page spécifique. Cette méthode est efficace pour les tâches de manipulation de documents PDF, notamment pour retirer des pages, enregistrer le document modifié et assurer une gestion appropriée des ressources.

1. Ouverture d'un fichier PDF.
1. Suppression d'une page spécifique avec [page_delete](https://reference.aspose.com/pdf/rust-cpp/core/page_delete/) fonction.
1. Enregistrement du Document en utilisant [save](https://reference.aspose.com/pdf/rust-cpp/core/save/) méthode.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document from file
        let pdf = Document::open("sample.pdf")?;

        // Delete specified page in PDF-document
        pdf.page_delete(1)?;

        // Save the previously opened PDF-document
        pdf.save()?;

        Ok(())
    }
```
