---
title: Définir le nombre de cases du champ
type: docs
weight: 70
url: /fr/python-net/set-field-comb-number/
description: Cet exemple montre comment définir un nombre de comb pour un champ de formulaire PDF à l'aide d'Aspose.PDF for Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Définir le nombre de comb pour les champs de formulaire PDF en utilisant Python
Abstract: Avec Aspose.PDF for Python, les développeurs peuvent définir programmatiquement le nombre de cases (nombre de comb) pour un champ de formulaire afin d'imposer une saisie de longueur fixe. Cet article montre comment définir le nombre de comb pour un champ nommé "PIN".
---

Le nombre de comb définit la façon dont le contenu du champ est réparti en cases espacées de manière égale, souvent utilisé pour les codes PIN, les numéros de série ou d'autres champs de saisie à longueur fixe. Le code ouvre un PDF existant, définit le nombre de comb pour un champ, puis enregistre le document modifié.

Le [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) La classe fournit la méthode ‘set_field_comb_number’ pour définir le nombre de cases (caractères) dans un champ de formulaire.

1. Ouvrez un formulaire PDF existant.
1. Crée un objet FormEditor.
1. Définit le nombre de comb du champ nommé "PIN" à 5.
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


def set_field_comb_number(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field comb number to 5
    form_editor.set_field_comb_number("PIN", 5)

    # Save updated document
    form_editor.save(outfile)
```
