---
title: Dateianhang-Annotation aus Stream hinzufügen
type: docs
weight: 40
url: /de/python-net/add-file-attachment-annotation-from-stream/
description: Das Beispiel lädt ein PDF, liest eine externe Datei in einen Speicher-Stream, fügt eine Dateianhang-Annotation zur ersten Seite hinzu und speichert das modifizierte Dokument.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dateianhang-Annotationen zu einem PDF aus einem Stream in Python hinzufügen
Abstract: Dieses Beispiel zeigt, wie man in einem PDF mit einem Dateistream und Aspose.PDF for Python über die Facades‑API eine Dateianhang-Annotation erstellt. Es demonstriert, wie man die Position der Annotation festlegt, eine Beschreibung setzt, einen Opazitätswert angibt und das modifizierte Dokument speichert.
---

Dateianhang-Annotationen ermöglichen das Einbetten von Dateien als interaktive Symbole innerhalb einer PDF‑Seite. Mit einem streambasierten Ansatz können Sie Dateien dynamisch anhängen, ohne auf einen physischen Dateipfad angewiesen zu sein. Diese Methode unterstützt zudem die Anpassung des Erscheinungsbildes der Annotation, einschließlich der Opazität.

1. Erstellen Sie das PdfContentEditor-Objekt.
1. Binden Sie das Eingabe-PDF.
1. Lesen Sie die Anhangsdatei als Stream.
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


def add_file_attachment_annotation_from_stream(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    with open(attachment_file, "rb") as source_stream:
        attachment_stream = BytesIO(source_stream.read())

    # Create file attachment annotation using stream+opacity overload
    content_editor.create_file_attachment(
        apd.Rectangle(130, 520, 20, 20),
        "Attachment annotation from stream",
        attachment_stream,
        path.basename(attachment_file),
        1,
        "Tag",
        0.75,
    )
    # Save updated document
    content_editor.save(outfile)
```
