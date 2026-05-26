---
title: Remplir la zone de liste
type: docs
weight: 40
url: /fr/python-net/fill-list-box/
description: Cet exemple montre comment remplir à l'aide d'un programme les zones de liste et les champs à sélection multiple dans un formulaire PDF en utilisant Aspose.PDF for Python via .NET. Il montre comment lier un document PDF, sélectionner des valeurs dans un champ de formulaire basé sur une liste, et enregistrer le fichier mis à jour.
lastmod: "2026-05-22"
---

Les zones de liste et les champs à sélection multiple permettent aux utilisateurs de choisir une ou plusieurs valeurs parmi un ensemble d'options prédéfini. Dans cet exemple, le [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) façade de [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) est utilisé pour accéder au formulaire PDF et attribuer une valeur sélectionnée au champ favorite_colors. Une fois l'option souhaitée sélectionnée, le document mis à jour est enregistré.

1. Initialisez 'pdf_facades.Form()' pour gérer et mettre à jour les champs de formulaire.
1. Appelez 'bind_pdf()' pour joindre le PDF source contenant des zones de liste ou des champs à sélection multiple.
1. Utilisez 'fill_field()' pour sélectionner une valeur parmi les options disponibles.
1. Enregistrez le Document mis à jour.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill List Box / Multi-Select Fields
def fill_list_box_fields(infile, outfile):
    """Fill list box and multi-select fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill list box / multi-select fields by name
    pdf_form.fill_field("favorite_colors", "Red")

    # Save updated PDF
    pdf_form.save(outfile)
```
