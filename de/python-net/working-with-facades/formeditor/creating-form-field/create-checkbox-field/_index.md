---
title: CheckBox-Feld erstellen
type: docs
weight: 10
url: /de/python-net/create-checkbox-field/
description: Erfahren Sie, wie Sie programmgesteuert ein Checkbox-Formularfeld zu einem PDF-Dokument hinzufügen, indem Sie Aspose.PDF for Python verwenden. Dieses Handbuch zeigt, wie die FormEditor-Klasse verwendet wird, um eine interaktive Checkbox in eine vorhandene PDF-Datei einzufügen und das aktualisierte Dokument zu speichern.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ein Checkbox-Feld in einem PDF mit Aspose.PDF for Python erstellen
Abstract: Interaktive Formularfelder ermöglichen es Benutzern, PDF-Dokumente digital auszufüllen und zu bearbeiten. In diesem Tutorial lernen Sie, wie Sie ein Checkbox-Feld zu einem PDF mithilfe der Aspose.PDF Python API hinzufügen. Das Beispiel zeigt, wie ein vorhandenes PDF-Dokument gebunden, ein Checkbox-Formularfeld an angegebenen Koordinaten erstellt und die geänderte Datei gespeichert wird.
---

PDF-Formulare werden häufig verwendet, um Benutzereingaben in Dokumenten wie Anträgen, Umfragen und Vereinbarungen zu erfassen. Ein Checkbox-Feld ermöglicht es Benutzern, eine Option innerhalb eines Formulars auszuwählen oder abzuwählen.

Mit Aspose.PDF for Python können Entwickler PDF-Formulare programmgesteuert manipulieren. Der [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) Klasse stellt Methoden zum Hinzufügen, Bearbeiten und Verwalten von Formularfeldern innerhalb eines PDF-Dokuments bereit.

1. Laden Sie eine vorhandene PDF-Datei.
1. Rufen Sie die Methode 'add_field()' mit dem Parameter 'FieldType.CHECK_BOX' auf, um das Kontrollkästchen zu erstellen und seine Position anzugeben.
1. Definieren Sie den Feldnamen, die Beschriftung und die Position.
1. Speichern Sie das aktualisierte PDF-Dokument.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_checkbox_field(infile, outfile):
    """Create CheckBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add CheckBox field to PDF form
    pdf_form_editor.add_field(
        pdf_facades.FieldType.CHECK_BOX,
        "checkbox1",
        "Check Box 1",
        1,
        240,
        498,
        256,
        514,
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
