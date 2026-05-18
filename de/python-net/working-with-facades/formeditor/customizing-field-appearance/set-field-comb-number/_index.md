---
title: Feld‑Kombinationszahl festlegen
type: docs
weight: 70
url: /de/python-net/set-field-comb-number/
description: Dieses Beispiel zeigt, wie man mithilfe von Aspose.PDF für Python die Kombinationszahl für ein PDF-Formularfeld festlegt.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Kombinationszahl für PDF-Formularfelder mit Python festlegen
Abstract: Mit Aspose.PDF für Python können Entwickler programmgesteuert die Anzahl der Kästchen (Kombinationszahl) für ein Formularfeld festlegen, um eine Eingabe fester Länge zu erzwingen. Dieser Artikel demonstriert das Festlegen der Kombinationszahl für ein Feld mit dem Namen "PIN".
---

Die Kombinationszahl definiert, wie der Inhalt des Feldes in gleichmäßig verteilte Kästchen aufgeteilt wird, was oft für PIN‑Codes, Seriennummern oder andere Eingabefelder fester Länge verwendet wird. Der Code öffnet ein vorhandenes PDF, legt die Kombinationszahl für ein Feld fest und speichert das geänderte Dokument.

Der [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) Die Klasse stellt die Methode ‘set_field_comb_number’ bereit, um die Anzahl der Kästchen (Zeichen) in einem Formularfeld zu definieren.

1. Öffnen Sie ein vorhandenes PDF-Formular.
1. Erstellt ein FormEditor-Objekt.
1. Setzt die Kombinationszahl eines Feldes namens "PIN" auf 5.
1. Speichern Sie das aktualisierte Dokument.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_comb_number(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field comb number to 5
    form_editor.set_field_comb_number("PIN", 5)

    # Save updated document
    form_editor.save(outfile)
```
