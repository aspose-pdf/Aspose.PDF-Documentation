---
title: Définir la limite du champ
type: docs
weight: 80
url: /fr/python-net/set-field-limit/
description: Cet exemple montre comment définir une limite maximale de caractères pour un champ de formulaire dans un document PDF à l'aide d'Aspose.PDF for Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Définir la limite maximale de caractères pour les champs de formulaire PDF en utilisant Python
Abstract: Cet exemple démontre la définition de la limite de caractères pour un champ nommé "Last Name" à 10 caractères, garantissant que les utilisateurs ne peuvent pas saisir plus que la limite spécifiée.
---

Les champs de formulaire dans les documents PDF peuvent nécessiter des restrictions d'entrée pour maintenir un formatage correct. En utilisant Aspose.PDF for Python, les développeurs peuvent définir programmatique une longueur maximale de caractères pour un champ.

Le [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) La classe fournit la méthode 'set_field_limit' pour définir la longueur maximale d'entrée pour un champ.

1. Ouvrez un formulaire PDF existant.
1. Créer un objet FormEditor.
1. Définissez la limite maximale de caractères pour le champ "Last Name".
1. Enregistrez le PDF mis à jour.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_limit(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field limit to 10
    if not form_editor.set_field_limit("Last Name", 10):
        raise Exception(
            "Failed to set field limit. Field may not support specified limit."
        )

    # Save updated document
    form_editor.save(outfile)
```
