---
title: Supprimer l'action du champ
type: docs
weight: 20
url: /fr/python-net/remove-field-action/
description: Supprimer le JavaScript des champs de formulaire peut être utile lors de la modification de formulaires PDF interactifs, de la désactivation des actions précédemment attribuées ou du nettoyage de documents contenant des scripts inutiles.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Supprimer les actions JavaScript des champs de formulaire PDF à l'aide de Python
Abstract: En utilisant Aspose.PDF for Python, les développeurs peuvent supprimer programmatiquement les actions JavaScript attachées aux champs de formulaire. Cet article explique comment ouvrir un formulaire PDF existant, supprimer le script associé à un champ spécifique à l'aide de la classe FormEditor, vérifier l'opération et enregistrer le document modifié.
---

Les formulaires PDF contiennent souvent des actions JavaScript qui s'exécutent lorsque les utilisateurs interagissent avec des éléments de formulaire tels que des boutons ou des champs de saisie. Dans certains cas, ces scripts doivent être supprimés pour simplifier le comportement du formulaire, améliorer la sécurité ou mettre à jour la logique du formulaire. Supprimez une action JavaScript d'un champ de formulaire dans un document PDF à l'aide d'Aspose.PDF for Python. Le code ouvre un formulaire PDF existant, localise un champ spécifique, supprime son action JavaScript associée et enregistre le document mis à jour en tant que nouveau fichier PDF.

En utilisant le [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) classe de la [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/), vous pouvez supprimer les actions JavaScript de champs spécifiques dans un formulaire PDF existant :

1. Ouvrez un formulaire PDF existant.
1. Localisez un champ de formulaire nommé 'Script_Demo_Button'.
1. Supprimez l'action JavaScript associée à ce champ.
1. Vérifiez si la suppression a réussi.
1. Enregistrez le document PDF mis à jour.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_field_script(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Remove JavaScript action from the field
    if not form_editor.remove_field_action("Script_Demo_Button"):
        raise Exception("Failed to remove field script")

    # Save output PDF file
    form_editor.save(output_file_name)
```
