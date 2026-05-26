---
title: Ajouter un pied de page au PDF
type: docs
weight: 10
url: /fr/python-net/add-footer/
description: Apprenez comment ajouter des pieds de page texte et image aux pages PDF en utilisant PdfFileStamp en Python.
lastmod: "2026-05-22"
TechArticle: true
AlternativeHeadline: Ajouter des pieds de page texte et image au PDF en Python
Abstract: Cet article explique comment ajouter du contenu de pied de page aux documents PDF avec Aspose.PDF for Python via .NET en utilisant la façade PdfFileStamp. Il montre comment ajouter un pied de page texte, placer un pied de page image et appliquer des marges de pied de page personnalisées avant d'enregistrer le PDF mis à jour.
---

Aspose.PDF for Python via .NET fournit le [PdfFileStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) façade pour ajouter du contenu répété aux pages PDF. Vous pouvez l'utiliser pour placer du texte de pied de page ou des images au bas de chaque page et ajuster les marges du pied de page pour contrôler le positionnement.

## Ajouter un texte de pied de page

Utiliser `add_footer()` avec un `FormattedText` objet lorsque vous voulez placer le même texte de pied de page sur chaque page du PDF. Le deuxième argument définit la marge inférieure utilisée pour le placement du pied de page.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_text_footer(infile: str, outfile: str) -> None:
    """Add a text footer with a bottom margin."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        text = pdf_facades.FormattedText("Sample Footer")
        pdf_stamper.add_footer(text, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Ajouter un pied de page d'image

Utiliser `add_footer()` avec un flux d'image lorsque le pied de page doit afficher un logo ou une autre image au lieu du texte. L'exemple ouvre le fichier image en tant que flux binaire et le place en bas de chaque page.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_image_footer(infile: str, image_file: str, outfile: str) -> None:
    """Add an image footer with a bottom margin."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_footer(image_file, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Ajouter un pied de page avec des marges personnalisées

Utilisez la surcharge avec trois valeurs de marge lorsque vous avez besoin de plus de contrôle sur le positionnement du pied de page. Dans cet exemple, le pied de page est ajouté avec des marges personnalisées en bas, à gauche et à droite.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_footer_with_margins(infile: str, outfile: str) -> None:
    """Add a text footer with bottom, left, and right margins."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        text = pdf_facades.FormattedText("This footer has margins on all sides.")
        pdf_stamper.add_footer(text, 20, 20, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```
