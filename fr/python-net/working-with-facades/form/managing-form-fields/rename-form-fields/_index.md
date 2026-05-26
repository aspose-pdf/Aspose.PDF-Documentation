---
title: Renommer les champs de formulaire
type: docs
weight: 30
url: /fr/python-net/rename-form-fields/
description: Cet exemple montre comment renommer les champs de formulaire dans un document PDF à l'aide d'Aspose.PDF for Python via .NET. Il montre comment lier un formulaire PDF, mettre à jour les noms de champs existants de manière programmatique, puis enregistrer le fichier modifié. Renommer les champs permet de standardiser les structures de formulaire, d'améliorer le mappage des données et de simplifier l'intégration avec des flux de travail automatisés ou des systèmes externes.
lastmod: "2026-05-22"
---

Renommer les champs de formulaire est utile lors de l'alignement des formulaires PDF avec les conventions de nommage internes ou lors de la préparation de documents pour le traitement de données structurées. Dans cet exemple, le [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) façade du [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) module est utilisé pour lier le PDF source et appliquer un mappage qui remplace les anciens noms de champ par de nouveaux. Après la mise à jour des identifiants de champ, le document est enregistré avec les modifications appliquées.

1. Initialisez pdf_facades.Form() pour interagir avec les champs de formulaire PDF.
1. Appelez 'bind_pdf()' pour attacher le modèle de formulaire PDF.
1. Créez une liste de tuples contenant les anciens noms de champ et leurs nouveaux noms correspondants.
1. Parcourez le mapping et appelez 'rename_field()' pour chaque entrée.
1. Enregistrez le Document mis à jour.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Rename form fields
def rename_form_fields(infile, outfile):
    """Rename form fields in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Rename form fields by providing a mapping of old names to new names
    field_renaming_map = [("First Name", "NewFirstName"), ("Last Name", "NewLastName")]
    for old_name, new_name in field_renaming_map:
        pdf_form.rename_field(old_name, new_name)

    # Save updated PDF
    pdf_form.save(outfile)
```
