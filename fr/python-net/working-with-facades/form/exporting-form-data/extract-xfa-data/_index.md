---
title: Extraire les données XFA
type: docs
weight: 50
url: /fr/python-net/extract-xfa-data/
description: Cet exemple explique comment extraire les données de formulaire XFA d'un fichier PDF en utilisant Aspose.PDF for Python via .NET. Il montre comment lier un document PDF basé sur XFA à la façade Form et exporter sa structure de données interne dans un flux de fichier.
lastmod: "2026-05-22"
---

Les formulaires XFA (XML Forms Architecture) diffèrent des AcroForms traditionnels car leurs données sont stockées en XML dans le PDF. Dans cet exemple, le [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) objet du [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) module est utilisé pour lier le PDF et extraire ses données XFA directement dans un fichier.

1. Créez une instance de pdf_facades.Form() pour gérer les données du formulaire.
1. Appelez 'bind_pdf()' pour attacher le PDF source contenant des formulaires XFA.
1. Utilisez 'FileIO()' pour créer un flux de fichier en écriture.
1. Appelez 'extract_xfa_data()' pour exporter les données XML XFA intégrées.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Extract XFA Data
def export_xfa_data(infile, outfile):
    """Export XFA form data."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    with FileIO(outfile, "w") as stream:
        # Export embedded XFA XML data to the output stream
        form.extract_xfa_data(stream)
```
