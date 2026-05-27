---
title: Exporter vers JSON
type: docs
weight: 30
url: /fr/python-net/export-to-json/
description: Cet exemple montre comment exporter les valeurs des champs de formulaire PDF vers un fichier JSON en utilisant Aspose.PDF for Python via .NET. Il explique comment charger un formulaire PDF, accéder à ses champs via la façade Form, et enregistrer les données extraites dans un format JSON structuré.
lastmod: "2026-05-22"
---

JSON est un format de données largement utilisé qui permet un échange fluide entre les applications et les services. Dans cet exemple, le [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) objet du [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) module est utilisé pour lier un fichier PDF et exporter ses valeurs de champs de formulaire dans une structure JSON lisible.

1. Initialisez pdf_facades.Form() pour travailler avec les champs de formulaire.
1. Utilisez 'bind_pdf()' pour attacher le document PDF source.
1. Créez un flux en écriture en utilisant 'FileIO()'.
1. Appelez 'export_json()' pour extraire les valeurs des champs du formulaire et les enregistrer au format JSON.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to JSON
def export_form_to_json(infile, outfile):
    """Export PDF form field values to JSON file."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    # Create JSON file stream
    with FileIO(outfile, "w") as json_stream:
        # Export form field values to JSON
        form.export_json(json_stream, indented=True)
```
