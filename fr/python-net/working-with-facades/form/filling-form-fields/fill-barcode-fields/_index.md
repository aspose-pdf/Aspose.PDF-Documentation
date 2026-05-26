---
title: Remplir les champs de code-barres
type: docs
weight: 50
url: /fr/python-net/fill-barcode-fields/
description: Cet exemple montre comment remplir programmétiquement des champs de code-barres dans un formulaire PDF en utilisant Aspose.PDF for Python via .NET. Il montre comment lier un document PDF, affecter une valeur à un champ de code-barres et enregistrer le fichier mis à jour.
lastmod: "2026-05-22"
---

Les champs de code-barres dans les formulaires PDF permettent de stocker des informations encodées et de les afficher visuellement sous forme de codes-barres. Dans cet exemple, le [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) façade du [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) module est utilisé pour accéder aux champs du formulaire et assigner une valeur de code-barres. Une fois les données remplies, le PDF est enregistré avec le contenu de code-barres mis à jour.

1. Initialisez 'pdf_facades.Form()' pour gérer les interactions avec les formulaires PDF.
1. Appelez 'bind_pdf()' pour attacher le PDF contenant les champs de code-barres.
1. Utilisez 'fill_field()' pour attribuer une valeur de code-barres.
1. Enregistrez le Document mis à jour.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Barcode Fields
def fill_barcode_fields(infile, outfile):
    """Fill barcode fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill barcode fields by name
    pdf_form.fill_field("product_barcode", "123456789012")

    # Save updated PDF
    pdf_form.save(outfile)
```
