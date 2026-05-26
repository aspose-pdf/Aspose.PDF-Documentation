---
title: Classe Stamp
type: docs
weight: 150
url: /fr/python-net/stamp-class/
description: Apprenez comment travailler avec la classe Stamp pour ajouter des tampons image, PDF et basés sur du texte aux documents PDF en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF pour Python via .NET fournit le [Stamp](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/stamp/) classe pour placer du contenu visuel réutilisable sur les pages PDF. Un tampon peut être basé sur du texte, une image, ou même une page d'un autre PDF, et il peut être positionné, pivoté, stylisé et limité à des pages spécifiques.

Cet article montre plusieurs flux de travail d’estampillage courants :

1. Créer des ressources texte réutilisables pour les tampons basés sur du texte.
1. Ajouter des tampons d'image et de page PDF.
1. Ajouter des tampons de texte stylisés.
1. Limiter un tampon aux pages sélectionnées.
1. Configurer un tampon d'image d'arrière-plan.

L'exemple utilise deux fonctions d'assistance : l'une crée du texte formaté pour les tampons basés sur du texte, et l'autre crée un `TextState` objet utilisé pour mettre en forme les tampons de texte.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def _create_text_logo(text: str) -> pdf_facades.FormattedText:
    """Create formatted text for text stamp examples."""
    return pdf_facades.FormattedText(
        text,
        drawing.Color.blue,
        drawing.Color.light_gray,
        pdf_facades.FontStyle.HELVETICA_BOLD,
        pdf_facades.EncodingType.WINANSI,
        True,
        14,
    )


def _create_text_state() -> ap.text.TextState:
    """Create a text state used to style text stamps."""
    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.dark_blue
    text_state.font_size = 16
    text_state.font_style = ap.text.FontStyles.BOLD
    return text_state
```

## Ajouter un tampon d'image

Utiliser `bind_image()` lorsque le tampon doit afficher une image telle qu'un logo, un badge ou une icône. Après avoir lié l'image, vous pouvez définir l'ID du tampon et l'origine avant de l'ajouter au document.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_image_stamp(infile: str, image_file: str, outfile: str) -> None:
    """Add an image stamp to the PDF."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)
        stamp.stamp_id = 1
        stamp.set_origin(36, 520)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Ajouter une page PDF en tant que tampon

Utiliser `bind_pdf()` lorsque vous souhaitez utiliser une page d'un autre fichier PDF comme contenu du tampon. Ceci est utile pour les superpositions telles que les approbations, les modèles ou les éléments visuels préconstruits stockés dans un document séparé.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_pdf_page_as_stamp(infile: str, stamp_pdf: str, outfile: str) -> None:
    """Add the first page of another PDF as a stamp."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_pdf(stamp_pdf, 1)
        stamp.page_number = 1
        stamp.set_origin(36, 250)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Ajouter un tampon de texte avec un état de texte

Utiliser `bind_logo()` avec `bind_text_state()` lorsque vous souhaitez créer un tampon texte avec une mise en forme de police personnalisée. Cette approche est utile pour les marques d'approbation, les étiquettes et les annotations spécifiques aux flux de travail.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_text_stamp_with_text_state(infile: str, outfile: str) -> None:
    """Add a text stamp and style it with a TextState object."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_logo(_create_text_logo("Approved by signing workflow"))
        stamp.bind_text_state(_create_text_state())
        stamp.set_origin(36, 700)
        stamp.rotation = 15.0

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Ajouter un tampon aux pages spécifiques

Si le tampon ne doit pas apparaître sur chaque page, attribuez les numéros de pages cibles à `pages` propriété. Cet exemple ajoute un ImageStamp uniquement à la première page.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_stamp_to_specific_pages(infile: str, image_file: str, outfile: str) -> None:
    """Add an image stamp only to the selected pages."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)
        stamp.pages = [1]
        stamp.set_origin(400, 40)
        stamp.set_image_size(120, 60)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Ajouter un tampon d'image d'arrière-plan

Utilisez un tampon d'arrière-plan lorsque l'image doit apparaître derrière le contenu de la page. Vous pouvez également contrôler l'opacité du tampon, la rotation, la qualité, la taille et la position pour créer des effets de type filigrane.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_background_image_stamp(infile: str, image_file: str, outfile: str) -> None:
    """Add a rotated background image stamp with opacity and quality settings."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)
        stamp.is_background = True
        stamp.opacity = 0.35
        stamp.quality = 90
        stamp.rotation = 45.0
        stamp.set_image_size(160, 80)
        stamp.set_origin(200, 300)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Sujets liés aux façades

- [Travailler avec les façades PDF en Python](/pdf/fr/python-net/working-with-facades/)
- [Ajoutez des en-têtes, des pieds de page et des tampons avec PdfFileStamp](/pdf/fr/python-net/pdffilestamp-class/)
- [Ajouter un tampon de page aux fichiers PDF en Python](/pdf/fr/python-net/add-stamp/)
