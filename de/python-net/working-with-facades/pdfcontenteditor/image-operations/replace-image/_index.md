---
title: Bilder in PDF ersetzen
type: docs
weight: 30
url: /de/python-net/replace-image/
description: Dieses Beispiel bindet ein Eingabe‑PDF, ersetzt das erste Bild auf Seite 1 durch ein neues Bild und speichert das geänderte Dokument.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ein Bild in einem PDF mit PdfContentEditor in Python ersetzen
Abstract: Dieses Beispiel demonstriert, wie man ein vorhandenes Bild in einem PDF‑Dokument mithilfe von Aspose.PDF for Python via the Facades API ersetzt. Es zeigt, wie man ein bestimmtes Bild auf einer Seite anvisiert und durch ein neues Bild ersetzt, dann das aktualisierte PDF speichert.
---

PDFs enthalten oft Bilder, die aktualisiert oder ersetzt werden müssen, wie Logos, Diagramme oder Fotos. Mit [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), können Sie ein bestimmtes Bild auf einer gegebenen Seite ersetzen, indem Sie die Seitennummer, den Bildindex und den Pfad zur neuen Bilddatei angeben.

1. Erstellen Sie eine PdfContentEditor-Instanz.
1. Binden Sie das Eingabe-PDF-Dokument.
1. Ersetzen Sie ein bestimmtes Bild auf einer angegebenen Seite.
1. Speichern Sie das aktualisierte PDF-Dokument.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_image(infile, image_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace image on page 1
    content_editor.replace_image(1, 1, image_file)
    # Save updated document
    content_editor.save(outfile)
```
