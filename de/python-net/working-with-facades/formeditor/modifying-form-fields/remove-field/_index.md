---
title: Feld entfernen
type: docs
weight: 60
url: /de/python-net/remove-field/
description: Dieses Beispiel zeigt, wie das Feld 'Country' aus einem PDF-Formular mit der Methode 'remove_field' der Klasse 'FormEditor' gelöscht wird.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ein Formularfeld aus einem PDF-Dokument mit Python entfernen
Abstract: Dieses Beispiel demonstriert, wie ein bestehendes Formularfeld aus einem PDF-Dokument mit Aspose.PDF for Python entfernt wird. Der Code lädt eine PDF-Datei, löscht das angegebene Feld mit der Klasse FormEditor und speichert das aktualisierte Dokument.
---

PDF-Formulare können Felder enthalten, die aufgrund von Designänderungen oder Workflow-Updates nicht mehr benötigt werden. Mit Aspose.PDF for Python können Entwickler bestimmte Formularfelder programmgesteuert einfach entfernen.

Der [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) Die Klasse in Aspose.PDF bietet die Methode 'remove_field', die es Entwicklern ermöglicht, ein Formularfeld anhand seines Namens zu löschen.

1. Laden Sie das PDF-Dokument.
1. Erstellen Sie ein FormEditor-Objekt.
1. Binden Sie das PDF an den FormEditor.
1. Entfernen Sie das angegebene Formularfeld.
1. Speichern Sie das aktualisierte Dokument.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Remove field from document
    form_editor.remove_field("Country")
    # Save updated document
    form_editor.save(outfile)
```
