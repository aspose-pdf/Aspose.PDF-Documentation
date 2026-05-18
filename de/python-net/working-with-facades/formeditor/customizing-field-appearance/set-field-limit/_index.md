---
title: Feldlimit festlegen
type: docs
weight: 80
url: /de/python-net/set-field-limit/
description: Dieses Beispiel zeigt, wie man mit Aspose.PDF für Python ein maximales Zeichenlimit für ein Formularfeld in einem PDF-Dokument festlegt.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Maximales Zeichenlimit für PDF-Formularfelder mit Python festlegen
Abstract: Dieses Beispiel demonstriert das Festlegen des Zeichenlimits für ein Feld mit dem Namen "Last Name" auf 10 Zeichen, wodurch sichergestellt wird, dass Benutzer nicht mehr als das angegebene Limit eingeben können.
---

Formularfelder in PDF-Dokumenten können Eingabebeschränkungen benötigen, um die korrekte Formatierung beizubehalten. Mit Aspose.PDF für Python können Entwickler programmgesteuert ein maximales Zeichenlimit für ein Feld festlegen.

Der [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) Die Klasse stellt die Methode 'set_field_limit' bereit, um die maximale Eingabelänge für ein Feld zu definieren.

1. Öffnen Sie ein vorhandenes PDF-Formular.
1. Erstellen Sie ein FormEditor-Objekt.
1. Setzen Sie das maximale Zeichenlimit für das Feld "Last Name".
1. Speichere das aktualisierte PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_limit(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field limit to 10
    if not form_editor.set_field_limit("Last Name", 10):
        raise Exception(
            "Failed to set field limit. Field may not support specified limit."
        )

    # Save updated document
    form_editor.save(outfile)
```
