---
title: Anhang aus Pfad hinzufügen
type: docs
weight: 20
url: /de/python-net/add-attachment-from-path/
description: Dieses Beispiel bindet ein Eingabe‑PDF, fügt eine externe Datei mithilfe ihres Dateipfads als Anhang hinzu und speichert das modifizierte PDF mit dem eingebetteten Anhang.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dateien an ein PDF anhängen mit Dateipfad‑Überladung in Python
Abstract: Dieses Beispiel zeigt, wie externe Dateien mithilfe der Dateipfad‑Überladung von 'add_document_attachment()' in Aspose.PDF for Python über die Facades‑API an ein PDF‑Dokument angehängt werden können. Es vereinfacht das Hinzufügen von Anhängen, ohne dass ein Datei‑Stream manuell geöffnet werden muss.
---

PDF kann eingebettete Dateien wie Dokumente, Tabellenkalkulationen oder Bilder für Referenz oder Verteilung enthalten. Die Dateipfad‑Überladung von 'add_document_attachment()' ermöglicht das Hinzufügen von Anhängen direkt aus einem Dateipfad und eliminiert die Notwendigkeit, die Datei manuell zu öffnen.

1. Erstelle das [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) Objekt.
1. Binden Sie das Eingabe-PDF.
1. Anhang mit Dateipfad hinzufügen.
1. Speichern Sie das aktualisierte Document.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_attachment_from_path(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add attachment using file-path overload
    content_editor.add_document_attachment(
        attachment_file,
        "Attachment added using file path overload.",
    )
    # Save updated document
    content_editor.save(outfile)
```
