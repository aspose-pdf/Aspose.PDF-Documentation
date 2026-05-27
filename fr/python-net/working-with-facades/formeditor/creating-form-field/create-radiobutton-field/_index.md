---
title: Créer un champ RadioButton
type: docs
weight: 40
url: /fr/python-net/create-radiobutton-field/
description: Apprenez comment ajouter de manière programmatique un champ de bouton radio à un document PDF en utilisant Aspose.PDF for Python. Cet exemple montre comment créer un groupe de boutons radio, définir des options sélectionnables et enregistrer le fichier PDF mis à jour.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Créer un champ de bouton radio dans un PDF en utilisant Aspose.PDF for Python
Abstract: Les boutons radio sont couramment utilisés dans les formulaires PDF pour permettre aux utilisateurs de sélectionner une option parmi un groupe de choix prédéfini. Dans ce tutoriel, vous apprendrez comment créer un champ de bouton radio dans un PDF en utilisant la classe FormEditor d'Aspose.PDF for Python. L'exemple montre comment définir les éléments du bouton radio, définir une sélection par défaut et enregistrer le document mis à jour.
---

Les formulaires PDF interactifs permettent aux utilisateurs de fournir des entrées structurées directement dans un document. Un champ de bouton radio est utile lorsque les utilisateurs doivent choisir une seule option parmi plusieurs choix, par exemple la sélection d'un pays, du genre ou d'une préférence.

Le [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) La classe fournit des méthodes pour créer différents types de champs, y compris les zones de texte, les cases à cocher, les listes déroulantes, les listes et les boutons radio.

1. Chargez un document PDF existant.
1. Définir une liste d'options de bouton radio.
1. Ajouter un champ de bouton radio à une page spécifique.
1. Définir une valeur sélectionnée par défaut.
1. Enregistrer le document PDF modifié.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_radiobutton_field(infile, outfile):
    """Create RadioButton field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add RadioButton field to PDF form
    pdf_form_editor.items = ["Australia", "New Zealand", "Malaysia"]
    pdf_form_editor.add_field(
        pdf_facades.FieldType.RADIO, "radiobutton1", "Malaysia", 1, 240, 498, 256, 514
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
