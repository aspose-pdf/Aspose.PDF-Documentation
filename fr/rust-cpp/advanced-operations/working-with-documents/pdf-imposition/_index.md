---
title: Imposition PDF utilisant Aspose.PDF for Rust via C++
linktitle: Imposition PDF
type: docs
weight: 30
url: /fr/rust-cpp/pdf-imposition/
description: Cet article explique comment réorganiser les pages PDF pour des mises en page optimisées pour l'impression en utilisant Aspose.PDF for Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment créer un livret ou un N‑Up de fichiers PDF
Abstract: Aspose.PDF for Rust via C++ fournit des outils puissants pour restructurer les documents PDF afin de répondre aux exigences d'impression et de mise en page. Cet article montre comment convertir un PDF standard en livret, en garantissant l'ordre correct des pages pour le pliage, et comment créer un PDF N‑Up qui combine plusieurs pages sur une seule feuille. En utilisant des exemples de code Rust concis, les développeurs peuvent rapidement mettre en œuvre des transformations PDF prêtes à l'impression pour les flux de travail de documentation, d'édition et d'archivage.
SoftwareApplication: rust-cpp
---

## Créer un N‑Up de PDF

Un PDF N‑Up place plusieurs pages source sur une seule page de sortie. Dans cet exemple, une disposition 2 × 2 est utilisée, de sorte que quatre pages originales sont combinées sur chaque page du document de sortie.

1. Ouvrez le document PDF source.
1. Enregistrez le document en utilisant une disposition N‑Up avec le nombre spécifié de lignes et de colonnes.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Convert and save the previously opened PDF-document as N-Up PDF-document
        pdf.save_n_up("sample_n_up.pdf", 2, 2)?;

        Ok(())
    }
```

## Créer un livret PDF

Aspose.PDF pour Rust via C++ explique comment convertir un document PDF standard en PDF au format livret.
Le format livret réarrange les pages de sorte que, lorsqu'elles sont imprimées et pliées, le document forme un livret correct avec les pages dans le bon ordre.

1. Ouvrez le document PDF source.
1. Enregistrez le document au format PDF livret.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as booklet PDF-document
      pdf.save_booklet("sample_booklet.pdf")?;

      Ok(())
  }
```

**Veuillez noter qu'une licence d'essai gratuite est requise pour une fonctionnalité complète.**

Explorez le résultat de la création d'un livret de 4 pages.

![Exemple d'un livret de 4 pages](sample_4.png)

Explorez le résultat de la création d'un livret de 3 pages.

![Exemple d'un livret de 3 pages](sample_3.png)