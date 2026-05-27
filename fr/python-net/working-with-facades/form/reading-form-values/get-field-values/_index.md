---
title: Obtenir les valeurs des champs
type: docs
weight: 50
url: /fr/python-net/get-field-values/
description: Récupération des valeurs des champs d'un formulaire PDF avec Aspose.PDF Facades en utilisant la classe Form.
lastmod: "2026-05-22"
---

Cet extrait de code montre comment récupérer les valeurs actuelles des champs de formulaire d'un document PDF en utilisant l'API Aspose.PDF Facades. Le [get_field()](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/#methods) Cette méthode vous permet d'accéder programmétiquement aux données saisies dans les champs de texte, les cases à cocher, les boutons radio et d'autres éléments AcroForm.

1. Liez le PDF à un objet Form.
1. Spécifiez les noms de champs que vous souhaitez lire.
1. Récupérez la valeur de chaque champ à l’aide de get_field().

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