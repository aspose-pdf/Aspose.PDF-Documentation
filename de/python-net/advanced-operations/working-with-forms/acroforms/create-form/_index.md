---
title: AcroForm erstellen - Ausfüllbares PDF in Python erstellen
linktitle: AcroForm erstellen
type: docs
weight: 10
url: /de/python-net/create-form/
description: Erstellen Sie AcroForm‑Felder von Grund auf in PDF‑Dokumenten mithilfe von Aspose.PDF für Python via .NET.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Wie man ein AcroForm in PDF mit Python erstellt
Abstract: Dieser Artikel erklärt, wie man AcroForm‑Felder in PDF‑Dokumenten mithilfe von Aspose.PDF for Python via .NET erstellt. Er behandelt die grundlegende Feldanlage mit TextBoxField, die Anpassung des Erscheinungsbildes von Mehrfach‑Widget‑Textfeldern sowie zusätzliche Feldtypen wie Radio‑Buttons, Kombinationsfelder, Kontrollkästchen, Listenfelder, Signaturfelder und Barcode‑Felder. Diese Beispiele helfen Ihnen, interaktive PDF‑Formulare für die Datenerfassung und Document‑Automatisierungs‑Workflows zu erstellen.
---

## Formular von Grund auf erstellen

### FormField zu einem PDF-Dokument hinzufügen

Der [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) Klasse bietet eine Sammlung mit dem Namen [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/) die Ihnen hilft, Formularfelder in einem PDF‑Dokument zu verwalten.

Um ein Formularfeld hinzuzufügen:

1. Erstellen Sie das Formularfeld, das Sie hinzufügen möchten.
1. Rufen Sie die Form-Sammlung auf [hinzufügen](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/#methods) Methode.

### TextBoxField hinzufügen

Das folgende Beispiel zeigt, wie man ein [TextBoxField](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/).

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

### Mehrfach-Widget-Textfeld im PDF

Erstellen Sie ein Textfeld-Formularfeld mit mehreren Widget-Darstellungen in einem PDF mit Python und Aspose.PDF. Es platziert mehrere Texteingabebereiche auf einer Seite, wendet unterschiedliche Schriftarten und Farben auf jedes Widget an, passt die Ränder an und legt die Hintergrundgestaltung für ein interaktives PDF-Formular fest.

1. Neues PDF-Dokument erstellen.
1. Definieren Sie Textfeldpositionen.
1. Erstelle verschiedene Standardauftritte.
1. Textfeld erstellen.
1. Erscheinungsbild auf jedes Widget anwenden.
1. Randstil anpassen.
1. Feld zum Formular hinzufügen.
1. PDF-Datei speichern.

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

## Andere Formularfelder hinzufügen

Die folgenden Code‑Snippets zeigen, wie verschiedene Feldtypen wie Optionsfelder, Kombinationsfelder, Kontrollkästchen, Listboxen, Signaturfelder und Barcode‑Felder hinzugefügt werden. Jede Funktion erstellt ein neues PDF‑Dokument, fügt ein Ziel‑Feld mit ausgewählten Optionen hinzu und speichert die aktualisierte Datei.

1. Radio-Button-Feld hinzufügen
1. Combo-Box-Feld hinzufügen
1. Checkbox-Feld hinzufügen
1. Listbox-Feld hinzufügen
1. Signaturfeld hinzufügen
1. Barcode-Feld hinzufügen

### Radio-Button-Feld hinzufügen

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

### Combo-Box-Feld hinzufügen

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

### Checkbox-Feld hinzufügen

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

### Listbox-Feld hinzufügen

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

### Signaturfeld hinzufügen

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

### Barcode-Feld hinzufügen

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

## Verwandte Themen

- [AcroForm ausfüllen](/pdf/de/python-net/fill-form/)
- [Extrahiere AcroForm](/pdf/de/python-net/extract-form/)
- [AcroForm ändern](/pdf/de/python-net/modifying-form/)
- [Formulardaten importieren und exportieren](/pdf/de/python-net/import-export-form-data/)
