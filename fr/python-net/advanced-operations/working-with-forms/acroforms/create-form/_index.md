---
title: Créer AcroForm - Créer un PDF remplissable en Python
linktitle: Créer AcroForm
type: docs
weight: 10
url: /fr/python-net/create-form/
description: Créez des champs AcroForm à partir de zéro dans les documents PDF en utilisant Aspose.PDF for Python via .NET.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment créer un AcroForm dans un PDF en utilisant Python
Abstract: Cet article explique comment créer des champs AcroForm dans des documents PDF en utilisant Aspose.PDF for Python via .NET. Il couvre la création de champs de base avec TextBoxField, la personnalisation de l'apparence des zones de texte à plusieurs widgets, ainsi que des types de champs supplémentaires tels que les boutons radio, les listes déroulantes, les cases à cocher, les listes, les champs de signature et les champs de code‑barres. Ces exemples vous aident à créer des formulaires PDF interactifs pour la collecte de données et les flux de travail d'automatisation de documents.
---

## Créer Form à partir de zéro

### Ajouter FormField dans un Document PDF

Le [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) la classe fournit une collection nommée [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/) qui vous aide à gérer les champs de formulaire dans un document PDF.

Pour ajouter un champ de formulaire :

1. Créez le champ de formulaire que vous voulez ajouter.
1. Appelez la collection Form [add](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/#methods) méthode.

### Ajout de TextBoxField

L'exemple suivant montre comment ajouter un [TextBoxField](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/).

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_text_box_field(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    rectangle = ap.Rectangle(10, 600, 110, 620, True)
    text_box_field = ap.forms.TextBoxField(page, rectangle)
    text_box_field.partial_name = "textbox1"
    text_box_field.value = "Text Box"

    text_box_field.default_appearance = ap.annotations.DefaultAppearance(
        "Arial", 10, drawing.Color.dark_blue
    )

    border = ap.annotations.Border(text_box_field)
    border.width = 1
    border.style = ap.annotations.BorderStyle.DASHED
    border.dash = ap.annotations.Dash(3, 3)
    text_box_field.border = border

    text_box_field.characteristics.border = ap.Color.red.to_rgb()
    text_box_field.characteristics.background = ap.Color.yellow.to_rgb()

    document.form.add(text_box_field, 1)
    document.save(output_file_name)
```

### Champ de zone de texte multi-widget dans le PDF

Créer un champ de formulaire de zone de texte avec plusieurs apparences de widget dans un PDF en utilisant Python et Aspose.PDF. Il place plusieurs zones de saisie de texte sur une page, applique différentes polices et couleurs à chaque widget, personnalise les bordures et définit le style d'arrière-plan pour un formulaire PDF interactif.

1. Créer un nouveau Document PDF.
1. Définir les positions des champs de texte.
1. Créer différentes apparences par défaut.
1. Créer un champ de zone texte.
1. Appliquer l'apparence à chaque widget.
1. Personnaliser le style de bordure.
1. Ajouter un champ au formulaire.
1. Enregistrer le fichier PDF.

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_text_box_field_nt(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    rects = [
        ap.Rectangle(10, 600, 110, 620, normalize_coordinates=True),
        ap.Rectangle(10, 630, 110, 650, normalize_coordinates=True),
        ap.Rectangle(10, 660, 110, 680, normalize_coordinates=True),
    ]

    default_appearances = [
        ap.annotations.DefaultAppearance("Arial", 10, drawing.Color.dark_blue),
        ap.annotations.DefaultAppearance("Helvetica", 12, drawing.Color.dark_green),
        ap.annotations.DefaultAppearance(
            ap.text.FontRepository.find_font("Calibri"), 14, drawing.Color.dark_magenta
        ),
    ]

    text_box_field = ap.forms.TextBoxField(page, rects)
    text_box_field.partial_name = "textbox1"
    text_box_field.value = "Some text"

    for i, widget in enumerate(text_box_field):
        widget.default_appearance = default_appearances[i]

    border = ap.annotations.Border(text_box_field)
    border.width = 1
    border.style = ap.annotations.BorderStyle.DASHED
    border.dash = ap.annotations.Dash(3, 3)
    text_box_field.border = border

    text_box_field.characteristics.border = ap.Color.red.to_rgb()
    text_box_field.characteristics.background = ap.Color.yellow.to_rgb()

    document.form.add(text_box_field)
    document.save(output_file_name)
```

## Ajout d'autres champs de formulaire

Les extraits de code suivants montrent comment ajouter différents types de champs, tels que des boutons radio, des boîtes combinées, des cases à cocher, des listes déroulantes, des champs de signature et des champs de code‑barres. Chaque fonction crée un nouveau document PDF, ajoute un champ cible avec les options sélectionnées et enregistre le fichier mis à jour.

1. Ajouter un champ de bouton radio
1. Ajouter un champ Combo Box
1. Ajouter un champ de case à cocher
1. Ajouter un champ de zone de liste
1. Ajouter un champ de signature
1. Ajouter un champ de code-barres

### Ajouter un champ de bouton radio

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_radio_button(output_file_name):
    document = ap.Document()
    document.pages.add()

    radio = ap.forms.RadioButtonField(document.pages[1])
    radio.add_option(
        "Option 1", ap.Rectangle(100, 640, 120, 680, normalize_coordinates=True)
    )
    radio.add_option(
        "Option 2", ap.Rectangle(140, 640, 160, 680, normalize_coordinates=True)
    )

    document.form.add(radio)
    document.save(output_file_name)
```

### Ajouter un champ Combo Box

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_combo_box(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    combo = ap.forms.ComboBoxField(
        page, ap.Rectangle(100, 640, 150, 656, normalize_coordinates=True)
    )
    combo.add_option("Red")
    combo.add_option("Yellow")
    combo.add_option("Green")
    combo.add_option("Blue")
    combo.selected = 3

    document.form.add(combo)
    document.save(output_file_name)
```

### Ajouter un champ de case à cocher

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_checkbox_field_to_pdf(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    checkbox = ap.forms.CheckboxField(
        page, ap.Rectangle(50, 620, 100, 650, normalize_coordinates=True)
    )
    checkbox.characteristics.background = ap.Color.aqua.to_rgb()
    checkbox.style = ap.forms.BoxStyle.CIRCLE

    document.form.add(checkbox)
    document.save(output_file_name)
```

### Ajouter un champ de zone de liste

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_list_box_field_to_pdf(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    list_box = ap.forms.ListBoxField(
        page, ap.Rectangle(50, 650, 100, 700, normalize_coordinates=True)
    )
    list_box.partial_name = "list"
    list_box.add_option("Red")
    list_box.add_option("Green")
    list_box.add_option("Blue")

    document.form.add(list_box)
    document.save(output_file_name)
```

### Ajouter un champ de signature

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_signature_field(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    signature_field = ap.forms.SignatureField(
        page, ap.Rectangle(100, 700, 200, 800, True)
    )
    signature_field.partial_name = "Signature1"
    document.form.add(signature_field)
    document.save(output_file_name)
```

### Ajouter un champ de code-barres

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_barcode_field(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    barcode = ap.forms.BarcodeField(page, ap.Rectangle(100, 700, 200, 740, True))
    barcode.partial_name = "Barcode1"
    barcode.add_barcode("1234567890")
    document.form.add(barcode)
    document.save(output_file_name)
```

## Sujets associés

- [Remplir AcroForm](/pdf/fr/python-net/fill-form/)
- [Extraire AcroForm](/pdf/fr/python-net/extract-form/)
- [Modification d'AcroForm](/pdf/fr/python-net/modifying-form/)
- [Importer et exporter les données du Form](/pdf/fr/python-net/import-export-form-data/)
