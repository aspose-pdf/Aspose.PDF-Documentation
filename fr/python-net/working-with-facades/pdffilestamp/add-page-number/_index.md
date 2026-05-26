---
title: Ajouter le numéro de page au PDF
type: docs
weight: 30
url: /fr/python-net/page-number/
description: Apprenez comment ajouter des numéros de page aux documents PDF en utilisant PdfFileStamp en Python.
lastmod: "2026-05-22"
TechArticle: true
AlternativeHeadline: Ajouter des numéros de page au PDF en Python
Abstract: Cet article explique comment ajouter des numéros de page aux documents PDF avec Aspose.PDF for Python via .NET en utilisant la façade PdfFileStamp. Il montre comment ajouter des numéros de page avec le placement par défaut, les positionner à des coordonnées personnalisées et contrôler l’alignement et les marges.
---

Aspose.PDF for Python via .NET fournit le [PdfFileStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) façade pour ajouter du contenu répété aux pages PDF. Vous pouvez l'utiliser pour insérer des numéros de page avec un placement par défaut, les positionner à des coordonnées spécifiques, ou contrôler leur alignement et leurs marges.

## Ajouter des numéros de page avec le placement par défaut

Utiliser `add_page_number()` sans arguments de position supplémentaires lorsque vous souhaitez que les numéros de page soient ajoutés à l'emplacement par défaut. C'est la façon la plus simple de numéroter chaque page du document.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_page_numbers_default(infile: str, outfile: str) -> None:
    """Add centered page numbers to the bottom of each page."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_page_number("Page #")
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Ajouter des numéros de page à des coordonnées personnalisées

Utilisez la surcharge basée sur les coordonnées lorsque vous avez besoin que les numéros de page apparaissent à une position X et Y spécifiques sur chaque page. Cette approche est utile lorsque la mise en page du document nécessite un placement personnalisé.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_page_numbers_at_coordinates(infile: str, outfile: str) -> None:
    """Add page numbers at explicit X/Y coordinates."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_page_number("Page #", 300, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Ajouter des numéros de page avec alignement et marges

Utilisez la surcharge avec les arguments de position et de marge lorsque vous avez besoin de plus de contrôle sur l'emplacement des numéros de page. Dans cet exemple, les numéros sont alignés dans la zone supérieure droite de la page avec des marges explicites.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_page_numbers_with_position_and_margins(infile: str, outfile: str) -> None:
    """Add page numbers using a predefined position and page margins."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_page_number(
            "Page #",
            pdf_facades.PdfFileStamp.POS_BOTTOM_RIGHT,
            10,
            10,
            10,
            10,
        )
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Ajouter des numéros de page au style romain

La fonction 'add_page_numbers_with_roman_style' montre comment améliorer un document PDF en ajoutant des numéros de page utilisant des chiffres romains majuscules. Elle exploite la classe PdfFileStamp d'Aspose.PDF pour appliquer une numérotation cohérente sur toutes les pages.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_page_numbers_with_roman_style(infile: str, outfile: str) -> None:
    """Add page numbers with a custom start value and Roman numbering."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.numbering_style = ap.NumberingStyle.NUMERALS_ROMAN_UPPERCASE
        pdf_stamper.starting_number = 42
        pdf_stamper.add_page_number("Page #", pdf_facades.PdfFileStamp.POS_UPPER_RIGHT)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```
