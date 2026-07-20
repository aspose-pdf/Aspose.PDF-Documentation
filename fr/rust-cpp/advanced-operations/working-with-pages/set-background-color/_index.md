---
title: Définir la couleur de fond pour le PDF avec Rust via C\u002B\u002B
linktitle: Définir la couleur de fond
type: docs
weight: 80
url: /fr/rust-cpp/set-background-color/
description: Définir la couleur de fond pour votre fichier PDF avec Rust via C\u002B\u002B.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Définir la couleur de fond pour le PDF avec Aspose.PDF pour Rust
Abstract: Aspose.PDF for Rust via C\u002B\u002B offre la fonctionnalité de définir la couleur de fond des pages PDF, permettant aux développeurs de personnaliser l'apparence des documents. Cette fonctionnalité permet d'appliquer des couleurs unies à l'ensemble du fond de la page, améliorant la présentation visuelle du document. Les développeurs peuvent facilement spécifier les valeurs de couleur en utilisant des modèles de couleur standard tels que RGB ou CMYK. La documentation fournit des instructions détaillées et des exemples de code pour aider les développeurs à implémenter efficacement la personnalisation de la couleur de fond dans leurs applications C\u002B\u002B.
SoftwareApplication: rust-cpp
---

1. L'extrait de code fourni montre comment définir une couleur de fond pour un fichier PDF en utilisant la bibliothèque Aspose.PDF en Rust.
1. Le [ouvrir](https://reference.aspose.com/pdf/rust-cpp/core/open/) La méthode charge le fichier PDF spécifié en mémoire, permettant d'autres manipulations, telles que la modification de son apparence ou de son contenu.
1. Le [set_background](https://reference.aspose.com/pdf/rust-cpp/organize/set_background/) La méthode applique une nouvelle couleur d'arrière-plan au document PDF. Les valeurs RVB permettent aux utilisateurs de personnaliser le style visuel du document.
1. Le [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) la méthode enregistre le PDF mis à jour sous un nouveau nom.

Ce code est idéal pour les applications qui doivent automatiser les personnalisations de PDF, comme la création de rapports de marque, l'ajout de filigranes ou l'amélioration de la cohérence visuelle à travers plusieurs documents.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Set PDF-document background color using RGB values
      pdf.set_background(200, 100, 101)?;

      // Save the previously opened PDF-document with new filename
      pdf.save_as("sample_set_background.pdf")?;

      Ok(())
  }
```