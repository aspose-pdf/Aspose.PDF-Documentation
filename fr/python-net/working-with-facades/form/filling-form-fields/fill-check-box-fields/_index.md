---
title: Remplir les champs de case à cocher
type: docs
weight: 20
url: /fr/python-net/fill-check-box-fields/
description: Cet exemple montre comment remplir programmétiquement les champs de case à cocher d'un formulaire PDF en utilisant Aspose.PDF for Python via .NET. Il montre comment lier un document PDF, mettre à jour les valeurs des cases à cocher par nom de champ, et enregistrer le fichier modifié.
lastmod: "2026-05-22"
---

La case à cocher est couramment utilisée dans les formulaires PDF pour représenter des choix binaires tels que les abonnements ou les confirmations d'accord. Dans cet exemple, la [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) façade de [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) est utilisée pour accéder aux champs du formulaire et définir leurs valeurs à l'état sélectionné. Après avoir mis à jour les cases à cocher, le PDF rempli est enregistré en tant que nouveau document.

1. Initialisez 'pdf_facades.Form()' pour gérer les interactions avec les champs du formulaire.
1. Utilisez 'bind_pdf()' pour joindre le PDF source contenant des champs de cases à cocher.
1. Appelez 'fill_field()' pour marquer les champs tels que 'subscribe_newsletter' et 'accept_terms' comme sélectionnés.
1. Enregistrez le Document mis à jour.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Check Box Fields
def fill_check_box_fields(infile, outfile):
    """Fill check box fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill check box fields by name
    pdf_form.fill_field("subscribe_newsletter", "Yes")
    pdf_form.fill_field("accept_terms", "Yes")

    # Save updated PDF
    pdf_form.save(outfile)
```
