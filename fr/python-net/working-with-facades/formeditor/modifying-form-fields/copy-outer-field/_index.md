---
title: Copier le champ externe
type: docs
weight: 30
url: /fr/python-net/copy-outer-field/
description: Cet exemple montre comment copier un champ de formulaire d’un document PDF à un autre en utilisant Aspose.PDF for Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Copier les champs de formulaire PDF d’un autre document en utilisant Python
Abstract: Cet article explique comment créer un nouveau document PDF, copier le champ "First Name" du PDF source vers la page 1 aux coordonnées (200, 600), et enregistrer le document cible mis à jour.
---

Parfois, les formulaires PDF nécessitent la réutilisation de champs d'un document à un autre. En utilisant Aspose.PDF for Python, les développeurs peuvent copier programmatiquement des champs de formulaire d'un PDF source vers un PDF cible.

Le [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) La classe fournit la méthode ‘copy_outer_field’, qui copie un champ d'un document source vers un document cible à une page et des coordonnées spécifiées.

Le code crée un nouveau PDF (cible), ajoute une page, puis copie un champ d'un PDF existant (source) vers le document cible aux coordonnées spécifiées.

1. Créer un nouveau document PDF cible.
1. Ajoutez au moins une page au PDF cible.
1. Enregistrez le document cible vide.
1. Créez un objet FormEditor et liez-le au PDF cible.
1. Copiez le champ 'First Name' du PDF source vers la page 1 à (200, 600).
1. Enregistrez le PDF cible mis à jour.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def copy_outer_field(infile, outfile):
    # Since copy_outer_field() method needs to copy field from source document to target document, we need to create a new document as target document first.
    doc = ap.Document()
    doc.pages.add()
    doc.save(outfile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(outfile)
    # Copies an existing field to a new position specified by both page number and ordinates.
    # A new document will be produced, which contains everything the source document has except for the newly copied field.
    form_editor.copy_outer_field(infile, "First Name", 1, 200, 600)
    # Save updated document
    form_editor.save(outfile)
```

**Veuillez noter :**

La signature de la méthode 'copy_outer_field' ressemble à ceci :

```python
copy_outer_field(original_field_name, new_field_name, page_number, x, y)
```

- 'original_field_name' – le champ que vous souhaitez dupliquer.
- 'new_field_name' – le nom du nouveau champ.
- 'page_number' – la page sur laquelle le nouveau champ apparaîtra.
- x, y – coordonnées sur cette page.

Le page_number doit être un entier positif correspondant à une page existante du PDF (indexation à partir de 1).

Si vous passez un paramètre négatif, par ex. :

```python
form_editor.copy_outer_field("First Name", "First Name Copy", 1, -200, 600)
```

Le programme réinitialisera alors aux paramètres précédents.
