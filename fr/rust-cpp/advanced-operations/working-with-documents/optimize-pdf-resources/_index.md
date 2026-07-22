---
title: Optimiser les ressources PDF à l'aide de Rust via C++
linktitle: Optimiser les ressources PDF
type: docs
weight: 15
url: /fr/rust-cpp/optimize-pdf-resources/
description: Optimiser les ressources des fichiers PDF à l'aide de l'outil Rust.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Optimiser les ressources PDF à l'aide d'Aspose.PDF for Rust
Abstract: Aspose.PDF for Rust via C++ offre des capacités avancées pour optimiser les ressources PDF, améliorant l'efficacité du document et réduisant la taille du fichier. La bibliothèque permet aux développeurs d'optimiser les polices, les images et les métadonnées en supprimant les données redondantes et en compressant les ressources sans compromettre la qualité du document. Ces techniques d'optimisation améliorent les performances du document, rendant les PDF plus adaptés au partage et au stockage. La documentation fournit des directives détaillées et des exemples de code pour aider les développeurs à mettre en œuvre efficacement l'optimisation des ressources dans leurs applications.
SoftwareApplication: rust-cpp
---

## Optimiser les ressources PDF

Optimiser les ressources dans le document:

  1. Les ressources qui ne sont pas utilisées sur les pages du document sont supprimées.
  1. Les ressources égales sont regroupées en un seul objet.
  1. Les objets non utilisés sont supprimés.

L'optimisation peut inclure la compression des images, la suppression des objets non utilisés et l'optimisation des polices pour réduire la taille du fichier et améliorer les performances. Toute erreur survenant pendant cette opération est enregistrée et termine le programme.  
 
1. Le [ouvrir](https://reference.aspose.com/pdf/rust-cpp/core/open/) method charge le fichier PDF spécifié (sample.pdf) en mémoire.
1. Optimise les ressources du PDF pour plus d'efficacité en utilisant [optimize_resource](https://reference.aspose.com/pdf/rust-cpp/organize/optimize_resource/) method.
1. Le [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) method enregistre le PDF optimisé dans un nouveau fichier.

L'extrait de code suivant montre comment optimiser un document PDF.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document named "sample.pdf"
      let pdf = Document::open("sample.pdf")?;
      pdf.optimize_resource()?;
      // Save the optimized PDF-document with new filename
      pdf.save_as("sample_optimize_resource.pdf")?;

      Ok(())
  }
```