---
title: Convertir le PDF en EPUB, TeX, texte, XPS en Rust
linktitle: Convertir le PDF en d'autres formats
type: docs
weight: 90
url: /fr/rust-cpp/convert-pdf-to-other-files/
lastmod: "2026-07-20"
description: Ce sujet vous montre comment convertir un fichier PDF en d'autres formats de fichier tels que EPUB, LaTeX, texte, XPS, etc. en utilisant Rust.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Outil Rust pour convertir PDF en EPUB, TeX, texte et XPS
Abstract: Aspose.PDF for Rust via C++ offre des capacités puissantes pour convertir des documents PDF en divers formats de fichier, notamment DOCX, PPTX, HTML, EPUB, SVG, et plus encore. Cette fonctionnalité permet aux développeurs d'extraire et de réutiliser le contenu PDF de manière transparente tout en conservant le formatage, la structure et la qualité à travers différents formats de sortie. La bibliothèque fournit des options flexibles pour personnaliser le processus de conversion selon des exigences spécifiques. La documentation comprend des directives complètes et des exemples de code pour aider les développeurs à mettre en œuvre efficacement la conversion PDF vers fichier dans leurs applications.
SoftwareApplication: rust-cpp
---

## Convertir le PDF en EPUB

**<abbr title="Electronic Publication">EPUB</abbr>** est une norme d'e-book libre et ouverte du International Digital Publishing Forum (IDPF). Les fichiers ont l’extension .epub.
EPUB est conçu pour le contenu refluable, ce qui signifie qu’un lecteur EPUB peut optimiser le texte pour un dispositif d’affichage particulier. EPUB prend également en charge le contenu à mise en page fixe. Le format est destiné à être un format unique que les éditeurs et les maisons de conversion peuvent utiliser en interne, ainsi que pour la distribution et la vente. Il remplace la norme Open eBook.

L'extrait de code Rust fourni montre comment convertir un document PDF en EPUB en utilisant la bibliothèque Aspose.PDF :

1. Ouvrez un document PDF.
1. Convertir un fichier PDF en EPUB en utilisant [save_epub](https://reference.aspose.com/pdf/rust-cpp/convert/save_epub/) fonction.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as Epub-document
      pdf.save_epub("sample.epub")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Essayez de convertir le PDF en EPUB en ligne**

Aspose.PDF for Rust vous présente une application en ligne gratuite ["PDF vers EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), où vous pouvez essayer d’enquêter sur la fonctionnalité et la qualité avec lesquelles il fonctionne.

[![Aspose.PDF Conversion PDF en EPUB avec Application gratuite](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

## Convertir le PDF en TeX

**Aspose.PDF for Rust** prend en charge la conversion de PDF en TeX.
Le format de fichier LaTeX est un format de fichier texte avec une balise spéciale et est utilisé dans le système de préparation de documents basé sur TeX pour une composition de haute qualité.

L'extrait de code Rust fourni montre comment convertir un document PDF en TeX à l'aide de la bibliothèque Aspose.PDF :

1. Ouvrez un document PDF.
1. Convertir un fichier PDF en TeX en utilisant [save_tex](https://reference.aspose.com/pdf/rust-cpp/convert/save_tex/) fonction.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as TeX-document
      pdf.save_tex("sample.tex")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Essayez de convertir le PDF en LaTeX/TeX en ligne**

Aspose.PDF for Rust vous présente une application en ligne gratuite ["PDF en LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), où vous pouvez essayer d’enquêter sur la fonctionnalité et la qualité avec lesquelles il fonctionne.

[![Aspose.PDF Conversion PDF vers LaTeX/TeX avec une application gratuite](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## Convertir PDF en TXT

L'extrait de code Rust fourni montre comment convertir un document PDF en TXT à l'aide de la bibliothèque Aspose.PDF :

1. Ouvrez un document PDF.
1. Convertir un fichier PDF en TXT en utilisant [save_txt](https://reference.aspose.com/pdf/rust-cpp/convert/save_txt/) fonction.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as Txt-document
      pdf.save_txt("sample.txt")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Essayez de convertir PDF en texte en ligne**

Aspose.PDF for Rust vous présente une application en ligne gratuite ["PDF en texte"](https://products.aspose.app/pdf/conversion/pdf-to-txt), où vous pouvez essayer d’enquêter sur la fonctionnalité et la qualité avec lesquelles il fonctionne.

[![Aspose.PDF Conversion PDF en texte avec application gratuite](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Convertir PDF en XPS

Le type de fichier XPS est principalement associé à la spécification XML Paper (XPS) de Microsoft Corporation. La spécification XML Paper (XPS), précédemment nom de code Metro et englobant le concept marketing Next Generation Print Path (NGPP), est l'initiative de Microsoft visant à intégrer la création et la visualisation de documents dans le système d'exploitation Windows.

**Aspose.PDF for Rust** offre la possibilité de convertir les fichiers PDF en <abbr title="XML Paper Specification">XPS</abbr> format. Essayons d'utiliser le fragment de code présenté pour convertir des fichiers PDF au format XPS avec Rust.

Le fragment de code Rust fourni montre comment convertir un document PDF en XPS à l'aide de la bibliothèque Aspose.PDF :

1. Ouvrez un document PDF.
1. Convertir un fichier PDF en XPS à l’aide de [save_xps](https://reference.aspose.com/pdf/rust-cpp/convert/save_xps/) fonction.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as Xps-document
      pdf.save_xps("sample.xps")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Essayez de convertir PDF en XPS en ligne**

Aspose.PDF for Rust vous présente une application en ligne gratuite ["PDF vers XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), où vous pouvez essayer d’enquêter sur la fonctionnalité et la qualité avec lesquelles il fonctionne.

[![Aspose.PDF Conversion PDF en XPS avec application gratuite](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

## Convertir le PDF en PDF en niveaux de gris

L'extrait de code Rust fourni montre comment convertir la première page d'un document PDF en PDF en niveaux de gris en utilisant la bibliothèque Aspose.PDF :

1. Ouvrez un document PDF.
1. Convertir une page PDF en PDF niveaux de gris en utilisant [page_niveaux_de_gris](https://reference.aspose.com/pdf/rust-cpp/organize/page_grayscale/) fonction.

Cet exemple convertit une page spécifique de votre PDF en niveaux de gris :

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document from file
      let pdf = Document::open("sample.pdf")?;

      // Convert page to black and white
      pdf.page_grayscale(1)?;

      // Save the previously opened PDF-document with new filename
      pdf.save_as("sample_page1_grayscale.pdf")?;

      Ok(())
  }
```

## Convertir PDF en Markdawn

Le fragment de code Rust fourni montre comment convertir un document PDF en fichier Markdown (.md) à l'aide d'Aspose.PDF for Rust.

1. Ouvrez le fichier PDF source.
1. Convertir le PDF en Markdown.
1. Enregistrez le document PDF ouvert au format Markdown.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as Markdown-document
      pdf.save_markdown("sample.md")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Essayez de convertir le PDF en MD en ligne**

Aspose.PDF for Rust vous présente une application en ligne gratuite [PDF en MD](https://products.aspose.app/pdf/conversion/md), où vous pouvez essayer d’enquêter sur la fonctionnalité et la qualité avec lesquelles il fonctionne.

[![Aspose.PDF Conversion PDF en MD avec application gratuite](pdf_to_md.png)](https://products.aspose.app/pdf/conversion/md)
{{% /alert %}}
