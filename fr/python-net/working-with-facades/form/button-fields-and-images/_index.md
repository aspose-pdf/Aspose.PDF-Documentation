---
title: Champs de bouton et images
type: docs
weight: 40
url: /fr/python-net/button-fields-and-images/
description: Cet exemple montre comment gérer les champs de bouton dans un formulaire PDF en utilisant l'API Aspose.PDF Facades.
lastmod: "2026-05-22"
TechArticle: true
AlternativeHeadline: Ajout d'une image aux champs de bouton et lecture des indicateurs de soumission
Abstract: Les formulaires PDF comprennent souvent des boutons interactifs qui déclenchent soit des actions JavaScript, soit la soumission des données du formulaire. Vous pouvez améliorer visuellement les champs de bouton en ajoutant des images comme apparence et inspecter leur comportement de soumission de manière programmatique.
---

## Ajouter une apparence d'image aux champs de bouton

Cet extrait de code explique comment ajouter une apparence d'image à un champ de bouton existant dans un formulaire PDF. L'opération améliore la présentation visuelle d'un bouton PDF en remplaçant son apparence par défaut par une image personnalisée.

1. Créer un objet Form.
1. Lier le fichier PDF à l'objet Form.
1. Ajouter une image au champ Button.

    - Déterminer le chemin du fichier image associé au PDF
    - Ouvrir l'image en mode binaire en tant que image_stream.
    - Appeler fill_image_field() avec le nom complet du champ button.

1. Enregistrer le PDF mis à jour.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Add image appearance to button fields
def add_image_appearance_to_button_fields(infile, outfile):
    """Add image appearance to button fields in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Add image appearance to button fields by providing the field name and image stream
    image_path = infile.replace(".pdf", ".jpg")
    with open(image_path, "rb") as image_stream:
        pdf_form.fill_image_field("Image1_af_image", image_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```

## Obtenir les indicateurs de soumission

La bibliothèque Python vous aide à récupérer les indicateurs de soumission d'un bouton de soumission dans un formulaire PDF en utilisant l'API Aspose.PDF Facades. Les indicateurs de soumission définissent le comportement d'un bouton de soumission, par exemple s'il envoie le formulaire complet, inclut les annotations, ou soumet au format FDF, XFDF, PDF ou HTML.

1. Créer un objet Form.
1. Appelez get_submit_flags() sur l'objet form en utilisant le nom complet du bouton de soumission.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_submit_flags(infile, outfile):
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)
    flags = pdf_form.get_submit_flags("Submit1_af_submit")

    print(f"Submit flags: {flags}")
```
