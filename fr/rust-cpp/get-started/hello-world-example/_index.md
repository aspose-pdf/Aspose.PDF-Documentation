---
title: Exemple de Hello World utilisant le langage Rust
linktitle: Exemple Hello World
type: docs
weight: 40
url: /fr/rust-cpp/hello-world-example/
description: Cet exemple montre comment créer un document PDF simple contenant le texte Hello World en utilisant Aspose.PDF for Rust.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hello World via Aspose.PDF for Rust
Abstract: Le guide de démarrage pour Aspose.PDF for Rust via C++ fournit une introduction à l'utilisation de la bibliothèque, couvrant les étapes de base pour créer et manipuler des documents PDF. Il comprend un exemple 'Hello World' démontrant comment générer un simple fichier PDF avec du texte, aidant les développeurs à comprendre rapidement la fonctionnalité principale de l'API.
SoftwareApplication: rust-cpp
---

Un exemple "Hello World" est traditionnellement utilisé pour introduire les fonctionnalités d'un langage de programmation ou d'un logiciel avec un cas d'utilisation simple.

**Aspose.PDF for Rust** est une API PDF riche en fonctionnalités qui permet aux développeurs d'intégrer la création, la manipulation et les capacités de conversion de documents PDF avec Rust. Elle prend en charge de nombreux formats de fichiers populaires, notamment PDF, TXT, XLSX, EPUB, TEX, DOC, DOCX, PPTX, les formats d'image, etc. Dans cet article, nous créons un document PDF contenant le texte "Hello World!" Après avoir installé Aspose.PDF for Rust dans votre environnement, vous pouvez exécuter l'exemple de code pour voir comment fonctionne l'API Aspose.PDF.
Le fragment de code ci‑dessous suit ces étapes :

1. Créer une nouvelle instance de document PDF.
1. Ajouter une nouvelle page au document PDF en utilisant [page_add](https://reference.aspose.com/pdf/rust-cpp/core/page_add/) fonction.
1. Définir la taille de la page en utilisant [page_set_size](https://reference.aspose.com/pdf/rust-cpp/organize/page_set_size/).
1. Ajouter le texte "Hello World!" à la première page en utilisant [page_add_text](https://reference.aspose.com/pdf/rust-cpp/organize/page_add_text/).
1. Enregistrer le document PDF en utilisant [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) méthode.

Le fragment de code suivant est un programme Hello World pour illustrer le fonctionnement de l'API Aspose.PDF for Rust.

```rs

    use asposepdf::{Document, PageSize};
    use std::error::Error;

    fn main() -> Result<(), Box<dyn Error>> {
        // Create a new PDF-document
        let pdf = Document::new()?;

        // Add a new page
        pdf.page_add()?;

        // Set the size of the first page to A4
        pdf.page_set_size(1, PageSize::A4)?;

        // Add "Hello World!" text to the first page
        pdf.page_add_text(1, "Hello World!")?;

        // Save the PDF-document as "hello.pdf"
        pdf.save_as("hello.pdf")?;

        println!("Saved PDF-document: hello.pdf");

        Ok(())
}
```
