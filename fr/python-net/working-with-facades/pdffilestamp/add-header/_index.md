---
title: Ajouter un en-tête au PDF
type: docs
weight: 20
url: /fr/python-net/add-header/
description: Découvrez comment ajouter des en-têtes texte et image aux pages PDF en utilisant PdfFileStamp en Python.
lastmod: "2026-05-22"
TechArticle: true
AlternativeHeadline: Ajouter des en-têtes texte et image au PDF en Python
Abstract: Cet article explique comment ajouter du contenu d'en-tête aux documents PDF avec Aspose.PDF for Python via .NET en utilisant la façade PdfFileStamp. Il montre comment ajouter un en-tête texte, placer un en-tête image et appliquer des marges d'en-tête personnalisées avant d'enregistrer le PDF mis à jour.
---

Aspose.PDF for Python via .NET fournit le [PdfFileStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) façade pour ajouter du contenu répété aux pages PDF. Vous pouvez l'utiliser pour placer du texte d'en‑tête ou des images en haut de chaque page et ajuster les marges d'en‑tête pour contrôler le placement.

## Ajouter un en‑tête texte

Utiliser `add_header()` avec un `FormattedText` objet lorsque vous souhaitez placer le même texte d'en-tête sur chaque page du PDF. Le deuxième argument définit la marge supérieure de l'en-tête.

```python
import sys
from os import path

import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_text_header(infile: str, outfile: str) -> None:
    """Add a text header with a top margin."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        text = pdf_facades.FormattedText("Sample Header")
        pdf_stamper.add_header(text, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Ajouter un en‑tête d'image

Utiliser `add_header()` avec un fichier d'image ou un flux d'image lorsque l'en-tête doit afficher un logo ou un autre graphique. Cela est utile pour les mises en page de documents de marque.

```python
import sys
from os import path

import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_image_header(infile: str, image_file: str, outfile: str) -> None:
    """Add an image header with a top margin."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_header(image_file, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Ajouter un en-tête avec des marges personnalisées

Utilisez la surcharge avec trois valeurs de marge lorsque vous avez besoin de plus de contrôle sur le placement de l'en-tête. Dans cet exemple, l'en-tête est ajouté avec les marges supérieures, gauche et droite personnalisées.

```python
import sys
from os import path

import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_header_with_margins(infile: str, outfile: str) -> None:
    """Add a text header with top, left, and right margins."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        text = pdf_facades.FormattedText(
            text="Sample Header",
            text_color=ap_pydrawing.Color.blue,
            font_name="Arial",
            text_encoding=pdf_facades.EncodingType.WINANSI,
            embedded=True,
            font_size=12.0,
        )
        pdf_stamper.add_header(text, 20, 20, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```
