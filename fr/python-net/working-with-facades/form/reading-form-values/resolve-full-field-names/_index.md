---
title: Résoudre les noms complets des champs
type: docs
weight: 60
url: /fr/python-net/resolve-full-field-names/
description: Cet exemple montre comment récupérer les noms pleinement qualifiés des champs de formulaire dans un document PDF en utilisant l'API Aspose.PDF Facades.
lastmod: "2026-05-22"
---

Dans les formulaires PDF, les champs peuvent être organisés hiérarchiquement, notamment lorsque des sous‑formulaires sont utilisés. Chaque champ possède un nom court et un nom pleinement qualifié. Le nom pleinement qualifié représente le chemin complet du champ au sein de la hiérarchie du formulaire et est requis par de nombreuses méthodes d'API qui manipulent ou lisent les données de formulaire.

1. Créer un objet Form.
1. Lier le document PDF.
1. Accéder à tous les noms de champs de formulaire.
1. Le nom pleinement qualifié de chaque champ est résolu à l'aide de get_full_field_name().

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Resolve full field names
def resolve_full_field_names(infile):
    """Resolve full field names in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Resolve full field names
    for field in pdf_form.field_names:
        name = pdf_form.get_full_field_name(field)
        print(f"Full field name: {name}")
```
