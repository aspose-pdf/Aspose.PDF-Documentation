---
title: Ajouter un lien de document PDF
type: docs
weight: 50
url: /fr/python-net/add-pdf-document-link/
description: Cet exemple lie un PDF d'entrée, ajoute un lien de couleur verte vers une page dans un autre PDF, et enregistre le document modifié.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter un lien de document PDF en utilisant PdfContentEditor en Python
Abstract: Cet exemple montre comment ajouter un lien vers un autre document PDF en utilisant Aspose.PDF for Python via the Facades API. Il montre comment créer une zone cliquable qui ouvre un PDF différent et enregistrer le document mis à jour.
---

Les liens de documents PDF permettent aux utilisateurs de naviguer d'un PDF à un autre de manière fluide. Using [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), vous pouvez définir un rectangle cliquable qui pointe vers une page d'un fichier PDF différent, rendant vos documents interactifs et connectés.

1. Créer une instance de PdfContentEditor.
1. Lier le document PDF d'entrée.
1. Définir un rectangle pour le lien cliquable.
1. Spécifiez le fichier PDF lié, la page source et la page de destination.
1. Définir la couleur du lien.
1. Enregistrer le document PDF mis à jour.

```python
import aspose.pdf.facades as pdf_facades
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as apd
import aspose.pdf as ap

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_pdf_document_link(infile, linked_pdf, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add link to another PDF document
    content_editor.create_pdf_document_link(
        apd.Rectangle(140, 590, 240, 20),
        linked_pdf,
        1,
        1,
        apd.Color.green,
    )
    # Save updated document
    content_editor.save(outfile)
```
