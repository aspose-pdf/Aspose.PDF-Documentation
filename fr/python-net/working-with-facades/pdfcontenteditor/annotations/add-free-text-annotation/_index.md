---
title: Ajouter des annotations de texte libre
type: docs
weight: 20
url: /fr/python-net/add-free-text-annotation/
description: Cet exemple charge un fichier PDF existant, ajoute une annotation de texte libre à la première page à une position définie, puis enregistre le document modifié.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter une annotation de texte libre à un PDF avec Python
Abstract: Cet exemple montre comment insérer une annotation de texte libre dans un document PDF en utilisant Aspose.PDF for Python via the Facades API. Il montre comment lier un PDF, définir le placement de l'annotation, ajouter du texte personnalisé et enregistrer le document mis à jour.
---

Les annotations de texte libre vous permettent de placer du texte visible directement sur une page PDF sans nécessiter de commentaires contextuels. En utilisant PdfContentEditor, vous pouvez spécifier le rectangle de l'annotation, le texte affiché et la page cible.

1. Créer le [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) objet.
1. Lier le PDF d'entrée.
1. Définir la position de l'annotation.
1. Ajoutez l'annotation de texte libre.
1. Enregistrer le Document mis à jour.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_free_text_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add free text annotation to page 1
    content_editor.create_free_text(
        apd.Rectangle(200, 480, 150, 25), "This is a free text annotation", 1
    )
    # Save updated document
    content_editor.save(outfile)
```
