---
title: Ajouter des pages au document PDF
linktitle: Ajouter des pages
type: docs
weight: 10
url: /fr/rust-cpp/add-pages/
description: Découvrez comment ajouter des pages à un PDF existant en Rust avec Aspose.PDF pour améliorer et étendre vos documents.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter des pages PDF avec Aspose.PDF pour Rust
Abstract: Aspose.PDF for Rust via C++ offre des fonctionnalités puissantes pour ajouter des pages aux documents PDF, permettant aux développeurs de créer de nouvelles pages dynamiquement et de les personnaliser selon des exigences spécifiques. La bibliothèque prend en charge l'insertion de pages vierges ou la copie de pages à partir de documents existants tout en offrant des options pour définir la taille de la page, l'orientation et le contenu. Ces capacités permettent une expansion et une personnalisation fluides du document. La documentation comprend des instructions détaillées et des exemples de code pour aider les développeurs à implémenter efficacement les fonctionnalités d'ajout de pages dans leurs applications.
SoftwareApplication: rust-cpp
---

## Ajouter une page dans un fichier PDF

L'extrait de code Rust fourni montre comment exécuter l'opération Add Page à la fin du PDF en utilisant la bibliothèque Aspose.PDF.

1. Le [open](https://reference.aspose.com/pdf/rust-cpp/core/open/) La fonction permet au programme de charger un fichier PDF existant (sample.pdf) pour le manipuler. Ceci est essentiel pour toutes les opérations liées au PDF, telles que l'édition, l'ajout de contenu ou la lecture de données.
1. Le [page_add](https://reference.aspose.com/pdf/rust-cpp/core/page_add/) La méthode est utilisée pour insérer une nouvelle page vierge dans le document PDF existant. Cela est utile pour étendre un document ou le préparer à du contenu supplémentaire.
1. La [save](https://reference.aspose.com/pdf/rust-cpp/core/save/) méthode garantit que les modifications apportées au PDF sont réécrites dans le fichier. Cette étape est cruciale pour conserver les changements, comme l'ajout de nouvelles pages.

Cet extrait est un exemple concis et efficace de la façon d'utiliser la bibliothèque Aspose.PDF Rust pour des tâches de manipulation de PDF de base.

Aspose.PDF for Rust vous permet d'insérer une page dans un document PDF à n\'importe quel emplacement du fichier ainsi que d\'ajouter des pages à la fin d\'un fichier PDF.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document from file
        let pdf = Document::open("sample.pdf")?;

        // Add new page in PDF-document
        pdf.page_add()?;

        // Save the previously opened PDF-document
        pdf.save()?;

        Ok(())
    }
```

## Insérer une page dans un fichier PDF

Le [page_insert](https://reference.aspose.com/pdf/rust-cpp/core/page_insert/) la méthode insère une nouvelle page à la position spécifiée. Cette fonctionnalité est utile lorsque vous devez insérer des pages supplémentaires dans un document existant, par exemple, ajouter une nouvelle section ou du contenu à un rapport ou à une présentation.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document from file
        let pdf = Document::open("sample.pdf")?;

        // Insert new page at the specified position in PDF-document
        pdf.page_insert(1)?;

        // Save the previously opened PDF-document
        pdf.save()?;

        Ok(())
    }
```