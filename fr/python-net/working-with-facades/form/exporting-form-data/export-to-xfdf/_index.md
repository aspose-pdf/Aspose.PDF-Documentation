---
title: Exporter vers XFDF
type: docs
weight: 20
url: /fr/python-net/export-to-xfdf/
description: Cet exemple montre comment exporter les données des champs de formulaire PDF vers un fichier XFDF (XML Forms Data Format) en utilisant Aspose.PDF for Python via .NET. Il démontre comment charger un formulaire PDF, accéder à ses champs via la façade Form, et enregistrer les valeurs extraites dans un flux XFDF.
lastmod: "2026-05-22"
---

XFDF est une représentation XML des données de formulaire PDF qui permet aux développeurs de transférer les valeurs des champs de formulaire indépendamment du document original. Dans cet exemple, le [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) objet de [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) est utilisé pour lier le PDF source et exporter ses données dans un fichier XFDF structuré.

1. Initialisez pdf_facades.Form() pour gérer les données du formulaire PDF.
1. Appelez 'bind_pdf()' pour joindre le document PDF source.
1. Utilisez 'open()' pour créer un flux binaire en écriture.
1. Exporter les données du formulaire. Appelez 'export_xfdf()' pour extraire et enregistrer les valeurs des champs de formulaire au format XFDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to XFDF
def export_pdf_form_to_xfdf(infile, outfile):
    """Export PDF form data to XFDF file."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Create XFDF file stream
    with open(outfile, "wb") as xfdf_output_stream:
        # Export form data to XFDF file
        pdf_form.export_xfdf(xfdf_output_stream)
```
