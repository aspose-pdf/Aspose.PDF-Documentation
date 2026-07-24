---
title: Ouvrir un document PDF de façon programmatique
linktitle: Ouvrir un PDF
type: docs
weight: 20
url: /fr/rust-cpp/open-pdf-document/
description: Apprenez comment ouvrir un fichier PDF avec Aspose.PDF for Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ouvrir un document PDF avec Aspose.PDF for Rust via C++
Abstract: Aspose.PDF for Rust via C++ offre des fonctionnalités puissantes pour ouvrir et charger des documents PDF de manière programmatique, permettant aux développeurs d'accéder et de manipuler le contenu PDF avec facilité. La bibliothèque prend en charge l'ouverture de fichiers PDF depuis diverses sources, telles que les chemins de fichiers et les flux mémoire, tout en assurant un traitement efficace et une gestion optimale des ressources. Elle propose des fonctionnalités pour inspecter les propriétés du document, extraire le texte et les images, et effectuer d'autres opérations sur les PDF chargés. La documentation comprend des instructions détaillées et des exemples de code pour aider les développeurs à intégrer les capacités d'ouverture de PDF dans leurs applications de manière fluide.
SoftwareApplication: rust-cpp
---

## Ouvrir un document PDF existant

L'extrait de code montre les opérations essentielles pour travailler avec des PDF en utilisant Aspose.PDF pour Rust. Il s'agit d'ouvrir un fichier, d'enregistrer les modifications et de fermer correctement les ressources. Cela en fait un exemple de base pour les développeurs qui manipulent des documents PDF.

L'exemple est simple, ce qui le rend facile à comprendre et à modifier. Il est idéal pour les débutants ou comme modèle de base pour des applications plus complexes.

La capacité d'ouvrir et d'enregistrer des documents PDF est une exigence fondamentale dans de nombreux scénarios, tels que la génération de rapports, la modification de documents ou la création de flux de travail automatisés.

Cet exemple montre la facilité d'utilisation de l'API pour la manipulation simple de PDF, qui peut être étendue pour inclure des fonctionnalités avancées telles que l'extraction de texte, l'annotation ou le remplissage de formulaires.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document named "sample.pdf"
        let pdf = Document::open("sample.pdf")?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_open.pdf")?;

        Ok(())
    }
```
