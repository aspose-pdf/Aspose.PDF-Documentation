---
title: Obtenir l'apparence du champ
type: docs
weight: 20
url: /fr/python-net/get-field-appearance/
description: Cet article explique comment ouvrir un PDF, accéder à un champ de formulaire, récupérer ses paramètres d'apparence et les afficher. L'exemple montre la récupération de l'apparence d'un champ nommé "Last Name".
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Récupérer l'apparence du champ de formulaire PDF à l'aide de Python
Abstract: Cet exemple montre comment récupérer les propriétés d'apparence visuelle d'un champ de formulaire dans un document PDF à l'aide d'Aspose.PDF for Python. Le code ouvre un PDF existant, accède à un champ de formulaire spécifique et imprime les détails de son apparence, y compris la couleur d'arrière-plan, la couleur du texte, la couleur de la bordure et l'alignement.
---

Les champs de formulaire dans les documents PDF possèdent des propriétés visuelles telles que la couleur d'arrière-plan, la couleur du texte, la couleur de la bordure et l'alignement. Avec Aspose.PDF for Python, les développeurs peuvent inspecter ces paramètres d'apparence de manière programmatique en utilisant le [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) classe.

1. Ouvrez un document PDF existant.
1. Créer un objet FormEditor.
1. Récupérer les informations d'apparence d'un champ spécifique.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_field_appearance(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Get field appearance
    appearance = form_editor.get_field_appearance("Last Name")
    print("Field Appearance: " + str(appearance))
```
