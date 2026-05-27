---
title: Ajouter une annotation caret
type: docs
weight: 10
url: /fr/python-net/add-caret-annotation/
description: Cet exemple charge un PDF existant, ajoute une annotation caret à la première page et enregistre le document modifié. L'annotation comprend un symbole caret rouge et un texte de commentaire descriptif.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter une annotation caret à un PDF en utilisant Python
Abstract: Cet exemple montre comment ajouter une annotation caret à un document PDF en utilisant Aspose.PDF for Python via the Facades API. L'exemple montre comment lier un fichier PDF, définir le placement de l'annotation à l'aide de rectangles, configurer les propriétés du caret et enregistrer le document mis à jour.
---

Les annotations caret sont couramment utilisées pour indiquer des insertions de texte ou des commentaires éditoriaux dans un document. Avec PdfContentEditor, vous pouvez ajouter des annotations caret de manière programmatique en spécifiant le numéro de page, les limites de l'annotation, la zone d'appel, le symbole, le texte de la note et la couleur.

1. Créer le [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) objet.
1. Lier le PDF d'entrée.
1. Définir les paramètres de l'annotation Caret :
  - Numéro de page où l'annotation sera ajoutée
  - Rectangle Caret (position de l'annotation)
  - Rectangle d'appel (zone de texte)
  - Symbole (par exemple "P")
  - Texte d'annotation
  - Couleur d'annotation
1. Ajouter l'annotation Caret.
1. Enregistrer le Document mis à jour.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_caret_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add caret annotation to page 1
    content_editor.create_caret(
        1,
        apd.Rectangle(350, 400, 10, 10),
        apd.Rectangle(300, 380, 115, 15),
        "P",
        "This is a caret annotation",
        apd.Color.red,
    )
    # Save updated document
    content_editor.save(outfile)
```
