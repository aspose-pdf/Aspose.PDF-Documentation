---
title: Ajouter un lien JavaScript
type: docs
weight: 30
url: /fr/python-net/add-javascript-link/
description: Cet exemple lie un PDF d'entrée, ajoute un lien JavaScript qui déclenche une alerte au clic, et enregistre le document modifié.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter un lien JavaScript à un PDF en utilisant PdfContentEditor en Python
Abstract: Cet exemple montre comment ajouter un lien JavaScript à un document PDF en utilisant Aspose.PDF for Python via l'API Facades. Il montre comment créer une zone cliquable qui exécute du code JavaScript lorsqu'elle est cliquée, et enregistrer le PDF mis à jour.
---

Les liens JavaScript dans les PDF offrent des fonctionnalités interactives telles que l'affichage d'alertes, l'exécution de calculs ou la modification dynamique du contenu du document. En utilisant [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), vous pouvez définir un rectangle cliquable sur une page et l'associer à du code JavaScript personnalisé.

1. Créer une instance de PdfContentEditor.
1. Lier le document PDF d'entrée.
1. Définissez un rectangle pour le lien JavaScript cliquable.
1. Spécifier le numéro de page et la couleur du lien.
1. Attribuez le code JavaScript à exécuter lorsqu'il est cliqué.
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


def add_javascript_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add JavaScript link action
    content_editor.create_java_script_link(
        "app.alert('PdfContentEditor JavaScript link');",
        apd.Rectangle(160, 560, 260, 20),
        1,
        apd.Color.orange,
    )
    # Save updated document
    content_editor.save(outfile)
```
