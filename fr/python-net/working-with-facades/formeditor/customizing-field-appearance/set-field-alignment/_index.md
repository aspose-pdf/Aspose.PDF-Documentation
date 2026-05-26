---
title: Définir l'alignement du champ
type: docs
weight: 30
url: /fr/python-net/set-field-alignment/
description: Cet exemple montre comment définir l'alignement du texte d'un champ de formulaire dans un document PDF en utilisant Aspose.PDF for Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Définir l'alignement du texte pour les champs de formulaire PDF avec Python
Abstract: Cet article explique comment ouvrir un document PDF, définir l'alignement d'un champ spécifique à l'aide de la classe FormEditor, et enregistrer le PDF mis à jour. L'exemple définit l'alignement du texte d'un champ nommé "First Name" au centre.
---

Les champs de formulaire PDF nécessitent souvent un alignement de texte personnalisé pour maintenir une mise en page cohérente et professionnelle. En utilisant Aspose.PDF for Python, les développeurs peuvent définir de manière programmatique l'alignement du contenu texte d'un champ de formulaire.

Le [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) classe, en combinaison avec le [FormFieldFacade](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formfieldfacade/) constants, permet aux développeurs de modifier l'alignement des champs de formulaire existants par programme.

1. Ouvrez un document PDF existant.
1. Créer un objet FormEditor.
1. Définir l'alignement d'un champ nommé "First Name" au centre.
1. Enregistrez le document modifié.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_alignment(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field alignment to center
    if form_editor.set_field_alignment(
        "First Name", pdf_facades.FormFieldFacade.ALIGN_CENTER
    ):
        # Save updated document
        form_editor.save(outfile)
    else:
        raise Exception(
            "Failed to set field alignment. Field may not support alignment."
        )
```
