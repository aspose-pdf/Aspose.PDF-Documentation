---
title: Créer un champ case à cocher
type: docs
weight: 10
url: /fr/python-net/create-checkbox-field/
description: Apprenez comment ajouter de manière programmatique un champ de formulaire case à cocher à un document PDF en utilisant Aspose.PDF for Python. Ce guide montre comment utiliser la classe FormEditor pour insérer une case à cocher interactive dans un fichier PDF existant et enregistrer le document mis à jour.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Créer un champ case à cocher dans un PDF en utilisant Aspose.PDF for Python
Abstract: Les champs de formulaire interactifs permettent aux utilisateurs de remplir et d’interagir avec les documents PDF de façon numérique. Dans ce tutoriel, vous apprendrez comment ajouter un champ case à cocher à un PDF en utilisant l’API Aspose.PDF Python. L’exemple montre comment lier un document PDF existant, créer un champ de formulaire case à cocher à des coordonnées spécifiées, et enregistrer le fichier modifié.
---

Les formulaires PDF sont largement utilisés pour recueillir les saisies des utilisateurs dans des documents tels que les formulaires de candidature, les enquêtes et les accords. Un champ case à cocher permet aux utilisateurs de sélectionner ou de désélectionner une option dans un formulaire.

En utilisant Aspose.PDF for Python, les développeurs peuvent manipuler les formulaires PDF de manière programmatique. Le [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) la classe fournit des méthodes pour ajouter, modifier et gérer les champs de formulaire dans un document PDF.

1. Chargez un fichier PDF existant.
1. Appelez la méthode 'add_field()' avec le paramètre 'FieldType.CHECK_BOX' pour créer la case à cocher et spécifier sa position.
1. Définissez le nom du champ, la légende et la position.
1. Enregistrez le document PDF mis à jour.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_checkbox_field(infile, outfile):
    """Create CheckBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add CheckBox field to PDF form
    pdf_form_editor.add_field(
        pdf_facades.FieldType.CHECK_BOX,
        "checkbox1",
        "Check Box 1",
        1,
        240,
        498,
        256,
        514,
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
