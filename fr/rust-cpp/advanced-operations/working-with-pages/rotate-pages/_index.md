---
title: Faire pivoter les pages PDF avec Rust via C++
linktitle: Faire pivoter les pages PDF
type: docs
weight: 50
url: /fr/rust-cpp/rotate-pages/
description: Ce sujet décrit comment faire pivoter l'orientation des pages dans un fichier PDF existant de manière programmatique avec Rust via C++
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Faire pivoter les pages PDF avec Aspose.PDF pour Rust
Abstract: Aspose.PDF pour Rust via C++ offre une fonctionnalité robuste permettant de faire pivoter les pages dans les documents PDF, offrant aux développeurs la possibilité de modifier l'orientation des pages selon les besoins. La bibliothèque prend en charge la rotation des pages de 90, 180 ou 270 degrés, permettant des ajustements rapides et efficaces de la mise en page du document. Cette fonctionnalité est utile pour corriger les pages mal orientées ou modifier la présentation du document. La documentation comprend des instructions étape par étape et des exemples de code pour aider les développeurs à intégrer de manière transparente les capacités de rotation des pages dans leurs applications.
SoftwareApplication: rust-cpp
---

Cette section décrit comment modifier l'orientation des pages d'un format paysage à portrait et vice versa dans un fichier PDF existant en utilisant Rust.

Faire pivoter les pages garantit un alignement correct pour l'impression ou l'affichage des PDF dans des environnements professionnels

1. Ouvrez le document PDF.
1. Faire pivoter les pages PDF. Le [pivoter](https://reference.aspose.com/pdf/rust-cpp/organize/rotate/) La fonction applique une rotation spécifique (dans ce cas, 180 degrés) à une page donnée.
1. Enregistrer les modifications dans un nouveau fichier. Le [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) La fonction crée un nouveau fichier PDF pour préserver l'original tout en enregistrant la version mise à jour.

Dans cet exemple, vous faites pivoter une page spécifique dans un document PDF :

```rs

    use asposepdf::{Document, Rotation};

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Rotate PDF-document
        pdf.rotate(Rotation::On270)?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_rotate.pdf")?;

        Ok(())
    }
```