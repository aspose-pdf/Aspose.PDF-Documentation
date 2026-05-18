---
title: AcroForm ändern
linktitle: AcroForm ändern
type: docs
weight: 45
url: /de/python-net/modifying-form/
description: AcroForm-Felder in PDF-Dokumenten mit Aspose.PDF for Python via .NET ändern, einschließlich Text löschen, Grenzen festlegen, Felder stylen und Felder entfernen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Verwalten und Anpassen von PDF-Formularfeldern
Abstract: Dieser Artikel präsentiert praktische Beispiele zum Ändern von AcroForm-Feldern mit Aspose.PDF for Python via .NET. Er behandelt das Löschen von Text aus Typewriter-Formularinhalten, das Festlegen und Auslesen von Zeichenlimits für Textfelder, das Anwenden benutzerdefinierter Schriftartdarstellungen und das Entfernen von Feldern nach Namen. Diese Workflows unterstützen gängige Formularwartungsaufgaben in automatisierten PDF-Verarbeitungspipelines.
---

## Text im Formular löschen

Dieses Beispiel demonstriert, wie man Text aus Typewriter-Formularfeldern in einem PDF mit Aspose.PDF for Python via .NET löscht. Es scannt die erste Seite des PDFs, identifiziert Typewriter-Formulare, entfernt deren Inhalt und speichert das aktualisierte Dokument. Dieser Ansatz ist nützlich, um Formularfelder zurückzusetzen oder zu bereinigen, bevor ein PDF erneut verteilt wird.

1. Laden Sie das Eingabe‑PDF‑Dokument.
1. Greifen Sie auf die Formulare auf der ersten Seite zu.
1. Iterieren Sie über jedes Formular und prüfen Sie, ob es ein `Typewriter` Form.
1. Verwenden Sie TextFragmentAbsorber, um Textfragmente im Form zu finden.
1. Löschen Sie den Text jedes Fragments.
1. Speichern Sie das modifizierte PDF in die Ausgabedatei.

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

## Feldlimit festlegen

Verwenden `set_field_limit(field, limit)` von `FormEditor` um die maximal zulässige Anzahl von Zeichen in einem Textfeld festzulegen.

1. Erstelle ein `FormEditor` Objekt.
1. Binden Sie das Eingabe-PDF.
1. Legen Sie die Feldbegrenzung für ein Zielfeld fest.
1. Speichere das aktualisierte PDF.

```python
import aspose.pdf as ap


def set_field_limit(input_file_name, output_file_name):
    form = ap.facades.FormEditor()
    form.bind_pdf(input_file_name)
    form.set_field_limit("First Name", 15)
    form.save(output_file_name)
```

## Feldlimit abrufen

Sie können das Zeichenlimit auch aus einem Textfeld auslesen.

1. Laden Sie das PDF-Dokument.
1. Greifen Sie auf das Zielformularfeld zu.
1. Stellen Sie sicher, dass das Feld ein `TextBoxField`.
1. Lesen und drucken `max_len`.

```python
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable


def get_field_limit(input_file_name):
    document = ap.Document(input_file_name)
    if is_assignable(document.form[1], ap.forms.TextBoxField):
        text_box_field = cast(ap.forms.TextBoxField, document.form[1])
        print(f"Limit: {text_box_field.max_len}")
```

## Benutzerdefinierte Schriftart für das Formularfeld festlegen

Dieses Beispiel legt ein benutzerdefiniertes Standardaussehen für ein Textfeld fest, einschließlich Schriftart, Größe und Farbe.

1. Laden Sie das PDF-Dokument.
1. Greifen Sie auf das Zielfeld zu und prüfen Sie dessen Typ.
1. Finde die Schrift in `FontRepository`.
1. Eine neue anwenden `DefaultAppearance`.
1. Speichere das aktualisierte PDF.

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

## Felder in einem vorhandenen Formular entfernen

Dieser Code entfernt ein bestimmtes Formularfeld (nach seinem Namen) aus einem PDF-Dokument und speichert die aktualisierte Datei mit Aspose.PDF for Python via .NET.

1. Laden Sie das PDF-Dokument.
1. Ein Formularfeld nach Namen löschen.
1. Speichere das aktualisierte PDF.

```python
import aspose.pdf as ap


def delete_form_field(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    document.form.delete("First Name")
    document.save(output_file_name)
```

## Verwandte Themen

- [AcroForm erstellen](/pdf/de/python-net/create-form/)
- [AcroForm ausfüllen](/pdf/de/python-net/fill-form/)
- [Extrahiere AcroForm](/pdf/de/python-net/extract-form/)
- [Formulardaten importieren und exportieren](/pdf/de/python-net/import-export-form-data/)
