---
title: PDF bis zum Ende teilen
type: docs
weight: 40
url: /de/python-net/split-pdf-to-end/
description: Teilen Sie ein PDF-Dokument von einer angegebenen Seite bis zur letzten Seite mit Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ein PDF von einer bestimmten Seite bis zum Ende in Python teilen
Abstract: Erfahren Sie, wie Sie ein PDF-Dokument von einer angegebenen Seite bis zur letzten Seite mit Aspose.PDF for Python teilen. Dieses Beispiel demonstriert das Extrahieren aller Seiten ab einer bestimmten Seite, um eine neue PDF-Datei zu erstellen.
---

Das Aufteilen eines PDFs von einer bestimmten Seite bis zum Ende ist nützlich, wenn Sie den hinteren Teil eines Dokuments als separate Datei benötigen. Mit Aspose.PDF for Python ermöglicht die split_to_end-Methode der [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) Klasse ermöglicht es Ihnen, Seiten ab einer beliebigen Seitenzahl bis zur letzten Seite des Dokuments zu extrahieren. Dies ist ideal, um Auszüge zu erstellen, Kapitel zu extrahieren oder Teile eines großen PDFs zu verarbeiten, ohne es manuell zu bearbeiten.

1. Erstelle ein PdfFileEditor-Objekt.
1. PDF von einer bestimmten Seite bis zum Ende teilen.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Split PDF to End
def split_pdf_to_end(input_pdf_path, output_pdf_path):
    pdf_file_editor = pdf_facades.PdfFileEditor()
    pdf_file_editor.split_to_end(input_pdf_path, 2, output_pdf_path)
```
