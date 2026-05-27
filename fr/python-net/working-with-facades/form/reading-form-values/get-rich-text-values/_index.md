---
title: Obtenir les valeurs de texte enrichi
type: docs
weight: 40
url: /fr/python-net/get-rich-text-values/
description: Cette section explique comment récupérer le contenu texte enrichi d’un champ de formulaire dans un document PDF à l’aide de l’API Aspose.PDF Facades. Contrairement aux champs de texte simple, les champs de texte enrichi peuvent contenir du contenu formaté tel que du texte en gras, différentes polices, des couleurs et la mise en forme des paragraphes.
lastmod: "2026-05-22"
---

Les formulaires PDF peuvent inclure des champs de texte qui prennent en charge le formatage du texte enrichi. Ces champs peuvent stocker du contenu avec des attributs de style en plus des valeurs de texte simple.

1. Créer un objet Form.
1. Lier le document PDF.
1. Récupérer les valeurs de texte enrichi.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Get rich text values
def get_rich_text_values(infile):
    """Get rich text values from a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Get rich text values by their names
    field_names = ["Summary"]
    for field_name in field_names:
        rich_text_value = pdf_form.get_rich_text(field_name)
        print(f"Rich text value of '{field_name}': {rich_text_value}")
```
