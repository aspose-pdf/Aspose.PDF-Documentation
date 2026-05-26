---
title: Définir l'URL de soumission
type: docs
weight: 40
url: /fr/python-net/set-submit-url/
description: Cet exemple montre comment configurer une action de soumission pour un champ bouton dans un formulaire PDF en utilisant Aspose.PDF for Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Définir une URL de soumission pour un bouton de formulaire PDF en utilisant Python
Abstract: Cet article explique comment ouvrir un formulaire PDF existant, définir une URL de soumission pour un champ bouton en utilisant la classe FormEditor, vérifier que l'opération réussit et enregistrer le document PDF mis à jour.
---

Les formulaires PDF peuvent être conçus pour soumettre leurs données à un serveur web lorsqu'un utilisateur clique sur un bouton de soumission. En utilisant Aspose.PDF for Python, les développeurs peuvent configurer programmétiquement une action de soumission pour les champs de formulaire.
En définissant une URL de soumission, le formulaire peut envoyer les données saisies par l'utilisateur à un serveur lorsque le bouton est cliqué. Cette fonctionnalité est utile pour les flux de travail où les formulaires PDF doivent soumettre des informations aux applications web, aux bases de données ou aux services de traitement.

En utilisant le [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) classe de la [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) module, les développeurs peuvent attribuer de manière programmatique une URL de soumission à un champ bouton dans un formulaire PDF existant.

1. Ouvrez un formulaire PDF existant.
1. Localisez un champ bouton nommé Script_Demo_Button.
1. Attribuez une URL où les données du formulaire seront soumises.
1. Vérifiez que l'action a été appliquée avec succès.
1. Enregistrez le document PDF mis à jour.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_submit_url(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Set license
    set_license()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Set submit URL for the button
    if not form_editor.set_submit_url(
        "Script_Demo_Button", "http://www.example.com/submit"
    ):
        raise Exception("Failed to set submit URL")

    # Save output PDF file
    form_editor.save(output_file_name)
```
