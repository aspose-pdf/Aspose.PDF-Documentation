---
title: RadioButton-Feld erstellen
type: docs
weight: 40
url: /de/python-net/create-radiobutton-field/
description: Erfahren Sie, wie Sie programmgesteuert ein Radio-Button-Formularfeld zu einem PDF-Dokument mit Aspose.PDF for Python hinzufügen. Dieses Beispiel zeigt, wie man eine Radio-Button-Gruppe erstellt, auswählbare Optionen definiert und die aktualisierte PDF-Datei speichert.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ein Radio-Button-Feld in einem PDF mit Aspose.PDF for Python erstellen
Abstract: Radio-Buttons werden häufig in PDF-Formularen verwendet, um Benutzern die Auswahl einer Option aus einer vordefinierten Gruppe von Möglichkeiten zu ermöglichen. In diesem Tutorial lernen Sie, wie Sie mit der FormEditor-Klasse in Aspose.PDF for Python ein Radio-Button-Feld in einem PDF erstellen. Das Beispiel zeigt, wie Radio-Button-Elemente definiert, eine Standardauswahl festgelegt und das aktualisierte Dokument gespeichert werden.
---

Interaktive PDF-Formulare ermöglichen es Benutzern, strukturierte Eingaben direkt im Dokument bereitzustellen. Ein Radio-Button-Feld ist nützlich, wenn Benutzer nur eine Option aus mehreren Möglichkeiten auswählen müssen, z. B. ein Land, ein Geschlecht oder eine Präferenz.

Der [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) Die Klasse bietet Methoden zum Erstellen verschiedener Feldtypen, einschließlich Textfelder, Kontrollkästchen, Kombinationsfelder, Listenfelder und Radio-Buttons

1. Laden Sie ein vorhandenes PDF-Dokument.
1. Definieren Sie eine Liste von Radio-Button-Optionen.
1. Fügen Sie ein Radio-Button-Feld zu einer bestimmten Seite hinzu.
1. Legen Sie einen standardmäßig ausgewählten Wert fest.
1. Speichern Sie das modifizierte PDF‑Dokument.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_radiobutton_field(infile, outfile):
    """Create RadioButton field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add RadioButton field to PDF form
    pdf_form_editor.items = ["Australia", "New Zealand", "Malaysia"]
    pdf_form_editor.add_field(
        pdf_facades.FieldType.RADIO, "radiobutton1", "Malaysia", 1, 240, 498, 256, 514
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
