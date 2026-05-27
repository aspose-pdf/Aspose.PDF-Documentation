---
title: Copier le champ interne
type: docs
weight: 20
url: /fr/python-net/copy-inner-field/
description: Copier les champs de formulaire PDF vers une nouvelle position en utilisant Python avec Aspose.PDF for Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Copier les champs de formulaire PDF vers une nouvelle position en utilisant Python
Abstract: Cet exemple montre comment copier un champ de formulaire existant vers une nouvelle position dans un document PDF en utilisant Aspose.PDF for Python. Le code ouvre un PDF, duplique un champ à une page et des coordonnées spécifiées, puis enregistre le document mis à jour.
---

Les formulaires PDF nécessitent souvent de dupliquer des champs tout en conservant le formatage et le comportement d'origine. En utilisant Aspose.PDF for Python, les développeurs peuvent copier un champ existant vers une nouvelle position sur la même page ou une autre page de manière programmatique.

Cet article explique comment copier un champ nommé 'First Name' vers un nouveau champ appelé 'First Name Copy' sur la page 2 à des coordonnées spécifiques (x=200, y=600), en produisant un PDF avec le champ nouvellement positionné.

1. Ouvrez un formulaire PDF existant.
1. Créer un objet FormEditor.
1. Liez le document PDF au FormEditor.
1. Copiez le champ 'First Name' vers un nouveau champ 'First Name Copy' sur la page 2 aux coordonnées (200, 600).
1. Enregistrez le document mis à jour.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def copy_inner_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Copies an existing field to a new position specified by both page number and ordinates.
    # A new document will be produced, which contains everything the source document has except for the newly copied field.
    form_editor.copy_inner_field("First Name", "First Name Copy", 2, 200, 600)
    # Save updated document
    form_editor.save(outfile)
```

**Veuillez noter :**

La signature de la méthode 'copy_inner_field' ressemble à ceci :

```python
copy_inner_field(original_field_name, new_field_name, page_number, x, y)
```

- 'original_field_name' – le champ que vous souhaitez dupliquer.
- 'new_field_name' – le nom du nouveau champ.
- 'page_number' – la page sur laquelle le nouveau champ apparaîtra.
- x, y – coordonnées sur cette page.

Le page_number doit être un entier positif correspondant à une page existante du PDF (indexation à partir de 1).

Si vous passez un paramètre négatif, par ex. :

```python
form_editor.copy_inner_field("First Name", "First Name Copy", -1, 200, 600)
```

Le programme réinitialisera alors aux paramètres précédents.
