---
title: Amélioration de l'extraction de texte à partir de PDF multi‑colonnes
linktitle: Extraction de texte à partir de PDF multi‑colonnes
type: docs
weight: 30
url: /fr/python-net/text-extraction-from-multi‑column-pdf/
description: Cette section contient des articles sur le formatage du texte et la mise à l'échelle en utilisant Aspose.PDF en Python.
lastmod: "2025-11-05"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
---

## Réduire manuellement la taille de police puis extraire

La précision de l'extraction dans les PDF multi-colonnes est obtenue en réduisant d'abord la taille de police de tous les fragments de texte avant l'extraction. Le processus aide à prévenir les problèmes de texte qui se chevauchent pouvant survenir dans des mises en page très formatées ou multi-colonnes.
Cela aide à extraire du texte à partir de mises en page complexes — comme les magazines, les articles académiques ou les brochures — où le redimensionnement du texte améliore la clarté de la mise en page et les résultats d'extraction.

1. Charger le PDF.
1. Réduire la taille de police des fragments de texte existants, enregistrer et rouvrir le document.
1. Utiliser 'TextAbsorber' pour extraire le texte des pages.
1. Écrire le texte extrait.

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
    try:
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
    finally:
        doc.close()
```

## Extraire le texte avec un facteur d'échelle

Extraire le texte des PDF avec des mises en page multi-colonnes en appliquant un facteur d'échelle au document. Ajuster le facteur d'échelle garantit que les fragments de texte sont correctement interprétés, réduisant le chevauchement ou le désalignement lors de l'extraction.
C'est utile pour les PDF avec des colonnes, des tableaux ou des mises en page denses, où la mise à l'échelle aide à maintenir l'ordre de lecture et la structure corrects dans le texte extrait.

1. Charger le PDF.
1. Configurer 'TextExtractionOptions.ScaleFactor'.
1. Utiliser 'TextAbsorber' pour extraire le texte des pages.
1. Écrire le texte extrait.

```python

import aspose.pdf as ap

def extract_text_with_scale_factor(infile, outfile, scale_factor=0.5):
    """
    Extract text from a PDF with multi-column layout using scale factor.
    Args:
        infile (str): Input PDF path.
        outfile (str): Output text file path.
        scale_factor (float): Scale factor between 0.1 and 1.0 or 0 for auto-scaling.
    """
    doc = ap.Document(infile)
    try:
        text_absorber = ap.text.TextAbsorber()
        ext_opts = ap.text.TextExtractionOptions(ap.text.TextExtractionOptions.TextFormattingMode.PURE)
        ext_opts.scale_factor = scale_factor
        text_absorber.extraction_options = ext_opts
        doc.pages.accept(text_absorber)
        extracted_text = text_absorber.text
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        doc.close()
```
