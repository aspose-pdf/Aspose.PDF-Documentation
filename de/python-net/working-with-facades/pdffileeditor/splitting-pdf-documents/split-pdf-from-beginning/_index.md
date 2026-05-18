---
title: PDF vom Anfang aufteilen
type: docs
weight: 10
url: /de/python-net/split-pdf-from-beginning/
description: Teilen Sie ein PDF-Dokument vom Anfang aus mithilfe von Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF vom Anfang in Python mit Aspose.PDF aufteilen
Abstract: Erfahren Sie, wie Sie ein PDF-Dokument vom Anfang aus mit Aspose.PDF for Python aufteilen. Dieses Beispiel demonstriert das Extrahieren einer bestimmten Anzahl von Seiten, beginnend mit der ersten Seite, um ein neues PDF-Dokument zu erstellen.
---

Das Aufteilen von PDFs vom Anfang ist nützlich, wenn Sie die ersten Seiten eines Dokuments als separate Datei benötigen. Mit Aspose.PDF for Python ermöglicht die split_from_first-Methode in der [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) Klasse ermöglicht es Ihnen, eine festgelegte Anzahl von Seiten beginnend mit Seite eins zu extrahieren. Diese Funktion ist ideal, um Auszüge, Vorschauen oder kleinere Abschnitte eines größeren PDFs zu erstellen, ohne die Originaldatei manuell zu bearbeiten.

1. Erstelle ein PdfFileEditor-Objekt.
1. PDF ab der ersten Seite aufteilen.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Split PDF from Beginning
def split_pdf_from_beginning(input_pdf_path, output_pdf_path):
    pdf_file_editor = pdf_facades.PdfFileEditor()
    pdf_file_editor.split_from_first(input_pdf_path, 3, output_pdf_path)
```
