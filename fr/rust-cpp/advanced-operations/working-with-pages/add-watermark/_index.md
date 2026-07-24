---
title: Ajouter un filigrane au PDF avec Rust
linktitle: Ajouter un filigrane
type: docs
weight: 80
url: /fr/rust-cpp/add-watermarks/
description: Cet exemple montre comment ajouter un filigrane texte personnalisable à un document PDF en utilisant Aspose.PDF for Rust via C\u002B\u002B.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter un filigrane texte
Abstract: Aspose.PDF for Rust via C\u002B\u002B offre une manière flexible d’ajouter des filigranes texte aux documents PDF. Cet exemple montre comment insérer un filigrane personnalisable en spécifiant le contenu du texte, la police, la taille, la couleur, la position, l’angle de rotation, le comportement de superposition et la transparence. Les filigranes sont couramment utilisés pour le marquage de marque, les étiquettes de confidentialité, les marques de brouillon ou la protection des documents.
SoftwareApplication: rust-cpp
---

Le [add_watermark](https://reference.aspose.com/pdf/rust-cpp/organize/add_watermark/) Cette méthode permet aux développeurs d'appliquer programmatiquement un filigrane texte à un document PDF existant. Le filigrane peut être entièrement personnalisé, y compris :

- Texte du filigrane
- Famille de police
- Taille de police
- Couleur du texte (format HEX)
- Coordonnées de position X et Y
- Angle de rotation
- Placement au premier plan ou en arrière-plan
- Opacité (niveau de transparence)

Dans cet exemple, l'application ouvre un fichier PDF existant, applique un filigrane semi-transparent et tourné, puis enregistre le document modifié sous un nouveau nom de fichier.

Cette fonctionnalité est particulièrement utile pour marquer les documents comme Brouillon, Confidentiel, Exemple, ou pour ajouter des éléments de marque avant la distribution.

1. Ouvrez le document PDF existant.
1. Appelez la méthode add_watermark et configurez les propriétés du filigrane.
1. Enregistrez le document mis à jour.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Add watermark to PDF-document
        pdf.add_watermark(
            "WATERMARK",
            "Arial",
            16.0,
            "#010101",
            100,
            100,
            45,
            true,
            0.5,
        )?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_add_watermark.pdf")?;

        Ok(())
    }
```