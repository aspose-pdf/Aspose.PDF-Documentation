---
title: Ajouter un élément de liste
type: docs
weight: 10
url: /fr/python-net/add-list-item/
description: Cet exemple démontre comment ajouter des éléments à un champ de zone de liste dans un document PDF en utilisant Aspose.PDF for Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter des éléments aux champs de zone de liste PDF à l'aide de Python
Abstract: Cet article montre comment ouvrir un document PDF, ajouter des éléments à un champ de zone de liste nommé "Country", et enregistrer le document mis à jour.
---

Les champs de zone de liste dans les PDF permettent aux utilisateurs de sélectionner une ou plusieurs options parmi un ensemble prédéfini. En utilisant Aspose.PDF for Python, les développeurs peuvent ajouter de nouveaux éléments à ces champs de manière programmatique. Le [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) La classe fournit la méthode ‘add_list_item’ pour ajouter des éléments à un champ de zone de liste existant.

1. Ouvrez un formulaire PDF existant.
1. Créer un objet FormEditor.
1. Lier le PDF au FormEditor.
1. Ajouter des éléments au champ de zone de liste "Country".
1. Enregistrez le document mis à jour.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_list_item(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Add list item to list box field
    form_editor.add_list_item("Country", ["New Zealand", "New Zealand"])
    # Save updated document
    form_editor.save(outfile)
```
