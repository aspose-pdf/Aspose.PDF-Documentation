---
title: Définir l'apparence du champ
type: docs
weight: 50
url: /fr/python-net/set-field-appearance/
description: Cet exemple montre comment modifier l'apparence visuelle d'un champ de formulaire PDF à l'aide d'Aspose.PDF for Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Définir l'apparence du champ de formulaire PDF à l'aide de Python
Abstract: Cet article explique comment ouvrir un PDF, définir l'apparence d'un champ de formulaire à l'aide de la classe FormEditor, et enregistrer le document mis à jour. L'exemple définit l'apparence d'un champ nommé "First Name" comme invisible en utilisant le drapeau AnnotationFlags.INVISIBLE.
---

Les champs de formulaire PDF prennent en charge des drapeaux d'apparence qui contrôlent la visibilité, l'impression et l'interactivité. Avec Aspose.PDF for Python, les développeurs peuvent modifier ces drapeaux de manière programmatique pour des champs de formulaire spécifiques.

En utilisant le [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) classe, les développeurs peuvent modifier ces drapeaux pour masquer, afficher ou personnaliser le comportement des champs de formulaire dans un PDF interactif.

1. Ouvrez un document PDF existant.
1. Créer un objet FormEditor.
1. Définissez l'apparence du champ nommé "First Name" sur invisible.
1. Enregistrez le document mis à jour.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_appearance(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field appearance to invisible
    if not form_editor.set_field_appearance(
        "First Name", ap.annotations.AnnotationFlags.INVISIBLE
    ):
        raise Exception(
            "Failed to set field appearance. Field may not support appearance flags."
        )

    # Save updated document
    form_editor.save(outfile)
```
