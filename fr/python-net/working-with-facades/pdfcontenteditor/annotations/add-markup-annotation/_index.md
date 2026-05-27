---
title: Ajouter des annotations de balisage
type: docs
weight: 30
url: /fr/python-net/add-markup-annotation/
description: Cet exemple lie un PDF d'entrée, ajoute quatre annotations de balisage différentes à la première page et enregistre le document mis à jour. Chaque annotation montre un style et une couleur de balisage différents.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter des annotations de surlignage, de soulignement, de rayure et d'ondulation dans un PDF avec Python
Abstract: Cet exemple montre comment ajouter plusieurs annotations de balisage — surlignage, soulignement, rayure et ondulation — à un document PDF à l'aide d'Aspose.PDF for Python via l'API Facades. L'exemple montre comment définir les zones d'annotation, spécifier les types de balisage, appliquer les couleurs et enregistrer le document modifié.
---

Les annotations de balisage sont utilisées pour mettre en évidence ou réviser du texte dans un PDF. Avec PdfContentEditor, vous pouvez appliquer programmétiquement différents styles de balisage en spécifiant une zone rectangulaire, le texte du commentaire, le type de balisage, le numéro de page et la couleur.

1. Créer le [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) objet.
1. Lier le PDF d'entrée.
1. Définir les rectangles d'annotation.
1. Ajouter des annotations de balisage.
1. Enregistrer le Document mis à jour.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_markup_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add markup annotation to page 1
    content_editor.create_markup(
        apd.Rectangle(120, 440, 200, 20),
        "This is a highlight annotation",
        0,
        1,
        apd.Color.yellow,
    )
    content_editor.create_markup(
        apd.Rectangle(110, 542, 200, 20),
        "This is a underline annotation",
        1,
        1,
        apd.Color.yellow,
    )
    content_editor.create_markup(
        apd.Rectangle(120, 568, 200, 20),
        "This is a strikeout annotation",
        2,
        1,
        apd.Color.orange_red,
    )
    content_editor.create_markup(
        apd.Rectangle(110, 598, 200, 20),
        "This is a squiggly annotation",
        3,
        1,
        apd.Color.dark_blue,
    )
    # Save updated document
    content_editor.save(outfile)
```
