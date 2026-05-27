---
title: Importer des données JSON
type: docs
weight: 30
url: /fr/python-net/import-json-data/
description: Cet exemple montre comment importer les données de champs de formulaire à partir d'un fichier JSON dans un formulaire PDF en utilisant Aspose.PDF for Python via .NET. Il montre comment lier un document PDF, lire les données JSON structurées via un flux de fichier, et remplir automatiquement les champs de formulaire correspondants.
lastmod: "2026-05-22"
---

JSON est largement utilisé pour stocker et transférer des données structurées entre systèmes. Dans cet exemple, le [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) façade du [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) Le module est utilisé pour lier un formulaire PDF et importer les valeurs des champs à partir d'un fichier JSON externe. Après le processus d'importation, le document mis à jour est enregistré en tant que nouveau PDF.

1. Initialisez pdf_facades.Form() pour interagir avec les champs de formulaire PDF.
1. Appelez 'bind_pdf()' pour attacher le modèle de formulaire PDF.
1. Utilisez 'FileIO()' pour lire le fichier JSON contenant les valeurs du formulaire.
1. Appelez 'import_json()' pour remplir les champs PDF en utilisant des paires clé‑valeur JSON.
1. Enregistrez le PDF mis à jour.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import from JSON
def import_json_to_pdf_form(infile, datafile, outfile):
    """Import form data from JSON file into PDF form fields."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    # Open JSON file as stream
    with FileIO(datafile, "r") as json_stream:
        # Import data from JSON into PDF form fields
        form.import_json(json_stream)

    # Save updated PDF
    form.save(outfile)
```
