---
title: Obtenir les façades de champ
type: docs
weight: 10
url: /fr/python-net/get-field-facades/
description: Cet exemple montre comment lire les valeurs de champs de formulaire spécifiques à partir d'un document PDF à l'aide de l'API Aspose.PDF Facades.
lastmod: "2026-05-22"
---

Les formulaires PDF contiennent des champs où les utilisateurs peuvent saisir des données, tels que des zones de texte, des cases à cocher ou des boutons radio. Pour traiter ces formulaires de manière programmatique, il est souvent nécessaire de récupérer les valeurs actuelles de ces champs.

1. Créer un objet Form.
1. Lier le document PDF à l'objet formulaire.
1. Récupérer les valeurs des champs.

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir


    # Get field values
    def get_field_values(infile):
        """Get field values from a PDF document."""
        # Create Form object
        pdf_form = pdf_facades.Form()

        # Bind PDF document
        pdf_form.bind_pdf(infile)

        # Get field values by their names
        field_names = ["First Name", "Last Name"]
        for field_name in field_names:
            value = pdf_form.get_field(field_name)
            print(f"Value of '{field_name}': {value}")
```