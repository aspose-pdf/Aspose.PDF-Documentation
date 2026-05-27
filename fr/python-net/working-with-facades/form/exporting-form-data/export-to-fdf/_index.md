---
title: Exporter vers FDF
type: docs
weight: 10
url: /fr/python-net/export-to-fdf/
description: Cet exemple explique comment exporter les données de champ de formulaire PDF vers un fichier FDF (Formats de données de formulaire) en utilisant Aspose.PDF for Python via .NET. Il montre comment accéder aux données de formulaire interactives via la façade Form, lier un document PDF source et enregistrer les valeurs extraites dans un flux FDF.
lastmod: "2026-05-22"
---

FDF est un format léger conçu spécifiquement pour stocker et transférer les données de formulaire PDF sans intégrer le document complet. Dans cet exemple, un [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) objet est initialisé à partir du [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) module, permettant aux développeurs d'interagir avec les champs AcroForm et d'exporter leurs valeurs.

1. Créez une instance de pdf_facades.Form() pour travailler avec les champs de formulaire PDF.
1. Appelez 'bind_pdf()' pour attacher le document PDF contenant le formulaire.
1. Utilisez 'open(')' pour créer un flux binaire ouvrable pour le fichier FDF.
1. Exportez les données du formulaire. Appelez 'export_fdf()' pour extraire et enregistrer toutes les valeurs des champs du formulaire.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to FDF
def export_form_data_to_fdf(infile, outfile):
    """Export PDF form data to FDF file."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Create FDF file stream
    with open(outfile, "wb") as fdf_output_stream:
        # Export form data to FDF file
        pdf_form.export_fdf(fdf_output_stream)
```
