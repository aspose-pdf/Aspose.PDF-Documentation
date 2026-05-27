---
title: Ajouter une annotation de ligne
type: docs
weight: 30
url: /fr/python-net/add-line-annotation/
description: Cet exemple lie un PDF d'entrée, dessine une annotation de ligne rouge avec des terminaisons de ligne carrées, et enregistre le PDF modifié.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter une annotation de ligne à un PDF en utilisant PdfContentEditor en Python
Abstract: Cet exemple montre comment ajouter une annotation de ligne à un document PDF en utilisant Aspose.PDF for Python via l'API Facades. Il explique comment définir les points de départ et d'arrivée de la ligne, les limites du rectangle, les propriétés d'apparence, et enregistrer le document mis à jour.
---

Les annotations de ligne sont utiles pour souligner du texte, mettre en évidence des relations, ou attirer l'attention sur des zones spécifiques d'un PDF. Avec [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), vous pouvez créer programmétiquement des annotations de ligne en spécifiant les points de départ et d'arrivée, le rectangle de délimitation, la couleur, le style de bordure, et les terminaisons de ligne.

1. Créer l'objet PdfContentEditor.
1. Lier le PDF d'entrée.
1. Définir les propriétés de l'annotation de ligne.
1. Ajouter l'annotation de ligne.
1. Enregistrer le Document mis à jour.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_line_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    # Create LineAnnotation object
    rect = apd.Rectangle(100, 100, 200, 200)
    contents = "This is line annotation"
    content_editor.create_line(
        rect,
        contents,
        100,
        100,
        200,
        200,
        1,
        1,
        apd.Color.red,
        "Solid",
        [3, 2],
        ["Square"],
    )

    # Save output PDF file
    content_editor.save(outfile)
```
