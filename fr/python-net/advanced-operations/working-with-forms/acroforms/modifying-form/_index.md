---
title: Modification d'AcroForm
linktitle: Modification d'AcroForm
type: docs
weight: 45
url: /fr/python-net/modifying-form/
description: Modifier les champs AcroForm dans les documents PDF en utilisant Aspose.PDF for Python via .NET, y compris la suppression du texte, la définition de limites, le style des champs et la suppression des champs.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gestion et personnalisation des champs de Form PDF
Abstract: Cet article présente des exemples pratiques pour modifier les champs AcroForm en utilisant Aspose.PDF for Python via .NET. Il couvre la suppression du texte du contenu de formulaire Typewriter, la définition et la lecture des limites de caractères des champs texte, l’application d’une apparence de Font personnalisée, et la suppression des champs par nom. Ces flux de travail prennent en charge les tâches courantes de maintenance de formulaires dans les pipelines automatisés de traitement PDF.
---

## Effacer le texte dans le Form

Cet exemple montre comment effacer le texte des champs de formulaire Typewriter dans un PDF en utilisant Aspose.PDF for Python via .NET. Il parcourt la première page du PDF, identifie les formulaires Typewriter, supprime leur contenu et enregistre le document mis à jour. Cette approche est utile pour réinitialiser ou assainir les champs de formulaire avant de redistribuer un PDF.

1. Chargez le document PDF d'entrée.
1. Accédez aux formulaires de la première page.
1. Parcourir chaque formulaire et vérifier s'il s'agit d'un `Typewriter` formulaire.
1. Utilisez TextFragmentAbsorber pour trouver les fragments de texte dans le formulaire.
1. Effacez le texte de chaque fragment.
1. Enregistrez le PDF modifié dans le fichier de sortie.

```python
import aspose.pdf as ap


def clear_text_in_form(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    forms = document.pages[1].resources.forms

    for form in forms:
        if form.it == "Typewriter" and form.subtype == "Form":
            absorber = ap.text.TextFragmentAbsorber()
            absorber.visit(form)

            for fragment in absorber.text_fragments:
                fragment.text = ""

    document.save(output_file_name)
```

## Définir la limite du champ

Utiliser `set_field_limit(field, limit)` de `FormEditor` définir le nombre maximal de caractères autorisés dans un champ texte.

1. Créer un `FormEditor` objet.
1. Lier le PDF d'entrée.
1. Définissez la limite du champ pour un champ cible.
1. Enregistrez le PDF mis à jour.

```python
import aspose.pdf as ap


def set_field_limit(input_file_name, output_file_name):
    form = ap.facades.FormEditor()
    form.bind_pdf(input_file_name)
    form.set_field_limit("First Name", 15)
    form.save(output_file_name)
```

## Obtenir la limite du champ

Vous pouvez également lire la limite de caractères d'un champ texte.

1. Chargez le document PDF.
1. Accédez au champ de formulaire cible.
1. Assurez-vous que le champ est un `TextBoxField`.
1. Lire et imprimer `max_len`.

```python
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable


def get_field_limit(input_file_name):
    document = ap.Document(input_file_name)
    if is_assignable(document.form[1], ap.forms.TextBoxField):
        text_box_field = cast(ap.forms.TextBoxField, document.form[1])
        print(f"Limit: {text_box_field.max_len}")
```

## Définir une police personnalisée pour le champ du formulaire

Cet exemple définit une apparence par défaut personnalisée pour un champ de zone de texte, incluant la police, la taille et la couleur.

1. Chargez le document PDF.
1. Accédez au champ cible et vérifiez son type.
1. Trouver la police dans `FontRepository`.
1. Appliquer un nouveau `DefaultAppearance`.
1. Enregistrez le PDF mis à jour.

```python
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable


def set_form_field_font(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    if is_assignable(document.form[1], ap.forms.TextBoxField):
        text_box_field = cast(ap.forms.TextBoxField, document.form[1])
        font = ap.text.FontRepository.find_font("Calibri")
        text_box_field.default_appearance = ap.annotations.DefaultAppearance(
            font, 10, ap.Color.black.to_rgb()
        )

    document.save(output_file_name)
```

## Supprimer des champs dans un formulaire existant

Ce code supprime un champ de formulaire spécifique (par son nom) d'un document PDF et enregistre le fichier mis à jour en utilisant Aspose.PDF for Python via .NET.

1. Chargez le document PDF.
1. Supprimer un champ de formulaire par son nom.
1. Enregistrez le PDF mis à jour.

```python
import aspose.pdf as ap


def delete_form_field(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    document.form.delete("First Name")
    document.save(output_file_name)
```

## Sujets associés

- [Créer AcroForm](/pdf/fr/python-net/create-form/)
- [Remplir AcroForm](/pdf/fr/python-net/fill-form/)
- [Extraire AcroForm](/pdf/fr/python-net/extract-form/)
- [Importer et exporter des données de formulaire](/pdf/fr/python-net/import-export-form-data/)
