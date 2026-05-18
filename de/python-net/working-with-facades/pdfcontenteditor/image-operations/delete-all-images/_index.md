---
title: Alle Bilder aus PDF löschen
type: docs
weight: 10
url: /de/python-net/delete-all-images/
description: Alle Bilder aus einem PDF-Dokument mit Aspose.PDF for Python über die Facades-API löschen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Alle Bilder aus einem PDF mit PdfContentEditor in Python entfernen
Abstract: Dieses Beispiel zeigt, wie man alle Bilder aus einem PDF-Dokument mit Aspose.PDF for Python über die Facades-API löscht. Es zeigt, wie ein PDF gebunden, alle eingebetteten Bilder entfernt und das aktualisierte Dokument gespeichert wird.
---

PDF-Dokumente enthalten häufig Bilder für Illustrationen, Markenkennzeichnung oder Dekoration. Es kann Fälle geben, in denen Sie alle Bilder aus einem PDF entfernen müssen, beispielsweise zur Reduzierung der Dateigröße, zum Schutz sensibler Grafiken oder zur Vorbereitung einer reinen Textversion.

Verwenden [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), Sie können programmgesteuert alle Bilder aus einer PDF entfernen und dabei sicherstellen, dass das Dokument nur Textinhalt enthält. Dieses Beispiel bindet ein Eingabe‑PDF, löscht alle Bilder und speichert die geänderte Datei.

1. Erstellen Sie das PdfContentEditor-Objekt.
1. Binden Sie das Eingabe-PDF.
1. Alle Bilder löschen.
1. Speichern Sie das aktualisierte Document.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_all_image(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Delete all images from the document
    content_editor.delete_image()
    # Save updated document
    content_editor.save(outfile)
```
