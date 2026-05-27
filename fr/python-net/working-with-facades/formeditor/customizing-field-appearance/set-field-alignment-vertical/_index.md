---
title: Définir l'alignement vertical du champ
type: docs
weight: 40
url: /fr/python-net/set-field-alignment-vertical/
description: Cet exemple montre comment définir l'alignement vertical d'un champ de formulaire dans un document PDF à l'aide d'Aspose.PDF for Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Définir l'alignement vertical pour les champs de formulaire PDF à l'aide de Python
Abstract: Cet article explique comment ouvrir un PDF, définir l'alignement vertical d'un champ à l'aide de la classe FormEditor, et enregistrer le PDF mis à jour. L'exemple définit l'alignement vertical d'un champ nommé "First Name" au bas de la zone du champ.
---

Les champs de formulaire PDF peuvent contenir du texte qui nécessite un alignement vertical approprié pour une apparence cohérente et professionnelle. En utilisant Aspose.PDF for Python, les développeurs peuvent modifier programmétiquement l'alignement vertical des champs de formulaire.
L'alignement vertical permet aux développeurs de contrôler si le texte du champ apparaît en haut, au centre ou en bas de la boîte englobante du champ, améliorant ainsi la mise en page et la lisibilité des données du formulaire.

En utilisant le [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) classe et le [FormFieldFacade](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formfieldfacade/) constantes, les développeurs peuvent ajuster l'alignement vertical par programme pour obtenir une disposition de formulaire cohérente:

1. Ouvrez un document PDF existant.
1. Créer un objet FormEditor.
1. Définissez l'alignement vertical d'un champ nommé "First Name" en bas.
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


def set_field_alignment_vertical(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Attempt to set vertical alignment of the "First Name" field to bottom
    if form_editor.set_field_alignment_v(
        "First Name", pdf_facades.FormFieldFacade.ALIGN_BOTTOM
    ):
        # Save updated document
        form_editor.save(outfile)
    else:
        raise Exception(
            "Failed to set field vertical alignment. Field may not support vertical alignment."
        )
```
