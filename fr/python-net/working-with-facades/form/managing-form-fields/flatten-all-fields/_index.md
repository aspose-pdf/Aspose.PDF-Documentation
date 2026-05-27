---
title: Aplatir tous les champs
type: docs
weight: 10
url: /fr/python-net/flatten-all-fields/
description: Cet exemple montre comment aplatir tous les champs de formulaire dans un PDF en utilisant Aspose.PDF for Python via .NET. Il montre comment lier un document PDF, convertir chaque élément de formulaire interactif en contenu de page statique, et enregistrer le fichier finalisé.
lastmod: "2026-05-22"
---

L'aplatissement supprime l'interactivité des formulaires PDF en fusionnant les valeurs des champs directement dans la mise en page du document. Dans cet exemple, le [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) façade de [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) est utilisé pour lier le PDF source et appliquer la méthode flatten_all_fields(), qui convertit tous les champs en contenu non modifiable.

1. Initialisez pdf_facades.Form() pour interagir avec les champs de formulaire PDF.
1. Appelez 'bind_pdf()' pour attacher le document source.
1. Appelez 'flatten_all_fields()' pour convertir tous les champs interactifs en contenu statique.
1. Enregistrez le Document mis à jour.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Flatten all fields
def flatten_all_fields(infile, outfile):
    """Flatten all fields in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Flatten all fields in the PDF document
    pdf_form.flatten_all_fields()

    # Save updated PDF
    pdf_form.save(outfile)
```
