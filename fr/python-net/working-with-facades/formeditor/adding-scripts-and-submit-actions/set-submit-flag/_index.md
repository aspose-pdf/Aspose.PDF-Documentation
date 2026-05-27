---
title: Définir le drapeau de soumission
type: docs
weight: 50
url: /fr/python-net/set-submit-flag/
description: Apprenez comment définir programmétiquement un drapeau de soumission pour un bouton de formulaire PDF à l'aide d'Aspose.PDF for Python. Cela permet au bouton de soumettre les données du formulaire dans un format spécifique, tel que XFDF, lorsqu'il est cliqué par l'utilisateur.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Définir le drapeau de soumission pour un bouton de formulaire PDF à l'aide d'Aspose.PDF for Python
Abstract: Les formulaires PDF peuvent être configurés pour soumettre les données du formulaire à un serveur ou point de terminaison dans différents formats. En définissant un drapeau de soumission sur le champ bouton, les développeurs peuvent préciser comment les données sont envoyées. Ce tutoriel montre comment utiliser la classe FormEditor pour définir un drapeau de soumission pour un bouton de soumission existant dans un document PDF et enregistrer le fichier mis à jour.
---

Les formulaires PDF incluent souvent des boutons de soumission pour envoyer les saisies de l'utilisateur à un serveur. Le drapeau de soumission détermine le format des données envoyées (par ex., XFDF, FDF, HTML).

1. Lier un document PDF.
1. Accédez à un bouton de soumission existant.
1. Définissez le drapeau de soumission pour le format souhaité.
1. Enregistrez le document PDF mis à jour.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_submit_flag(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Set submit flag for the form
    form_editor.set_submit_flag("Script_Demo_Button", ap.facades.SubmitFormFlag.XFDF)

    # Save output PDF file
    form_editor.save(output_file_name)
```
