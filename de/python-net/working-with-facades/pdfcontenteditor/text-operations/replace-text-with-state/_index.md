---
title: Text mit Status ersetzen
type: docs
weight: 50
url: /de/python-net/replace-text-with-state/
description: In diesem Beispiel werden alle Vorkommen von "software" durch "SOFTWARE" ersetzt und in Blau mit einer Schriftgröße von 14 formatiert.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Text in einem PDF mit benutzerdefinierter Formatierung unter Verwendung von PdfContentEditor in Python ersetzen
Abstract: Dieses Beispiel zeigt, wie man Text in einem PDF-Dokument ersetzt und dabei benutzerdefinierte Formatierung mithilfe von Aspose.PDF for Python über die Facades-API anwendet. Es zeigt, wie man die Textfarbe und Schriftgröße während des Ersetzens steuert.
---

Beim Aktualisieren von Text in einem PDF möchten Sie möglicherweise, dass der ersetzte Inhalt hervorsticht. Durch die Verwendung eines TextState-Objekts können Sie Stilmerkmale wie Farbe und Schriftgröße definieren und dann auf allen ersetzten Text anwenden.

1. Erstelle ein [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)  Instanz.
1. Binden Sie das Eingabe‑PDF‑Dokument.
1. Definieren Sie einen TextState mit benutzerdefinierter Formatierung.
1. Ersetzungsbereich konfigurieren.
1. Text im gesamten Dokument ersetzen.
1. Speichern Sie das aktualisierte PDF-Dokument.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_with_state(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.blue
    text_state.font_size = 14

    # Replace text with explicit text formatting
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text("software", "SOFTWARE", text_state)
    # Save updated document
    content_editor.save(outfile)
```
