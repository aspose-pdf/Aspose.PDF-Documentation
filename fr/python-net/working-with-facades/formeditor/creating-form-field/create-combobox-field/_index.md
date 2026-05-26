---
title: Créer un champ ComboBox
type: docs
weight: 20
url: /fr/python-net/create-combobox-field/
description: Vérifiez comment ajouter programmétiquement un champ ComboBox (liste déroulante) à un document PDF en utilisant Aspose.PDF for Python. Cet exemple montre comment insérer un champ de formulaire ComboBox, ajouter des éléments sélectionnables et enregistrer le fichier PDF mis à jour.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Créer un champ ComboBox dans un PDF en utilisant Aspose.PDF for Python
Abstract: Les champs de formulaire interactifs rendent les PDF plus dynamiques et conviviaux. Un champ ComboBox permet aux utilisateurs de sélectionner une option dans une liste déroulante prédéfinie. Dans ce tutoriel, vous apprendrez comment créer un ComboBox dans un PDF en utilisant la classe FormEditor d'Aspose.PDF for Python, le remplir avec des options et enregistrer le document modifié.
---

Les formulaires PDF sont largement utilisés pour recueillir des informations structurées dans des documents numériques tels que des candidatures, des enquêtes et des formulaires d'inscription. Un champ ComboBox offre un moyen pratique aux utilisateurs de choisir parmi une liste de valeurs prédéfinies tout en maintenant le formulaire compact et organisé.

Le [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) La classe permet de créer et de gérer différents types de champs, y compris les zones de texte, les cases à cocher, les boutons radio et les listes déroulantes.

1. Chargez un document PDF existant.
1. Ajoutez un champ ComboBox avec la méthode 'add_field()' et le paramètre 'FieldType.COMBO_BOX'.
1. Utilisez la méthode 'add_list_item()' pour insérer des options sélectionnables dans la liste déroulante.
1. Enregistrez le document PDF mis à jour.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_combobox_field(infile, outfile):
    """Create ComboBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add ComboBox field to PDF form
    pdf_form_editor.add_field(
        pdf_facades.FieldType.COMBO_BOX, "combobox1", "Australia", 1, 230, 498, 350, 514
    )
    pdf_form_editor.add_list_item("combobox1", ["Australia", "Australia"])
    pdf_form_editor.add_list_item("combobox1", ["New Zealand", "New Zealand"])

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
