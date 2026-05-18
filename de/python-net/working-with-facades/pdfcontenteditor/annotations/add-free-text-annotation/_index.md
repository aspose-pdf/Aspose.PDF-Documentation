---
title: Freitext-Annotationen hinzufügen
type: docs
weight: 20
url: /de/python-net/add-free-text-annotation/
description: Dieses Beispiel lädt eine vorhandene PDF-Datei, fügt der ersten Seite an einer definierten Position eine Freitext-Annotation hinzu und speichert das modifizierte Dokument.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Freitext-Annotation zu einem PDF mit Python hinzufügen
Abstract: Dieses Beispiel zeigt, wie man mit Aspose.PDF für Python via the Facades API eine Freitext-Annotation in ein PDF-Dokument einfügt. Es demonstriert, wie man ein PDF bindet, die Platzierung der Annotation definiert, benutzerdefinierten Text hinzufügt und das aktualisierte Dokument speichert.
---

Freitext-Annotationen ermöglichen es, sichtbaren Text direkt auf einer PDF-Seite zu platzieren, ohne dass Pop-up-Kommentare erforderlich sind. Mit PdfContentEditor können Sie das Annotationsrechteck, den angezeigten Text und die Zielseite festlegen.

1. Erstelle das [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) Objekt.
1. Binden Sie das Eingabe-PDF.
1. Definieren Sie die Position der Annotation.
1. Fügen Sie die Freitext-Annotation hinzu.
1. Speichern Sie das aktualisierte Document.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_free_text_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add free text annotation to page 1
    content_editor.create_free_text(
        apd.Rectangle(200, 480, 150, 25), "This is a free text annotation", 1
    )
    # Save updated document
    content_editor.save(outfile)
```
