---
title: Convertir des formats PDF en PDF/A en Python
linktitle: Convertir des formats PDF en PDF/A
type: docs
weight: 100
url: /python-net/convert-pdf-to-pdfa/
lastmod: "2022-12-23"
description: Ce sujet vous montre comment Aspose.PDF pour Python via Python permet de convertir un fichier PDF en un fichier PDF conforme au format PDF/A.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF pour Python** vous permet de convertir un fichier PDF en un fichier PDF conforme au format <abbr title="Portable Document Format / A">PDF/A</abbr>. Avant de le faire, le fichier doit être validé. Ce sujet explique comment.

{{% alert color="primary" %}}

Veuillez noter que nous suivons Adobe Preflight pour valider la conformité PDF/A. Tous les outils sur le marché ont leur propre "représentation" de la conformité PDF/A. Veuillez consulter cet article sur les outils de validation PDF/A pour référence. Nous avons choisi les produits Adobe pour vérifier comment Aspose.PDF produit des fichiers PDF parce qu'Adobe est au centre de tout ce qui est lié au PDF.

{{% /alert %}}

Convertissez le fichier en utilisant la méthode Convert de la classe Document.
 Avant de convertir le PDF en fichier conforme PDF/A, validez le PDF à l'aide de la méthode Validate. Le résultat de la validation est stocké dans un fichier XML, puis ce résultat est également passé à la méthode Convert. Vous pouvez également spécifier l'action pour les éléments qui ne peuvent pas être convertis à l'aide de l'énumération ConvertErrorAction.

{{% alert color="success" %}}
**Essayez de convertir PDF en PDF/A en ligne**

Aspose.PDF pour Python vous propose une application en ligne gratuite ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en PDF/A avec application gratuite](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}


## Convertir un fichier PDF en PDF/A-1b

L'extrait de code suivant montre comment convertir des fichiers PDF en PDF conforme PDF/A-1b.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_pdfa.pdf"
    output_log = DIR_OUTPUT + "convert_pdf_to_pdfa.log"
    # Ouvrir le document PDF
    document = ap.Document(input_pdf)
    # Convertir en document conforme PDF/A
    document.convert(output_log, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE)
    # Enregistrer le document de sortie
    document.save(output_pdf)
```