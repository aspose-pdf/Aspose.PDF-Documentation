---
title: Ajouter une annotation carrée
type: docs
weight: 60
url: /fr/python-net/add-square-annotation/
description: Cet exemple lie un PDF d'entrée, ajoute une annotation carrée remplie en bleu sur la première page et enregistre le document modifié.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter une annotation carrée à un PDF à l'aide de PdfContentEditor en Python
Abstract: Cet exemple montre comment ajouter une annotation carrée à un document PDF en utilisant Aspose.PDF for Python via l'API Facades. Il montre comment définir le rectangle de l'annotation, le texte du contenu, la couleur, les options de remplissage et enregistrer le document mis à jour.
---

Les annotations carrées sont couramment utilisées pour mettre en évidence des zones d'intérêt, marquer des sections importantes ou fournir des repères visuels dans un document PDF. En utilisant [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), vous pouvez créer des annotations carrées (ou circulaires) en spécifiant le rectangle englobant, le texte du contenu, la couleur de la bordure, l'option de remplissage, le numéro de page et la largeur de la bordure.

1. Créer l'objet PdfContentEditor.
1. Lier le PDF d'entrée.
1. Définir l'annotation Square.
1. Ajouter l'annotation Square.
1. Enregistrer le Document mis à jour.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_square_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    # Create SquareAnnotation object
    rect = apd.Rectangle(100, 300, 200, 400)
    contents = "This is square annotation"
    content_editor.create_square_circle(rect, contents, apd.Color.blue, True, 1, 3)

    # Save output PDF file
    content_editor.save(outfile)
```
