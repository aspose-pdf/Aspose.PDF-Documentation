---
title: Ajouter un lien Web
type: docs
weight: 60
url: /fr/python-net/add-web-link/
description: Cet exemple lie un PDF d’entrée, ajoute une annotation de lien web bleu sur la page 1 pointant vers la page produit Python PDF d’Aspose, et enregistre le document modifié.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter un lien Web à un PDF en utilisant PdfContentEditor en Python
Abstract: Cet exemple montre comment ajouter un lien web à un document PDF en utilisant Aspose.PDF for Python via l’API Facades. Il montre comment créer une zone cliquable sur une page qui ouvre une URL spécifiée dans un navigateur Web et enregistrer le document mis à jour.
---

Les liens web dans les PDF permettent aux utilisateurs de naviguer directement vers des ressources en ligne, des sites Web ou de la documentation. En utilisant [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), vous pouvez définir une zone rectangulaire sur une page PDF qui, lorsqu’elle est cliquée, ouvre une URL dans le navigateur Web par défaut.

1. Créer une instance de PdfContentEditor.
1. Lier le document PDF d'entrée.
1. Définissez un rectangle pour le lien web cliquable.
1. Spécifiez l'URL, le numéro de page et la couleur du lien.
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


def add_web_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add a web link annotation to page 1
    content_editor.create_web_link(
        apd.Rectangle(100, 650, 200, 20),
        "https://products.aspose.com/pdf/python-net/",
        1,
        apd.Color.blue,
    )
    # Save updated document
    content_editor.save(outfile)
```
