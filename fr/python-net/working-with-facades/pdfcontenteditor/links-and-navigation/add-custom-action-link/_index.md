---
title: Ajouter un lien d'action personnalisé
type: docs
weight: 20
url: /fr/python-net/add-custom-action-link/
description: Cet exemple lie un PDF d'entrée, ajoute un lien d'action personnalisé sur la première page et enregistre le document modifié. Une liste d'actions vide est utilisée pour simplifier, mais les implémentations réelles peuvent inclure des actions réelles.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter un lien d'action personnalisé à un PDF en utilisant PdfContentEditor en Python
Abstract: Cet exemple montre comment ajouter un lien d'action personnalisé à un document PDF en utilisant Aspose.PDF for Python via l'API Facades. Il montre comment créer une zone cliquable sur une page, affecter une action personnalisée et enregistrer le document mis à jour.
---

Les liens d'action personnalisés vous permettent de définir des zones interactives dans un PDF pouvant déclencher des actions spécifiques lorsqu'elles sont cliquées, comme exécuter des scripts, naviguer entre les pages ou exécuter des commandes spécifiques à l'application. En utilisant [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), vous pouvez créer un lien d'action personnalisé en spécifiant la page, le rectangle, la couleur et les actions.

1. Créer une instance de PdfContentEditor.
1. Lier le document PDF d'entrée.
1. Définir un rectangle pour le lien cliquable.
1. Spécifier le numéro de page et la couleur du lien.
1. Attribuer des actions personnalisées (vide dans cet exemple).
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


def add_custom_action_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add custom action link. Empty action list keeps the sample runnable
    # without requiring additional enum lookups.
    content_editor.create_custom_action_link(
        apd.Rectangle(200, 500, 260, 20),
        1,
        apd.Color.dark_red,
        [],
    )
    # Save updated document
    content_editor.save(outfile)
```
