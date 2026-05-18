---
title: Dateianhang-Annotation hinzufügen
type: docs
weight: 30
url: /de/python-net/add-file-attachment-annotation/
description: Das Beispiel bindet ein Eingabe‑PDF, fügt mit dem Dateipfad eine Dateianhang-Annotation zur ersten Seite hinzu und speichert das aktualisierte Dokument.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dateianhang-Annotationen zu einem PDF mit Python hinzufügen
Abstract: Dieses Beispiel zeigt, wie man mit einem Dateipfad eine Dateianhang-Annotation in einem PDF erstellt, indem man Aspose.PDF für Python via die Facades‑API verwendet. Es demonstriert, wie man die Platzierung der Annotation definiert, Beschreibungstext festlegt, einen Symboltyp auswählt und das bearbeitete Dokument speichert.
---

Dateianhang-Annotationen ermöglichen es, externe Dateien als interaktive Symbole auf einer PDF‑Seite einzubetten. Mit dem Dateipfad‑Überladung können Sie Dateien direkt von der Festplatte anhängen, ohne Streams manuell zu öffnen. Diese Methode erlaubt zudem das Anpassen des Annotationssymbols und das Bereitstellen einer Beschreibung für Benutzer.

1. Erstelle das [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) Objekt.
1. Binden Sie das Eingabe-PDF.
1. Definieren Sie das Annotationsrechteck.
1. Fügen Sie die Dateianhang-Annotation hinzu.
1. Speichern Sie das aktualisierte Document.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_file_attachment_annotation(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Create file attachment annotation on page 1
    content_editor.create_file_attachment(
        apd.Rectangle(100, 520, 20, 20),
        "Attachment annotation contents",
        attachment_file,
        1,
        "PushPin",
    )
    # Save updated document
    content_editor.save(outfile)
```
