---
title: ListBox-Feld erstellen
type: docs
weight: 30
url: /de/python-net/create-listbox-field/
description: Erfahren Sie, wie Sie programmgesteuert ein ListBox-Formularfeld zu einem PDF-Dokument hinzufügen können, indem Sie Aspose.PDF für Python verwenden. Diese Anleitung zeigt, wie Sie ein ListBox-Feld einfügen, auswählbare Elemente definieren und die aktualisierte PDF-Datei speichern.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ein ListBox-Feld in einem PDF mit Aspose.PDF für Python erstellen
Abstract: PDF-Formulare ermöglichen es Benutzern, mit Dokumenten zu interagieren, indem sie Optionen auswählen, Daten eingeben und Informationen digital übermitteln. Ein ListBox-Feld lässt Benutzer einen oder mehrere Werte aus einer sichtbaren Optionsliste auswählen. In diesem Tutorial lernen Sie, wie Sie ein ListBox-Feld in einem PDF mithilfe der FormEditor-Klasse in Aspose.PDF für Python erstellen und es mit vordefinierten Elementen füllen.
---

PDF-Formulare werden häufig für Anträge, Umfragen und Registrierungsdokumente verwendet. Ein ListBox-Feld zeigt mehrere Optionen gleichzeitig an, was es den Benutzern erleichtert, Elemente aus einer Liste zu prüfen und auszuwählen.

Der [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) Die Klasse bietet Funktionalität zum Hinzufügen verschiedener interaktiver Felder, einschließlich ListBox-Elementen.

1. Laden Sie ein vorhandenes PDF-Dokument.
1. Definieren Sie eine Liste auswählbarer Optionen.
1. Fügen Sie ein ListBox-Feld zu einer bestimmten Seite hinzu.
1. Legen Sie einen standardmäßig ausgewählten Wert fest.
1. Speichern Sie das aktualisierte PDF-Dokument.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_listbox_field(infile, outfile):
    """Create ListBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add ListBox field to PDF form
    pdf_form_editor.items = ["Australia", "New Zealand", "Malaysia"]
    pdf_form_editor.add_field(
        pdf_facades.FieldType.LIST_BOX, "listbox1", "Australia", 1, 230, 398, 350, 514
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
