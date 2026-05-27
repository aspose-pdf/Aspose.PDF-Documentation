---
title: Ajouter un lien local
type: docs
weight: 40
url: /fr/python-net/add-local-link/
description: Cet exemple lie un PDF d'entrée, ajoute un lien local de couleur rouge sur la page 1 qui pointe vers la page 1, puis enregistre le document modifié.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter un lien local à un PDF en utilisant PdfContentEditor en Python
Abstract: Cet exemple montre comment ajouter un lien local à un document PDF en utilisant Aspose.PDF pour Python via l'API Facades. Il montre comment créer une zone cliquable qui mène à une autre page du même PDF et enregistrer le document mis à jour.
---

Les liens locaux dans les PDF permettent une navigation rapide entre les pages du même document. En utilisant [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), vous pouvez définir un rectangle cliquable qui relie une page à une autre, améliorant la convivialité et la navigation du document.

1. Créer une instance de PdfContentEditor.
1. Lier le document PDF d'entrée.
1. Définissez un rectangle pour le lien local cliquable.
1. Spécifiez la page source et la page de destination.
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


def add_local_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add a local link on page 1 to destination page 1
    content_editor.create_local_link(
        apd.Rectangle(120, 620, 220, 20),
        1,
        1,
        apd.Color.red,
    )
    # Save updated document
    content_editor.save(outfile)
```
