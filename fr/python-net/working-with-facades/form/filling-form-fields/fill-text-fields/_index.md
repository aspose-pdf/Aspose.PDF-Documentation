---
title: Remplir les champs texte
type: docs
weight: 10
url: /fr/python-net/fill-text-fields/
description: Cet exemple montre comment remplir automatiquement les champs texte d'un formulaire PDF à l'aide d'Aspose.PDF for Python via .NET. Il montre comment charger un document PDF, remplir des champs de formulaire spécifiques par leur nom, et enregistrer le fichier mis à jour.
lastmod: "2026-05-22"
---

Le remplissage programmatique des champs texte permet aux applications de réutiliser des modèles PDF et d'insérer du contenu dynamique sans édition manuelle. Dans cet exemple, le [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) façade de [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) est utilisé pour lier un formulaire PDF et mettre à jour plusieurs champs tels que le nom, l'adresse et l'e‑mail. Après avoir attribué les valeurs, le PDF modifié est enregistré comme un nouveau document.

1. Initialisez 'pdf_facades.Form()' pour gérer les opérations sur les champs de formulaire.
1. Utilisez 'bind_pdf()' pour attacher le PDF d'entrée contenant les champs texte.
1. Appelez 'fill_field()' pour insérer des données dans des champs tels que le nom, l'adresse et l'e-mail.
1. Enregistrez le PDF mis à jour.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Text Fields
def fill_text_fields(infile, outfile):
    """Fill text fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill text fields by name
    pdf_form.fill_field("name", "John Doe")
    pdf_form.fill_field("address", "123 Main St, Anytown, USA")
    pdf_form.fill_field("email", "john.doe@example.com")

    # Save updated PDF
    pdf_form.save(outfile)
```
