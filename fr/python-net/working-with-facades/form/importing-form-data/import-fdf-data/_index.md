---
title: Importer les données FDF
type: docs
weight: 10
url: /fr/python-net/import-fdf-data/
description: Cet exemple montre comment importer des données de formulaire à partir d'un fichier FDF dans un formulaire PDF en utilisant Aspose.PDF for Python via .NET. Il montre comment lier un document PDF, lire les valeurs des champs de formulaire à partir d'un flux FDF, et remplir automatiquement les champs correspondants.
lastmod: "2026-05-22"
---

FDF (Formats de données de formulaires) est un format léger utilisé pour stocker et transférer les valeurs des champs de formulaire PDF sans inclure le document complet. Dans cet exemple, le [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) façade de [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) est utilisé pour charger un formulaire PDF et importer les données des champs à partir d'un fichier FDF externe. Après le processus d'importation, le PDF mis à jour est enregistré en tant que nouveau fichier.

1. Initialisez pdf_facades.Form() pour travailler avec les champs de formulaire PDF interactifs.
1. Appelez 'bind_pdf()' pour attacher le modèle de formulaire PDF.
1. Utilisez 'open()' pour lire le fichier FDF en mode binaire.
1. Appelez 'import_fdf()' pour remplir les champs PDF avec les données du fichier FDF.
1. Enregistrez le PDF mis à jour.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import Data from FDF
def import_fdf_to_pdf_form(infile, datafile, outfile):
    """Import form data from FDF file into PDF form fields."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open FDF file as stream
    with open(datafile, "rb") as fdf_input_stream:
        pdf_form.import_fdf(fdf_input_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```
