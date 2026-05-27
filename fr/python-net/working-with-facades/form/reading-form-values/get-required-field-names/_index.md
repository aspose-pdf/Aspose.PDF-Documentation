---
title: Obtenir les noms des champs obligatoires
type: docs
weight: 30
url: /fr/python-net/get-required-field-names/
description: Cet exemple montre comment identifier et récupérer les noms des champs de formulaire obligatoires dans un document PDF en utilisant l'API Aspose.PDF Facades.
lastmod: "2026-05-22"
---

Les formulaires PDF peuvent contenir des champs obligatoires que les utilisateurs doivent remplir avant la soumission. Ces champs sont généralement marqués comme requis dans les propriétés du formulaire.

1. Créer un objet Form.
1. Lier le document PDF.
1. Accédez à tous les noms de champs en utilisant 'pdf_form.field_names'.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Get required field names
def get_required_field_names(infile):
    """Get required field names from a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Get required field names
    for field in pdf_form.field_names:
        if pdf_form.is_required_field(field):
            print(f"Required field: {field}")
```
