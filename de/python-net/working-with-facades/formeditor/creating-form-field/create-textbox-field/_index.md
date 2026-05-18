---
title: TextBox-Feld erstellen
type: docs
weight: 60
url: /de/python-net/create-textbox-field/
description: Erfahren Sie, wie Sie TextBox-Felder programmgesteuert zu einem PDF-Dokument mit Aspose.PDF for Python hinzufügen. Dieses Tutorial zeigt, wie mehrere Textfelder eingefügt, Standardwerte festgelegt und das aktualisierte PDF-Dokument gespeichert werden.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: TextBox-Felder in einem PDF mit Aspose.PDF for Python erstellen
Abstract: TextBox-Felder in PDF-Formularen ermöglichen es Benutzern, Text einzugeben und zu bearbeiten, wodurch Dokumente interaktiv und benutzerfreundlich werden. In diesem Tutorial lernen Sie, wie Sie TextBox-Formularfelder in einem PDF mit der FormEditor-Klasse in Aspose.PDF for Python erstellen. Das Beispiel demonstriert das Hinzufügen mehrerer Felder, das Festlegen von Standardwerten und das Speichern des modifizierten PDFs.
---

PDF-Formulare erfordern häufig Texteingaben von Benutzern, wie Namen, Adressen oder Kommentare. TextBox-Felder ermöglichen diese Funktionalität, indem sie bearbeitbare Felder direkt im PDF-Dokument bereitstellen.

Der [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) Die Klasse ermöglicht das Hinzufügen von Textfeldern, Kontrollkästchen, Optionsschaltern, Listboxen, Kombinationsfeldern und Schaltflächen, wodurch das Erstellen interaktiver PDFs erleichtert wird.

1. Laden Sie ein vorhandenes PDF-Dokument.
1. Fügen Sie mehrere TextBox-Felder für Benutzereingaben hinzu.
1. Legen Sie Standardwerte für jedes Feld fest.
1. Speichern Sie das aktualisierte PDF-Dokument.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_textbox_field(infile, outfile):
    """Create TextBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add TextBox field to PDF form
    pdf_form_editor.add_field(
        pdf_facades.FieldType.TEXT, "first_name", "Alexander", 1, 50, 570, 150, 590
    )
    pdf_form_editor.add_field(
        pdf_facades.FieldType.TEXT, "last_name", "Smith", 1, 235, 570, 330, 590
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
