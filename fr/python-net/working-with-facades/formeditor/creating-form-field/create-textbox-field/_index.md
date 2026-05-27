---
title: Créer un champ TextBox
type: docs
weight: 60
url: /fr/python-net/create-textbox-field/
description: Apprenez comment ajouter programmatiquement des champs TextBox à un document PDF à l'aide d'Aspose.PDF for Python. Ce tutoriel montre comment insérer plusieurs champs de texte, définir des valeurs par défaut et enregistrer le document PDF mis à jour.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Créer des champs TextBox dans un PDF à l'aide d'Aspose.PDF for Python
Abstract: Les champs TextBox dans les formulaires PDF permettent aux utilisateurs de saisir et de modifier du texte, rendant les documents interactifs et conviviaux. Dans ce tutoriel, vous apprendrez comment créer des champs de formulaire TextBox dans un PDF en utilisant la classe FormEditor d'Aspose.PDF for Python. L'exemple montre comment ajouter plusieurs champs, spécifier des valeurs par défaut et enregistrer le PDF modifié.
---

Les formulaires PDF nécessitent souvent une saisie de texte de la part des utilisateurs, comme des noms, adresses ou commentaires. Les champs TextBox offrent cette fonctionnalité en fournissant des champs éditables directement dans le document PDF.

Le [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) La classe permet d'ajouter des champs de texte, des cases à cocher, des boutons radio, des listes déroulantes, des listes combinées et des boutons, facilitant la création de PDF interactifs.

1. Chargez un document PDF existant.
1. Ajouter plusieurs champs TextBox pour la saisie de l'utilisateur.
1. Définir des valeurs par défaut pour chaque champ.
1. Enregistrez le document PDF mis à jour.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_textbox_field(infile, outfile):
    """Create TextBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add TextBox field to PDF form
    pdf_form_editor.add_field(
        pdf_facades.FieldType.TEXT, "first_name", "Alexander", 1, 50, 570, 150, 590
    )
    pdf_form_editor.add_field(
        pdf_facades.FieldType.TEXT, "last_name", "Smith", 1, 235, 570, 330, 590
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
