---
title: Zwei PDF-Dateien zusammenführen
type: docs
weight: 60
url: /de/python-net/concatenate-two-files/
description: Erfahren Sie, wie Sie zwei PDF-Dateien mit Aspose.PDF for Python zu einem einzigen Dokument zusammenführen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Zwei PDF-Dateien in Python zu einer einzigen PDF zusammenführen
Abstract: Erfahren Sie, wie Sie zwei PDF-Dateien mit Aspose.PDF for Python zu einem einzigen Dokument verketten. Dieses Beispiel zeigt, wie Sie zwei PDFs nahtlos zusammenführen, wobei der ursprüngliche Inhalt und das Format erhalten bleiben.
---

Das Kombinieren von zwei PDF-Dateien ist eine gängige Aufgabe beim Konsolidieren von Berichten, Verträgen oder Formularen. Mit Aspose.PDF for Python können Sie programmgesteuert zwei PDFs zu einem einzigen Dokument zusammenführen, indem Sie die concatenate‑Methode der [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) Klasse. Dies stellt sicher, dass alle Seiten aus beiden Dateien in das Ausgabe‑PDF übernommen werden, wobei das ursprüngliche Layout, der Inhalt und die Struktur erhalten bleiben.

1. Erstelle ein PdfFileEditor-Objekt.
1. Zwei PDF-Dateien zusammenführen.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_two_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.concatenate(files_to_merge[0], files_to_merge[1], output_file)
```
