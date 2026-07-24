---
title: Ajout d'en-tête et de pied de page au PDF avec Rust
linktitle: Ajout d'en-tête et de pied de page au PDF
type: docs
weight: 90
url: /fr/rust-cpp/add-headers-and-footers-of-pdf-file/
description:
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment ajouter un en-tête et un pied de page au PDF avec Rust
Abstract: Cet article montre comment ajouter des en-têtes et des pieds de page textuels aux documents PDF en utilisant la bibliothèque asposepdf Rust. Il explique comment ouvrir un PDF existant, insérer du texte cohérent dans l'en-tête ou le pied de page de chaque page, et enregistrer le document modifié en tant que nouveau fichier. Les exemples illustrent un flux de travail simple et sûr qui peut être utilisé pour des tâches telles que l'ajout de numéros de page, de titres ou de branding de manière programmatique dans les applications Rust.
SoftwareApplication: rust-cpp
---

## Ajout d'en-têtes et de pieds de page sous forme de fragments de texte

### Ajouter du texte dans le pied de page d'un document PDF

Notre outil vous permet d'ouvrir un PDF existant, d'ajouter un pied de texte à toutes les pages, et d'enregistrer le PDF modifié comme un nouveau fichier en utilisant la bibliothèque asposepdf Rust. Il gère les erreurs de façon élégante avec le type Result de Rust.

1. Ouvrez un document PDF existant.
1. Ajoutez du texte au pied de page avec [add_text_footer](https://reference.aspose.com/pdf/rust-cpp/organize/add_text_footer/).
1. Enregistrez le PDF modifié.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Add text in Footer of a PDF-document
        pdf.add_text_footer("FOOTER")?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_add_text_footer.pdf")?;

        Ok(())
    }
```

### Ajouter du texte dans l'en-tête d'un PDF-document

Cet extrait de code montre comment ouvrir un fichier PDF existant, ajouter un en-tête de texte à toutes les pages et enregistrer le document modifié en tant que nouveau fichier en utilisant la bibliothèque asposepdf. Il fournit une méthode simple et automatisée pour insérer des en-têtes cohérents dans les PDF.

1. Ouvrir un PDF existant.
1. Ajouter du texte à l'en-tête avec helps [add_text_header](https://reference.aspose.com/pdf/rust-cpp/organize/add_text_header/).
1. Enregistrez le PDF modifié.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Add text in Header of a PDF-document
        pdf.add_text_header("HEADER")?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_add_text_header.pdf")?;

        Ok(())
    }
```