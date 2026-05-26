---
title: Importer les données XML
type: docs
weight: 40
url: /fr/python-net/import-xml-data/
description: Cet exemple montre comment importer des données de formulaire à partir d'un fichier XML dans les champs de formulaire PDF en utilisant Aspose.PDF for Python via .NET. Il montre comment lier un document PDF, lire des données XML structurées via un flux de fichier, et remplir automatiquement les champs de formulaire correspondants.
lastmod: "2026-05-22"
---

XML est couramment utilisé pour stocker des données de formulaire structurées, ce qui en fait un format pratique pour transférer des valeurs entre systèmes. Dans cet exemple, le [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) façade de [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) est utilisé pour charger un formulaire PDF et appliquer les valeurs des champs directement à partir d'un fichier XML. Après l'importation des données, le PDF mis à jour est enregistré en tant que nouveau document.

1. Initialisez pdf_facades.Form() pour interagir avec les champs de formulaire PDF.
1. Appelez 'bind_pdf()' pour attacher le modèle de formulaire PDF.
1. Utilisez 'FileIO()' pour accéder au fichier XML contenant les données du formulaire.
1. Appelez 'import_xml()' pour remplir les champs PDF avec les valeurs du fichier XML.
1. Enregistrez le PDF mis à jour.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import data from XML
def import_xml_to_pdf_fields(infile, datafile, outfile):
    """Import form data from XML file into PDF form fields."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open XML file as stream
    with FileIO(datafile, "r") as xml_input_stream:
        # Import data from XML into PDF form fields
        pdf_form.import_xml(xml_input_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```
