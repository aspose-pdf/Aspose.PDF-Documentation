---
title: Importer les données XFDF
type: docs
weight: 20
url: /fr/python-net/import-xfdf-data/
description: Cet exemple montre comment importer des données de formulaire à partir d'un fichier XFDF dans un formulaire PDF en utilisant Aspose.PDF for Python via .NET. Il montre comment lier un document PDF, lire les données XFDF basées sur XML via un flux de fichier, et remplir automatiquement les champs de formulaire correspondants. L'importation des données XFDF permet un échange efficace de données de formulaire et prend en charge les flux de travail documentaires automatisés qui reposent sur des formats XML structurés.
lastmod: "2026-05-22"
---

XFDF (XML Forms Data Format) est une représentation XML des données de formulaire PDF conçue pour l'interopérabilité et l'échange de données. Dans cet exemple, le [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) façade du [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) module est utilisé pour lier un formulaire PDF et importer les valeurs des champs à partir d'un fichier XFDF externe. Après l'importation des données, le PDF mis à jour est enregistré en tant que nouveau document.

1. Initialisez pdf_facades.Form() pour interagir avec les champs de formulaire PDF.
1. Appelez 'bind_pdf()' pour attacher le modèle de formulaire PDF.
1. Utilisez 'open()' pour lire le fichier XFDF.
1. Appelez 'import_xfdf()' pour remplir les champs PDF avec les valeurs du fichier XFDF.
1. Enregistrez le Document mis à jour.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import Data from XFDF
def import_data_from_xfdf(infile, datafile, outfile):
    """Import form data from XFDF file into PDF form fields."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open XFDF file as stream
    with open(datafile, "rb") as xfdf_input_stream:
        # Import data from XFDF into PDF form fields
        pdf_form.import_xfdf(xfdf_input_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```
