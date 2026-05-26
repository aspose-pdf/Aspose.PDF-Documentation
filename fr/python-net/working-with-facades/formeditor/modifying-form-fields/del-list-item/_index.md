---
title: Supprimer l'élément de la liste
type: docs
weight: 40
url: /fr/python-net/del-list-item/
description:
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Supprimer des éléments des champs de zone de liste PDF avec Python
Abstract: Cet exemple montre comment supprimer un élément d'un champ de formulaire de zone de liste dans un document PDF à l'aide d'Aspose.PDF for Python. Le code ouvre un PDF existant, supprime un élément spécifique d'un champ de zone de liste et enregistre le document mis à jour.
---

Les champs de zone de liste dans les PDF permettent aux utilisateurs de sélectionner une ou plusieurs options pré‑définies. Avec Aspose.PDF for Python, les développeurs peuvent supprimer programmatiquement des éléments de ces champs.

Cet article explique comment supprimer l'élément « UK » d'un champ de zone de liste nommé « Country », en veillant à ce que le champ ne contienne que les options souhaitées.

Le [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) La classe fournit la méthode « del_list_item » pour supprimer un élément spécifique d'un champ de zone de liste.

1. Ouvrez un formulaire PDF existant.
1. Créer un objet FormEditor.
1. Liez le document PDF au FormEditor.
1. Supprimez l'élément "UK" de la zone de liste "Country".
1. Enregistrez le document mis à jour.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def del_list_item(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Delete list item from list box field
    form_editor.del_list_item("Country", "UK")
    # Save updated document
    form_editor.save(outfile)
```

