---
title: Ajouter des annotations de texte
type: docs
weight: 50
url: /fr/python-net/add-text-annotation/
description: Ajoutez des annotations de texte à un document PDF en utilisant la classe PdfContentEditor dans Aspose.PDF for Python via .NET.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter des annotations de texte en Python
Abstract: Apprenez comment ajouter des annotations de texte à un document PDF en utilisant la classe PdfContentEditor dans Aspose.PDF for Python via .NET. Cet exemple montre comment placer une annotation de texte à une position spécifique, définir son titre et son contenu, puis enregistrer le fichier PDF mis à jour.
---

Cet article montre comment ajouter une annotation de texte à un document PDF en utilisant le [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) classe dans Aspose.PDF.

Les annotations de texte vous permettent d’ajouter des commentaires, des notes ou des informations supplémentaires à des parties spécifiques d’une page PDF. Ces annotations peuvent apparaître sous forme d’icônes et être développées par les utilisateurs lors de la visualisation du document.

Dans cet exemple :

- Un document PDF est chargé dans le PdfContentEditor.
- Une annotation de texte est ajoutée à une position spécifique sur la page.
- L'annotation comprend un titre, un contenu, un type d’icône et des paramètres de visibilité.
- Le document modifié est enregistré dans un nouveau fichier.

1. Créer un objet PdfContentEditor.
1. Lier le Document PDF d'entrée.
1. Définir la position de l'annotation.
1. Ajouter une annotation Text.
1. Enregistrer le PDF mis à jour.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_text_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add text annotation to page 1
    content_editor.create_text(
        apd.Rectangle(100, 400, 50, 50),
        "Text Annotation",
        "This is a text annotation",
        True,
        "Insert",
        1,
    )
    # Save updated document
    content_editor.save(outfile)
```
