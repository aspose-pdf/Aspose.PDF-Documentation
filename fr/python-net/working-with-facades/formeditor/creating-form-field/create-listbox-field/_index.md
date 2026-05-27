---
title: Créer un champ ListBox
type: docs
weight: 30
url: /fr/python-net/create-listbox-field/
description: Apprenez à ajouter programmétiquement un champ de formulaire ListBox à un document PDF à l'aide d'Aspose.PDF for Python. Ce guide montre comment insérer un champ ListBox, définir les éléments sélectionnables et enregistrer le fichier PDF mis à jour.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Créer un champ ListBox dans un PDF à l'aide d'Aspose.PDF for Python
Abstract: Les formulaires PDF permettent aux utilisateurs d'interagir avec les documents en sélectionnant des options, en saisissant des données et en soumettant des informations numériquement. Un champ ListBox permet aux utilisateurs de choisir une ou plusieurs valeurs parmi une liste visible d'options. Dans ce tutoriel, vous apprendrez à créer un champ ListBox dans un PDF en utilisant la classe FormEditor d'Aspose.PDF for Python et à le remplir avec des éléments prédéfinis.
---

Les formulaires PDF sont couramment utilisés pour les demandes, les enquêtes et les documents d'inscription. Un champ ListBox affiche plusieurs options simultanément, ce qui facilite la révision et la sélection d'éléments dans une liste par les utilisateurs.

Le [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) class fournit des fonctionnalités pour ajouter différents types de champs interactifs, y compris les éléments ListBox.

1. Chargez un document PDF existant.
1. Définir une liste d'options sélectionnables.
1. Ajouter un champ ListBox à une page spécifique.
1. Définir une valeur sélectionnée par défaut.
1. Enregistrez le document PDF mis à jour.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_listbox_field(infile, outfile):
    """Create ListBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add ListBox field to PDF form
    pdf_form_editor.items = ["Australia", "New Zealand", "Malaysia"]
    pdf_form_editor.add_field(
        pdf_facades.FieldType.LIST_BOX, "listbox1", "Australia", 1, 230, 398, 350, 514
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
