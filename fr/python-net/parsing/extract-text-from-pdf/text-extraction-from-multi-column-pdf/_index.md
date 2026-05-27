---
title: Améliorer l'extraction de texte des PDF multi‑colonnes
linktitle: Extraction de texte à partir de PDF multi‑colonnes
type: docs
weight: 30
url: /fr/python-net/text-extraction-from-multi-column-pdf/
description: Apprenez des techniques pour améliorer l'extraction de texte à partir de mises en page PDF multi‑colonnes avec Aspose.PDF for Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Réduisez la taille de la police manuellement, puis extrayez

Dans certaines mises en page à plusieurs colonnes, réduire la taille de la police des fragments de texte avant l'extraction peut améliorer l'ordre de lecture et réduire les problèmes de chevauchement. Cette technique peut aider avec des documents fortement formatés tels que des magazines, des articles de recherche, des brochures ou des rapports contenant des colonnes de texte denses.

1. Chargez le PDF.
1. Utiliser [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) collecter les fragments de texte.
1. Réduisez la taille de police de chaque fragment, puis enregistrez et rouvrez le document.
1. Utiliser [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/) extraire le texte.
1. Écrire le texte extrait dans un fichier de sortie.

```python
import io
import aspose.pdf as ap


def extract_text_reduce_font(infile, outfile, reduce_ratio=0.7):
    """
    Extract text from a multi-column PDF by first reducing font size of all text fragments.
    Args:
        infile (str): Path to input PDF.
        outfile (str): Output text file.
        reduce_ratio (float): Ratio to reduce font size (e.g., 0.7 = 70%).
    """
    doc = ap.Document(infile)

    frag_absorber = ap.text.TextFragmentAbsorber()
    doc.pages.accept(frag_absorber)
    for frag in frag_absorber.text_fragments:
        frag.text_state.font_size = frag.text_state.font_size * reduce_ratio
    # Save to memory stream and reopen (to apply changes)
    ms = io.BytesIO()
    doc.save(ms)
    ms.seek(0)
    doc2 = ap.Document(ms)
    text_absorber = ap.text.TextAbsorber()
    doc2.pages.accept(text_absorber)
    extracted_text = text_absorber.text
    with open(outfile, "w", encoding="utf-8") as tw:
        tw.write(extracted_text)
```

## Extraire le texte avec un facteur d'échelle

Une autre option pour l'extraction multicolonnes consiste à configurer [TextExtractionOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textextractionoptions/) avec un facteur d'échelle. Ajuster le facteur d'échelle peut améliorer l'interprétation des fragments très rapprochés et aider à préserver un ordre de lecture plus précis dans les mises en page denses, les tableaux ou les documents à colonnes.

1. Chargez le PDF.
1. Créer un [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/).
1. Configurer `TextExtractionOptions.scale_factor`.
1. Attribuez les options d'extraction à l'absorbeur.
1. Extrayez le texte de la page et écrivez le résultat dans un fichier de sortie.

```python
import aspose.pdf as ap


def extract_text_scale_factor(infile, outfile, scale_factor=0.5):
    """
    Extract text from a PDF with multi-column layout using scale factor.
    Args:
        infile (str): Input PDF path.
        outfile (str): Output text file path.
        scale_factor (float): Scale factor between 0.1 and 1.0 or 0 for auto-scaling.
    """
    doc = ap.Document(infile)
    text_absorber = ap.text.TextAbsorber()
    ext_opts = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    ext_opts.scale_factor = scale_factor
    text_absorber.extraction_options = ext_opts
    doc.pages.accept(text_absorber)
    extracted_text = text_absorber.text
    with open(outfile, "w", encoding="utf-8") as tw:
        tw.write(extracted_text)
```
