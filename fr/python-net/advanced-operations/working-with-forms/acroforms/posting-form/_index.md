---
title: Publication de formulaires PDF via Python
linktitle: Publication de formulaires
type: docs
weight: 75
url: /fr/python-net/posting-form/
description: Ajoutez des boutons d’envoi et des actions de soumission aux AcroForms PDF en utilisant Aspose.PDF for Python via .NET.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment ajouter des boutons d’envoi et des actions de soumission de formulaire à un PDF en utilisant Python
Abstract: Cet article présente deux approches pour ajouter une fonctionnalité d’envoi aux formulaires PDF en utilisant Aspose.PDF for Python via .NET. Vous pouvez ajouter un bouton d’envoi prêt à l’emploi via FormEditor ou créer un champ de bouton personnalisé avec SubmitFormAction pour un contrôle avancé. Ces modèles aident à intégrer les formulaires PDF aux points de terminaison de traitement de formulaires côté serveur.
---

## Ajouter un bouton d’envoi avec FormEditor

L'extrait de code suivant montre comment ajouter un bouton de soumission à un formulaire PDF en utilisant la classe FormEditor dans Aspose.PDF for Python via .NET. Le bouton est configuré pour envoyer les données du formulaire à une URL spécifiée lorsqu'il est cliqué.

1. Créer un `FormEditor` objet.
1. Ajoutez un bouton de soumission à la page cible.
1. Définissez l'URL de soumission et les coordonnées du bouton.
1. Enregistrez le PDF mis à jour.

```python
import aspose.pdf as ap

def add_submit_button(input_file_name, output_file_name):
    editor = ap.facades.FormEditor(input_file_name, output_file_name)
    editor.add_submit_btn(
        "submitbutton", 1, "Submit", "http://localhost/testing/show", 100, 450, 150, 475
    )
    editor.save()
```

## Ajouter une action de soumission personnalisée

L'extrait de code suivant explique comment créer un bouton de soumission personnalisé dans un formulaire PDF en utilisant Aspose.PDF for Python via .NET. Le bouton est configuré pour envoyer les données du formulaire à une URL spécifiée lorsqu'il est cliqué.

1. Ouvrez le PDF avec ap.Document().
1. Créer une action de soumission.
1. Définissez l'URL cible et les indicateurs de soumission.
1. Créez un champ bouton et associez son action de clic.
1. Ajoutez le bouton au formulaire.
1. Enregistrez le PDF mis à jour.

```python
import aspose.pdf as ap

def add_submit_action(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    submit_action = ap.annotations.SubmitFormAction()
    submit_action.url = ap.FileSpecification("http://localhost:3000/submit")
    submit_action.flags = (
        ap.annotations.SubmitFormAction.EXPORT_FORMAT
        | ap.annotations.SubmitFormAction.SUBMIT_COORDINATES
    )

    rect = ap.Rectangle(10, 10, 100, 40)
    submit_button = ap.forms.ButtonField(document.pages[1], rect)
    submit_button.partial_name = "SubmitButton"
    submit_button.value = "Submit"
    submit_button.actions.on_release_mouse_btn = submit_action

    document.form.add(submit_button, 1)
    document.save(output_file_name)
```

## Sujets associés

- [Créer AcroForm](/pdf/fr/python-net/create-form/)
- [Remplir AcroForm](/pdf/fr/python-net/fill-form/)
- [Modification d'AcroForm](/pdf/fr/python-net/modifying-form/)
- [Importer et exporter des données de formulaire](/pdf/fr/python-net/import-export-form-data/)