---
title: Exporter vers XML
type: docs
weight: 40
url: /fr/python-net/export-to-xml/
description: Cet exemple montre comment exporter les données de formulaire PDF vers un fichier XML en utilisant Aspose.PDF for Python via .NET. Il montre comment charger un document PDF, accéder à ses champs de formulaire via la façade Form, et enregistrer les données extraites en XML structuré en utilisant Form Class.
lastmod: "2026-05-22"
---

L'exportation des données de formulaire permet aux développeurs de réutiliser les informations stockées dans les PDF AcroForms sans copier manuellement les valeurs des champs. Dans cet exemple, un [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) objet est créé à partir de aspose.pdf. Dans le module facades, le PDF source est lié à celui-ci, et les données du formulaire sont écrites dans un flux XML.

1. Créez un objet Form. Initialisez pdf_facades.Form() pour accéder aux champs de formulaire et les gérer.
1. Utilisez 'bind_pdf()' pour attacher le document PDF source à l'instance Form.
1. Créez un flux de fichier accessible en écriture en utilisant 'FileIO()'.
1. Appelez 'export_xml()' pour extraire toutes les valeurs des champs de formulaire et les écrire dans le fichier XML.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to XML
def export_pdf_form_data_to_xml(infile, datafile):
    """Export PDF form data to XML file."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open XML file as stream
    with FileIO(datafile, "w") as xml_output_stream:
        # Export data from PDF form fields to XML
        pdf_form.export_xml(xml_output_stream)
```
