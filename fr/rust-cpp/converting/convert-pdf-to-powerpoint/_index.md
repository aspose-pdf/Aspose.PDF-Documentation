---
title: Convertir PDF en PPTX en Rust
linktitle: Convertir PDF en PowerPoint
type: docs
weight: 30
url: /fr/rust-cpp/convert-pdf-to-powerpoint/
lastmod: "2026-07-20"
description: Aspose.PDF vous permet de convertir le PDF au format PPTX en utilisant Rust.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Outil Rust pour convertir PDF en PowerPoint
Abstract: Aspose.PDF for Rust via C++ fournit une solution fiable pour convertir des documents PDF au format PowerPoint (PPTX) tout en préservant la mise en page, le formatage et la structure du contenu d'origine. Cette fonctionnalité permet aux développeurs de transformer de manière transparente des fichiers PDF statiques en présentations dynamiques et modifiables. La bibliothèque offre des options de personnalisation pour contrôler le processus de conversion, garantissant une sortie de haute qualité adaptée à une utilisation professionnelle et commerciale. La documentation fournit des instructions détaillées étape par étape ainsi que des exemples de code pour aider les développeurs à intégrer efficacement la conversion PDF-to-PowerPoint dans leurs applications.
SoftwareApplication: rust-cpp
---

## Convertir PDF en PPTX

L'extrait de code Rust fourni montre comment convertir un document PDF en PPTX en utilisant la bibliothèque Aspose.PDF :

1. Ouvrez un document PDF.
1. Convertissez un fichier PDF en PPTX en utilisant [save_pptx](https://reference.aspose.com/pdf/rust-cpp/convert/save_pptx/) fonction.

```rust

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as PptX-document
      pdf.save_pptx("sample.pptx")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Essayer de convertir le PDF en PowerPoint en ligne**

Aspose.PDF for Rust vous propose une application en ligne gratuite [“PDF to PPTX”](https://products.aspose.app/pdf/conversion/pdf-to-pptx), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Convertion PDF vers PPTX avec l'application gratuite](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}