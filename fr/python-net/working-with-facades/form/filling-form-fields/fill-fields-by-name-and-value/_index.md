---
title: Remplir les champs par nom et valeur
type: docs
weight: 60
url: /fr/python-net/fill-fields-by-name-and-value/
description: Cet article explique comment remplir dynamiquement plusieurs champs de formulaire PDF par nom et valeur en utilisant Aspose.PDF for Python via .NET. Au lieu de définir chaque champ individuellement, il utilise une structure de dictionnaire pour associer les noms de champs aux valeurs et les remplit dans une boucle.
lastmod: "2026-05-22"
---

Remplir les champs de formulaire à l'aide d'une collection nom–valeur permet aux développeurs de créer des solutions évolutives et flexibles pour l'automatisation des formulaires PDF. Dans cet exemple, le [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) façade de [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) est utilisé pour lier un document PDF et parcourir un dictionnaire de données de champs. Chaque entrée est appliquée en utilisant la méthode ‘fill_field’, permettant des mises à jour groupées efficaces des champs de formulaire.

1. Initialisez ‘pdf_facades.Form()’ pour travailler avec les champs de formulaire interactifs.
1. Utilisez 'bind_pdf()' pour attacher le document PDF source.
1. Créez un dictionnaire contenant les noms des champs et les valeurs que vous souhaitez insérer.
1. Itérer à travers le dictionnaire et appeler 'fill_field()' pour chaque entrée.
1. Enregistrez le Document mis à jour.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Fields by Name and Value
def fill_fields_by_name_and_value(infile, outfile):
    """Fill PDF form fields by name and value."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill fields by name and value
    fields = {
        "name": "Jane Smith",
        "address": "456 Elm St, Othertown, USA",
        "email": "jane.smith@example.com",
    }
    for field_name, value in fields.items():
        pdf_form.fill_field(field_name, value)

    # Save updated PDF using outfile
    pdf_form.save(outfile)
```
