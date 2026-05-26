---
title: Ajouter un lien d'application
type: docs
weight: 10
url: /fr/python-net/add-application-link/
description: Cet exemple lie un PDF d'entrée, ajoute un lien de lancement d'application sur la première page et enregistre le document modifié.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter un lien de lancement d'application à un PDF en utilisant PdfContentEditor en Python
Abstract: Cet exemple montre comment ajouter un lien de lancement d'application à un document PDF en utilisant Aspose.PDF for Python via l'API Facades. Il montre comment créer une zone cliquable qui ouvre une application spécifiée lorsqu'elle est cliquée, et enregistrer le PDF mis à jour.
---

PDF peut inclure des éléments interactifs tels que des liens qui lancent des applications externes. Using [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), vous pouvez définir une région rectangulaire sur une page qui, lorsqu'elle est cliquée, ouvre un fichier exécutable spécifique.

1. Créer une instance de PdfContentEditor.
1. Lier le document PDF d'entrée.
1. Définir une zone rectangulaire pour le lien cliquable.
1. Spécifiez le chemin de l'application à lancer.
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


def add_application_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add application launch link
    content_editor.create_application_link(
        apd.Rectangle(180, 530, 260, 20),
        "notepad.exe",
        1,
        apd.Color.purple,
    )
    # Save updated document
    content_editor.save(outfile)
```
