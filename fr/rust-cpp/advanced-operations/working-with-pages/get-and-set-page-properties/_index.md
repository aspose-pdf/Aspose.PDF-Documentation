---
title: Obtenir et définir les propriétés de la page
linktitle: Obtenir et définir les propriétés de la page
type: docs
weight: 70
url: /fr/rust-cpp/get-and-set-page-properties/
description: Apprenez comment obtenir et définir les propriétés des pages pour les documents PDF en utilisant Aspose.PDF for Rust, permettant une mise en forme personnalisée du document.
lastmod: "2026-07-20"
TechArticle: true
AlternativeHeadline: Obtenir et définir les propriétés de la page avec Aspose.PDF for Rust
Abstract: Aspose.PDF for Rust via C++ fournit des fonctionnalités complètes pour obtenir et définir les propriétés des pages dans les documents PDF, permettant aux développeurs d’accéder et de modifier divers attributs de page tels que la taille, la rotation, les marges et les métadonnées. Ces capacités permettent un contrôle précis de la mise en page et de l’apparence du document afin de répondre à des exigences d’application spécifiques. La bibliothèque assure une personnalisation et une optimisation fluides des pages PDF. La documentation propose des directives détaillées et des exemples de code pour aider les développeurs à récupérer et à mettre à jour efficacement les propriétés des pages dans leurs applications.
SoftwareApplication: rust-cpp
---


Aspose.PDF for Rust vous permet de lire et de définir les propriétés des pages d’un fichier PDF. Cette section montre comment obtenir le nombre de pages d’un fichier PDF, récupérer des informations sur les propriétés des pages PDF telles que la couleur et définir les propriétés de la page.

## Obtenir le nombre de pages d’un fichier PDF

Lorsque vous travaillez avec des documents, vous souhaitez souvent savoir combien de pages ils contiennent. Avec Aspose.PDF, cela ne prend pas plus de deux lignes de code.

**Aspose.PDF for Rust via C++** vous permet de compter les Pages avec [page_count](https://reference.aspose.com/pdf/rust-cpp/core/page_count/) fonction.

L'extrait de code suivant est conçu pour ouvrir un document PDF, récupérer le nombre de pages et afficher le résultat.

Le [page_count](https://reference.aspose.com/pdf/rust-cpp/core/page_count/) La méthode est appelée pour obtenir le nombre total de pages dans le document PDF. Ceci est utile pour les tâches qui doivent connaître la longueur du document, comme lors de l'extraction de pages spécifiques ou de l'exécution d'opérations sur toutes les pages. Cette méthode constitue une façon simple d'interroger la structure du document.

Pour obtenir le nombre de pages dans un fichier PDF :

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document from file
      let pdf = Document::open("sample.pdf")?;

      // Return page count in PDF-document
      let count = pdf.page_count()?;

      // Print the page count
      println!("Count: {}", count);

      Ok(())
  }
```

## Définir la taille de la page

Dans cet exemple, la méthode pdf.PageSetSize() modifie la taille de la première page du document PDF. La constante PageSizeA1 garantit que la première page est définie au format de papier A1. Cela est utile lors de la conversion de documents vers un format standardisé ou pour s'assurer que le contenu spécifique s'adapte correctement aux pages.

1. Ouverture du document PDF avec [ouvrir](https://reference.aspose.com/pdf/rust-cpp/core/open/) méthode.
1. Définition de la taille de la page avec [page_set_size](https://reference.aspose.com/pdf/rust-cpp/organize/page_set_size/) fonction.
1. Enregistrement du Document en utilisant [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) méthode.

```rs

    use asposepdf::{Document, PageSize};

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Set the size of a page in the PDF-document
        pdf.page_set_size(1, PageSize::A1)?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_page1_set_size_A1.pdf")?;

        Ok(())
    }
```
