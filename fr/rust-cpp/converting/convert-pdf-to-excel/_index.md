---
title: Convertir PDF en Excel en Rust
linktitle: Convertir PDF en Excel
type: docs
weight: 20
url: /fr/rust-cpp/convert-pdf-to-xlsx/
lastmod: "2026-07-20"
description: Aspose.PDF for Rust vous permet de convertir un PDF au format XLSX.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Outil Rust pour convertir des documents PDF en Excel
Abstract: La bibliothèque Aspose.PDF for Rust via C++ offre une solution robuste pour convertir des documents PDF au format XLSX avec une grande précision et efficacité. Cette fonctionnalité permet aux développeurs d'extraire des données tabulaires des PDF tout en préservant la mise en page, la structure et le formatage d'origine des feuilles de calcul Excel. La documentation propose des conseils détaillés pour implémenter le processus de conversion, incluant du code d'exemple et des instructions étape par étape afin de faciliter une intégration transparente dans les applications Rust.
SoftwareApplication: rust-cpp
---

**Aspose.PDF for Rust** prend en charge la fonctionnalité de conversion des fichiers PDF au format Excel.

## Convertir le PDF en XLSX

Excel propose des outils avancés pour trier, filtrer et analyser les données, ce qui facilite l'exécution de tâches telles que l'analyse des tendances ou la modélisation financière, qui sont difficiles avec des fichiers PDF statiques. Copier manuellement les données des PDF dans Excel prend du temps et est source d'erreurs. La conversion automatise ce processus, économisant un temps considérable pour de grands ensembles de données.

Aspose.PDF for Rust utilise [save_xlsx](https://reference.aspose.com/pdf/rust-cpp/convert/save_xlsx/) pour convertir le fichier PDF téléchargé en une feuille de calcul Excel et l'enregistrer.

1. Importer les packages requis.
1. Ouvrir un fichier PDF.
1. Convertir le PDF en XLSX en utilisant [save_xlsx](https://reference.aspose.com/pdf/rust-cpp/convert/save_xlsx/).

```rust

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as XlsX-document
      pdf.save_xlsx("sample.xlsx")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Essayez de convertir PDF en Excel en ligne**

Aspose.PDF for Rust vous présente une application en ligne gratuite ["PDF vers XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), où vous pouvez essayer d'examiner la fonctionnalité et la qualité avec lesquelles il fonctionne.

[![Conversion Aspose.PDF PDF vers Excel avec une application gratuite](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}