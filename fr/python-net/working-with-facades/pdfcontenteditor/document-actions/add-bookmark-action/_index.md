---
title: Ajouter une action de signet
type: docs
weight: 10
url: /fr/python-net/add-bookmark-action/
description: Cet exemple lie un PDF d'entrée, crée un signet libellé "PdfContentEditor Bookmark" qui navigue vers la page 1, puis enregistre le document mis à jour.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Créer un signet avec une action de navigation dans un PDF en utilisant Python
Abstract: Cet exemple montre comment ajouter un signet avec une action de navigation à un document PDF en utilisant Aspose.PDF for Python via l'API Facades. Il montre comment configurer le texte du signet, son apparence et une action qui dirige les utilisateurs vers une page spécifique.
---

Les signets offrent une navigation rapide au sein des documents PDF. En utilisant [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), vous pouvez créer programmétiquement des signets et attribuer des actions telles que la navigation vers une page. Vous pouvez également personnaliser l'apparence du signet, y compris les options de couleur et de style comme gras ou italique.

1. Créer l'objet PdfContentEditor.
1. Lier le PDF d'entrée.
1. Définir les propriétés du signet.
1. Attribuer une action au signet.
1. Enregistrer le Document mis à jour.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_bookmark_action(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add a bookmark action to navigate to page 1
    content_editor.create_bookmarks_action(
        "PdfContentEditor Bookmark",
        apd.Color.blue,
        True,
        False,
        "",
        "GoTo",
        "1",
    )
    # Save updated document
    content_editor.save(outfile)
```