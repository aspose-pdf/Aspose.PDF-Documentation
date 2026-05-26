---
title: Créer un bouton Submit
type: docs
weight: 50
url: /fr/python-net/create-submit-button/
description: Apprenez comment ajouter un bouton Submit à un document PDF de manière programmatique à l'aide d'Aspose.PDF for Python. Ce tutoriel montre comment créer un bouton qui soumet les données du formulaire à une URL spécifiée et enregistre le PDF mis à jour.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Créer un bouton Submit dans un PDF à l'aide d'Aspose.PDF for Python
Abstract: Les boutons Submit dans les formulaires PDF permettent aux utilisateurs d'envoyer les données du formulaire directement à un serveur ou un point de terminaison. Dans ce guide, vous apprendrez comment ajouter un champ Submit Button à un PDF en utilisant la classe FormEditor d'Aspose.PDF for Python. L'exemple montre comment configurer le nom du bouton, son libellé, l'URL cible et la position, puis enregistrer le document PDF mis à jour.
---

Les formulaires PDF interactifs exigent souvent que les utilisateurs soumettent leurs saisies pour traitement, par exemple l'envoi de résultats d'enquête, de formulaires de demande ou de données de retour. Un champ Submit Button fournit cette fonctionnalité en liant le bouton à un point de terminaison web.

Le [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) La classe permet d'ajouter des boutons, des cases à cocher, des boutons radio, des champs de texte et d'autres contrôles de formulaire.

1. Chargez un document PDF existant.
1. Ajouter un champ Bouton d'envoi à une page spécifique.
1. Définir le libellé du bouton et l'URL cible de soumission.
1. Enregistrer le PDF mis à jour avec le nouveau bouton.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_submit_button(infile, outfile):
    """Create Submit Button in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add Submit Button to PDF form
    pdf_form_editor.add_submit_btn(
        "submitbtn1",
        1,
        "Submit Button",
        "http://example.com/submit",
        100,
        450,
        200,
        470,
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
