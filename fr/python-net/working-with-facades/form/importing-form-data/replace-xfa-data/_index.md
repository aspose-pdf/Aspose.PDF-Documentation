---
title: Remplacer les données XFA
type: docs
weight: 50
url: /fr/python-net/replace-xfa-data/
description: Cet exemple montre comment remplacer les données de formulaire XFA existantes dans un PDF à l’aide d’Aspose.PDF for Python via .NET. Il montre comment lier un document PDF basé sur XFA, charger de nouvelles données à partir d’un fichier XFA externe, et mettre à jour le contenu du formulaire de manière programmatique.
lastmod: "2026-05-22"
---

Les formulaires XFA (XML Forms Architecture) stockent leurs données au format XML dans la structure du PDF. Dans cet exemple, le [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) façade du [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) module est utilisé pour lier un PDF et remplacer son jeu de données XFA existant à l’aide d’un flux XML externe. Après l’application des nouvelles données, le PDF mis à jour est enregistré comme un fichier séparé.

1. Initialisez pdf_facades.Form() pour gérer les données du formulaire XFA.
1. Appelez 'bind_pdf()' pour attacher le modèle de formulaire PDF.
1. Utilisez 'FileIO()' pour lire le fichier XML XFA.
1. Appelez 'set_xfa_data()' pour mettre à jour le PDF avec le nouveau contenu XFA.
1. Enregistrez le Document mis à jour.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Replace from XFA data
def replace_xfa_data(infile, datafile, outfile):
    """Import form data from XFA file into PDF form fields."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    # Open XFA file as stream
    with FileIO(datafile, "r") as xfa_stream:
        # Import data from XFA into PDF form fields
        form.set_xfa_data(xfa_stream)

    # Save updated PDF
    form.save(outfile)
```
