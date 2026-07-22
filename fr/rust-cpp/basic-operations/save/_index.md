---
title: Enregistrer le document PDF de manière programmatique
linktitle: Enregistrer le PDF
type: docs
weight: 30
url: /fr/rust-cpp/save-pdf-document/
description: Apprenez comment enregistrer un fichier PDF avec Aspose.PDF for Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Enregistrer le document PDF avec Aspose.PDF for Rust via C++
Abstract: Aspose.PDF for Rust via C++ offre une fonctionnalité complète pour enregistrer des documents PDF dans différents formats et emplacements avec une grande efficacité et flexibilité. La bibliothèque permet aux développeurs d’enregistrer les PDF sur les systèmes de fichiers, dans des flux mémoire, ou de les exporter dans des formats alternatifs tels que DOCX, XLSX et des images. Elle fournit des options pour personnaliser les paramètres d’enregistrement, optimiser la taille du fichier et garantir l’intégrité des données. La documentation comprend des instructions détaillées et des exemples de code pour aider les développeurs à mettre en œuvre efficacement les capacités d’enregistrement de PDF dans leurs applications.
SoftwareApplication: rust-cpp
---

## Enregistrer le document PDF sur le système de fichiers

L'exemple montre le [nouveau](https://reference.aspose.com/pdf/rust-cpp/core/new/) méthode de création d'un nouveau document PDF, qui est une fonctionnalité fondamentale pour générer des documents dynamiquement, comme des rapports ou des factures.

Le code est simple et peut servir de modèle pour des fonctionnalités plus avancées telles que l'ajout de texte, d'images ou d'annotations au PDF.

Cet exemple montre l'utilisation simple de la bibliothèque Aspose.PDF Rust, mettant en avant son potentiel pour créer, modifier et enregistrer des documents.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Create a new PDF-document
        let pdf = Document::new()?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_new.pdf")?;

        Ok(())
    }
```
