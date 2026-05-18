---
title: Text auf Seite mit State ersetzen
type: docs
weight: 20
url: /de/python-net/replace-text-on-page-with-state/
description: In diesem Beispiel werden alle Vorkommen des Wortes "software" auf Seite 1 durch "SOFTWARE PAGE 1" ersetzt, wobei roter Text mit einer Schriftgröße von 12 verwendet wird.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Text mit benutzerdefinierter Formatierung auf einer bestimmten Seite mithilfe von PdfContentEditor in Python ersetzen
Abstract: Dieses Beispiel zeigt, wie man Text auf einer bestimmten Seite in einem PDF ersetzt und dabei benutzerdefinierte Formatierung mithilfe von Aspose.PDF for Python via the Facades API anwendet. Es zeigt, wie man die Schriftgröße und Farbe während des Textaustauschs steuert.
---

Manchmal erfordert das Ersetzen von Text in einem PDF auch Formatierungsänderungen wie Farbe oder Schriftgröße. Mit TextState können Sie Stil-Eigenschaften definieren und diese beim Ersetzen anwenden. Dies ermöglicht es, geänderten Text hervorzuheben oder eine konsistente Formatierung über Dokumente hinweg durchzusetzen.

1. Erstelle ein [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) Instanz.
1. Binden Sie das Eingabe‑PDF‑Dokument.
1. Definieren Sie einen TextState mit benutzerdefinierter Formatierung.
1. Konfigurieren Sie die Ersetzungsstrategie.
1. Text auf einer bestimmten Seite ersetzen.
1. Speichern Sie das aktualisierte PDF-Dokument.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_on_page_with_state(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.red
    text_state.font_size = 12

    # Replace text on a specific page with explicit text formatting
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text("software", 1, "SOFTWARE PAGE 1", text_state)
    # Save updated document
    content_editor.save(outfile)
```
