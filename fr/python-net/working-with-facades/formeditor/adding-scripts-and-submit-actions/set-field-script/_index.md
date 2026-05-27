---
title: Définir le script du champ
type: docs
weight: 30
url: /fr/python-net/set-field-script/
description: Cet extrait de code montre comment attribuer une action JavaScript à un champ de formulaire dans un document PDF à l'aide d'Aspose.PDF for Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Définir les actions JavaScript pour les champs de formulaire PDF à l'aide de Python
Abstract: Cet article explique comment ouvrir un document PDF, affecter du code JavaScript à un champ de formulaire, mettre à jour le script à l'aide de la classe FormEditor, et enregistrer le fichier modifié. L'exemple montre comment les scripts existants peuvent être remplacés afin de modifier le comportement des champs de formulaire.
---

Les formulaires PDF interactifs s'appuient souvent sur JavaScript pour effectuer des tâches telles que l'affichage d'alertes, la validation des entrées ou le déclenchement d'un comportement dynamique du formulaire. Avec Aspose.PDF for Python, les développeurs peuvent gérer ces scripts de manière programmatique.

L'exemple ajoute d'abord une action JavaScript au champ, puis la remplace par un autre script en utilisant la méthode \u0027set_field_script\u0027. Cette approche permet aux développeurs de contrôler ou de mettre à jour le comportement interactif des éléments de formulaire PDF tels que les boutons ou les champs de saisie.

Le champ de formulaire utilisé dans cet exemple s'appelle 'Script_Demo_Button', qui représente généralement un bouton qui exécute le script assigné lorsqu'il est déclenché.

En utilisant le [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) classe de la [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) module, les développeurs peuvent gérer de manière programmatique les actions JavaScript associées aux champs de formulaire :

1. Ouvrez un document de formulaire PDF existant.
1. Ajoutez une action JavaScript à un champ de formulaire.
1. Définissez (remplacez) l'action JavaScript avec un nouveau script.
1. Enregistrer le document PDF modifié.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_script(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Add JavaScript action to the field
    form_editor.add_field_script(
        "Script_Demo_Button", "app.alert('Script 1 has been executed');"
    )

    # Set JavaScript action for the field
    form_editor.set_field_script(
        "Script_Demo_Button", "app.alert('Script 2 has been executed');"
    )

    # Save output PDF file
    form_editor.save(output_file_name)
```
