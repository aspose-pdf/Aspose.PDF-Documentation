---
title: Versuchen Sie, zwei PDF-Dateien zu verketten
type: docs
weight: 90
url: /de/python-net/try-concatenate-two-files/
description: Verketten Sie zwei PDF-Dateien mit Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Zwei PDF-Dateien in Python sicher zusammenführen ohne Ausnahmen
Abstract: Erfahren Sie, wie Sie zwei PDF-Dateien sicher mit Aspose.PDF for Python verketten. Die Methode try_concatenate fügt die Dateien zusammen, ohne Ausnahmen zu werfen, und ermöglicht eine elegante Fehlerbehandlung für den Fall, dass der Vorgang fehlschlägt.
---

Das Zusammenführen zweier PDF-Dateien kann manchmal aufgrund von Dateibeschädigungen, inkompatiblen Formaten oder anderen Problemen fehlschlagen. Mit Aspose.PDF for Python ermöglicht Ihnen die Methode try_concatenate der Klasse PdfFileEditor, das Zusammenführen zweier PDFs sicher zu versuchen. Scheitert der Vorgang, gibt sie False zurück, anstatt eine Ausnahme zu werfen, und gibt Ihnen die vollständige Kontrolle über die Fehlerbehandlung in automatisierten Workflows oder Batch‑Verarbeitung.

1. Erstelle ein PdfFileEditor-Objekt.
1. Versuchen Sie, zwei PDF-Dateien zusammenzuführen.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def try_concatenate_two_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    if not pdf_editor.try_concatenate(
        files_to_merge[0], files_to_merge[1], output_file
    ):
        print("Concatenation failed for the provided files.")
```
