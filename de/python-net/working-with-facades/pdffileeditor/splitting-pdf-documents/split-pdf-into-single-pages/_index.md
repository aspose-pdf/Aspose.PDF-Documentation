---
title: PDF in einzelne Seiten aufteilen
type: docs
weight: 30
url: /de/python-net/split-pdf-into-single-pages/
description: PDF-Dokument in einseitige PDFs aufteilen mit Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ein PDF in einzelne Seiten aufteilen in Python
Abstract: Erfahren Sie, wie Sie ein PDF-Dokument mit Aspose.PDF for Python in einseitige PDFs aufteilen. Diese Methode extrahiert jede Seite aus dem Original-PDF und speichert sie als separate Datei für flexible Dokumentenverwaltung und -verarbeitung.
---

Das Aufteilen eines PDFs in einzelne Seiten ist nützlich für die Verarbeitung auf Seitenebene, den Druck oder die Verteilung von Dokumentabschnitten einzeln. Mit Aspose.PDF for Python ist die \u0027split_to_pages\u0027 Methode der [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) Klasse erstellt separate PDF-Dateien für jede Seite im Quelldokument. Dieser Ansatz ermöglicht die automatische Extraktion von Seiten für Archivierung, Überprüfung oder individuelles Teilen, wobei das ursprüngliche Layout und der Inhalt erhalten bleiben.

1. Erstelle ein PdfFileEditor-Objekt.
1. PDF in einzelne Seiten aufteilen.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Split PDF into Single Pages
def split_pdf_into_single_pages(input_pdf_path, output_pdf_path):
    pdf_file_editor = pdf_facades.PdfFileEditor()
    pdf_file_editor.split_to_pages(input_pdf_path, output_pdf_path)
```
