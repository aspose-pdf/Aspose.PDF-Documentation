---
title: Mehrere PDF-Dateien zusammenführen
type: docs
weight: 20
url: /de/python-net/concatenate-pdf-files/
description: Kombiniere mehrere PDF-Dateien zu einem einzigen Dokument mit Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Mehrere PDF-Dateien zu einem PDF in Python zusammenführen
Abstract: Lernen Sie, wie Sie mehrere PDF-Dateien zu einem einzigen Dokument mit Aspose.PDF for Python kombinieren. Dieses Beispiel zeigt, wie Sie die concatenate‑Methode verwenden, um mehrere PDFs nahtlos zusammenzuführen und dabei deren Inhalt und Formatierung beizubehalten.
---

Das Zusammenführen von PDF-Dateien ist eine gängige Aufgabe im Dokumentenmanagement, Reporting und automatisierten Workflows. Mit Aspose.PDF for Python können Entwickler einfach mehrere PDF-Dateien zu einem einzigen konsolidierten Dokument kombinieren. Die concatenate‑Methode der [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) Klasse stellt sicher, dass alle Seiten der Eingabedateien im endgültigen Ergebnis erhalten bleiben und deren ursprüngliches Layout und Inhalt bewahren. Dieser Ansatz ist nützlich, um umfassende Berichte zu erstellen, Formulare zu kombinieren oder mehrere Dokumente effizient zu archivieren.

1. Erstelle ein PdfFileEditor-Objekt.
1. Mehrere PDF-Dateien zusammenführen.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_pdf_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.concatenate(files_to_merge, output_file)
```
