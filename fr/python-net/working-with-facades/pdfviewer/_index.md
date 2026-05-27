---
title: Classe PdfViewer
type: docs
weight: 135
url: /fr/python-net/pdfviewer-class/
description: Apprenez à utiliser la classe PdfViewer dans Aspose.PDF for Python via .NET pour décoder toutes les pages PDF, décoder une page spécifique et inspecter les métadonnées PDF liées au visualiseur.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Décoder les pages PDF et inspecter les données du visualiseur en Python avec PdfViewer
Abstract: Cet article explique comment utiliser la façade PdfViewer dans Aspose.PDF for Python via .NET pour le décodage de pages et les tâches d'inspection liées au visualiseur. Apprenez à décoder toutes les pages PDF, à rendre une page spécifique et à inspecter des propriétés telles que le nombre de pages, le type de coordonnées et la résolution.
---

Aspose.PDF for Python via .NET fournit le [PdfViewer](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfviewer/) façade pour travailler avec la visualisation de PDF et les scénarios de décodage de pages. Un cas d'utilisation courant consiste à convertir des pages PDF en objets image qui peuvent ensuite être enregistrés sur le disque.

## Créer un assistant PdfViewer réutilisable

Avant de décoder les pages ou de lire les propriétés liées au visualiseur, créez un petit assistant qui initialise et renvoie un `PdfViewer` instance. Cela rend les exemples ci-dessous autonomes et clarifie comment l'objet viewer est créé avant d'être lié à un document PDF.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades


def _create_viewer() -> pdf_facades.PdfViewer:
    """Create a PdfViewer configured for decoding examples."""
    viewer = pdf_facades.PdfViewer()
    viewer.coordinate_type = ap.PageCoordinateType.MEDIA_BOX
    viewer.resolution = 150
    viewer.scale_factor = 1.0
    viewer.show_hidden_areas = False
    return viewer
```

## Décoder toutes les pages du PDF

Utiliser `decode_all_pages()` lorsque vous souhaitez convertir chaque page du PDF en une image distincte. Les images de page renvoyées peuvent ensuite être enregistrées une par une dans un répertoire de sortie.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def decode_all_pages(infile: str, output_dir: str) -> None:
    """Decode all pages of a PDF document into image files."""
    viewer = _create_viewer()
    try:
        viewer.open_pdf_file(infile)
        decoded_pages = viewer.decode_all_pages()

        for index, page_image in enumerate(decoded_pages, start=1):
            image_path = path.join(output_dir, f"decode_all_pages_{index}.png")
            page_image.save(image_path)
    finally:
        viewer.close_pdf_file()
```

## Décoder une page PDF spécifique

Utiliser `decode_page()` Lorsque vous avez besoin d'une seule page du document. Cela est utile lors de la génération d'aperçus, de miniatures ou d'exportations spécifiques à une page.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def decode_specific_page(infile: str, outfile: str, page_number: int = 1) -> None:
    """Decode a specific PDF page into an image file."""
    viewer = _create_viewer()
    try:
        viewer.bind_pdf(infile)
        page_image = viewer.decode_page(page_number)
        page_image.save(outfile)

    finally:
        viewer.close()
```

## Inspecter les métadonnées PDF

Le `inspect_pdf_metadata` La fonction montre comment ouvrir un document PDF et récupérer les métadonnées de base liées au visualiseur en utilisant Aspose.PDF. Elle se concentre sur l'extraction d'informations qui décrivent comment le document est interprété et affiché plutôt que son contenu.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def inspect_pdf_metadata(infile: str) -> None:
    """Open a PDF and print page-count related viewer metadata."""
    viewer = _create_viewer()
    try:
        viewer.open_pdf_file(infile)
        print(f"Page count: {viewer.page_count}")
        print(f"Coordinate type: {viewer.coordinate_type}")
        print(f"Resolution: {viewer.resolution}")
    finally:
        viewer.close_pdf_file()
```
