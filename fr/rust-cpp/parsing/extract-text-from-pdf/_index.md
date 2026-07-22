---
title: Extraire du texte d'un PDF avec Rust
linktitle: Extraire du texte d'un PDF
type: docs
weight: 30
url: /fr/rust-cpp/extract-text-from-pdf/
description: Cet article décrit différentes manières d'extraire du texte de documents PDF à l'aide d'Aspose.PDF for Rust.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraire du texte avec Aspose.PDF for Rust
Abstract: Aspose.PDF for Rust via C++ offre un moyen puissant et efficace d'extraire du texte de documents PDF. La bibliothèque prend en charge plusieurs techniques d'extraction, permettant aux utilisateurs de récupérer du texte d'un document entier, de pages spécifiques ou de zones prédéfinies dans un PDF.
SoftwareApplication: rust-cpp
---

## Extraire du texte d'un document PDF

L'extraction de texte à partir du document PDF est une tâche très courante et utile. Les PDF contiennent souvent des informations critiques qui doivent être accessibles, analysées ou traitées à diverses fins.

L'extraction de texte rend le contenu PDF recherchable, permettant aux utilisateurs de localiser rapidement des informations spécifiques sans parcourir manuellement l'ensemble du document.

Dans le cas où vous souhaitez extraire du texte d'un document PDF, vous pouvez utiliser [extract_text](https://reference.aspose.com/pdf/rust-cpp/core/extract_text/) fonction.
Veuillez consulter le fragment de code suivant afin d'extraire du texte d'un fichier PDF en utilisant Rust.

1. Ouvrez un document PDF avec le nom de fichier fourni.
1. [extract_text](https://reference.aspose.com/pdf/rust-cpp/core/extract_text/) extrait le contenu texte du document PDF.
1. Affichez le texte extrait dans la console.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Return the PDF-document contents as plain text
        let txt = pdf.extract_text()?;

        // Print extracted text
        println!("Extracted text:\n{}", txt);

        Ok(())
    }
```