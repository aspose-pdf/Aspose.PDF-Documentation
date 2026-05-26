---
title: Ajouter des annotations contextuelles
type: docs
weight: 40
url: /fr/python-net/add-popup-annotation/
description: Cet exemple charge un PDF, ajoute une annotation contextuelle à la première page et enregistre le document modifié. L'annotation contextuelle est définie comme visible par défaut et affiche le texte de commentaire spécifié.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter des annotations contextuelles à un PDF en utilisant Python
Abstract: Cet exemple montre comment insérer une annotation contextuelle dans un document PDF en utilisant Aspose.PDF for Python via l'API Facades. Il explique comment définir la zone de l'annotation, définir le texte de l'annotation, contrôler la visibilité et enregistrer le document mis à jour.
---

Les annotations contextuelles sont utiles pour ajouter des commentaires, des explications ou des notes interactives dans les fichiers PDF. En utilisant [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), vous pouvez créer des annotations contextuelles programmatiquement en spécifiant l'emplacement, le contenu, la visibilité et le numéro de page.

1. Créer l'objet PdfContentEditor.
1. Lier le PDF d'entrée.
1. Définir le rectangle de l'annotation Popup.
1. Ajouter l'annotation Popup.
1. Enregistrer le Document mis à jour.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_popup_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add popup annotation to page 1
    content_editor.create_popup(
        apd.Rectangle(220, 520, 180, 80),
        "This is a popup annotation",
        True,
        1,
    )
    # Save updated document
    content_editor.save(outfile)
```
