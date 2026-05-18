---
title: Bilder aus PDF löschen
type: docs
weight: 20
url: /de/python-net/delete-images/
description:
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Bestimmte Bilder von einer PDF-Seite mit PdfContentEditor in Python löschen
Abstract: Dieses Beispiel demonstriert, wie man bestimmte Bilder aus einem PDF-Dokument mit Aspose.PDF für Python über die Facades-API löscht. Es zeigt, wie man Bilder auf einer bestimmten Seite anvisiert und das aktualisierte Dokument speichert.
---

Manchmal möchte man nur bestimmte Bilder aus einem PDF entfernen, anstatt alle visuellen Elemente zu löschen. Mit [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), kann man ausgewählte Bilder löschen, indem man die Seitenzahl und den Bildindex angibt.

Dieses Code‑Snippet bindet ein Eingabe‑PDF, löscht das zweite Bild auf Seite 1 und speichert das modifizierte PDF, wobei andere Bilder unverändert bleiben.

1. Erstellen Sie eine PdfContentEditor-Instanz.
1. Binden Sie das Eingabe-PDF-Dokument.
1. Löschen Sie bestimmte Bilder von einer festgelegten Seite.
1. Speichern Sie das aktualisierte PDF-Dokument.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_images(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Delete image on page 1
    content_editor.delete_image(1, [2])
    # Save updated document
    content_editor.save(outfile)
```
