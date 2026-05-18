---
title: Caret-Annotation hinzufügen
type: docs
weight: 10
url: /de/python-net/add-caret-annotation/
description: Dieses Beispiel lädt ein vorhandenes PDF, fügt der ersten Seite eine Caret-Annotation hinzu und speichert das geänderte Dokument. Die Annotation enthält ein rotes Caret-Symbol und beschreibenden Kommentartext.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Caret-Annotation zu einem PDF mit Python hinzufügen
Abstract: Dieses Beispiel zeigt, wie man mithilfe von Aspose.PDF for Python über die Facades-API eine Caret-Annotation zu einem PDF-Dokument hinzufügt. Das Beispiel demonstriert, wie man eine PDF-Datei bindet, die Platzierung der Annotation mithilfe von Rechtecken definiert, Caret-Eigenschaften konfiguriert und das aktualisierte Dokument speichert.
---

Caret-Annotationen werden häufig verwendet, um Texteinfügungen oder redaktionelle Kommentare in einem Dokument anzuzeigen. Mit PdfContentEditor können Sie programmgesteuert Caret-Annotationen hinzufügen, indem Sie die Seitenzahl, die Annotationsgrenzen, den Callout-Bereich, das Symbol, den Notiztext und die Farbe angeben.

1. Erstelle das [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) Objekt.
1. Binden Sie das Eingabe-PDF.
1. Definieren Sie die Parameter für die Caret-Annotation:
  - Seitenzahl, an der die Annotation hinzugefügt wird
  - Caret-Rechteck (Positionsbereich der Annotation)
  - Callout-Rechteck (Textbereich)
  - Symbol (z. B. "P")
  - Anmerkungstext
  - Anmerkungsfarbe
1. Füge die Caret-Anmerkung hinzu.
1. Speichern Sie das aktualisierte Document.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_caret_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add caret annotation to page 1
    content_editor.create_caret(
        1,
        apd.Rectangle(350, 400, 10, 10),
        apd.Rectangle(300, 380, 115, 15),
        "P",
        "This is a caret annotation",
        apd.Color.red,
    )
    # Save updated document
    content_editor.save(outfile)
```
