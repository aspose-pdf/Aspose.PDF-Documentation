---
title: Remplir les champs de boutons radio
type: docs
weight: 30
url: /fr/python-net/fill-radio-button-fields/
description: Cet exemple montre comment remplir programmétiquement les champs de boutons radio dans un formulaire PDF en utilisant Aspose.PDF for Python via .NET. Il montre comment lier un document PDF, sélectionner une option de bouton radio par index, et enregistrer le fichier mis à jour.
lastmod: "2026-05-22"
---

Les boutons radio permettent aux utilisateurs de sélectionner une seule option parmi un groupe prédéfini, tel que les champs de genre ou de préférence. Dans cet exemple, le [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) façade du [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) module est utilisé pour lier le PDF source et attribuer une option sélectionnée par sa valeur d'index. Une fois l'option désirée choisie, le document modifié est enregistré.

1. Initialisez pdf_facades.Form() pour gérer les champs de formulaire PDF.
1. Appelez 'bind_pdf()' pour attacher le PDF contenant les champs de boutons radio.
1. Utilisez 'fill_field()' pour sélectionner la première option (indice 0).
1. Enregistrez le PDF mis à jour.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Radio Button Fields
def fill_radio_button_fields(infile, outfile):
    """Fill radio button fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill radio button fields by name
    pdf_form.fill_field("gender", 0)  # Select male option (index 0)
    # pdf_form.fill_field("gender", 1) # Select female option (index 1)

    # Save updated PDF
    pdf_form.save(outfile)
```
