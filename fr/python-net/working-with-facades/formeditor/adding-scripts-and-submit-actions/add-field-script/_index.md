---
title: Ajouter le script du champ
type: docs
weight: 10
url: /fr/python-net/add-field-script/
description: Les formulaires PDF interactifs peuvent inclure du JavaScript pour automatiser des actions lorsque les utilisateurs interagissent avec les champs de formulaire. En utilisant Aspose.PDF for Python, les développeurs peuvent facilement attacher des scripts aux éléments de formulaire tels que des boutons ou des champs de texte.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter des actions JavaScript aux champs de formulaire PDF en utilisant Python
Abstract: Cet article explique comment ouvrir un formulaire PDF, affecter du code JavaScript à un champ de formulaire spécifique, ajouter des actions de script supplémentaires et enregistrer le document mis à jour. L'exemple utilise la classe FormEditor de l'API Aspose.PDF Facades pour manipuler le comportement du formulaire de manière programmatique.
---

## Ajouter des actions JavaScript aux champs de formulaire PDF en utilisant Python

Cet extrait de code vous permet d'ajouter des actions JavaScript à un champ de formulaire PDF existant en utilisant la bibliothèque Aspose.PDF for Python. Il ouvre un document PDF, assigne une action JavaScript à un champ de formulaire et ajoute un script qui s'exécute lorsque le champ est déclenché. Enfin, le PDF mis à jour est enregistré sous un nouveau fichier.
En utilisant le [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) classe de la [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) module, vous pouvez attacher programmatiquement du JavaScript aux champs de formulaire existants :

1. Ouvrez un formulaire PDF existant.
1. Définissez une action JavaScript pour un champ spécifique.
1. Ajouter une autre action JavaScript au même champ.
1. Enregistrer le document PDF modifié.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_field_script(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Set JavaScript action for the field
    form_editor.set_field_script(
        "Script_Demo_Button", "app.alert('Script 1 has been executed');"
    )

    # Add JavaScript action to the field
    form_editor.add_field_script(
        "Script_Demo_Button", "app.alert('Script 2 has been executed');"
    )

    # Save output PDF file
    form_editor.save(output_file_name)
```
