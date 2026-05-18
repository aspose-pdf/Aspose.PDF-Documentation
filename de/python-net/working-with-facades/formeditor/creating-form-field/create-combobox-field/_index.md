---
title: ComboBox-Feld erstellen
type: docs
weight: 20
url: /de/python-net/create-combobox-field/
description: Prüfen Sie, wie Sie programmgesteuert ein ComboBox (Dropdown-Liste) Feld zu einem PDF-Dokument mit Aspose.PDF for Python hinzufügen. Dieses Beispiel zeigt, wie man ein ComboBox-Formularfeld einfügt, auswählbare Elemente hinzufügt und die aktualisierte PDF-Datei speichert.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Erstellen Sie ein ComboBox-Feld in einem PDF mit Aspose.PDF for Python
Abstract: Interaktive Formularfelder machen PDFs dynamischer und benutzerfreundlicher. Ein ComboBox-Feld ermöglicht es Benutzern, eine Option aus einer vordefinierten Dropdown-Liste auszuwählen. In diesem Tutorial lernen Sie, wie Sie ein ComboBox in einem PDF mithilfe der FormEditor-Klasse in Aspose.PDF for Python erstellen, es mit Optionen füllen und das geänderte Dokument speichern.
---

PDF-Formulare werden häufig zum Sammeln strukturierter Informationen in digitalen Dokumenten wie Anträgen, Umfragen und Registrierungsformularen verwendet. Ein ComboBox-Feld bietet eine bequeme Möglichkeit für Benutzer, aus einer Liste vordefinierter Werte auszuwählen, wobei das Formular kompakt und übersichtlich bleibt.

Der [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) Die Klasse ermöglicht es Ihnen, verschiedene Feldtypen zu erstellen und zu verwalten, darunter Textfelder, Checkboxen, Optionsschalter und Dropdown-Listen.

1. Laden Sie ein vorhandenes PDF-Dokument.
1. Fügen Sie ein ComboBox-Feld mit der Methode 'add_field()' und dem Parameter 'FieldType.COMBO_BOX' hinzu.
1. Verwenden Sie die Methode 'add_list_item()', um auswählbare Optionen in die Dropdown-Liste einzufügen.
1. Speichern Sie das aktualisierte PDF-Dokument.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_combobox_field(infile, outfile):
    """Create ComboBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add ComboBox field to PDF form
    pdf_form_editor.add_field(
        pdf_facades.FieldType.COMBO_BOX, "combobox1", "Australia", 1, 230, 498, 350, 514
    )
    pdf_form_editor.add_list_item("combobox1", ["Australia", "Australia"])
    pdf_form_editor.add_list_item("combobox1", ["New Zealand", "New Zealand"])

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
