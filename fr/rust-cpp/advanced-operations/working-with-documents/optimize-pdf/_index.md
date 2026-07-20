---
title: Optimiser le PDF en utilisant Aspose.PDF for Rust via C++
linktitle: Optimiser le fichier PDF
type: docs
weight: 10
url: /fr/rust-cpp/optimize-pdf/
description: Optimiser et compresser les fichiers PDF à l'aide de l'outil Rust.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Optimiser et compresser les fichiers PDF à l'aide d'Aspose.PDF for Rust
Abstract: Aspose.PDF for Rust via C++ offre de puissantes fonctionnalités d'optimisation pour réduire la taille et améliorer les performances des documents PDF. La bibliothèque propose diverses options d'optimisation, notamment la compression des images, la suppression des objets inutilisés, la réduction des tailles de police et l'optimisation des flux de contenu. Ces fonctionnalités aident à améliorer l'efficacité du stockage des documents et garantissent des temps de traitement et de chargement plus rapides. La documentation fournit des instructions étape par étape et des exemples de code pour aider les développeurs à mettre en œuvre l'optimisation des PDF efficacement au sein de leurs applications.
SoftwareApplication: rust-cpp
---

## Optimiser le document PDF

Le kit d'outils avec Aspose.PDF for Rust via C++ vous permet d'optimiser un document PDF.

Ce extrait est utile pour les applications où la réduction de la taille ou l'amélioration de l'efficacité des fichiers PDF est cruciale, comme pour les téléchargements Web, l'archivage ou le partage sur une bande passante limitée.

1. Le [ouvrir](https://reference.aspose.com/pdf/rust-cpp/core/open/) La méthode charge le fichier PDF spécifié (sample.pdf) en mémoire.
1. Le [optimiser](https://reference.aspose.com/pdf/rust-cpp/organize/optimize/) réduit la taille du fichier en effectuant des optimisations telles que la suppression des objets inutilisés, la compression d'images, l'aplatissement des annotations, le détachement des polices et l'activation de la réutilisation du contenu. Ces étapes permettent de réduire les besoins de stockage et d'améliorer la vitesse de traitement du document PDF.
1. Le [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) La méthode enregistre le PDF optimisé dans un nouveau fichier.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Optimize PDF-document content
        pdf.optimize()?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_optimize.pdf")?;

        Ok(())
    }
```