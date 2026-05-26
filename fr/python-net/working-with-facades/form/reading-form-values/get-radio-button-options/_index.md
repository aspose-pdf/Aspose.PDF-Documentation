---
title: Obtenir les options de bouton radio
type: docs
weight: 20
url: /fr/python-net/get-radio-button-options/
description: Cet article démontre comment récupérer la valeur actuellement sélectionnée d'un champ de bouton radio dans un document PDF en utilisant l'API Aspose.PDF Facades.
lastmod: "2026-05-22"
---

Les champs de bouton radio dans les formulaires PDF sont des contrôles groupés où une seule option peut être sélectionnée à la fois. Chaque groupe a un nom de champ, et chaque option a une valeur correspondante.

1. Créer un objet Form.
1. Lier le document PDF.
1. Récupérer l'option de bouton radio sélectionnée.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Get radio button options
def get_radio_button_options(infile):
    """Get radio button options from a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Get radio button options by their names
    field_names = ["WorkType"]
    for field_name in field_names:
        options = pdf_form.get_button_option_current_value(field_name)
        print(f"Options for '{field_name}': {options}")
```
