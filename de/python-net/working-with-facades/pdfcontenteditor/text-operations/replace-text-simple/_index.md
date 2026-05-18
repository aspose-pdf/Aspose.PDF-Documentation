---
title: Einfachen Text ersetzen
type: docs
weight: 40
url: /de/python-net/replace-text-simple/
description: In diesem Beispiel werden alle Vorkommen von "33" im gesamten Dokument durch "XXXIII " ersetzt. Dies demonstriert eine einfache Zeichenketten-Ersetzung ohne benutzerdefinierte Formatierung oder Regex.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Text in einem PDF mit PdfContentEditor in Python ersetzen
Abstract: Dieses Beispiel zeigt, wie man Text im gesamten PDF-Dokument mit Aspose.PDF für Python über die Facades-API ersetzt. Es ersetzt alle Vorkommen einer angegebenen Zeichenkette durch neuen Text.
---

Einfache Text-Ersetzung ist nützlich, wenn wiederholte Werte in einem Dokument aktualisiert werden. Mit [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), können Sie einen Ersetzungsbereich definieren und Text global über alle Seiten hinweg ersetzen.

1. Erstelle ein [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) Instanz.
1. Binden Sie das Eingabe‑PDF‑Dokument.
1. Ersetzenbereich für alle Vorkommen konfigurieren.
1. Ersetzen Sie den Zieltext.
1. Speichern Sie das aktualisierte PDF-Dokument.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_simple(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace text in the whole document
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text("33", "XXXIII ")
    # Save updated document
    content_editor.save(outfile)
```
